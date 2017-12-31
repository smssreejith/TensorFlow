import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(10.0)

c = a * b

d = tf.sin(c)

e = b / d

with tf.Session() as sess:
    ans = sess.run(e)

print(ans)
