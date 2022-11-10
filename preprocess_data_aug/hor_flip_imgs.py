import cv2
import os
import tensorflow as tf

folder = "/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output3/train/class_4/"

i = 0
for filename in os.listdir(folder):
    image = folder + filename
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hor_image = tf.image.flip_left_right(image)

    new_name = "hor_" + filename
    
    tf.keras.preprocessing.image.save_img(f"/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output3/train/aug4/{new_name}", hor_image)
    i+=1
    print(i)