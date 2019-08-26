import os
from glob import glob
import pandas as pd
import json

sensor = 'accel'

list_files = pd.Series(glob(f'../data/{sensor}*json'))

print(f"Total files {len(list_files)}")

total_files = sorted(list_files.str.split('/', expand=True)[2].str.split('.',expand=True)[0].str.split('_',expand=True)[1].astype(int))

# check if continuous
assert len(total_files) == total_files[-1] +1, print(len(total_files), total_files[-1] +1)

data = {}
list_ts = []
for fn in list_files:
    with open(fn) as f:
        d = json.load(f)
        timestamp = int(d['real_timestamp'][-1]) # when devide to seconds some of the timestamp are already existed
        list_ts.append(timestamp)
        if timestamp in d.keys():
            print(f"{timestamp} existed")
        del d['real_timestamp']
        del d['timestamp']
        data[timestamp] = d
        
        
# write data
output_dir = "../data/processed_data"
os.makedirs(output_dir, exist_ok = True)
with open(f"{output_dir}/{sensor}_flat_still.json", 'w') as f:
    json.dump(data, f, indent=4)
