import os
import random
import shutil

# --- 1. 源头路径（请根据你的实际情况微调引号里的内容） ---
# 题目（图片）在哪：
src_img_dir = r'D:\Datasets\KITTI\image_2\.data_object_image_2/training/image_2'
# 答案（你刚才转好的标签）在哪：

src_label_dir = r'D:\Datasets\KITTI\yolo_labels'

# --- 2. 目的地（最终给 YOLO 训练用的干净目录） ---
dst_root = r'/yolo_data'

# 定义子文件夹   path.join用来路径拼接避免斜杠问题
train_img = os.path.join(dst_root, 'images', 'train')
val_img = os.path.join(dst_root, 'images', 'val')
train_lab = os.path.join(dst_root, 'labels', 'train')
val_lab = os.path.join(dst_root, 'labels', 'val')

# 自动创建目的地文件夹
for d in [train_img, val_img, train_lab, val_lab]:
    os.makedirs(d, exist_ok=True)

# --- 3. 开始“咔嚓”一刀切 ---
all_imgs = [f for f in os.listdir(src_img_dir) if f.endswith('.png')]
random.seed(42)
#随机打乱
random.shuffle(all_imgs)

split = int(len(all_imgs) * 0.8)
train_files = all_imgs[:split]
val_files = all_imgs[split:]


def do_move(file_list, target_i, target_l):
    for f_name in file_list:
        # 1. 搬图片 (copy 是复制，不怕弄丢原始数据)
        shutil.copy(os.path.join(src_img_dir, f_name), os.path.join(target_i, f_name))

        # 2. 搬对应的标签 (.png 换成 .txt)
        l_name = f_name.replace('.png', '.txt')
        src_l_path = os.path.join(src_label_dir, l_name)
        if os.path.exists(src_l_path):
            shutil.copy(src_l_path, os.path.join(target_l, l_name))


print("正在为你搬运 12GB 的数据，请稍等...")
do_move(train_files, train_img, train_lab)
print("训练集搬好了！")
do_move(val_files, val_img, val_lab)
print("验证集也搬好了！")

print(f"【大功告成】\n最终训练数据在: {dst_root}")