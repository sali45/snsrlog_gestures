from FeatureSelection.FeatureSelection import principal_components
from pomegranate import *
import numpy as np


def hidden_markov_model(training, test):
    X = np.array(training)
    y = np.array([0, 1, 2])

    model_circle = HiddenMarkovModel.from_samples(MultivariateGaussianDistribution, 4, X[y == 0])
    model_wave = HiddenMarkovModel.from_samples(MultivariateGaussianDistribution, 4, X[y == 1])
    model_pickup = HiddenMarkovModel.from_samples(MultivariateGaussianDistribution, 2, X[y == 2])

    model = BayesClassifier([model_circle, model_wave, model_pickup])
    Z = model.predict(test)
    numpy.savetxt("FILENAME.csv", Z.reshape(1,-1), fmt='%d', delimiter=",")

hidden_markov_model(principal_components()[0], principal_components()[1])
