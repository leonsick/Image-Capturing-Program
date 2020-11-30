import os
import argparse
import cv2
import uuid
import random


parser = argparse.ArgumentParser(description='Take a specific number of images with a pause of 3 seconds.')
parser.add_argument('-n', '--number', type=int, help='`Specifiy the number of images you want to take.', required=True)
parser.add_argument('-ic', '--iclass', help='`Specifiy the class of images you want to take.', choices=['apple', 'banana', 'broccoli', 'paprika', 'aubergine', 'cucumber', 'orange', 'pear'], required=True)
parser.add_argument('-ds', '--dataset', help='`Specifiy the class of images you want to take.', choices=['train', 'test'], required=True)
parser.add_argument('-s', '--size', default="large", help='Specifiy the class of images you want to take. If no param is chosen, it will be random between small, medium and large', choices=['large', 'medium', 'small', 'random'])

args = parser.parse_args()
number_of_images = args.number
image_class = str(args.iclass)
dataset = str(args.dataset)
size = str(args.size)

camera = cv2.VideoCapture(0)

img_counter = 0

print("~~Image capturing device is started~~")
print("~~Press ESC to exit and SPACE to save an image~~")

while img_counter < number_of_images:
	status, image = camera.read()
	if not status:
		print("Image capture failed")
		break
	if size == "random":
		rand = random.randint(1, 3)
		print(rand)
		if rand == 1:
			size = "small"
		if rand == 2:
			size = "medium"
		if rand == 3:
			size = "large"
		print(size)
	if size == "small":
		image_resized = cv2.resize(image, (300, 300))
	elif size == "medium":
		image_resized = cv2.resize(image, (608, 608))
	else:
		image_resized = cv2.resize(image, (1080, 720))
	cv2.imshow("Press SPACE to save image", image_resized)
	
	k = cv2.waitKey(1)
	if k%256 == 27:
		# ESC pressed
		print("Escape hit, closing...")
		break
	elif k%256 == 32:
		# SPACE pressed
		img_uuid = uuid.uuid4()
		img_name = "{}_{}.png".format(image_class, img_uuid)
		path = "{}/dataset/{}/{}/".format(os.getcwd(), dataset, image_class)
		print(path + img_name)
		cv2.imwrite(path + img_name, image_resized)
		print("{} written!".format(img_name))
		img_counter += 1