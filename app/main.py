import streamlit as st
import cv2
import numpy as np
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inference import load_model, predict_image

# Load the YOLOv8 model only once
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Streamlit App
st.set_page_config(page_title="YOLOv8 Mask Detection", layout="centered")
st.title("🧠 Real-time Mask Detection with YOLOv8")

# Sidebar options
st.sidebar.header("🔧 Settings")
use_webcam = st.sidebar.checkbox("Use Webcam", value=True)

# Webcam OR Image Upload
if use_webcam:
    start_button = st.button("Start Webcam")
    stop_button = st.button("Stop Webcam")
    FRAME_WINDOW = st.image([])
    fps_display = st.empty()

    cap = None
    if start_button:
        cap = cv2.VideoCapture(0)

    while cap and cap.isOpened() and not stop_button:
        start = time.time()
        ret, frame = cap.read()
        if not ret:
            st.warning("❌ Failed to capture frame.")
            break

        # results = predict_image(model, frame)
        results = predict_image(model, frame)

        if len(results) > 0:
            annotated_frame = results[0].plot()
            frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame_rgb)
        else:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)  # Just show raw frame if nothing to display

        frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame_rgb, channels="RGB")

        fps = 1 / (time.time() - start)
        fps_display.markdown(f"**FPS:** `{fps:.2f}`")

    if cap:
        cap.release()
        st.success("✅ Webcam stopped.")

else:
    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        file_bytes = uploaded_file.read()
        img_array = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        results = predict_image(model, img)
        if len(results) > 0:
            annotated_img = results[0].plot()
            img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
            
        else:
            img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        st.image(img_rgb, caption="Detection Result", use_column_width=True)
