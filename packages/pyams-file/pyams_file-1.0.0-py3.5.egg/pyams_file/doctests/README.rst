==================
PyAMS_file package
==================

Introduction
------------

This package is composed of a set of utility functions, usable into any Pyramid application.

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> import os, sys, tempfile
    >>> temp_dir = tempfile.mkdtemp()

Blos storage requires a blobs storage directory, which can only be used with a FileStorage,
ZEOStorage of RelStorage:

    >>> config = setUp()
    >>> config.registry.settings['zodbconn.uri'] = 'file://{dir}/Data.fs?blobstorage_dir={dir}/blobs'.format(
    ...     dir=temp_dir)

    >>> import transaction
    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_site import includeme as include_site
    >>> include_site(config)
    >>> from pyams_i18n import includeme as include_i18n
    >>> include_i18n(config)
    >>> from pyams_catalog import includeme as include_catalog
    >>> include_catalog(config)
    >>> from pyams_file import includeme as include_file
    >>> include_file(config)

    >>> from pyams_site.generations import upgrade_site
    >>> request = DummyRequest()
    >>> app = upgrade_site(request)
    Upgrading PyAMS timezone to generation 1...
    Upgrading PyAMS I18n to generation 1...
    Upgrading PyAMS catalog to generation 1...
    Upgrading PyAMS file to generation 3...

    >>> from zope.traversing.interfaces import BeforeTraverseEvent
    >>> from pyramid.threadlocal import manager
    >>> from pyams_utils.registry import handle_site_before_traverse
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))
    >>> manager.push({'request': request, 'registry': config.registry})


Blobs references manager
------------------------

The blobs references manager is a local utility which is in charge of keeping internal references
to file *blobs*; when a content containing a file is created, a reference is added to this file;
if the content is duplicated, the file is not duplicated but a new reference is added to it.

If the file associated with the copy is modified afterwards, one of the references is removed and
replaced by a reference to a new blob file; when the number of references to a given file is
reduced to zero, the blob file is physically deleted.

    >>> from pyams_utils.registry import get_utility
    >>> from pyams_file.interfaces import IBlobReferenceManager
    >>> from pyams_file.tests import find_files
    >>> refs = get_utility(IBlobReferenceManager)
    >>> len(refs.refs)
    0
    >>> list(find_files("*.blob", os.path.join(temp_dir, 'blobs')))
    []


Defining file schema fields and properties
------------------------------------------

Doctests defined classes can't be persisted, so we use testing classes defined into
PyAMS_file.tests:

    >>> from pyams_file.tests import MyContent

File content can be set from a simple string:

    >>> content = MyContent()
    >>> content.data = 'This is my file content'
    Traceback (most recent call last):
    ...
    AttributeError: 'NoneType' object has no attribute 'add'

Why this error? It's because blob files have to be "parented" to their context to get a
database reference before being able to set their content:

    >>> from zope.location import locate
    >>> locate(content, app)

    >>> content.data = 'This is my file content'
    >>> content.data
    <pyams_file.file.File object at 0x... oid 0x... in <Connection at ...>>
    >>> content.data.__parent__ is content
    True
    >>> content.data.__name__
    '++attr++data'
    >>> bool(content.data)
    True

A simple "locate" call to define the parent is enough; another option can be to set the "__parent__"
attribute, or to set a value, for example, in a parent folder, like in:

    >>> app['content'] = content

When retrieving file content, you will notice that this content has been converting to bytes
(using UTF-8 encoding):

    >>> content.data.data
    b'This is my file content'
    >>> content.data.get_size()
    23
    >>> len(refs.refs)
    1
    >>> len(refs.refs[list(refs.refs)[0]])
    1
    >>> refs.refs[list(refs.refs)[0]]
    {<pyams_file.file.File object at 0x...>}
    >>> list(find_files("*.blob", os.path.join(temp_dir, 'blobs')))
    []

Why don't we have any file in the blobs directory? That's because our transaction hasn't been
committed yet!

    >>> transaction.commit()
    >>> len(list(find_files("*.blob", os.path.join(temp_dir, 'blobs'))))
    1

You can also provide a file-like object to set a file property content:

    >>> with open(os.path.join(temp_dir, 'data.txt'), 'w') as file:
    ...     _ = file.write('This is my file content')
    >>> with open(os.path.join(temp_dir, 'data.txt'), 'r+b') as file:
    ...     content.data = file


Using a file as context manager
-------------------------------

Any File object can be used as a context manager, as a builtin *file* object; but as we changed
file contents, transaction must be committed first:

    >>> transaction.commit()
    >>> with content.data as file:
    ...     print(file.read())
    ...     file.close()
    b'This is my file content'


Iterating over file content
---------------------------

Instead of reading the whole file content in a single operation, you can iterate over file contents
by blocks of 64kb each:

    >>> for block in content.data:
    ...     print(block)
    b'This is my file content'


Copying a file
--------------

Copying a file should only generate a new reference into blobs manager, without creating a new
blob file:

    >>> from zope.copy import copy
    >>> copied_content = copy(content)
    >>> app['copy'] = copied_content
    >>> len(refs.refs)
    1
    >>> len(refs.refs[list(refs.refs)[0]])
    2
    >>> refs.refs[list(refs.refs)[0]]
    {<pyams_file.file.File object at 0x...>, <pyams_file.file.File object at 0x...>}

