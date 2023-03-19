"""
concat.py - Concatenate multiple videos to a single video

usage:
    python concat.py clips_dir output_dir
    
    clips_dir: The dir with short clips
    output_dir: The new dir where concatenated files will be stored

example:
    python concat.py videos merged_videos
    This will take every random 20 files from the videos dir and merge those 20 and save it to merged_videos dir.
    
"""
from random import shuffle
from pathlib import Path
from pprint import pprint
import subprocess
import sys
import os

input_dir = sys.argv[1]
output_dir = sys.argv[2]
# The number of files to be combined 10 means 10 files will become 1.
combine_number = 20

files = list(Path(input_dir).glob('*.mp4'))
shuffle(files)
files = [files[i:i+combine_number]
         for i in range(0, len(files), combine_number)]


for index, files_list in enumerate(files):
    with open('tmp_file.txt', 'w') as fp:
        for f in files_list:
            fp.write(f"file '{str(f)}'\n")

    output_file = os.path.join(output_dir, f"video__{index}.mp4")
    command = f"ffmpeg -f concat -safe 0 -i tmp_file.txt -c copy {output_file}"
    subprocess.run(command)
    os.remove("tmp_file.txt")
