

import requests
import pandas as pd

names_levels = {'Vault': 11,
                'Infirmary': 12,
                'Academy': 13,
                'Trading_Post': 14,
                'Quarry': 16,
                'Lumber_Mill': 16,
                'Farm': 16,
                'Mine': 16,
                'Workshop': 16,
                'Barrack': 16,
                'Watchtower': 16,
                'Manor': 16,
                'Castle': 17}


def convert_days_to_hours(time_string):
    days_in_sec = 0
    if 'd' in time_string:
        substring = time_string.split('d')
        days = int(substring[0])
        days_in_sec = days*86400
        time_string = substring[1]

    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time_string.split(':')))) + days_in_sec


def get_data(name):

    url = f'https://lordsmobile.fandom.com/wiki/{name}'

    response = requests.request("GET", url)

    list_of_dfs = pd.read_html(response.text,  decimal='.', thousands=',')

    if name == "Workshop":
        df = list_of_dfs[2]
    else:
        df = list_of_dfs[0]
    df=df.fillna("0")

    df["Orig. Time"] = df["Orig. Time"].apply(lambda x: convert_days_to_hours(x))

    df.to_csv('building_info/' + name + '.csv')


def main():
    for key in names_levels.keys():
        get_data(key)


if __name__ == '__main__':
    main()
