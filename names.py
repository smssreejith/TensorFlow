import tensorflow as tf

with tf.Graph().as_default():
    c1 = tf.constant(4,dtype=tf.float64,name='c')
    c2 = tf.constant(4,dtype=tf.int32,name='c')
print(c1.name)
print(c2.name)
#Objects residing within the same graph cannot have the same name TensorFlow forbids it. As a consequence, it will automatically add an underscore and a number to distinguish the two. Of course, both objects can have the same name when they are associated with different graphs.
