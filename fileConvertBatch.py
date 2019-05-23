import glob
import os
from fileConvertF import fileConvert

targetDir = "E:\\Projects\\fake\\defectTracker\\labels"
outDir = "E:\\Projects\\fake\\defectTracker\\labels\\out"

if not os.path.exists(outDir):
    os.makedirs(outDir)

filePattern = 	targetDir+"\\*.txt"   

for filename in glob.glob(filePattern):
    fileConvert(filename,outDir)

