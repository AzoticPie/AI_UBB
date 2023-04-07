import numpy as np
class MyLinearMultivariateRegression:
    def __init__(self):
        self.intercept_ = None
        self.coef_ = None

    # learn a linear multivariate regression model by using training inputs (x) and outputs (y) 
    def fit(self, x1, x2, y):
        n = len(x1)
        sx1, sx2 = sum(x1), sum(x2)
        sy = sum(y)
        sx1_2 = sum(i * i for i in x1)
        sx2_2 = sum(i * i for i in x2)
        sx1x2 = sum(i * j for (i,j) in zip(x1, x2))
        sxy = sum(i * j for (i,j) in zip(x1, y))
        sxy2 = sum(i * j for (i,j) in zip(x2, y))
        A = np.array([[n, sx1, sx2], [sx1, sx1_2, sx1x2], [sx2, sx1x2, sx2_2]])
        b = np.array([sy, sxy, sxy2])
        self.coef_ = np.linalg.solve(A, b)
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]

    # predict the outputs for some new inputs (by using the learnt model)
    def predict(self, x1, x2):
        return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in zip(x1, x2)]

