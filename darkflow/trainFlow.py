from darkflow.net.build import TFNet
import cv2
#dataset is the image folder
options = {"model": "cfg/yolo_custom2.cfg", 
           "load": "bin/yolo.weights",
           "batch": 8,
           "epoch": 100,
           "gpu": 1.0,
           "train": True,
           "annotation": "E:/Projects/fake/simulations/fortran/LandauGin/dataFolder/accumulated/out",
		   "labels": "one_label.txt",
           "dataset": "E:/Projects/fake/simulations/fortran/LandauGin/dataFolder/accumulated"}
           
tfnet = TFNet(options)
tfnet.train()
tfnet.savepb()