from tkinter import *
import pandas


def choose_language(file_name):
    csv_dataframe = pandas.read_csv(f"data/{file_name}")
    csv_dictionary = {value.symbol: [value.pronunciation, value.meaning] for (key, value) in csv_dataframe.iterrows()}

    return csv_dictionary


def update_language(file_name, csv_dictionary):
    # csv_dictionary = {}
    # i = 0
    # csv_dataframe = pandas.read_csv(f"data/{file_name}")
    # csv_data_symbols = csv_dataframe["symbol"].to_list()
    # csv_data_pronunciation = csv_dataframe["pronunciation"].to_list()
    # csv_data_meaning = csv_dataframe["meaning"].to_list()
    #
    # for entry in csv_data_symbols:
    #     csv_dictionary[entry] = [csv_data_pronunciation[i], csv_data_meaning[i]]
    #     i += 1

    print(csv_dictionary)
