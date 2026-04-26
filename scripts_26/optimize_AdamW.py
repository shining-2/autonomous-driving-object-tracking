from ultralytics import YOLO

# 1. 【核心】加载你那个 0.634 分的 Baseline 权重
model = YOLO(r'/runs/detect/kitti_yolov8n_320_50epoch/weights/best.pt')

if __name__ == '__main__':
    results = model.train(
        data='kitti.yaml',
        epochs=30,  # 既然是精修，30 轮足够了
        imgsz=320,
        batch=8,
        amp=False,  # 依然建议关掉，为了 MX550 的稳定性

        # --- 调优参数组合 ---
        optimizer='AdamW',
        lr0=0.001,  # 【关键】用更小的学习率进行微调

        # --- 数据增强的平衡 ---
        mosaic=0.5,  # 【策略】不要全开 1.0，开 0.5 降低拼图频率
        close_mosaic=10,  # 最后 10 轮关掉它，让模型回归真实画面

        device=0
    )