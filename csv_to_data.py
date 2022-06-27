import pandas as pd


class CsvToData(object):
    def __init__(self):
        pass

    def read_data(data_name: str):
        data = pd.read_csv(data_name)
        return data

    def get_data_address(addr_name, data):
        return data[addr_name]
