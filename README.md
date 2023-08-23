# py_dds_dev

pyDDS is a loader for .DDS files for Python 3.9 and newer. It's a pure Python package without any external
runtime dependencies.

Supported texture formats:
- 
- BC1 with (DXT1a) and without alpha (DXT1c)
- BC2 (DXT2 / DXT3)
- BC3 (DXT4 / DXT5)
- DX10 BC1
- DX10 BC2
- DX10 BC3
- uncompressed, with (32bpp) and without alpha (24bpp)

Notes:
- Only 2D textures are supported. No volume textures and no cube maps.
- With the exception of Uncompressed 24 bit images, all images have an alpha channel. However this alpha channel may be 
  completely set to opaque. In tha case of DXT1 there is also no distinction in the format between DXT1a and DXT1c with
  many encoders, so this info has to be gotten from elsewhere (e.g. from a file naming convention).
  In practical terms, this means that unless you're dealing with a Uncompressed 24bpp image, assume that it has an alpha channel.
  Of course, you're free to discard the alpha information at your own discretion.
- Example DDS files can be found in the `example_images` folder.
- An example for loading and displaying a DDS image using Qt can be found in the `examples` folder
  (make sure to have PySide6 installed)

## Usage

Importing the package and loading an image:
```python
import py_dds

try:
    dds = py_dds.DDSImage("foo.dds")
except py_dds.DDSException as e:
    print(e)
```

Getting the image properties:
```python
width: int = dds.width(mip=0)  # get width for Mip map 0 (the largest Mip map)
height: int = dds.height(mip=0)  # get height for Mip map 0
number_of_mip_maps: int = dds.mip_count()
dds_format: py_dds.DDSFormat = dds.format()
```
Methods which require a `mip=` input to choose a mip map will raise an `IndexError` if an invalid
mip map has been specified.

Interpreting the file format: The DDSFormat is an enum which can be used to check the compression used. The DDSFormat enum is defined such:
```python
class DDSFormat(Enum):
    """supported DDS formats, including DX9 and DX10 formats"""
    DXT1 = "DXT1"  # includes DXT1a, DXT1c
    DXT3 = "DXT3"  # includes DXT2, DXT3
    DXT5 = "DXT5"  # includes DXT3, DXT4
    UNCOMPRESSED32 = "UNCOMPRESSED32"
    UNCOMPRESSED24 = "UNCOMPRESSED24"
    DXGI_FORMAT_BC1_UNORM_SRGB = "DXGI_FORMAT_BC1_UNORM_SRGB"
    DXGI_FORMAT_BC2_UNORM_SRGB = "DXGI_FORMAT_BC2_UNORM_SRGB"
    DXGI_FORMAT_BC3_UNORM_SRGB = "DXGI_FORMAT_BC3_UNORM_SRGB"
```

Getting a specific mip map from the image:
```python
def set_pixel_callback(x: int, y: int, r: int, g: int, b: int, a: int) -> None:
    """
    :param x: X coordinate
    :param y: Y coordinate
    :param r: sRGB Red (0 - 255)
    :param g: sRGB Green (0 - 255)
    :param b: sRGB Blue (0 - 255)
    :param a: Alpha (0 - 255)
    """
    # insert your own code here to draw to e.g. a byte buffer, a QImage, a PIL image, etc.

dds.draw(set_pixel_callback=set_pixel_callback, mip=0)  # draws Mip map 0 via the specified callback
```
