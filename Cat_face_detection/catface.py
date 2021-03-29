#construct argument parser and import packages
import argparse
import cv2
ap=argparse.ArgumentParser()
ap.add_argument("-i","--cats",required=True, help="Path where image is saved")
ap.add_argument("-c","--cascade", default="haarcascade_frontalcatface.xml", help="Cascade file used")
args=vars(ap.parse_args())

#reading the Image
image=cv2.imread(args["cats"])
#grayscale conversion
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector=cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=10, minSize=(75, 75))
#foor loop
for (i, (x,y,w,h)) in enumerate (rects):
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0),2)
    cv2.putText(image, "Cat #{}".format(i+1),(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0,255,0),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
