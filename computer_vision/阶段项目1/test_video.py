from PIL import Image
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on 'bus.jpg'
model.predict(source='football.mp4', save=True, show=True, save_txt=False)
# model.train(data='data.yaml', epochs=10)