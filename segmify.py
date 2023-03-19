"""
segmify.py - Create equal segments of a video
usage:
    python segmify.py filename seconds
    
    filename: The large video file 
    seconds: The number of seconds on which it will be segmify 
    
example:
    python segmify.py video.mp4 10
    
    This will create a folder called video where 10 seconds parts of video will be stored.
"""
import subprocess
import sys
import os


input_file = sys.argv[1]
duration_time = sys.argv[2] if len(sys.argv) >= 3 else 10

fname, _ = os.path.splitext(input_file)

if not os.path.exists(fname) and not os.path.isfile(fname):
    os.mkdir(fname)


output_file = f"./{fname}/{fname}__%03d.mp4"
command = f'ffmpeg -i {input_file} -c copy -f segment -segment_time {duration_time} {output_file}'

subprocess.run(command)
