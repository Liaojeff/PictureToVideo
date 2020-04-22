import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
import os

#file path
img_root="./"

#set output video fps
fps=5
fourcc=VideoWriter_fourcc(*"MJPG")

#set output video
videoWriter=cv2.VideoWriter("22.mp4",fourcc,fps,(1920,1080))

im_names=os.listdir(img_root)
for im_name in range(len(im_names)):
	frame=cv2.imread(img_root+str(im_name)+'.jpg')
	print (im_name)
	videoWriter.write(frame)
	
videoWriter.release()
