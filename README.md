# AI_16_CP1_DS

패키지 디렉토리 구조 

```bash
├── data
│   ├── sample1.mp4
│   ├── sample2.mp4
│   └── sample3.mp4
├── models
│   └── best.pt
├── results
│   ├── sample1_result.mp4
├── test
│   └── test.py
├── util
│   ├── __init__.py
│   └── detection.py
├── README.md
└── requirments.txt
``` 

- data: 모델의 입력값으로 사용할 샘플 영상들이 저장되어 있는 폴더 입니다. 
- models: 추론에 사용될 사전학습된 모델의 가중치 파일(yolov5의 best.pt)이 저장되어 있습니다. 
- results: test를 진행하여 생성되는 결과 영상이 저장되는 폴더 입니다. 
- test: test.py를 통해 모델을 작동시켜볼 수 있씁니다. 
- util: models 내 모델을 통해 영상 내 객체를 탐지하는 object detection을 진행하고 결과를 .mp4 형태로 생성하는 detect 모듈이 저장되어 있습니다.

test/test.py를 통해 모델 사용이 가능합니다. 
아래는 사용 예시 입니다. 
```python
print('hello')
```
