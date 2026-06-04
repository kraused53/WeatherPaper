#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
/home/dan/WeatherPaper/.venv/bin/python3 /home/dan/WeatherPaper/PushImage.py /home/dan/WeatherPaper/PNGs/today.png
