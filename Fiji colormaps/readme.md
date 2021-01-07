# Fiji colormaps

Some colormaps/look-up-tables for Fiji/ImageJ which I use for plotting qualitative 2D maps, e.g. EELS or EDS maps.

The LUTs were created in Fiji via the `Image --> Color --> Edit LUT...` dialogue. The RGB values are from the sources below.

## Colorbrewer

Colorbrewer [maps](https://colorbrewer2.org/?type=qualitative&scheme=Set1&n=9).

## Matplotlib

Colors are taken from [here](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) and converted to 8-bit RGB for Fiji via

```python
import matplotlib.colors
[print(i*255) for i in matplotlib.colors.to_rgb('tab:red')] #insert other colors
```