from ultralytics import YOLO

# 1. 依然加载最小的 n 模型
model = YOLO("../yolo26n.pt")

if __name__ == '__main__':
    # 2. 针对 MX550 (2GB) 的极限调优
    results = model.train(
        data='my_kitti.yaml',
        project='D:/Projects/ultralytics-main/runs/detect/26',
        epochs=50,  # 建议先跑 50 轮看看效果
        imgsz=320,  # 【关键修改】将 640 改为 320。
        # 显存占用会下降 4 倍！虽然精度稍微降一点，但能跑得动最重要。
        batch=4,  # 【关键修改】将默认的 16 改为 8。
        # 如果跑起来还是卡，可以改写成 4。
        device=0,
        workers=2,  # MX550 这种轻薄本 CPU 核心也不会太多，2 个工人读图足够了
        amp=False,  # 【关键修改】MX550 这种显卡对混合精度加速支持一般，关掉更稳

        patience=10,  # 新增：如果10轮没提升就提前停止
        save_period=5,  # 每5轮保存一次，防止中途出错
        verbose=True  # 显示详细训练信
    )