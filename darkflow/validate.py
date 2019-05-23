import shutil
import glob
import os

truthPath = os.path.abspath("C:/Users/Eric Minor/TrackingML/defectTracker/BBox-Label-Tool/AnnotationsXML/001/")
detectionPath = os.path.abspath("C:/Users/Eric Minor/TrackingML/defectTracker/images/out/")

mAPTruthPath = os.path.abspath("C:/Users/Eric Minor/TrackingML/defectTracker/mAP/input/ground-truth/")
mAPDetectionPath = os.path.abspath("C:/Users/Eric Minor/TrackingML/defectTracker/mAP/input/detection-results")


def wipeFolder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)



wipeFolder(mAPTruthPath)
wipeFolder(mAPDetectionPath)


filePattern = 	os.path.join(truthPath,"*.xml")
#print(filePattern)
for filename in glob.glob(filePattern):
    drive,pathAndFile = os.path.splitdrive(filename)
    path, file = os.path.split(pathAndFile)
    newFilename = os.path.join(mAPTruthPath,file)
    shutil.copyfile(filename,newFilename)
    #print(filename)
    
    
filePattern = 	os.path.join(detectionPath,"*.json")
#print(filePattern)
for filename in glob.glob(filePattern):
    drive,pathAndFile = os.path.splitdrive(filename)
    path, file = os.path.split(pathAndFile)
    newFilename = os.path.join(mAPDetectionPath,file)
    shutil.copyfile(filename,newFilename)
	
