import os
import glob
import math
import pandas as pd
import matplotlib.pyplot as plt

input_dir = '../Gas_vers_scurta'
output_dir = '../Gas_vers_scurtaout'
os.makedirs(output_dir, exist_ok=True)

# Unupload schema (16 fields, lowercase header):
#   0:datetime  1:no2  2:nh3  3:co  4:t  5:rh  6:p  7:deviceid  8:no2ppb
#   9:latitude  10:longitude  11:elevation   <-- skip per request
#   12:id  13:pm1  14:pm25  15:pm10
#
# Columns to plot with their CSV index.
columns_with_index = [
    ('no2', 1), ('nh3', 2), ('co', 3), ('t', 4),
    ('rh', 5), ('p', 6), ('deviceid', 7), ('no2ppb', 8),
    ('id', 12), ('pm1', 13), ('pm25', 14), ('pm10', 15),
]


def parse_float(s):
    """Return float, or NaN for empty / unparseable cells (id/lat/lon/elev are often blank)."""
    s = s.strip()
    if not s:
        return math.nan
    try:
        return float(s)
    except ValueError:
        return math.nan


for file_path in glob.glob(os.path.join(input_dir, '*_unupload.txt')):
    data = []
    with open(file_path, 'r') as f:
        next(f)  # skip header
        for line in f:
            parts = line.split(',')
            # Need all 16 fields; filters truncated/garbage lines like Meteo.py does.
            if len(parts) >= 16:
                row = {
                    'Date': parts[0].split()[0],
                    'Time': parts[0].split()[1],
                }
                for col, idx in columns_with_index:
                    row[col] = parse_float(parts[idx])
                data.append(row)

    df = pd.DataFrame(data)
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    for col, _ in columns_with_index:
        plt.figure(figsize=(12, 6))
        plt.plot(df['DateTime'], df[col])
        plt.xlabel('Date and Time')
        plt.ylabel(col)
        plt.title(f'{col} Over Time')
        plt.grid(True)

        output_path = os.path.join(output_dir, f'{base_name}_{col}.png')
        plt.savefig(output_path)
        plt.close()
        print(f'Saved {output_path}')
