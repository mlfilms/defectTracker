from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo_custom.cfg", 
           "load": "bin/yolo.weights",
           "batch": 8,
           "epoch": 100,
           "gpu": 1.0,
           "train": True,
           "annotation": "C:/Users/Eric/Downloads/soccer_ball_data/annotations/",
		   "labels": "ball_label.txt",
           "dataset": "C:/Users/Eric/Downloads/soccer_ball_data/images/"}
           
tfnet = TFNet(options)
tfnet.train()