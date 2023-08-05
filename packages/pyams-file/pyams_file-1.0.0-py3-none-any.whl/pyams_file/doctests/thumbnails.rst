PyAMS_file thumbnails management
================================

PyAMS_file package provides a set of adapters related to thumbnails management, which is the
ability to automatically generate smaller images, adapted to a web page, of an original image.

You can also use custom selections of predefined images ratios (like square, portrait, panoramic...)
by selecting adapted areas of the original images, and you can then generate smaller thumbnails
from these selections.


Initialization
--------------

You'll notice in this tests that the current transaction is committed regularly: it's because of
how blob files are functionning, a blob file can't be reopened without being committed.

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

    >>> from pyams_file.tests import MyContent
    >>> img_name = os.path.join(sys.modules['pyams_file.tests'].__path__[0], 'test_image.png')

    >>> content = MyContent()
    >>> app['content'] = content
    >>> with open(img_name, 'rb') as file:
    ...     content.img_data = file
    >>> transaction.commit()


Getting default thumbnails
--------------------------

Let's now try to get image thumbnails:

    >>> from pyams_file.interfaces.thumbnail import IThumbnails
    >>> img = content.img_data
    >>> thumbs = IThumbnails(img)

Thumbnails are defined by their size, and by their name for custom selections; sizes can be given
in width, height or both: in any case, it's the maximum size of the resulting thumbnail:

    >>> th1 = thumbs.get_thumbnail('128x128')
    >>> th1
    <pyams_file.file.ImageFile object at 0x...>
    >>> th1.get_image_size()
    (128, 39)
    >>> th2 = thumbs.get_thumbnail('w128')
    >>> th2.get_image_size()
    (128, 39)
    >>> th3 = thumbs.get_thumbnail('h128')
    >>> th3.get_image_size()
    (412, 128)

If you look for a thumbnail of a bigger size than the original one, it's the original image which
is returned:

    >>> th4 = thumbs.get_thumbnail('1024x1024')
    >>> th4.get_image_size()
    (535, 166)
    >>> th4 is img
    True

Each thumbnail has it's own URL, to be included into a web page:

    >>> from pyams_utils.url import absolute_url
    >>> absolute_url(th3, request)
    'http://example.com/content/++attr++img_data/++thumb++412x128.png'

Generated thumbnails are stored into original image annotations, so that they don't have to be
computed each time; they are cleared when the image is modified:

    >>> sorted(thumbs.thumbnails.keys())
    ['128x39', '412x128']

    >>> from pyams_file.interfaces import FileModifiedEvent
    >>> config.registry.notify(FileModifiedEvent(img))
    >>> sorted(thumbs.thumbnails.keys())
    []

Thumbnails are automatically generated into original file format, but you can request a specific
file format for a given thumbnail:

    >>> th5 = thumbs.get_thumbnail('128x128', 'JPEG')
    >>> th5.content_type
    'image/jpeg'


Using selections
----------------

Selections allow to select parts of your image of a selected ratio; they can also be used, in
different circumstances, to provide custom parts of an image which will be used in responsive
mode in a "<picture />" HTML tag; selections are given names based on the different Bootstrap
medias sizes ("xs", "sm", "md" and "lg"), and on custom predefined aspect ratios: "portrait",
"square", "pano", "card" and "banner" which are used inside PyAMS:

    >>> th6 = thumbs.get_thumbnail('sm')
    >>> th6 is None
    True

Why is this thumbnail empty? It's because, to support responsive thumbnails, an image has to be
marked with a custom interface:

    >>> from zope.interface import alsoProvides
    >>> from pyams_file.interfaces import IResponsiveImage
    >>> alsoProvides(img, IResponsiveImage)

    >>> th6 = thumbs.get_thumbnail('sm')
    >>> th6.get_image_size()
    (535, 166)
    >>> th6 is img
    False

You can combine a custom selection with a custom size by separating them with ":":

    >>> transaction.commit()
    >>> th7 = thumbs.get_thumbnail('sm:128x128')
    >>> th7.get_image_size()
    (128, 39)

