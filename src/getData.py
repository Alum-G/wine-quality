import pandas as pd
import yaml
import logging
import argparse
import os

def read_configurations(configuration_path):
    with open(configuration_path) as yaml_file:
        configuration = yaml.safe_load(yaml_file)
    return configuration

def get_data(configuration_path):
    configuration = read_configurations(configuration_path)
    path_to_data = configuration["data_source"]["s3_source"]
    df = pd.read_csv(path_to_data, sep = ",")
    return df

if __name__ ==  "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--configuration", default = "params.yaml")
    #args.add_argument("--datasource", default = (os.path.join("dataset", "winequality.csv")))

    parsed_args = args.parse_args()
    get_data(configuration_path = parsed_args.configuration)