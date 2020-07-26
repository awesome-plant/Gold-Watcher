
FROM ubuntu:16.04
USER root
#copy script 
RUN mkdir /wav_files /other_scripts 
# https://stackoverflow.com/questions/43312975/record-sound-on-ubuntu-docker-image
RUN apt-get update && \
    apt-get install pulseaudio socat alsa-utils ffmpeg -y 
    # apt-get install  -y && \ 
    # apt-get install  -y
#copy pulse server setup 
COPY other_scripts /other_scripts/
# CMD ["/other_scripts/Run_Pulse.sh"]
# docker run -it --rm -p 127.0.0.1:3000:3000 \
# --mount type=bind,source=$(pwd)/wav_files,target=/wav_files \
# gw_rec 