import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

c = a * b
d = a + b

e = d - c
f = d + c

g = f / e

with tf.Session() as sess:
    ans = sess.run(g)

print(ans)
