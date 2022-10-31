import pandas


def choose_language(file_name):
    csv_dataframe = pandas.read_csv(f"data/{file_name}")
    csv_dictionary = {value.symbol: [value.pronunciation, value.meaning] for (key, value) in csv_dataframe.iterrows()}
    print(csv_dictionary)
    return csv_dictionary


def update_language(file_name, new_dict_symbol, new_dict_pronunciation, new_dict_translation):
    # with open(f"data/{file_name}", mode="a") as file:
    #     file.write("\n")
    updated_dataframe = pandas.DataFrame({'symbol': [new_dict_symbol], "pronunciation": [new_dict_pronunciation],
                                          "meaning": [new_dict_translation], })
    updated_dataframe.to_csv(f"data/{file_name}", mode="a", index=False, header=False)
