from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="data.yaml", epochs=10)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("../football4.mp4")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format