# Clipy

FFMPEG utility scripts to help me with my youtube channel.

## segmify.py

> Segmify equal segments of a video

```cmd
usage:
    python segmify.py filename seconds
    
    filename: The large video file 
    seconds: The number of seconds on which it will be segmify 
    
example:
    python segmify.py video.mp4 10
    
    This will create a folder called video where 10 seconds parts of video will be stored.
```

## crop.py

> crop.py - Crop the videos to 3/4 ratio

```cmd
usage: 
    python crop.py clips_folder output_folder
    
    clips_folder: The folder that have raw uncropped video files.
    output_folder: The folder where new cropped videos will be stored.
    
example:
    python crop.py clips_dir output_dir
    
    This will take all the clips from clips_dir and crop every clip by 3/4 ratio after that it will save the clips to output_dir.
```

## concat.py

> Concatenate multiple videos to a single video

```cmd
usage:
    python concat.py clips_dir output_dir
    
    clips_dir: The dir with short clips
    output_dir: The new dir where concatenated files will be stored

example:
    python concat.py videos merged_videos
    
    This will take every random 20 files from the videos dir and merge those 20 and save it to merged_videos dir.
```