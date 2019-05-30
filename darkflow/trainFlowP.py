from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo_custom2.cfg", 
           "load": -1,
           "batch": 8,
           "epoch": 1000,
           "gpu": 1.0,
           "train": True,
           "lr": 1e-6,
           "annotation": "E:/Projects/fake\simulations/fortran\LandauGin/run20190529_144637/data-k-1.00-beta-10.000-mu-0.000/out",
		   "labels": "one_label.txt",
           "dataset": "E:/Projects/fake/simulations/fortran/LandauGin/run20190529_144637/data-k-1.00-beta-10.000-mu-0.000/images"}
           
tfnet = TFNet(options)
tfnet.train()
tfnet.savepb()