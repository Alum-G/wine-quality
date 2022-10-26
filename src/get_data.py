import pandas as pd
import yaml
import logging
import argparse
import os

def read_configurations(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_configurations(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep = ",")
    return df

if __name__ ==  "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    #args.add_argument("--datasource", default = (os.path.join("dataset", "winequality.csv")))

    parsed_args = args.parse_args()
    get_data(config_path = parsed_args.config)