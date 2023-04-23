import pandas as pd
import matplotlib.pyplot as plt

def evalClassification(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, log_loss, ConfusionMatrixDisplay

    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)

    #loss = log_loss(realLabels, computedLabels, labels = labelNames)

    cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labelNames)
    fig, ax = plt.subplots(figsize=(8, 8))
    cm_display.plot(ax=ax)

    plt.title(f'Model Predictions vs Actual Measurements\nAccuracy = {acc:.4}\nPrecision = D: {precision[0]:.4} T: {precision[1]:.4} R: {precision[2]:.4}\nRecall = D: {recall[0]:.4} T: {recall[1]:.4} R: {recall[2]:.4}')
    plt.show()

    return acc, precision, recall 


df = pd.read_csv('data\\flowers.csv')

evalClassification(df['Type'], df['PredictedType'], ['Daisy', 'Tulip', 'Rose'])