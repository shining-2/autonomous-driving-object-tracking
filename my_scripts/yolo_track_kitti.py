from ultralytics import YOLO

# 1. 加载你辛苦练好的那个 best.pt
# 请务必确认这个绝对路径在你的 D 盘是真实存在的
model_path = r'D:\Projects\ultralytics-main\runs\detect\v8\detect\train2\weights\best.pt'
model = YOLO(model_path)

# 2. 核心操作：直接调用官方内置的 track 接口
# 这是自动驾驶工业界的标准写法：检测 + 跟踪 一次搞定
if __name__ == '__main__':
    results = model.track(
        project='D:/Projects/ultralytics-main/runs/detect/v8/track1',
        source=r'D:\Datasets\KITTI\image_2\data_object_image_2\training\image_2', # KITTI 图片文件夹
        conf=0.3,
        imgsz=320,       # 依然用 320 照顾你的 MX550
        device=0,
        save=True,       # 结果会自动存到 runs/detect/trackX 文件夹
        tracker="botsort.yaml" # BoTSORT 是 DeepSORT 的现代升级版，效果更好！
    )