import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

input_dir = '../Gas_vers_scurta'
output_dir = '../Gas_vers_scurtaout'
os.makedirs(output_dir, exist_ok=True)

# *ECS.txt skips the paired *ECS_unupload.txt files
for file_path in glob.glob(os.path.join(input_dir, '*ECS.txt')):
    data = []
    with open(file_path, 'r') as f:
        next(f)
        for line in f:
            parts = line.split(',')
            if len(parts) > 5:
                data.append({
                    'Date': parts[0].split()[0],
                    'Time': parts[0].split()[1],
                    'NO2': float(parts[1])
                })

    df = pd.DataFrame(data)
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    plt.figure(figsize=(12, 6))
    plt.plot(df['DateTime'], df['NO2'])
    plt.xlabel('Date and Time')
    plt.ylabel('NO2 Level')
    plt.title('NO2 Level Over Time')
    plt.grid(True)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, base_name + '.png')
    plt.savefig(output_path)
    plt.close()
    print(f'Saved {output_path}')
