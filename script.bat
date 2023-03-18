@echo off

setlocal enabledelayedexpansion

set /p folder_name="Enter the folder name: "
set /p n="Enter the number of clips to concatenate: "

set /a count=0
set /a index=0

for /f "delims=" %%a in ('dir /b "%folder_name%\*.mp4"') do (
    set /a count+=1
    set /a mod=!count! %% !n!

    if !mod! == 1 (
        set /a index+=1
        set "files[!index!]=%%a"
    )
)

for /l %%i in (1,1,!index!) do (
    set "cmd=ffmpeg -i "concat:"
    set "separator="

    for /l %%j in (0,1,!n!-1) do (
        set /a file_index=(%%i-1)*!n!+%%j+1
        set "cmd=!cmd!!separator!"%folder_name%\!files[!file_index!]!"
        set "separator=|"
    )

    set "cmd=!cmd!" -c copy %folder_name%\output%%i.mp4"

    echo Running command: !cmd!
    !cmd!
)

pause
