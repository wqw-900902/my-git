import tensorflow as tf
import time

t1=time.time()
print(t1)
a = tf.constant(10)
b = tf.constant(20)
with tf.Session() as sess:
    c = a+b
    r = sess.run(c)
    print(r)
t2=time.time()
print(t2-t1)