import tensorflow as tf
import numpy as np
import os
from convnet_builder import ConvNetBuilder
from mobilenet_v2 import mobilenet_v2
from Reader import ActionGenerator

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
gpu_options = tf.GPUOptions(allow_growth=True)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
#######################################################################
train_dataset_path = '/psk/OSNRdata/trainmiprobonly/'
test_dataset_path = '/psk/OSNRdata/testmiprobonly/'
checkpoint_path_finetune = '/modelmiprobonly/'
batch_size = 64
nClasses = 6
height = 224
width = 224
training_epoch = 300
imgs = tf.placeholder(tf.float32, [None, height, width, 3])
target = tf.placeholder("int64",[None])
#print('##########################################')
validation_ratio = 0.3
obj = ActionGenerator(train_dataset_path, test_dataset_path, nClasses, batch_size, validation_ratio)
print('##############################################')
learning_rate = 1e-5
########################################################################
cnn = ConvNetBuilder(input_op = imgs,
               input_nchan = 3,
               phase_train = True,
               use_tf_layers = False,
               data_format='NHWC')
mobilenet_out, end = mobilenet_v2(cnn = cnn, num_classes = nClasses, dropout_keep_prob=1)
total_loss = tf.losses.softmax_cross_entropy(onehot_labels=tf.one_hot(target, nClasses), logits = mobilenet_out)
mean_loss = tf.reduce_mean(total_loss)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate, name='Adam')
train_step = optimizer.minimize(mean_loss)
prediction = tf.equal(tf.argmax(mobilenet_out, 1), tf.argmax(tf.one_hot(target, nClasses), 1))
accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
################################################################################
saver = tf.train.Saver()
print('saver is done ############################')
sess.run(tf.global_variables_initializer())
print('training start! ###############################')
saver.restore(sess, '/modelmiprobonly/modelfinetune_di.ckpt-61')
#print('successfully restore!')
#################################################################################
for epoch in range(1, training_epoch+1):
    batch_list = obj.train_batch_list()
    all_acc = 0
    all_cost = 0
    total_batch = len(batch_list)
    for i, batch in enumerate(batch_list):
        input_imgs, labels = obj.get_train_batch(batch, height, width)
        #print("hereherehere",input_imgs.shape)
        sess.run(train_step, feed_dict={imgs:input_imgs, target:labels})
        cost = sess.run(mean_loss, feed_dict={imgs:input_imgs, target:labels})
        acc = accuracy.eval(feed_dict={imgs: input_imgs, target:labels}, session=sess)
        all_acc += acc
        all_cost += cost
    print("========================================================== epoch"+str(epoch)+" ========================================================")
    print("train accuracy:", all_acc/total_batch, " Fusion loss:", all_cost/total_batch)
    if epoch % 10 == 0 :
        batch_list = obj.test_batch_list()
        all_acc = 0
        all_cost = 0
        total_batch = len(batch_list)
        for i, batch in enumerate(batch_list):
            input_imgs, labels = obj.get_train_batch(batch, height, width)
            #print(input_imgs.shape)
            acc = accuracy.eval(feed_dict={imgs: input_imgs, target:labels}, session=sess)
            all_acc += acc
        print("test accuracy:", all_acc/total_batch)
    if epoch % 10 == 0 :    
        checkpoint_path = os.path.join(checkpoint_path_finetune, 'modelfinetune_di.ckpt')
        saver.save(sess, checkpoint_path, global_step=epoch+1)
        print("saved to " + checkpoint_path)
