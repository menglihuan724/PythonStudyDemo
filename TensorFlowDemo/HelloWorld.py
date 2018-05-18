import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
hello=tf.constant('fuck the world')
sess=tf.Session()
print(sess.run(hello))