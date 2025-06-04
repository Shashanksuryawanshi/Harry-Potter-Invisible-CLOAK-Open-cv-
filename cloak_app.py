import streamlit as st
import cv2
import numpy as np
import time
from PIL import Image
from app.color_detection import auto_detect_dominant_color
from app.cloak_logic import apply_invisibility
from app.voice_activation import listen_for_command

st.set_page_config(page_title="🧙‍♂️ Invisibility Cloak", layout="centered")
st.title("🧙‍♂️ Invisibility Cloak Web App")

st.markdown("""
This app lets you become **invisible** using OpenCV, powered by **real-time video masking**,
**voice activation**, and **machine learning-based color detection**.
""")

# ------------------------------------------
# 🎯 Cloak Color Auto-Detection using KMeans
# ------------------------------------------
st.subheader("🎯 Auto-Detect Cloak Color")
uploaded = st.camera_input("📸 Capture Yourself Wearing the Cloak")

if uploaded:
    img = Image.open(uploaded)
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    h, w, _ = frame.shape
    roi_x, roi_y = w // 3, h // 3
    roi_w, roi_h = w // 5, h // 5

    lower_hsv, upper_hsv, dominant_bgr = auto_detect_dominant_color(frame, (roi_x, roi_y, roi_w, roi_h))

    st.success(f"Detected BGR Color: {dominant_bgr}")
    st.info(f"Auto HSV Range:\nLower: {lower_hsv}\nUpper: {upper_hsv}")

    frame_with_box = frame.copy()
    cv2.rectangle(frame_with_box, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (0, 255, 0), 2)
    st.image(frame_with_box, channels="BGR", caption="Cloak Area Detected")

    st.session_state["auto_lower"] = lower_hsv.tolist()
    st.session_state["auto_upper"] = upper_hsv.tolist()

# ------------------------------------------
# 🗣️ Voice Activation
# ------------------------------------------
st.subheader("🗣️ Voice Activation")
if st.button("🎙 Listen for 'Make me invisible!'"):
    command = listen_for_command()
    st.write(f"🔊 You said: `{command}`")
    if "invisible" in command.lower():
        st.session_state["triggered"] = True
    else:
        st.warning("Voice command not recognized. Try again!")

# ------------------------------------------
# 🧙‍♂️ Run the Invisibility Cloak
# ------------------------------------------
if st.button("🎬 Start Cloak") or st.session_state.get("triggered"):
    st.success("🧙‍♂️ Cloak Activated!")
    lower = np.array(st.session_state.get("auto_lower", [0, 120, 70]))
    upper = np.array(st.session_state.get("auto_upper", [10, 255, 255]))
    apply_invisibility(lower, upper)
