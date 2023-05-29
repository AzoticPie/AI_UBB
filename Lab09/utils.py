import numpy as np

def keep_row(row, keep_indexes):
    if row.name in keep_indexes:
        return True
    return False


def separate_data_df(df, labels, split = 0.8):
    indexes = [i for i in range(df.shape[0])]
    train_sample = np.random.choice(indexes, int(split * len(indexes)), replace = False)

    df_train = df[labels].copy()
    df_validate = df[labels].copy()

    df_train['keep'] = df.apply(keep_row, axis=1, keep_indexes=train_sample)
    df_validate['keep'] = df.apply(keep_row, axis=1, keep_indexes=train_sample)

    df_train = df_train[df_train['keep'] == True]
    df_validate = df_validate[df_validate['keep'] == False]

    return df_train.drop('keep', axis=1), df_validate.drop('keep', axis=1)

def evalMultiClass(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix

    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])
    return acc, precision, recall, confMatrix
