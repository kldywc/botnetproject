

#imports
from __future__ import division
import os, sys
from sklearn.linear_model import *
from sklearn.svm import *
from sklearn.metrics import confusion_matrix
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from keras.models import *
from keras.layers import Dense, Activation
from keras.optimizers import *
import threading


import matplotlib.pyplot as plt
conf = sklearn.metrics.c
onfusion_matrix(y_true,y_pred)
plt.imshow(conf,cmap='binary',
interpolation='None')
plt.show()




class SVMModel(threading.Thread):
    """Threaded Support Vector Machine Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        for i in range(9):
            X[:, i] = (X[:, i] - X[:, i].mean()) / (X[:, i].std())
        for i in range(9):
            XT[:, i] = (XT[:, i] - XT[:, i].mean()) / (XT[:, i].std())
        svModel = SVC(kernel='rbf')
        svModel.fit(X, Y)
        sd = svModel.predict(XT)
        acc =  (sum(sd == YT) / len(YT) * 100)
	print("Confusion Matrix: ",confusion_matrix(sd, YT))
        print("Accuracy of SVM Model: %.2f"%acc+' %')
        print('=' * 100)
        if self.accLabel: self.accLabel.set("Accuracy of SVM Model: %.2f" % (acc)+' %')



class DTModel(threading.Thread):
    """Threaded Decision Tree Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        dtModel = DecisionTreeClassifier()
        dtModel.fit(X, Y)
        sd = dtModel.predict(XT)
        acc = (sum(sd == YT) / len(YT) * 100)
	print("Confusion Matrix: ",confusion_matrix(sd, YT))
        print("Accuracy of Decision Tree Model: %.2f" % acc+' %')
        print('=' * 100)
        if self.accLabel: self.accLabel.set("Accuracy of Decision Tree Model: %.2f" % (acc)+' %')


class NBModel(threading.Thread):
    """Threaded Gaussian Naive Bayes Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        nbModel = GaussianNB()
        nbModel.fit(X, Y)
        sd = nbModel.predict(XT)
        acc = (sum(sd == YT) / len(YT) * 100)
	print("Confusion Matrix: ",confusion_matrix(sd, YT))
        print("Accuracy of Gaussian Naive Bayes Model: %.2f" % acc +' %')
        print('='*100)
        if self.accLabel: self.accLabel.set("Accuracy of Gaussian Naive Bayes Model: %.2f" % (acc)+' %')


class KNNModel(threading.Thread):
    """Threaded K Nearest Neighbours Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        for i in range(9):
            X[:, i] = (X[:, i] - X[:, i].mean()) / (X[:, i].std())
        for i in range(9):
            XT[:, i] = (XT[:, i] - XT[:, i].mean()) / (XT[:, i].std())
        knnModel = KNeighborsClassifier()
        knnModel.fit(X, Y)
        sd = knnModel.predict(XT)
        acc = (sum(sd == YT) / len(YT) * 100)
	print("Confusion Matrix: ",confusion_matrix(sd, YT))
        print("Accuracy of KNN Model: %.2f" % acc+' %')
        print('=' * 100)
        if self.accLabel: self.accLabel.set("Accuracy of KNN Model: %.2f" % (acc)+' %')



