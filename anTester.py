imgPath = 'C:\Users\Eric Minor\TrackingML\defectTracker\images\circle_1.jpg'
xmlfilename = 'circle_1'

bboxList = []
im = Image.open(imgPath)
bboxList.append((10, 10, 20, 20))

createXMLAnnotation(imgPath, bboxList, im.size, self.xmlfilename)