from ultralytics import YOLO

# 1. 加载模型 这里..表示上一级，目录
model = YOLO("../yolo26n.pt")

# 2. 预测
results = model.predict(
    source="bus.jpg", save=True, device=0, project='D:/Projects/ultralytics-main/runs/detect/26/predict')
'''results = model.predict(
    source="bus.jpg",

    # === 输出相关 ===
    save=True,           # 保存结果图片（默认存到 runs/detect/predict/）
    save_txt=True,       # 保存检测结果为txt文件
    save_conf=True,      # txt文件里包含置信度

    # === 检测参数 ===
    conf=0.25,           # 置信度阈值（默认0.25，低于这个的框不显示）
    iou=0.7,             # NMS的IOU阈值（默认0.7，去重框）

    # === 图像参数 ===
    imgsz=640,           # 输入图片尺寸（默认640，越大越准但越慢）

    # === 性能参数 ===
    device=0,            # 设备（0=GPU, "cpu"=CPU）
    half=True,           # 半精度推理（GPU上更快）
    augment=False,       # 测试时增强（更准但慢4倍）

    # === 显示参数 ===
    show=False,          # 实时显示结果窗口
    show_labels=True,    # 显示类别标签
    show_conf=True,      # 显示置信度分数
    line_width=None,     # 框的线宽（None=自动）
)'''

# 3. 打印结果（修正后的写法）
for result in results:
    # 类别 ID 实际上是在 boxes 对象里面的
    clss = result.boxes.cls
    print(f"检测到的物体类别 ID 是: {clss}")

print("任务圆满成功！")