By default, responsive selections cover the whole area of the original image; let's try to create
a define a custom area for this selection:

    >>> from pyams_file.image import ThumbnailGeometry
    >>> geometry = ThumbnailGeometry()
    >>> geometry.x1 = 20
    >>> geometry.y1 = 20
    >>> geometry.x2 = 515
    >>> geometry.y2 = 146
    >>> geometry
    <ThumbnailGeometry: x1,y1=20,20 - x2,y2=515,146>

    >>> thumbs.set_geometry('sm', geometry)
    >>> th8 = thumbs.get_thumbnail('sm')
    >>> th8.get_image_size()
    (495, 126)

    >>> transaction.commit()
    >>> th9 = thumbs.get_thumbnail('sm:128x128')
    >>> th9.get_image_size()
    (128, 32)


Using selections with default ratio
-----------------------------------

Selections with default ratios are used regularly inside PyAMS; they are used like responsive
selections and unless specified otherwise, they are centered into the original image, with the
biggest possible size:

    >>> transaction.commit()
    >>> th10 = thumbs.get_thumbnail('square')
    >>> th10.get_image_size()
    (166, 166)

"portrait" is a selection with a 3/4 ratio:

    >>> th11 = thumbs.get_thumbnail('portrait')
    >>> th11.get_image_size()
    (125, 166)

"pano" is a selection with a 16/9 ratio:

    >>> th12 = thumbs.get_thumbnail('pano')
    >>> th12.get_image_size()
    (295, 166)

"card" is a selection with a 2/1 ratio, which can be used for Twitter cards:

    >>> th13 = thumbs.get_thumbnail("card")
    >>> th13.get_image_size()
    (332, 166)

And finally "banner" is a selection with a ratio of 5/1:

    >>> th14 = thumbs.get_thumbnail("banner")
    >>> th14.get_image_size()
    (535, 106)

Standard selections can also be resized in a single operation:

    >>> transaction.commit()
    >>> th15 = thumbs.get_thumbnail("banner:128x128")
    >>> th15.get_image_size()
    (128, 25)


Rendering images
----------------

PyAMS_file provides a few helpers to include an image tag into an HTML template:

    >>> transaction.commit()
    >>> from pyams_file.skin import render_image
    >>> render_image(img, width=128, request=request)
    '<img src="http://example.com/content/++attr++img_data/++thumb++128x39.jpeg" class="" />'
    >>> render_image(th15, request=request)
    '<img src="http://example.com/content/++attr++img_data/++thumb++banner:535x106.png/++thumb++128x25.png" class="" />'


Watermarking
------------

The "get_thumbnail" method accepts a "watermark" parameter; this allows you to set a watermark
image which will be applied on top of the original image before creating a thumbnail. The given
argument can be a file-like object, a file path or another instance of an ImageFile object.

The "watermark_position" parameter allows to define watermark position; default "scale" value is
scaling the watermark image to fit the original image size; you can use the "tile" value to tile
the watermark over the original image several times, or you can provide a tuple to set watermark
position in (x, y) above the original image, without scaling in this case.


Rendering pictures
------------------

"picture" is a PyAMS TALES extension which can be used to render a complete responsive "<picture >"
HTML tag including all responsive selections of a given image; for testing purposes, we have to
register Pyramid's renderer:

    >>> from pyramid_chameleon import zpt
    >>> config.add_renderer('.pt', zpt.renderer_factory)

    >>> from zope.interface import Interface
    >>> from pyams_utils.interfaces.tales import ITALESExtension
    >>> from pyams_utils.adapter import ContextRequestAdapter
    >>> view = ContextRequestAdapter(app, request)
    >>> alsoProvides(view, Interface)
    >>> extension = config.registry.queryMultiAdapter((img, request, view), ITALESExtension, name='picture')
    >>> extension.render()
    '<picture>...<source media="(max-width: 767px)"...srcset="http://example.com/content/++attr++img_data/++thumb++xs:w768?_=..." />...<source media="(max-width: 991px)"...srcset="http://example.com/content/++attr++img_data/++thumb++sm:w992?_=..." />...<source media="(max-width: 1199px)"...srcset="http://example.com/content/++attr++img_data/++thumb++md:w1200?_=..." />...<source media="(min-width: 1200px)"...srcset="http://example.com/content/++attr++img_data/++thumb++lg:w1600?_=..." />...<img style="width: 100%;" class=""... alt="" src="http://example.com/content/++attr++img_data/++thumb++md:w1200?_=..." />...</picture>\n'

Tests cleanup:

    >>> from pyams_utils.registry import set_local_registry
    >>> set_local_registry(None)
    >>> manager.clear()
    >>> transaction.commit()
    >>> tearDown()
