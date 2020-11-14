## TVIPS reader for Gatan Microscopy Suite (GMS) / Digital Micrograph (DM)

Uses the newly integrated miniconda python enviroment in GMS3 to read in TVIPS tiff files (Tietz Video and Image Processing Systems).  
It uses [tifffile](https://pypi.org/project/tifffile/) to read in the image and metadata (stored as taggroup 'TVIPS_metadata').  
Stored metadata can be easily expanded/changed to your needs.  

![tvipsreader](/images/tvipsreader.png)

## Installing tifffile (or other packages)
After a clean installation of GMS3, the tifffile package is probably missing and has to be installed. (See also https://www.youtube.com/watch?v=-pQMytgaRVg)  
You can find the path to the relevant miniconda enviroment in GMS under "File --> Global info... --> Scripting --> Python version".  
Open an anaconda prompt window and activate the enviroment, e.g. something like "conda activate C:\ProgramData\Miniconda3\envs\GMS_VENV_PYTHON".  
Then run "pip install tifffile" to install the package.  

## Notes:
For older versions you can use this DM script: https://stackoverflow.com/questions/58892185/how-to-import-tif-calibration-from-tvips-camera-into-dm  





