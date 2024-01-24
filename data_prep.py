import os
import shutil

def process_file(filename):
    # 从文件名中提取相关部分
    parts = filename.split('_')
    if len(parts) < 2:
        return None
    
    # 构建新的文件名和路径
    id_part = parts[1].split('-')[0]
    new_filename = '_'.join(parts[1:]).replace('.wav', '') + '.wav'
    new_path = os.path.join('voxceleb2', 'wav', f'id_{id_part}', new_filename)

    return new_path

def move_files(source_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            new_path = process_file(filename)
            if new_path:
                # 创建目标目录（如果不存在）
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                
                # 移动文件
                shutil.move(os.path.join(source_dir, filename), new_path)
                print(f"Moved {filename} to {new_path}")

# 替换以下路径为您的源文件夹路径
source_directory = '/home/rlg/projects/sig/VoxCeleb/single-channel/enrollment'
move_files(source_directory)