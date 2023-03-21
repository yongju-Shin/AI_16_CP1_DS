import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.detection import Detection

model_path = 'C:/Users/user/cp1_yolo/models/best.pt' 
input_path = 'C:/Users/user/cp1_yolo/data/sample1.mp4' 
output_path = 'C:/Users/user/cp1_yolo/results/sample1_result.mp4'   
threshold = 0.2

detector = Detection(model_path,threshold)

detector.detect(input_path,output_path)