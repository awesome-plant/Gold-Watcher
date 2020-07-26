# https://stackoverflow.com/questions/26573556/record-speakers-output-with-pyaudio
# """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
# this script listens to live audio input on pc and stores in dir 

import pyaudio
import wave
from datetime import datetime
import sys

Record_Length=15
saveDir="/wav_files/"

p = pyaudio.PyAudio()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = Record_Length
# WAVE_OUTPUT_FILENAME = "output.wav" #defined later with current timestamp
print("starting output-------------------------------------------------------")
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    # if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
    #     dev_index = dev['index']
    print('dev_index', dev['name']) #dev_index)
print("ending output-------------------------------------------------------")
sys.exit() 
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = dev_index,
                frames_per_buffer = CHUNK)
data = stream.read(CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

#saving file 
wf = wave.open(saveDir + datetime.now().strftime("%Y-%m-%d,%H.%M.%S") + ".wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()