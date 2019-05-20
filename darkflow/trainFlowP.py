from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo_custom2.cfg", 
           "load": -1,
           "batch": 8,
           "epoch": 100,
           "gpu": 1.0,
           "train": True,
           "annotation": "E:/Projects/defectTracker/BBox-Label-Tool/AnnotationsXML/001/",
		   "labels": "one_label.txt",
           "dataset": "E:/Projects/defectTracker/BBox-Label-Tool/Images/001/"}
           
tfnet = TFNet(options)
tfnet.train()
tfnet.savepb()