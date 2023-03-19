import os
from pathlib import Path
import subprocess
import sys

input_dir = sys.argv[1]
output_dir = sys.argv[2]


for in_file in Path(input_dir).glob('*.mp4'):
    out_file = os.path.join(output_dir, in_file.name)
    command = f"ffmpeg -i {in_file} -filter:v crop=ih*3/4:ih -c:a copy {out_file}"
    subprocess.run(command)
