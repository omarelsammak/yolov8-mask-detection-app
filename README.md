# YOLOv8 Mask Detection App 🩺😷

An interactive Streamlit web application for real-time face mask detection using a YOLOv8 model.

This project allows you to run inference on images and videos,
visualize detection results, and experiment with deploying YOLOv8 in a user-friendly interface.

----------------------------------------------------------------------------------------------------------------------------------
📂 Project Structure
yolov8-mask-detection-app/
│── app/
│   ├── main.py               # Streamlit app entry point
│── model/
│   ├── best.pt               # Trained YOLOv8 model weights
│── inference_utils.py        # Utility functions for inference
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation

----------------------------------------------------------------------------------------------------------------------------------
⚙️ Installation
Clone this repository:

git clone 'project_link'
cd yolov8-mask-detection-app

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

----------------------------------------------------------------------------------------------------------------------------------
🚀 Running the App
Run the Streamlit app with:

streamlit run app/main.py


Then open your browser at:
👉 http://localhost:8501

----------------------------------------------------------------------------------------------------------------------------------
🎯 App Features
Upload images or videos for mask detection

Real-time inference powered by YOLOv8

Visualization of detection results (bounding boxes, labels, confidence)

Easy-to-use Streamlit interface

----------------------------------------------------------------------------------------------------------------------------------
🧠 Model
YOLOv8 was trained on the [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)

Classes:

mask 😷
no_mask 🚫
incorrect_mask 😑
