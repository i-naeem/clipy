from pathlib import Path
import ffmpeg
import sys
import os

SEGMENT_DURATION = 10

input_file = sys.argv[1]


filename, ext = os.path.splitext(input_file)
clips_dir = Path(filename)


if not clips_dir.exists():
    clips_dir.mkdir()


output_name = os.path.join(os.path.abspath(clips_dir), f'{filename}__%03d.mp4')
stream = ffmpeg.input(input_file)
stream = stream.output(output_name, c="copy", map="0",
                       segment_time=SEGMENT_DURATION, f="segment")

stream.run()
