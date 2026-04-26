from ultralytics import YOLO

# 1. 加载刚才导出的 ONNX 模型 (请确保路径正确)
onnx_model_path = r'/runs/detect/train2/weights/best.onnx'
model = YOLO(onnx_model_path)

# 2. 跑一次预测
# 我们直接用项目里的 bus.jpg
results = model.predict(source='bus.jpg', save=True, imgsz=320)

print("---------------------------------------")
print("验证完成！结果保存在 runs/detect/predict 目录下。")
print("请检查图片里的框是否和 .pt 模型预测的一致。")