import pandas as pd

df = pd.read_excel("raw_text.ods", sheet_name = "Sheet1")

df = df.drop(columns =["Unknown"])

def sum_digits(code):
    total = 0
    for char in code:
        if char.isdigit():
            total += int(char)
    return total

df["SumCode"] = df["Code"].apply(sum_digits)

filtered_df = df[df["Description"].str.contains("Returns", na = False)]

filtered_df.to_csv('processed_data.csv', index = False)

























































