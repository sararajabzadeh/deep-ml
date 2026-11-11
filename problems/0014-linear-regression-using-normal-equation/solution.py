import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    multiplication = np.matmul(X.T, X)
    inverse = np.linalg.inv(multiplication)
    theta = inverse @ (X.T) @ y

    return np.round(theta, 4)