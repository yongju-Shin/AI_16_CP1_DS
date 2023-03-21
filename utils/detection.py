import cv2 
import numpy as np 
import torch
from tqdm import tqdm


class Detection():
    def __init__(self, model_path, threshold=0.5):
        self.model_path = model_path
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', self.model_path, trust_repo=True)
        self.threshold = threshold
    
    def detect(self, input_path, output_path):
        cap = cv2.VideoCapture(input_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                results = self.model(frame)
                result_frame = results.render()[0]
                out.write(result_frame)
                pbar.update(1)
        
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
    