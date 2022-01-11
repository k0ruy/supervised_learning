# Libraries:
import numpy as np
from math import sqrt


# mean of the actual values of the target:
def y_mean_array(array: np.ndarray) -> np.ndarray:
    y_bar = np.mean(array, dtype=np.float64)
    y_m_a = np.array([y_bar] * len(array))
    return y_m_a


def bias(actual: np.ndarray, predicted: np.ndarray) -> float:
    bias_value = sqrt(sum((actual - y_mean_array(predicted)) ** 2))
    return bias_value


def variance(predicted: np.ndarray) -> float:
    var = float(np.mean((y_mean_array(predicted) - predicted) ** 2, dtype=np.float64))
    return var


# distance between the actual and the predicted values of the target, using the sum of squares method, the larger the
# value, the worse the model.
def sum_of_squares(actual: np.ndarray, predicted: np.ndarray) -> float:
    sse = sum((actual-predicted) ** 2)
    return sse


# between sum of squares, plus within sum of squares, computed above.
def total_sum_of_squares(actual: np.ndarray) -> float:
    tss = sum((actual - y_mean_array(actual)) ** 2)
    return tss


# mean of the sum of squares, just divide the sum of squares by the number of samples:
def mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    mse = sum_of_squares(actual, predicted) / len(actual)
    return mse


# square root of the mean squared error
def root_mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    return sqrt(mean_squared_error(actual, predicted))


# Coefficient of determination, how much can be explained by the independent variable.
def r_squared(actual: np.ndarray, predicted: np.ndarray) -> float:
    r_2 = 1 - sum_of_squares(actual, predicted) / total_sum_of_squares(actual)
    return r_2


if __name__ == '__main__':
    # Change with the data provided:
    y_actual = np.array([1, 2, 3, 4, 5])
    y_predicted = np.array([1.6, 2.5, 2.9, 3, 4.1])
    root_mean_squared_error = root_mean_squared_error(y_actual, y_predicted)
    r_squared = r_squared(y_actual, y_predicted)

    print(f"Bias: {bias(y_actual, y_predicted)}")
    print(f"Variance:{variance(y_predicted)}")
    print(f"Root Mean Square Error: {root_mean_squared_error}")
    print(f"R squared: {r_squared}")
