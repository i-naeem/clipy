"""
crop.py - Crop the videos to 3/4 ratio
usage: 
    python crop.py clips_folder output_folder
    
    clips_folder: The folder that have raw uncropped video files.
    output_folder: The folder where new cropped videos will be stored.
    
example:
    python crop.py clips_dir output_dir
    
    This will take all the clips from clips_dir and crop every clip by 3/4 ratio after that it will save the clips to output_dir.
"""
import os
import sys
import subprocess
from pathlib import Path

input_dir = sys.argv[1]
output_dir = sys.argv[2]


for in_file in Path(input_dir).glob('*.mp4'):
    out_file = os.path.join(output_dir, in_file.name)
    command = f"ffmpeg -i {in_file} -filter:v crop=ih*3/4:ih -c:a copy {out_file}"
    subprocess.run(command)
