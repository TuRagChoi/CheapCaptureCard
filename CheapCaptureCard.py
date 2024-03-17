import cv2
import numpy as np
import pyaudio
import threading

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)
def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)
def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_1080p()
change_res(1920, 1080)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

cv2.namedWindow('Nintendo Switch', cv2.WINDOW_NORMAL)
p = pyaudio.PyAudio()

# SELECT AUDIO DEVICE
input_device_index = 8

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                input_device_index=input_device_index,
                frames_per_buffer=CHUNK)

def audio_thread():
    while True:
        try:
            audio_data = stream.read(CHUNK)
            stream.write(audio_data)
        except KeyboardInterrupt:
            break

audio_thread = threading.Thread(target=audio_thread)
audio_thread.start()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1920, 1057), fx=1, fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('Nintendo Switch', frame)

    # Get the window size
    width = cv2.getWindowImageRect('Nintendo Switch')[2]
    height = cv2.getWindowImageRect('Nintendo Switch')[3]

    print(f"{width}, {height}")

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()