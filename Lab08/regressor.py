import numpy as np
from sklearn.metrics import accuracy_score
import random

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(z):
    return np.exp(z) / np.sum(np.exp(z), keepdims=True)  

class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = [0.0]
        self.coef_ = []
        self.classes_ = [1, 2, 3]

    # use the gradient descent method
    # simple stochastic GD
    def fit(self, x, y, df_val, df_out, learningRate = 0.001, noEpochs = 2000):
        #self.coef_ = [[0.0 for _ in range(x.shape[1])]]   #beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        self.coef_ = [[random.random() for _ in range(x.shape[1])]]    #beta or w coefficients 

        self.classes_ = np.unique(y)
        results = np.array([])
        for _ in range(noEpochs):
            # shuffle the training examples in order to prevent cycles
            permutation = np.random.permutation(x.shape[0])
            x = x.iloc[permutation]
            y = y.iloc[permutation]
            
            for i in range(x.shape[0]): # for each sample from the training data
                ycomputed = sigmoid(self.eval(x.iloc[i]))     # estimate the output
                crtError = ycomputed - y.iloc[i]     # compute the error for the current sample
                # update the coefficients
                self.coef_[0] -= learningRate * crtError * x.iloc[i]
                self.intercept_[0] -= learningRate * crtError * 1

            predicted = np.array(self.predict(df_val))
            results = np.append(results, accuracy_score(df_out, predicted))
        
        return results
    def eval(self, xi):
        yi = self.intercept_[0]
        for j in range(len(xi)):
            yi += self.coef_[0][j] * xi[j]
        return yi 

    def predict(self, X):
        z = np.dot(X, self.coef_[0].T) + self.intercept_[0]
        ypredicted = sigmoid(z)
        return self.classes_[np.argmax(ypredicted, axis=1)]

    def predict2(self, X):
        # compute predicted probabilities for each class
        proba = self.predict_proba(X)
        
        # determine the number of unique target values in the training data
        n_classes = len(self.classes_)

        # if there is only one class, return the predicted probabilities for that class
        if n_classes == 1:
            return np.ravel(proba)

        # if there are two classes, return the predicted probabilities for the positive class
        if n_classes == 2:
            return proba[:, 1]

        # if there are more than two classes, return the class with the highest predicted probability
        predicted = np.argmax(proba, axis=1)
        return np.array([self.classes_[i] for i in predicted])

    def predict_proba(self, X):
        # compute predicted probabilities for each class
        z = np.dot(X, self.coef_[0].T) + self.intercept_[0]
        proba = 1 / (1 + np.exp(-z))

        # if there is only one class, return the predicted probabilities for that class
        if len(self.classes_) == 1:
            return np.column_stack([1 - proba, proba])

        # otherwise, stack the predicted probabilities for each class
        return np.column_stack([1 - proba, proba])
    

class MyLogisticRegression2:
    def _init_(self, learning_rate=0.001, num_iterations=1000, fit_intercept=True):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.fit_intercept = fit_intercept
        self.accuracy = []
        self.classes_ = []

    def fit(self, X, y, Z, t):
        if self.fit_intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))

        self.classes_ = np.unique(y)
        self.coef_ = np.zeros((len(self.classes_), X.shape[1]))

        for i, c in enumerate(self.classes_):
            binary_y = (y == c).astype(int)
            theta = np.zeros(X.shape[1])

            for j in range(self.num_iterations):
                z = np.dot(X, theta)
                h = sigmoid(z)
                gradient = np.dot(X.T, (h - binary_y)) / len(binary_y)
                theta -= self.learning_rate * gradient

                predictions = self.predict(Z, ok=True)
                a = 100 * np.mean(predictions == t)
                self.accuracy.append(a)

            self.coef_[i, :] = theta

    def predict(self, X, ok=False):
        if not ok:
            if X.shape[1] != len(self.coef_[0]):
                # Add a column of ones to the beginning of X
                ones_column = np.ones((X.shape[0], 1))
                X = np.concatenate((ones_column, X), axis=1)
        else:
                # Add a column of ones to the beginning of X
                ones_column = np.ones((X.shape[0], 1))
                X = np.concatenate((ones_column, X), axis=1)
        # Compute the dot product of X with the transposed coefficient matrix and apply the sigmoid function
        z = np.dot(X, self.coef_.T)
        y_pred_prob = sigmoid(z)

        # Return the class label with the highest probability for each row of y_pred_prob
        return self.classes_[np.argmax(y_pred_prob, axis=1)]
    

class MyLogisticRegression3:
    def __init__(self):
        self.intercept_ = [0.0]
        self.coef_ = []
        self.classes_ = []

    def fit(self, X, y, y_oh, df_val, df_out, learningRate = 0.1, noEpochs = 15000):
        #self.coef_ = [0.0 for _ in range(x.shape[1])]   #beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        self.classes_ = np.unique(y)
        results_loss = np.array([])
        results_acc = np.array([])
        for c in range(len(self.classes_)):
            self.coef_.append(np.array([random.random() for _ in range(X.shape[1])]))   #beta or w coefficients 
            self.intercept_.append(0.0)

        for epoch in range(noEpochs):
            print(epoch)
            for c in range(len(self.classes_)):
                permutation = np.random.permutation(X.shape[0])
                X = X.iloc[permutation]
                y = y.iloc[permutation]
                y_oh = y_oh.take(permutation, axis=0)

                ycomputed = self.predict(X, c)
                sig = sigmoid(ycomputed)
                grad_w = self.dldw(X, y_oh[:,c], sig)
                grad_b = self.dldb(y_oh[:,c], sig)
                self.coef_[c] = np.array(self.update(self.coef_[c], grad_w,learningRate))
                self.intercept_[c] = self.update(self.intercept_[c], grad_b,learningRate)
        
            predicted = np.array(self.predicted(df_val))
            results_acc = np.append(results_acc, accuracy_score(df_out, predicted))
            results_loss = np.append(results_loss, np.min(self.loss(y_oh[:, c], sig)))
            #print(type(np.argmin(self.loss(y_oh[:, c], sig), axis=0)))
            #results_loss = np.append(results_loss, self.loss(df_out, np.max(self.sigs(df_val), axis=0)))
        
        return results_acc, results_loss

    def sigs(self, X):
        sigs = []
        for c in range(len(self.classes_)):
            yhat = self.predict(X, c)
            sig = sigmoid(yhat)
            sigs.append(sig)
        return np.array(sigs)
    
    def predicted(self, X):
        sigs = []
        for c in range(len(self.classes_)):
            yhat = self.predict(X, c)
            sig = sigmoid(yhat)
            sigs.append(sig)
        return np.argmax(sigs,axis = 0)

    def predict(self, x, c):
        #print(len(self.coef_[c]))
        temp = np.matmul(self.coef_[c], x.T)
        return temp + self.intercept_[c]  

    def loss(self, y, sig):
        return -((y*np.log(sig)+(1-y)*np.log(1-sig)).mean())
    
    def dldw(self, x, y, sig):
        temp = np.reshape([sig-y], (x.shape[0], 1))
        temp = temp * x
        return temp.mean(axis = 0)
    
    def dldb(self, y, sig):
        return (sig-y).mean(axis = 0)

    def update(self, w, grad, lr):
        return w-(grad*lr)