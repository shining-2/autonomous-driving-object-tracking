import os
import cv2

# --- 配置路径 ---
# 请确保这里的路径指向你 D 盘的实际位置
KITTI_IMG_PATH = r'/image_2/data_object_image_2/training/image_2'
KITTI_LABEL_PATH = r'/label_2/data_object_label_2/training/label_2'
YOLO_LABEL_PATH = r'/yolo_labels'  # 转换后的标签存这里

if not os.path.exists(YOLO_LABEL_PATH):
    os.makedirs(YOLO_LABEL_PATH)

# --- 类别映射 (将 KITTI 的 8 类简化为常用类) ---
# 面试考点：为什么要合并？因为有些类样本太少（如 Tram），合并能提高模型泛化能力
class_map = {
    'Car': 0, 'Van': 0, 'Truck': 0,  # 统一归为“车辆”
    'Pedestrian': 1, 'Person_sitting': 1,  # 统一归为“行人”
    'Cyclist': 2  # 骑行者
}


def convert(size, box):
    """ 核心逻辑：将像素坐标转为归一化中心点坐标 """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)


# 遍历所有标签文件名

label_files = [f for f in os.listdir(KITTI_LABEL_PATH) if f.endswith('.txt')]

print(f"开始转换，总计 {len(label_files)} 个文件...")

#遍历，吧id和图片对上
for label_file in label_files:
    #。spilt返回的是列表，然后取第一位就是id
    file_id = label_file.split('.')[0]
    #join是自动智能拼接，避免出错
    img_path = os.path.join(KITTI_IMG_PATH, file_id + '.png')

    # 1. 获取图片尺寸 (因为归一化需要用到宽和高)
    img = cv2.imread(img_path)
    #读取的第三个数据是通道数
    h, w, _ = img.shape

    # 2. 读取每一个文件，r是只读 原始标签并转换
    with open(os.path.join(KITTI_LABEL_PATH, label_file), 'r') as f:
        #把每一行都读取，放进一个列表
        lines = f.readlines()

    yolo_content = []
    for line in lines:
        data = line.split()
        cls_name = data[0]

        if cls_name in class_map:
            cls_id = class_map[cls_name]
            # KITTI 坐标在第 4, 5, 6, 7 个位置 (索引 4-7)
            left, top, right, bottom = float(data[4]), float(data[5]), float(data[6]), float(data[7])
            bb = convert((w, h), (left, right, top, bottom))
            yolo_content.append(f"{cls_id} {' '.join([f'{x:.6f}' for x in bb])}")

    # 3. 保存新标签 \n一行一行输入
    with open(os.path.join(YOLO_LABEL_PATH, label_file), 'w') as f:
        f.write('\n'.join(yolo_content))

print("转换完成！请检查 D:\Datasets\KITTI\yolo_labels 目录。")