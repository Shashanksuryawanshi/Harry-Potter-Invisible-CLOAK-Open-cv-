import cv2
import time
import numpy as np
import tempfile
import streamlit as st
from datetime import datetime

def apply_invisibility(frame, background, lower_hsv, upper_hsv):
    """
    Applies invisibility cloak effect by replacing pixels within the HSV color range
    from the frame with corresponding pixels from the background.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    frame[np.where(mask == 255)] = background[np.where(mask == 255)]
    return frame

def run_cloak_effect():
    cap = cv2.VideoCapture(0)
    time.sleep(3)  # Warm-up time for camera

    background = 0
    for _ in range(30):
        ret, background = cap.read()

    background = np.flip(background, axis=1)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".avi")
    output_path = temp_output.name

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))

    stframe = st.empty()

    # Define HSV color ranges for red (cloak color)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break

        img = np.flip(img, axis=1)

        # Apply invisibility effect for both red hue ranges and combine
        invis_img1 = apply_invisibility(img.copy(), background, lower_red1, upper_red1)
        invis_img2 = apply_invisibility(img.copy(), background, lower_red2, upper_red2)

        # Combine the two processed images so all red hues are covered
        final = np.where(invis_img1 != img, invis_img1, img)
        final = np.where(invis_img2 != img, invis_img2, final)

        stframe.image(final, channels="BGR")

        out.write(final)

        if cv2.waitKey(10) == 27:
            break

    cap.release()
    out.release()

    with open(output_path, 'rb') as video_file:
        st.download_button(
            label="📥 Download Invisibility Cloak Video",
            data=video_file,
            file_name=f"invisibility_cloak_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi",
            mime='video/avi'
        )
