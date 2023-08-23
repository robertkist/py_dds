from enum import Enum


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
