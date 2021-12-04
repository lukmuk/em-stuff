# Fiji colormaps

Some colormaps/look-up-tables (LUTs) for Fiji/ImageJ which I use for plotting qualitative 2D maps, e.g. EELS or EDS maps.

The LUTs were created in Fiji via the `Image --> Color --> Edit LUT...` dialogue. All LUTs start from black and gradually change to the specified color. The RGB values for the latter are from the sources below.

The `.lut` files have to be copied to the `luts` folder of your ImageJ/Fiji installation. They can then be applied by searching their name in the search bar or under `Image --> Lookup Tables`.

## Colorbrewer

Colorbrewer [light](https://colorbrewer2.org/?type=qualitative&scheme=Set3&n=12#type=qualitative&scheme=Set3&n=12) (12) and [dark](https://colorbrewer2.org/?type=qualitative&scheme=Set1&n=9) (9) qualitative maps. Named `cb_<style>_<color>`.

## Matplotlib Tableau

Named `mpl_tab_<color>`. Colors are taken from [here](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) and converted to 8-bit RGB for Fiji via

```python
import matplotlib.colors
[print(i*255) for i in matplotlib.colors.to_rgb('tab:red')] #insert other colors
```

## Paul Tol

Named `pt_<style>_<color>`. Selected colormaps from [Paul Tol's](https://personal.sron.nl/~pault/) website, which are also used by [SciencePlots](https://github.com/garrettj403/SciencePlots).