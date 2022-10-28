import os
import argparse
from sklearn.model_selection import train_test_split
import pandas as pd
from getData import read_configurations


def train_test_split_data(configuration_path):
    configuration = read_configurations(configuration_path)
    raw_data_path = configuration["load_data"]["raw_dataset_csv"]
    train_data_path = configuration["split_data"]["training_path"]
    test_data_path = configuration["split_data"]["test_path"]
    split_ratio_path = configuration["split_data"]["test_size"]
    random_state_path = configuration["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep = ",")
    train, test = train_test_split(
        df,
        test_size = split_ratio_path,
        random_state= random_state_path
    )

    train.to_csv(train_data_path, sep = ",", index = False, encoding = "utf-8")
    test.to_csv(test_data_path, sep = ",", index = False, encoding = "utf-8")




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--configuration", default = "params.yaml")
    parsed_args = args.parse_args()
    train_test_split_data(configuration_path=parsed_args.configuration)