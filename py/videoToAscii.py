import os 
import sys
import cv2
from PIL import Image
import time

start_time = time.time()
seconds = 0.01
frame_count = 0
ascii_frame_count = 0

# Ascii characters used to create the output 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generate_frame(image,new_width=70):
	global frame_count
	global ascii_frame_count
	new_image_data = pix2chars(resized_gray_image(image))
	#time.sleep(0.5)
	total_pixels = len(new_image_data)

	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

    #f = open("myfile.txt", "x")
	sys.stdout.write(ascii_image)
	frame_count += 1
	if int(frame_count) % 10 == 0:
		ascii_frame_count += 1
		f = open("testToAscii.txt", "a")
		f.write("\n"+ascii_image+"\n <break> asciiFrameCount="+str(ascii_frame_count)+" frameCount="+str(frame_count))
		f.close()

	# os.system('cls' if os.name == 'nt' else 'clear')

	#export to json
	# {
	# 	"1":"qweqwe",
	# 	"2":"qasdasd"
	# }




cap = cv2.VideoCapture("test2.mp4")

while True:

	ret,frame = cap.read()
	cv2.imshow("frame",frame)
	# current_time = time.time()
	# elapsed_time = current_time - start_time
	# if elapsed_time > seconds:
	# 	generate_frame(Image.fromarray(frame))
	# 	start_time = time.time()
	generate_frame(Image.fromarray(frame))
	cv2.waitKey(1)