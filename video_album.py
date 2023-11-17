import os
import cv2

path = "images"

images = []

for img in os.listdir(path):
    name, ext = os.path.splitext(img)

    file_name = path + "/" + img

    images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape

size = (width, height)

out = cv2.VideoWriter("album.mp4", cv2.VideoWriter_fourcc(*'DIVX'), .8, size)

for i in range(0, count-1):
    frame = cv2.imread(images[i])

    out.write(frame)

out.release()
# cv2.waitKey(0)