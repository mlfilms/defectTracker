Tools for object detection
BBox-Label-Tool
https://github.com/puzzledqs/BBox-Label-Tool

This program allows you to annotate images.
Usage:
clone the repo
Put images you want to annotate into /images/02 (or other sub directory)
In the root folder, run python main.py
Must use python 2, the code is incompatible with python 3
Enter the director name at the top of the GUI and hit load
Click twice to draw bounding boxes, then press next to go to the next image
The annotations compatible with the ML algorithm are stored in AnnotationsXML

YOLOv2 with darkflow
YOLO works by dividing images up into a grid and using a CNN to draw bounding boxes in that grid that contain certain object classes. It makes a large, fixed number of predictions but only keeps the predictions with high confidence scores. YOLO has been pretrained on a variety of large datasets to detect real-world objects such as cars and people, however for our application we only need the network to be trained for a single class, defects.

Setup: 
Much of this is taken from https://medium.com/coinmonks/detecting-custom-objects-in-images-video-using-yolo-with-darkflow-1ff119fa002f

For this section, you will need to use python 3
Clone the repo
git clone https://github.com/thtrieu/darkflow.git
This contains all the code necessary to train and run a YOLOv2 model in python
To install dependencies, run the commands:
pip install tensorflow
install opencv-contrib-python
pip install numpy

Training:
Cd into the darkflow root directory
Run the command:
python flow --model cfg/yolo-new.cfg --labels one_label.txt --train --trainer adam --dataset "C:\Users\Eric Minor\TrackingML\fake\BBox-Label-Tool\Images\001" --annotation "C:\Users\Eric Minor\TrackingML\fake\BBox-Label-Tool\AnnotationsXML\001" --lr 0.001

but replace "C:\Users\Eric Minor\TrackingML\fake\BBox-Label-Tool\Images\001" with the path to the images on your machine and replace  "C:\Users\Eric Minor\TrackingML\fake\BBox-Label-Tool\AnnotationsXML\001" with the path to the annotations on your machine.

The model will now be trained. This will take awhile. If you have a machine with a good GPU, add --gpu 1.0 to the end of the command

Every 250 steps the model will be saved
Running:
In the darkflow root directory, run the command
python flow --model cfg/yolo-new.cfg --imgdir "C:\Users\Eric Minor\TrackingML\fake\images" --load -1 --labels one_label.txt

replacing "C:\Users\Eric Minor\TrackingML\fake\images" with the path to the images you want annotated.
An out folder should be created in the directory you specified containing the annotated images.

Testing with Circles:
For testing purposes, use circlemaker.m to generate noisy images with circles along with annotations for those images. Images will be stored in /images and annotations (not xml) will be stored in /labels. To get the xml annotations, copy the images into BBox-Label-Tool as previously mentioned and put the text annotations in the Labels folder in BBox-Label-Tool. When you run the tool, you should be able to just click next repeatably to generate the xml annotations.




