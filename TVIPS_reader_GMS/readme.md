## TVIPS reader for Gatan Microscopy Suite (GMS) / Digital Micrograph (DM)

Uses the integrated miniconda python environment in GMS3 to read in TVIPS tiff files (Tietz Video and Image Processing Systems).   
The [tifffile](https://pypi.org/project/tifffile/) package is used to read in the image and metadata (stored as taggroup 'TVIPS_metadata'). Stored metadata can be expanded/changed to your needs.  
The images are currently opened as single images, but the script should be adjustable to load them directly as a stack in GMS.

![tvipsreader](https://github.com/lukmuk/em-stuff/blob/main/TVIPS_reader_GMS/images/tvipsreader.PNG)

### Installing tifffile (or other packages)
After a clean installation of GMS3, the tifffile package is probably missing and has to be installed (see also this [Youtube video](https://www.youtube.com/watch?v=-pQMytgaRVg)):
  * You can find the path to the relevant miniconda enviroment in GMS under `File --> Global info... --> Scripting --> Python version`. 
  * Open an windows terminal/conda terminal and activate the GMS environment, e.g. something like `conda activate C:\ProgramData\Miniconda3\envs\GMS_VENV_PYTHON`
  * Run `conda install tifffile -c conda-forge` to install the package.  

### Notes
For older versions of GMS/DM without the implemented Python environment you can use this [DM script](https://stackoverflow.com/questions/58892185/how-to-import-tif-calibration-from-tvips-camera-into-dm) to load single TVIPS tiff images.





