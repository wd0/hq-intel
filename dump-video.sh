basepath="shots"
if ! [ -d "$basepath" ]; then mkdir $basepath; fi
adb shell screenrecord --output-format=h264 - | ffmpeg -i - -vf fps=2 "$basepath"/shot%d.png

#adb shell screenrecord --output-format=h264 - | ffplay -framerate 60 -probesize 32 -sync video -
