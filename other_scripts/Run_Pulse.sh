echo "starting pulse server setup"
pulseaudio -D --exit-idle-time=-1 
pacmd load-module module-virtual-sink sink_name=v1 
pacmd set-default-sink v1 
pacmd set-default-source v1.monitor 
_DT=$(date '+%Y-%m-%d_%H.%M.%S')
echo "saved filename is: " + $_DT
ffmpeg -f pulse -i default -t 00:00:5 /wav_files/$_DT.mp3