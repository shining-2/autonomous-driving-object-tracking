
---

# 基于 YOLOv8 与 BoTSORT 的自动驾驶多目标跟踪系统

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8.0-green.svg)](https://github.com/ultralytics/ultralytics)

## 📌 项目简介
本项目是一个端到端的自动驾驶环境感知系统，基于 **KITTI** 数据集，实现了对车辆、行人及骑行者的实时检测与时序跟踪。

**项目亮点：** 
- **深度定制化：** 实现了从 KITTI 原始标注到 YOLO 格式的自动化转换流水线。
- **低算力优化：** 针对入门级显卡 (NVIDIA MX550 2GB) 进行了训练策略调优，在有限显存下实现了高精度模型训练。
- **工业级集成：** 集成了目前最先进的 **BoTSORT** 跟踪算法，并支持 **ONNX** 模型部署。

---

## 📊 性能表现 (KITTI Validation Set)
针对 MX550 硬件，训练采用 `imgsz=320`, `batch=4` 的配置。

| 类别 (Class) | 精确率 (mAP@0.5) | 推理延迟 (GPU) | 理论帧率 (FPS) |
| :--- | :--- | :--- | :--- |
| **全类平均 (Overall)** | **0.634** | **2.0ms / frame** | **500+ FPS** |
| **车辆 (Vehicle)** | **0.857** | - | - |
| **行人 (Pedestrian)** | 0.549 | - | - |

> *注：行人及骑行者精度受限于 320px 分辨率，若提升至 640px 预计可进一步提高 10%-15% 的召回率。*

---

## 🛠️ 技术栈
- **核心框架:** PyTorch 2.0.1, Ultralytics YOLOv8
- **跟踪算法:** BoTSORT, DeepSORT
- **数据处理:** OpenCV, Numpy, Pandas
- **部署工具:** ONNX, ONNX Runtime

---

## 📂 项目结构
```text
.
├── configs/              # 数据集及跟踪器配置文件
├── data_utils/           # KITTI数据预处理与划分脚本
├── experiments/          # YOLOv8 vs YOLO26/11 消融实验与调优脚本
├── src/                  # 核心运行代码 (检测、跟踪、导出)
├── weights/              # 模型权重存放处
├── README.md             # 项目说明文档
└── LICENSE               # MIT 许可证
```

---

## 🚀 核心调优经验 (Hardware Tuning)
在 **2GB 显存** 的极限环境下，本项目通过以下策略成功跑通了工业级训练：
1. **显存管理：** 手动关闭了 **AMP (自动混合精度)** 训练，避免了初级阶段因梯度数值不稳定导致的 mAP 归零问题。
2. **增强控制：** 采用了二阶段微调策略，利用 `close_mosaic=10` 在训练后期关闭 Mosaic 增强，显著提升了目标框的定位精度。
3. **优化器选择：** 实验对比发现，在低分辨率（320px）下，传统的 **SGD** 优化器比 AdamW 展现出更稳健的收敛性能。

---

## 🔧 环境搭建与使用
1. **环境准备：**
   ```bash
   conda create -n yolo_env python=3.10
   conda activate yolo_env
   pip install ultralytics filterpy onnx onnxruntime-gpu
   ```

2. **数据转换：**
   ```bash
   python data_utils/kitti_to_yolo.py
   ```

3. **运行跟踪：**
   ```bash
   python src/final_track.py
   ```

---

## 📜 许可证
本项目采用 [MIT License](LICENSE) 许可。

---

### 📩 联系与交流
如果你对本项目感兴趣，欢迎通过 GitHub Issues 提出建议或点一个 **Star** 🌟 鼓励！

---


