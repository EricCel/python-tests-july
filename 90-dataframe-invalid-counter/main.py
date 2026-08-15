#Read a DataFrame and count how many rows contain valid values versus how many contain null or empty values.

#-Importing : The module
import pandas as pd, numpy as np, datetime

#-Creating : The DataFrame
data = {
    "user_id": [101, 102, 103, 104, 105, 106],
    "age": [25, -5, 30, np.nan, 150, 22],  # -5 and 150 are invalid ages
    "email": [
        "alex@example.com",
        "invalid_email_at_domain",  # Missing @ symbol
        None,
        "carol@example.com",
        "dan@domain.c",  # Invalid TLD format
        np.nan,
    ],
    "join_date": [
        "2023-01-15",
        "2023-02-30",  # Invalid date (Feb 30 doesn't exist)
        "2023-03-10",
        "not_a_date",  # Invalid string format
        "2023-05-01",
        None,
    ],
    "score": [88.5, 92.0, -10.0, 75.0, np.nan, 105.0],  # Scores below 0 or above 100 are invalid
}

user_data = pd.DataFrame(data)

#-Reading : The DataFrame
valid, invalid = 0,0
for n in range(user_data.shape[0]):
    row = user_data.iloc[n]
    row_valid = 0
    for data, n, key in zip(row, range(len(row)),user_data.keys()):
        if len(row) == 5:
            match n:
                case 0:
                    row_valid += 1
                    continue
                case 1:
                    if data >= 0 or data <= 120 or data != np.nan:
                        row_valid += 1
                case 2:
                    if len(str(data).replace('@','*').replace('.com','*').split('*')) == 3:
                        row_valid += 1
                case 3:
                    try:
                        datetime.datetime.fromisoformat(data)
                        row_valid += 1
                    except:
                        pass
                case 4:
                    if data >= 0 or data <= 10 or data != np.nan:
                        row_valid += 1
        else:
            raise IndexError("Len of data doens't match with the fields")
    if row_valid == 5:
        valid += 1
    else:
        invalid += 1

print(f'The DataFrame has {valid} valid rows and {invalid} invalid rows')