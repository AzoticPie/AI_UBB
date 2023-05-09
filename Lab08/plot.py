import matplotlib.pyplot as plt 

def plot_metrics(df, target_label='target', predicted_label='predicted'):
    error = 0.0
    for t1, t2 in zip(df[target_label], df[predicted_label]):
        if (t1 != t2):
            error += 1
    error = error / df.shape[0]
    print("classification error (manual): ", error)

    from sklearn.metrics import accuracy_score
    error = 1 - accuracy_score(df[target_label], df[predicted_label])
    print("classification error (tool): ", error)

def plot_gen_mse(computed_mses, name):
    fig = plt.plot(range(computed_mses.size), computed_mses, 'r-', label='mse')
    plt.title(f'final {name} = ' + str(computed_mses[-1]))
    plt.xlabel('Generation')
    plt.ylabel('mse')
    plt.show()