import tensorflow as tf
import numpy as np

tf.set_random_seed(777)  ##그래프 수준의 난수 시드 설정

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 2]) ##직접 값을 주지 않는 것
Y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([2, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name='bias')

##시그모이드를 사용하는 가정
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

##hypothesis가 0.5보다 크면 True, 나머지는 False
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        _, cost_val, w_val = sess.run(
            [train, cost, W], feed_dict={X: x_data, Y: y_data}
        )

        if step % 100 ==0:
            print(step, cost_val, w_val)

    h, c, a = sess.run(
        [hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data}
    )
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

##출력값##

'''
Hypothesis: [[ 0.5]
  [0.5]
  [0.5]
  [0.5]]
Correct: [[ 0.]
  [ 0.]
  [ 0.]
  [ 0.]]
Accuracy:  0.5
'''
