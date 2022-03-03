import glob
import os
import random
from shutil import move
import tqdm

def split_data(SOURCE, DESTINATION, SPLIT_SIZE):
    source_files = os.listdir(SOURCE)
    print(f"Files in source before split: {len(os.listdir(SOURCE))}")
    randomized_source_files = random.sample(source_files, len(source_files))

    valid_split = randomized_source_files[int(SPLIT_SIZE * len(source_files)): ]
    
    for file in valid_split:
        if os.path.getsize(os.path.join(SOURCE, file)) != 0:
            move(os.path.join(SOURCE, file), os.path.join(DESTINATION, file))
        else:
            print(f"{file} has size 0, so ignoring")

    print(f"Files in source after split: {len(os.listdir(SOURCE))}")

split_size = .85

for dir in tqdm.tqdm(os.listdir('train')):
    print(dir)
    source_dir = os.path.join("train", dir)
    dest_dir = os.path.join("valid", dir)
    split_data(source_dir, dest_dir, split_size)
