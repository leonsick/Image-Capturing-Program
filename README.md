# Image-Capturing-Program
This program helps anyone looking to generate their own training data for image recognition or object detection source images in bulk quickly and already sorted by class.

## Getting started

### First step: Clone the repo


### Second step: Set up the application
To setup the program, simply run the following command in the cloned folder:
python3 setup.py --classes all your classes seperated with spaces

Example:
python3 setup.py --classes apple banana orange cucumber

## Third step: Start capturing images for your project
To start capturing, call the capture_images.py script with the following flags:
- --number: The number of images you want to capture (required)
- --iclass: The image class you want to capture data for (e.g. banana) (required)
- --dataset: Whether you want to capture data for your train or test set (required)
- --size: You can choose between "large" (1080 x 720), "medium" (600 x 600) and "small" (300 x 300) image size (optional, default is "large").

Start capturing images with your webcam by calling:
python3 capture_images.py --number [NUMBER] --iclass [ICLASS] --dataset [DATASET]

Example:
python3 capture_images.py --number 20 --iclass apple --dataset train --size small
