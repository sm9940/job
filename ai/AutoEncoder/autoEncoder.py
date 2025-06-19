# import tensorflow as tf
import tensorflow.compat.v1 as tf
# from tensorflow.keras.utils import np_utils
from tensorflow.python.keras.utils import np_utils
# from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist

tf.disable_v2_behavior()
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
y_train = np_utils.to_categorical(y_train)
y_test  = np_utils.to_categorical(y_test)

def plot_image(data, classes, width=28, height=28, row_len=3):
    for i in range(10):
        idxs = (classes == i)
        #./deeplearning/autoencoders = data[idxs][0:10]
        autoencoders = data[idxs][0:10]
        # print(idxs, end=" : "); print(autoencoders)

        for j in range(row_len):
            plt.subplot(row_len, 10, i + j*10 + 1)
            plt.imshow(autoencoders[j].reshape(width, height), cmap = "gray")
            if j == 0:
                plt.title(1)
            plt.axis("off")
    plt.show()
classes = np.argmax(y_train, 1)
plot_image(x_train, classes)

class Autoencoder(object):
    def __init__(self, sess, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.weights = {
            # "W_fc1" : tf.Variable(tf.truncated_normal([self.input_size,
            #                                            self.hidden_size], stddev=0.1), name="W_fc1"),
            # "W_fc2" : tf.Variable(tf.truncated_normal([self.hidden_size,
            #                                            self.input_size], stddev=0.1), name="W_fc1")
            "W_fc1" : tf.Variable(tf.random.truncated_normal([self.input_size,
                                                       self.hidden_size], stddev=0.1), name="W_fc1"),
            "W_fc2" : tf.Variable(tf.random.truncated_normal([self.hidden_size,
                                                       self.input_size], stddev=0.1), name="W_fc2")
        }
        self.biases = {
            "b_fc1": tf.Variable(tf.constant(0.1, shape=[self.hidden_size]), name="b_fc1"),
            "b_fc2" : tf.Variable(tf.constant(0.1, shape=[self.input_size]), name="b_fc2")
        }

        #model
        self.x_input = tf.placeholder(tf.float32, [None, self.input_size])
        self.hidden = tf.matmul(self.x_input, self.weights["W_fc1"]) + self.biases['b_fc1']
        self.hidden = tf.nn.relu(self.hidden)
        self.reconstruction = tf.matmul(self.hidden, self.weights["W_fc2"]) + self.biases['b_fc2']
        self.reconstruction = tf.nn.relu(self.reconstruction)

        #cost
        self.loss = tf.losses.mean_squared_error(self.reconstruction, self.x_input)
        learning_rate = 1e-4
        optimizer = tf.train.AdamOptimizer(learning_rate)
        self.optimizer = optimizer.minimize(self.loss)
    # end of function

# Hiper parameter
input_size = 28 * 28
hidden_size = 10 * 10
num_of_iter = 5000
batch_size = 1000

# sess = tf.InteractiveSession()
sess=tf.compat.v1.InteractiveSession()
ae = Autoencoder(sess, input_size, hidden_size)
init = tf.global_variables_initializer()
sess.run(init)

for i in range(num_of_iter) :
    # batch = mnist.train.next_batch(batch_size)
    batch = (x_train[i:(i+batch_size)], y_train[i:(i+batch_size)])##################
    batch_image_flat = batch[0].reshape(-1, 28*28)
    _, loss, reconstruction = sess.run([ae.optimizer, ae.loss, ae.reconstruction],
                                       feed_dict={ae.x_input : batch_image_flat})

    if i%1000 == 0:
        print("step: %d, loss: %g"%(i, loss))
        classes = np.argmax(batch[1], 1)
        print("Original Image (step: %d)"%(i))
        plot_image(batch[0], classes)
        print("")
        print("Reconstruction Image (step: %d)"%(i))
        reconstruction = reconstruction.reshape(-1, 28,28)
        plot_image(reconstruction, classes)
        # image_flat = mnist.train.image.reshape(-1, 28,28)
        image_flat = x_train.reshape(-1, 28*28)########################
        hidden = sess.run(ae.hidden, feed_dict = {ae.x_input: image_flat})
        classes = np.argmax(y_train, 1)
        print("Hidden layer Image")
        hidden = hidden.reshape(-1, 10, 10)
        plot_image(hidden, classes, 10, 10)
