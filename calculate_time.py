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
                'Manor': 16}


def main():
    free_time_sec = 21 * 60
    building_speed = 160.1
    formula = 1/(1+(building_speed/100))
    help = 0.99 ** 30
    sum = 0
    for building_key in names_levels.keys():
        df = pd.read_csv("building_info/" + building_key + ".csv")
        building_level = names_levels.get(building_key)
        small_df = df.iloc[:building_level]
        small_df["Orig. Time"] = small_df["Orig. Time"].apply(lambda x: x*formula)
        small_df["Orig. Time"] = small_df["Orig. Time"].apply(lambda x: x*help)
        small_df = small_df[(small_df['Orig. Time'] > free_time_sec)]
        print(small_df)
        subsum = small_df['Orig. Time'].sum()
        sum += subsum
        print(f'{subsum = }')

    print(f'sum is = {sum/86400}')


if __name__ == "__main__":
    main()