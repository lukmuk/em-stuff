# This is a python script meant to be run in GMS3.X with python support.
# Missing python packages can be installed in the GMS miniconda enviroment.
# Reads in a stack of TVIPS .tifs, optionally saves them as dm3.
# Some metadata is read and saved as tags in GMS -> can be changed/expanded to your desire.

import DigitalMicrograph as DM
import tifffile as tiff
import glob
import os
import time

folder = input('Folder path to TVIPS .tifs: ')
files = glob.glob(folder+'\*.tif')

savedm3 = input('Save files as dm3? (Yes=1, No=0)')
if savedm3 == '1':
	dm3path = folder+'\dm3'
	try: os.mkdir(dm3path)
	except: FileExistsError: print("Directory " , dm3path ,  " already exists")

print('Reading TVIPS tifs...')
print('Folder: ', folder)
print('tif-files found: ', len(files))

for f in files:
	with tiff.TiffFile(f) as tif:
		#Image data
		data = tif.asarray()
		
		#Create image and set data
		img = DM.CreateImage(data)
		
		#Read TVIPS tags
		tag1 = tif.pages[0].tags['TVIPS']

		#Calibration: Depends on mode: 0= bright field, 1=dark field carthesian, 2= dark field conical, 3= diffraction
		#Only consider 0, 1, and 3 for now...
		if tag1.value['TemMode'] == 0: #BF/HRTEM
			img.SetDimensionCalibration(0, 0, tag1.value['PixelSizeX'], 'nm', 0)
			img.SetDimensionCalibration(1, 0, tag1.value['PixelSizeY'], 'nm', 0)
		if tag1.value['TemMode'] == 1: #Dark field
			img.SetDimensionCalibration(0, 0, tag1.value['PixelSizeX'], 'nm', 0)
			img.SetDimensionCalibration(1, 0, tag1.value['PixelSizeY'], 'nm', 0)
		elif tag1.value['TemMode'] == 3: #Diffraction
			img.SetDimensionCalibration(0, 0, tag1.value['PixelSizeX']/1000, 'mrad', 0)
			img.SetDimensionCalibration(1, 0, tag1.value['PixelSizeY']/1000, 'mrad', 0)
		
		#Set image name and other metadata as tags
		#img.SetName(tag1.value['ImageName']) #from TVIPS metadata
		img.SetName(os.path.basename(f).split('.')[0]) #from filename
		
		#Get the images taggroup
		imgTG = img.GetTagGroup()
		imgTG.SetTagAsString('TVIPS_metadata:Misc:SaveTime', time.ctime(os.path.getmtime(f)))
		imgTG.SetTagAsString('TVIPS_metadata:Misc:AcquisitionTime', time.strftime('%H:%M:%S', time.gmtime(tag1.value['Time'])))
		imgTG.SetTagAsFloat('TVIPS_metadata:HighTension', tag1.value['TemHighTension'])
		imgTG.SetTagAsFloat('TVIPS_metadata:ExposureTime(ms)', tag1.value['ExposureTime'])
		if tag1.value['TemMode'] == 0:
			imgTG.SetTagAsFloat('TVIPS_metadata:Magnification', tag1.value['TemMagnification'])
		if tag1.value['TemMode'] == 1:
			imgTG.SetTagAsFloat('TVIPS_metadata:Magnification', tag1.value['TemMagnification'])
		if tag1.value['TemMode'] == 3:
			imgTG.SetTagAsFloat('TVIPS_metadata:CameraLength(mm)', tag1.value['TemMagnification'])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:MagnificationCorrection', tag1.value['TemMagnificationCorrection'])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:ImageShift:x', tag1.value['TemImageShift'][0])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:ImageShift:y', tag1.value['TemImageShift'][1])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:BeamShift:x', tag1.value['TemBeamShift'][0])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:BeamShift:y', tag1.value['TemBeamShift'][1])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:BeamTilt:x', tag1.value['TemBeamTilt'][0])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:BeamTilt:y', tag1.value['TemBeamTilt'][1])
		imgTG.SetTagAsFloat('TVIPS_metadata:SpotSize', tag1.value['TemIllumination'][0])
		imgTG.SetTagAsFloat('TVIPS_metadata:Misc:TEMMode', tag1.value['TemMode'])
		imgTG.SetTagAsString('TVIPS_metadata:Misc:CameraType', tag1.value['CameraType'])
		imgTG.SetTagAsString('TVIPS_metadata:Misc:FlatfieldDescription', tag1.value['FlatfieldDescription'])
		#Stage
		imgTG.SetTagAsFloat('TVIPS_metadata:StagePosition:x(um)', tag1.value['TemStagePosition'][0]*1e6)
		imgTG.SetTagAsFloat('TVIPS_metadata:StagePosition:y(um)', tag1.value['TemStagePosition'][1]*1e6)
		imgTG.SetTagAsFloat('TVIPS_metadata:StagePosition:z(um)', tag1.value['TemStagePosition'][2]*1e6)
		imgTG.SetTagAsFloat('TVIPS_metadata:StagePosition:alpha(deg)', tag1.value['TemStagePosition'][3])
		imgTG.SetTagAsFloat('TVIPS_metadata:StagePosition:beta(deg)', tag1.value['TemStagePosition'][4])
		
		#Display image
		img.ShowImage()
		
		#Optional: Save as dm3
		if savedm3 == '1':
			#img.SaveAsGatan3(dm3path+'\\'+tag1.value['ImageName']+'.dm3') #Get name from TVIPS tag, does not work well for tiling images
			img.SaveAsGatan3(dm3path+'\\'+os.path.basename(f).split('.')[0]+'.dm3') #Get filename directly
			

	del img
	del data

print('Finished importing.')