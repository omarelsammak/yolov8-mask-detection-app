
from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt
# import the specific class

def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "model", "best.pt")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    # load YOLO model here
    from ultralytics import YOLO
    return YOLO(model_path)
def predict_image(model, image):
    """
    Run inference on a single image and return results.
    """
    results = model(image)
    return results


def visualize_results(results, save_path='outputs/output.jpg'):
    """
    Visualize and save the detection results using result.plot().
    """
    for result in results:
        # Plot returns an annotated image as a numpy array (BGR)
        annotated_img = result.plot()

        # Save manually
        cv2.imwrite(save_path, annotated_img)
        print(f"✅ Saved annotated image to {save_path}")

        # Optional: Display using matplotlib
        img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.title("Detection Result")
        plt.show()

