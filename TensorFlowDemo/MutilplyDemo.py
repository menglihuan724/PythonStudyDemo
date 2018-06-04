import tensorflow as tf
# with tf.Graph().as_default(), tf.Session() as sess:
#     # Task: Reshape two tensors in order to multiply them
#
#     # Here are the original operands, which are incompatible
#     # for matrix multiplication:
#     a = tf.constant([5, 3, 2, 7, 1, 4])
#     b = tf.constant([4, 6, 3])
#     a_change=tf.reshape(a,[2,3])
#     b_change=tf.reshape(b,[3,1])
#     c=tf.matmul(a_change,b_change)
#     print(c.eval())

with tf.Graph().as_default(), tf.Session() as sess:
    col_1=tf.Variable(tf.random_uniform([10,1],minval=1,maxval=7,dtype=tf.int32))
    col_2=tf.Variable(tf.random_uniform([10,1],minval=1,maxval=7,dtype=tf.int32))
    sum=tf.add(col_1,col_2)
    res=tf.concat(values=[col_1,col_2,sum],axis=1)
    sess.run(tf.global_variables_initializer())
    print(res.eval())