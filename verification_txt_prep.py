import os
from itertools import combinations, product

def generate_combinations(directory, output_file):
    files_by_id = {}
    all_ids = set()

    # 遍历目录
    for id_dir in os.listdir(directory):
        if id_dir.startswith('id_'):
            id_path = os.path.join(directory, id_dir)
            if os.path.isdir(id_path):
                all_ids.add(id_dir)
                files_by_id[id_dir] = []

                for file in os.listdir(id_path):
                    if file.endswith('.wav'):
                        files_by_id[id_dir].append(file)

    with open(output_file, 'w') as f:
        # 同一个 ID 的组合
        for id, files in files_by_id.items():
            for combo in combinations(files, 2):
                f.write(f"1 {os.path.join(id, combo[0])} {os.path.join(id, combo[1])}\n")

        # 不同 ID 的组合
        for id1, id2 in combinations(all_ids, 2):
            for file1, file2 in product(files_by_id[id1], files_by_id[id2]):
                f.write(f"0 {os.path.join(id1, file1)} {os.path.join(id2, file2)}\n")
                
if __name__ == "__main__":
    generate_combinations('/Users/boris/Documents/VoxCeleb/voxceleb2/wav/', 'output.txt')