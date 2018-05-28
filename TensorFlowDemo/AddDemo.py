import tensorflow as tf
with tf.Graph().as_default():
    x=tf.constant([1,2,3,4,5],dtype=tf.int32)
    y=tf.ones(5,dtype=tf.int32)
    sum=tf.add(x,y)
    with tf.Session():
        print(sum.eval())
        with tf.Graph().as_default():
    #A scalar (0-D tensor).
    scalar = tf.zeros([])

    # A vector with 3 elements.
    vector = tf.zeros([3])

    # A matrix with 3 rows and 4 columns.
    matrix = tf.zeros([3, 4])

    with tf.Session() as sess:
        print( 'scalar has shape', scalar.get_shape(), 'and value:\n', scalar.eval())
        print('vector has shape', vector.get_shape(), 'and value:\n', vector.eval())
        print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.eval())

with tf.Graph().as_default():
    # Create a six-element vector (1-D tensor).
    primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

    # Create a constant scalar with value 1.
    ones = tf.constant(1, dtype=tf.int32)

    # Add the two tensors. The resulting tensor is a six-element vector.
    just_beyond_primes = tf.add(primes, ones)

    with tf.Session() as sess:
        print (just_beyond_primes.eval())