import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

input_dir = '../18_0904_0908'
output_dir = '../18_0904_0908out'
os.makedirs(output_dir, exist_ok=True)

for file_path in glob.glob(os.path.join(input_dir, '*.txt')):
    data = []
    with open(file_path, 'r') as f:
        # Skip the header line
        next(f)
        for line in f:
            parts = line.split(',')
            # Check if the line has enough columns
            if len(parts) > 5:
                # Extract Date, Time, and NO2. Extract only the time part from the Time column. Convert NO2 to float.
                data.append({
                    'Date': parts[0].split()[0],
                    'Time': parts[0].split()[1],  # Extract only the time part
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
