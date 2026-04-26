from ultralytics import YOLO

model = YOLO("../yolov8n.pt")

if __name__ == '__main__':
    results = model.train(
        data='kitti.yaml',
        epochs=50,
        imgsz=320,
        batch=8,
        resume=True,

        # --- 核心修复：必须关掉 AMP，适合 MX550 ---
        amp=False,

        # --- 针对性调优：AdamW 需要配合合理的学习率 ---
        optimizer='AdamW',
        lr0=0.01,  # 【修正】恢复到 0.01，让模型起步快一点
        warmup_epochs=3.0,

        # --- 数据增强 ---
        mosaic=1.0,
        mixup=0.0,  # 依然建议先关掉 mixup，MX550 算力有限

        device=0,
        workers=2
    )