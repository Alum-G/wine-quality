import argparse
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from getData import read_configurations
import json


def metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def train_and_evaluate(configuration_path):
    configuration = read_configurations(configuration_path)
    train_data_path = configuration["split_data"]["training_path"]
    test_data_path = configuration["split_data"]["test_path"]
    random_state = configuration["base"]["random_state"]

    alpha = configuration["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = configuration["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    output = [configuration["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep = ",")
    test = pd.read_csv(test_data_path, sep = ",")

    train_y = train[output]
    test_y = test[output]

    train_x = train.drop(output, axis = 1)
    test_x = test.drop(output, axis = 1)

    

    lr = ElasticNet(
        alpha = alpha,
        l1_ratio = l1_ratio,
        random_state = random_state
        )

    lr.fit(train_x, train_y)
    predicted_values = lr.predict(test_x)

    (rmse, mae, r2) = metrics(test_y, predicted_values)

    print("Elastic Model (alpha =%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print(" RMSE: %s" % rmse)
    print(" MAE: %s" % mae)
    print(" R2: %s" % r2)

    scores_file = configuration["report"]["scores"]
    parameters = configuration["report"]["parameters"]

    with open(scores_file, "w") as g:
        scores = {
            "RMSE" : rmse,
            "MAE" : mae,
            "r2" : r2
        }
        json.dump(scores, g)

    with open(parameters, "w") as g:
        parameters = {
            "alpha" : alpha,
            "l1_ratio" : l1_ratio,
        }
        json.dump(parameters, g)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--configuration", default = "params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(configuration_path = parsed_args.configuration)
