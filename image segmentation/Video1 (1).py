#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def calculate_noise(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.std(gray_frame)

def find_frame_with_least_noise(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None
    
    least_noise_frame = None
    min_noise = float('inf')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        noise = calculate_noise(frame)
        if noise < min_noise:
            min_noise = noise
            least_noise_frame = frame
    
    cap.release()
    
    return least_noise_frame

# Usage
video_path = "Test_vid.mp4"  # Replace with the actual path to your video file
least_noise_frame = find_frame_with_least_noise(video_path)

if least_noise_frame is not None:
    cv2.imshow("Frame with Least Noise", least_noise_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No frames in the video.")


# In[ ]:




