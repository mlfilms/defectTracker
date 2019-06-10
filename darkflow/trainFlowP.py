from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo_custom2.cfg", 
           "load": -1,
           "batch": 8,
           "epoch": 1,
           "gpu": 1.0,
           "train": True,
           "lr": 1e-5,
           "annotation": "E:/Projects/fake/simulations/randomDefects/accumulated/out",
		   "labels": "one_label.txt",
           "dataset": "E:/Projects/fake/simulations/randomDefects/accumulated/outMess"}
           
tfnet = TFNet(options)
tfnet.train()
tfnet.savepb()