We can now change data of the copied content, to see that this added a reference to a new file,
and that the first reference was removed:

    >>> copied_content.data = 'This is a new content'
    >>> len(refs.refs)
    2
    >>> blob_refs = list(refs.refs.keys())
    >>> len(refs.refs[blob_refs[0]])
    1
    >>> len(refs.refs[blob_refs[1]])
    1

And we can remove copy data to remove a reference:

    >>> copied_content.data = None
    >>> len(refs.refs)
    1
    >>> blob_refs = list(refs.refs.keys())
    >>> len(refs.refs[list(refs.refs)[0]])
    1


I18n files properties
---------------------

I18n file properties are working exactly like normal I18n properties:

    >>> from pyams_file.tests import MyI18nContent

    >>> i18n_content = MyI18nContent()
    >>> locate(i18n_content, app)
    >>> i18n_content.data = {'en': 'This is my I18n content'}
    >>> i18n_content.data
    {'en': <pyams_file.file.File object at 0x...>}
    >>> i18n_content.data['en'].data
    b'This is my I18n content'


Managing images
---------------

Let's now try to use an image instead of a simple text content:

    >>> img_name = os.path.join(sys.modules['pyams_file.tests'].__path__[0], 'test_image.png')
    >>> with open(img_name, 'rb') as file:
    ...     content.data = file
    >>> content.data
    <pyams_file.file.ImageFile object at 0x...>
    >>> content.data.get_size()
    20212

As we can see, the image has automatically been recognized as such:

    >>> content.data.content_type
    'image/png'
    >>> content.data.get_image_size()
    (535, 166)

We now have a few helpers to manipulate images; let's commit first:

    >>> transaction.commit()
    >>> content.data.resize(500, 500, keep_ratio=True)
    >>> content.data.get_size()
    30391
    >>> content.data.get_image_size()
    (500, 155)

We can also rotate image, or crop on a given selection:

    >>> transaction.commit()
    >>> content.data.rotate(-90)
    >>> content.data.get_size()
    30819
    >>> content.data.get_image_size()
    (155, 500)

    >>> transaction.commit()
    >>> content.data.crop(50, 50, 300, 300)
    >>> content.data.get_size()
    12324
    >>> content.data.get_image_size()
    (250, 250)

Please note also that if you can store any type of content in a generic file field, you can only
store images in an image field:

    >>> content.img_data = 'This is a bad text content'
    Traceback (most recent call last):
    ...
    zope.schema._bootstrapinterfaces.WrongType: (<pyams_file.file.File object at 0x...>, <InterfaceClass pyams_file.interfaces.IBaseImageFile>, 'img_data')

    >>> content.img_data = content.data
    >>> content.img_data.content_type
    'image/png'
    >>> content.img_data.get_size()
    12324
    >>> content.img_data.get_image_size()
    (250, 250)


Downloading a file
------------------

Each file has it's own URL, which is defined via "absolute_url()" on any File object instance.
The FileView is used to download a file:

    >>> transaction.commit()

We can suppress warnings here to avoid a RessourceWarning about unclosed files; in a normal
Pyramid context, the response body is closed automatically:

    >>> import warnings
    >>> warnings.filterwarnings('ignore')

    >>> from pyams_file.skin.view import FileView
    >>> request = DummyRequest(context=content.data, range=None)
    >>> response = FileView(request)
    >>> response.status
    '200 OK'
    >>> response.content_type
    'image/png'
    >>> response.has_body
    True
    >>> result = response({'REQUEST_METHOD': 'GET'}, lambda x, y: None)
    >>> len(list(result)[0])
    12324

You can also specify a request parameter to get a download of a file, instead of a link to a file
that will be automatically displayed into a web browser:

    >>> request = DummyRequest(context=content.data, params={'download': 1}, range=None)
    >>> response = FileView(request)
    >>> response.status
    '200 OK'
    >>> response.content_disposition
    'attachment; filename="noname.txt"'

To get a file name, we have to set it into file properties:

    >>> content.data.filename = 'pyams-test.png'
    >>> request = DummyRequest(context=content.data, params={'download': 1}, range=None)
    >>> response = FileView(request)
    >>> response.status
    '200 OK'
    >>> response.content_disposition
    'attachment; filename="pyams-test.png"'


Deleting a file
---------------

Two options are available to delete a file (if it's not required!): the first one is just to
assign a null value to the given property; but to be able to delete a file from a form, there is
a special value called **TO_BE_DELETED**, defined by PyAMS_utils:

    >>> from pyams_utils.interfaces.form import TO_BE_DELETED
    >>> content.data = TO_BE_DELETED
    >>> content.data is None
    True
    >>> i18n_content.data = {'en': TO_BE_DELETED}
    >>> len(refs.refs)
    0


Removing unused blobs
---------------------

After these tests, we can see that despite the fact that we don't have any File object anymore
into our database, several blobs are still present on the filesystem:

    >>> transaction.commit()
    >>> len(list(find_files("*.blob", os.path.join(temp_dir, 'blobs'))))
    8

Why so many files? Because each time a File object is committed, even when using an history-free
storage, a new blob file is stored on the filesystem; these files will be removed when using the
"zeopack" (when using ZEO) or "zodbpack" (when using Relstorage) command line scripts.


Tests cleanup:

    >>> from pyams_utils.registry import set_local_registry
    >>> set_local_registry(None)
    >>> manager.clear()
    >>> transaction.commit()
    >>> tearDown()
