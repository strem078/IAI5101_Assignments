import sys
print (sys.version)
# 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]
import tensorflow as tf
print("Tensorflow version: ")
print(tf.__version__)
print("Available devices for tensorflow use: ") 
print(tf.get_available_devices())