from ultralytics import YOLO

# 1. 加载你练好的 best.pt (请确认路径)
model_path = r'/runs/detect/train2/weights/best.pt'
model = YOLO(model_path)

# 2. 导出为 ONNX 格式
# format='onnx' 指定导出格式
# opset=12 或 17 (通常 12 兼容性最好，最新的用 17)
# dynamic=True 如果你希望未来输入图片的尺寸可变
success = model.export(format='onnx', opset=12)

print(f"导出结果: {success}")