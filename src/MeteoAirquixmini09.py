import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

input_dir = '../airquixmini09_cBivolaru/airquixmini09/GAS'
output_dir = '../airquixmini09_cBivolaru/airquixmini09/GASout'
os.makedirs(output_dir, exist_ok=True)

# All files in this folder (including *_unupload.txt) share the same 9-column
# header: DateTime,NO2,NH3,CO,T,RH,P,DeviceID,NO2ppb
columns = ['NO2', 'NH3', 'CO', 'T', 'RH', 'P', 'DeviceID', 'NO2ppb']

# *.txt picks up both *ECS.txt and *ECS_unupload.txt.
for file_path in glob.glob(os.path.join(input_dir, '*.txt')):
    data = []
    with open(file_path, 'r') as f:
        next(f)
        for line in f:
            parts = line.split(',')
            # Need DateTime + 8 numeric columns => at least 9 fields.
            if len(parts) >= 9:
                row = {
                    'Date': parts[0].split()[0],
                    'Time': parts[0].split()[1],
                }
                for i, col in enumerate(columns, start=1):
                    row[col] = float(parts[i])
                data.append(row)

    df = pd.DataFrame(data)
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    for col in columns:
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
