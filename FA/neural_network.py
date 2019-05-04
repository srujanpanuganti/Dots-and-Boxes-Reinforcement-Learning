# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:12:40 2019

@author: Srujan Panuganti
"""

import tensorflow as tf
import numpy as np

class neural:
    def __init__(self,
                 n_features,
                 n_classes,
                 training_epochs = 2,
                 n_neurons_in_h1 = 60,
                 n_neurons_in_h2 = 60,
                 learning_rate = 0.01
                 ):
        
        self.training_epochs = training_epochs
        self.n_features = n_features
        self.n_classes = n_classes
        
        self.X = tf.placeholder(tf.float32, [None, self.n_features], name='features')
        self.Y = tf.placeholder(tf.float32, [None, self.n_classes], name='labels')


        ## first layer 
        self.W1 = tf.Variable(tf.truncated_normal([self.n_features, n_neurons_in_h1], mean=0, stddev=1 / np.sqrt(self.n_features)), name='weights1')
        self.b1 = tf.Variable(tf.truncated_normal([n_neurons_in_h1],mean=0, stddev=1 / np.sqrt(self.n_features)), name='biases1')


        self.y1 = tf.nn.tanh((tf.matmul(self.X, self.W1)+self.b1), name='activationLayer1')


        ## second layer
        self.W2 = tf.Variable(tf.random_normal([n_neurons_in_h1, n_neurons_in_h2],mean=0,stddev=1/np.sqrt(self.n_features)),name='weights2')
        self.b2 = tf.Variable(tf.random_normal([n_neurons_in_h2],mean=0,stddev=1/np.sqrt(self.n_features)),name='biases2')
        #activation function(sigmoid)
        self.y2 = tf.nn.sigmoid((tf.matmul(self.y1,self.W2)+self.b2),name='activationLayer2')


        #output layer
        self.Wo = tf.Variable(tf.random_normal([n_neurons_in_h2, self.n_classes], mean=0, stddev=1/np.sqrt(self.n_features)), name='weightsOut')
        self.bo = tf.Variable(tf.random_normal([self.n_classes], mean=0, stddev=1/np.sqrt(self.n_features)), name='biasesOut')
        # actuvation  function - softmax
        self.a = tf.nn.softmax((tf.matmul(self.y2, self.Wo) + self.bo), name='activationOutputLayer')
        

        # cost function
        self.cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.Y * tf.log(self.a),reduction_indices=[1]))


    def train(self,tr_features,tr_labels,ts_features,keep_prob,ts_labels):
        
            #optimizer
        train_step = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.cross_entropy)


        #compare predicted value from network with the expected value/target
        correct_prediction = tf.equal(tf.argmax(self.a, 1), tf.argmax(self.Y, 1))

        #accuracy determination
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name="Accuracy")
        
        # initialization of all variables

        initial = tf.global_variables_initializer()
        
        
        
        #creating a session
        
        with tf.Session() as sess:
        
            sess.run(initial)
        
            writer = tf.summary.FileWriter("./TrainResults")
        
            writer.add_graph(sess.graph)
        
            merged_summary = tf.summary.merge_all()
        
            
        
            # training loop over the number of epoches
        
            batchsize=10
        
            for epoch in range(self.training_epochs):
        
                for i in range(len(tr_features)):
        
        
        
                    start=i
                    end=i+batchsize
        
                    x_batch=tr_features[start:end]
        
                    y_batch=tr_labels[start:end]
        
                    
        
                    # feeding training data/examples
        
                    sess.run(train_step, feed_dict={self.X:x_batch , self.Y:y_batch,keep_prob:0.5})
        
                    i+=batchsize
        
                # feeding testing data to determine model accuracy
        
                y_pred = sess.run(tf.argmax(self.a, 1), feed_dict={self.X: ts_features,keep_prob:1.0})
        
                y_true = sess.run(tf.argmax(ts_labels, 1))
        
                summary, acc = sess.run([merged_summary, accuracy], feed_dict={self.X: ts_features, self.Y: ts_labels,keep_prob:1.0})
        
                # write results to summary file
        
                writer.add_summary(summary, epoch)
        
                # print accuracy for each epoch
        
                print('epoch',epoch, acc)
        
                print ('---------------')
        
                print(y_pred, y_true)
