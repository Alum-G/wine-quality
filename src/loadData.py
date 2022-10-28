### This file will read the data from the data source, clean it and save in the data/raw

import os 
from getData import read_configurations, get_data
import argparse

def load_and_save(configuration_path):
    configuration = read_configurations(configuration_path)
    df = get_data(configuration_path)
    cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = configuration["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep = ",", index = False, header = cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--configuration", default = "params.yaml")
    #args.add_argument("--datasource", default = (os.path.join("dataset", "winequality.csv")))

    parsed_args = args.parse_args()
    load_and_save(configuration_path = parsed_args.configuration)