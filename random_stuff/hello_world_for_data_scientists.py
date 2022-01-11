# Every time we do classification we are dealing with a specific context.

# In this context we want to identify the species of an isis flower by an amateur botanist.
# In this case she collected 4 numerical measurements (in centimeter).$
# It's important to have consistency of measurement for the same feature.
# She also has measurements of previously identified flowers by an expert, given the measurements.
# It's important to know the reliability of the supervision (ground rule).

# We also assume that the botanist only collects 3 kinds of flowers, setosa, versicolor and virginica.
# This is a strong assumption that limits the number of targets to 3.

# Goal, building an ML that predicts the species of a new Iris flower.

# This is a supervised learning problem, furthermore it's a classification problem.

# The classes are 3, so this is a multiclass classification problem with 3 classes (setosa ...)

# A label (desired output) is what needs to be associated to our data points.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


if __name__ == '__main__':
    iris_dataset = load_iris()

    print("Key of iris dataset: \n{}" .format(iris_dataset.keys()))
    print(iris_dataset["DESCR"][:500] + "\n...")
    print('Target names:\n {}' .format(iris_dataset['target_names']))
    print('Data names:\n {}' .format(iris_dataset['data'][:10]))
    print('frame names:\n {}' .format(iris_dataset['frame']))
    print('feature names:\n {}' .format(iris_dataset['feature_names']))
    print('filename:\n {}' .format(iris_dataset['filename']))
    print('Type of the data:\n {}' .format(type(iris_dataset['data'])))
    print('Shape of the data:\n {}' .format(iris_dataset['data'].shape))
    # the shape tells us there are 150 samples and 4 features.
    print('The first 5 rows of data: \n{}' .format(iris_dataset['data'][:5]))
    # for some algorithms the difference between the measurements may be important,
    # in those cases the features should be scaled, normalized, ... .

    print('Type of the target:\n {}' .format(type(iris_dataset['target'])))
    print('Shape of the target:\n {}' .format(iris_dataset['target'].shape))

    # The first thing to do after having selected the model is to make sure the model is able to predict well the new
    # label. We will measure how we can trust the model. So we need an evaluation phase. We cannot use the same dataset
    # to evaluate the model!.
    # We want to generate a metric (a number) that tells us how well the model is going to perform on new data.

    # We need a test data or hold-out data, related to the methodology of how the data is kept aside.

    # How much data do you need? No common answer but good practices, 80 - 20 or 75 - 25, are acceptable splits of
    # train - test. 50 - 50 is only to be used if there is a strong reason to do so.

    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                        iris_dataset['target'],
                                                        random_state=0,
                                                        test_size=0.25)
    # 0.25 is the default for the test size so could be omitted. other than that the module needs the observation and
    # the target

    # the random_state is the seed for the pseudo random number generator that creates the indexes for the data,
    # mimicking a shuffle of the dataset. Here it's specified so results can be compared.

    # X are the independent variables and y are the labels. See notes.
    print('Shape of the X_train:\n {}' .format(X_train.shape))
    print('Shape of the y-train:\n {}' .format(y_train.shape))
    print('Shape of the X-test:\n {}' .format(y_test.shape))
    print('Shape of the y-test:\n {}' .format(y_test.shape))

    # Looking at the data, very important step for both supervised and unsupervised learning.
    # - "Guestimate" how hard the problem is going to be.
    # - In real life also helps you to inspect the data and see if you need to clean-
    # in this case flowers measured in inches instead of cm.
    # up to 80% of the time goes into prepping the data.

    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])
    pd.plotting.scatter_matrix(iris_dataframe, c=y_train,
                                     figsize=(15, 15), marker='o', s=60, alpha=.8)
    # just looking at the pair of features is insufficient to check if a model is feasible
    plt.show()

    knn = KNeighborsClassifier(n_neighbors=1)

    knn.fit(X_train, y_train)
    # behind the scenes there are many tuning parameters, for instance how k nearest neighbor measures distance,
    # the default is minkowski.

    X_new = np.array([[5, 2.9, 1, 0.2]])
    print("X_new.shape: {}" .format(X_new.shape))

    prediction = knn.predict(X_new)

    print("Prediction: " .format(prediction))

    # Do we trust the model? We don't really know, the best known metric for testing
    # is called accuracy, how many are correct amongst all the predictions?

    y_pred = knn.predict(X_test)

    print(y_pred)
    print(y_test)

    print(np.mean(y_pred == y_test))

    # alternative:

    print("The accuracy is: {:.2f}" .format(knn.score(X_test, y_test)))











