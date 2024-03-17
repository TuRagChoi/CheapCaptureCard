import pyaudio
import threading
import cv2

p = pyaudio.PyAudio()

print('Mics:')

# Print available audio devices
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Index {i}: {info['name']}")
print('')
print('Cameras:')


# Print available cameras
i = 0
while True:
    cap = cv2.VideoCapture(i)
    if not cap.isOpened():
        break
    print(f"Camera index {i}: {cap.get(cv2.CAP_PROP_BACKEND)} - {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    cap.release()
    i += 1

print('')
input('Press Any Key to close')