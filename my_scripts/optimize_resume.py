from ultralytics import YOLO

model = YOLO(r'/runs/detect/train2/weights/last.pt')
if __name__ == '__main__':
    # 2. 恢复训练，同时压低 batch
    results = model.train(
        resume=True,
        batch=4,    # 【关键】从 8 降到 4，确保稳定性
        workers=0,  # 【关键】设为 0，防止多进程占用显存
        amp=False
    )