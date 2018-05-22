import tensorflow as tf
g=tf.Graph()
with g.as_default():
    x=tf.constant(10,name="x_c")
    y=tf.constant(20,name="y_c")
    sum=tf.add(x,y,name="sum")
    z=tf.constant(30,name="z_c")
    sum=tf.add(z,sum)
    with tf.Session() as  sess:
        print(sum.eval())
