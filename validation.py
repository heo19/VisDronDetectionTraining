from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    #modelNotTrained = YOLO("yolov8n.pt")  # load an official model
    modelTrainEPOCH10 = YOLO("runs/detect/train6/weights/best.pt")  # load a custom model
    modelTrainEPOCH100 = YOLO("runs/detect/train8/weights/best.pt")  # load a custom model
    # Validate the model
    #print("Pretrained YOLOv8: " + modelNotTrained.val().box.map50)
    print("Trained EPOCH 10: " + str(modelTrainEPOCH10.val().box.map50))
    print("Trained EPOCH 100: " + str(modelTrainEPOCH100.val().box.map50))
