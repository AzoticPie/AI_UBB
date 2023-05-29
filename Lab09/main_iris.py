from sklearn import neural_network
from sklearn.datasets import load_iris
from sklearn import neural_network
import normalisation
import utils
import plot

#read dataset as dataframe
data = load_iris(as_frame=True)
df = data.frame
target_names = data.target_names
labels = list(df.columns)

#normalize data
df = normalisation.sklearn_norm(df, labels[:-1])

#divide into train and test data
df_train, df_validate = utils.separate_data_df(df, df.columns)

#invatare cu tool
classifier = neural_network.MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=200, solver='sgd', random_state=1, learning_rate_init=.1)
classifier.fit(df_train[labels[:-1]], df_train[labels[-1]])

df_validate['predicted'] = classifier.predict(df_validate[labels[:-1]])

acc, prec, recall, cm = utils.evalMultiClass(df_validate[labels[-1]], df_validate['predicted'], target_names)

plot.plotConfusionMatrix(cm, target_names, "iris classification")

print('acc: ', acc)
print('precision: ', prec)
print('recall: ', recall)