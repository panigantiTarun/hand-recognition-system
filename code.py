import torch

model = torch.hub.load('ultralytics/yolov5', 'best.pt or last.pt')

img = 'path of the image'

results = model(img) 

results.pandas().xyxy[0]
