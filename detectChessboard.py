import cv2
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt


def getImagePath():
    imagePath = Path.cwd() / "img" / "emptyboard.jpg"
    print(imagePath)
    return str(imagePath)


def readImage(path):
    img = cv2.imread(path)
    if img is None:
        print("Error: Image not found.")
        sys.exit()
    return img


def processImage(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a bilateral filter to reduce noise
    # https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
    bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
    
    return bilateral
    

def displayImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def main():
    path = getImagePath()
    img = readImage(path)
    preprocessed_image = processImage(img)
    displayImage(preprocessed_image)
    

if __name__ == "__main__":
    main()
