# YOLOv8 Mask Detection App 🩺😷

An interactive Streamlit web application for real-time face mask detection using a YOLOv8 model.

This project allows you to run inference on images and videos,
visualize detection results, and experiment with deploying YOLOv8 in a user-friendly interface.

----------------------------------------------------------------------------------------------------------------------------------
📂 Project Structure <br>
yolov8-mask-detection-app/ <br>
│── app/ <br>
│   ├── main.py               # Streamlit app entry point <br>
│── model/ <br>
│   ├── best.pt               # Trained YOLOv8 model weights <br>
│── inference_utils.py        # Utility functions for inference <br>
│── requirements.txt          # Dependencies <br>
│── README.md                 # Project documentation <br>

----------------------------------------------------------------------------------------------------------------------------------
⚙️ Installation
Clone this repository:

git clone 'project_link'

cd yolov8-mask-detection-app


----------------------------------------------------------------------------------------------------------------------------------
🚀 Running the App
Run the Streamlit app with:

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


streamlit run app/main.py


Then open your browser at:
👉 http://localhost:8501

Note:
    The app always shows two modes:
    
        1. Webcam Mode (works when running locally, not inside Docker on Windows/macOS).
        2. File Upload Mode (works everywhere)



----------------------------------------------------------------------------------------------------------------------------------

🐳 Running with Docker

You can also run this app using Docker.


1. Build the image
   docker build -t yolov8-mask-app .
2. Run in upload mode (default, works everywhere) <br>
    docker run -it -p 8501:8501 yolov8-mask-app

Now open 👉 http://localhost:8501

⚠️ Inside Docker, only file upload mode is supported. Webcam mode will not work in containers unless explicitly enabled.

📌 Important Notes:
Webcam access is not available by default inside containers on Windows/macOS.

----------------------------------------------------------------------------------------------------------------------------------

🎯 App Features
Upload images or videos for mask detection
Real-time inference powered by YOLOv8
Visualization of detection results (bounding boxes, labels, confidence)
Easy-to-use Streamlit interface
Two modes:
 1. File upload mode (works in Docker & locally)
 2. Webcam mode (works locally)

----------------------------------------------------------------------------------------------------------------------------------
🧠 Model
YOLOv8 was trained on the [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)

Classes:

mask 😷 <br>
no_mask 🚫 <br>
incorrect_mask 😑 <br>
