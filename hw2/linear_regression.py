import numpy as np
from scipy import stats


def linear_regression(X, y):
    B_hat, standard_error, CI_lower, CI_upper = None, None, None, None

    # perform list-wise deletion for handling NaN values
    X_clean = X.dropna().to_numpy()
    y = y.dropna().to_numpy()

    # adding 1 to the X matrix for the intercept
    one_column = np.ones((X_clean.shape[0], 1))
    X = np.concatenate((one_column, X_clean), axis=1)

    # finding B_hat using linear algebra
    B_hat = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))

    # finding y_hat values
    n = X.shape[1]
    h = np.ones((X.shape[0], 1))
    theta = B_hat.reshape(1, n)
    for i in range(0, X.shape[0]):
        h[i] = float(np.matmul(theta, X[i]))
    y_hat = h.reshape(X.shape[0])

    # finding the residuals
    e = np.subtract(y, y_hat)
    sigma_squared_numerator = np.dot(e.T, e)
    sample_no = X.shape[0]
    unbiased_denominator = sample_no - n

    # finding the variance of B_hat
    sigma_squared = np.true_divide(sigma_squared_numerator, unbiased_denominator)
    inverse = np.linalg.inv(np.dot(X.T, X))
    variance_B = np.dot(sigma_squared, inverse)
    var_B = np.diag(variance_B)

    # finding the standard error of B_hat
    standard_error = np.sqrt(var_B)

    # t statistics
    t = stats.t.ppf(1 - 0.025, unbiased_denominator)
    t_part = t * standard_error

    # finding the upper and lower credible intervals of 95%
    upper = np.add(theta, t_part)
    CI_upper = upper.reshape(-1, )
    lower = np.subtract(theta, t_part)
    CI_lower = lower.reshape(-1, )
    return B_hat, standard_error, CI_lower, CI_upper, X_clean, y
