import unittest
import numpy as np
import pandas as pd
from linear_regression import linear_regression
import numpy.testing as npt


class LinearRegressionTest(unittest.TestCase):
    def setUp(self):  # set up Unit Test
        self.X = pd.DataFrame(
            [[1.0, np.nan, 2.0], [12.0, 24.0, 36.0], [3.0, 6.0, 8.0], [8.0, 12.0, 9.0], [8.0, 10.0, 4.0]])
        self.y = pd.DataFrame([10.0, np.nan, 20.0, 40.0, 20.0])
        np.seterr(divide='ignore')  # ignore zero division warnings
        B_hat, standard_error, CI_lower, CI_upper, self.X_clean, self.y_clean = linear_regression(self.X, self.y)

    def test_nan(self):
        X = self.X.dropna().to_numpy()
        y = self.y.dropna().to_numpy()
        npt.assert_array_equal(X, self.X_clean)
        npt.assert_array_equal(y, self.y_clean)

    def test_empty(self):
        X = self.X.dropna()
        y = self.y.dropna()
        shape_X = np.shape(X)
        shape_y = np.shape(y)
        control_X = np.zeros(shape_X, dtype=bool)
        control_y = np.zeros(shape_y, dtype=bool)
        npt.assert_array_equal(control_X, pd.isnull(self.X_clean))
        npt.assert_array_equal(control_y, pd.isnull(self.y_clean))


if __name__ == "__main__":
    unittest.main()
