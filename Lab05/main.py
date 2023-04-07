# packages required

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
# consider some real labels and some predicted labels (obtained by the ML algorithm - a classifier)
# we want ot estimate the error of prediction (classification)

# Problem specification:
# input: realLabels, computedLabels - arrays of the same length containing binary labels (some discrete values)
# output: accuracy, precision, recall - real values in range [0,1]


# a balanced data set (each class containes the same numer of samples)

realLabels =        ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
computedLabels =    ['spam', 'ham', 'ham', 'spam', 'spam', 'ham']



# suppose that 'spam' is the positive class (and 'ham' is the negative class)
# compute the prediction performance

# version 1 - using the sklearn functions
def evalClassificationV1(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)
    return acc, precision, recall 

# version 2 - native code
def evalClassificationV2(realLabels, computedLabels, pos, neg):
    # noCorrect = 0
    # for i in range(0, len(realLabels)):
    #     if (realLabels[i] == computedLabels[i]):
    #         noCorrect += 1
    # acc = noCorrect / len(realLabels)
    acc = sum([1 if realLabels[i] == computedLabels[i] else 0 for i in range(0, len(realLabels))]) / len(realLabels)

    # TP = 0
    # for i in range(0, len(realLabels)):
    #     if (realLabels[i] == 'spam' and computedLabels[i] == 'spam'):
    #         TP += 1
    TP = sum([1 if (realLabels[i] == pos and computedLabels[i] == pos) else 0 for i in range(len(realLabels))])
    FP = sum([1 if (realLabels[i] == neg and computedLabels[i] == pos) else 0  for i in range(len(realLabels))])
    TN = sum([1 if (realLabels[i] == neg and computedLabels[i] == neg) else 0 for i in range(len(realLabels))])
    FN = sum([1 if (realLabels[i] == pos and computedLabels[i] == neg) else 0  for i in range(len(realLabels))])

    precisionPos = TP / (TP + FP)
    recallPos = TP / (TP + FN)
    precisionNeg = TN / (TN + FN)
    recallNeg = TN / (TN + FP)

    return acc, precisionPos, precisionNeg, recallPos, recallNeg
    
acc, prec, recall = evalClassificationV1(realLabels, computedLabels, ['spam', 'ham'])

# acc, prec, recall = evalClassificationV2(realLabels, computedLabels, 'spam', 'ham')

print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)