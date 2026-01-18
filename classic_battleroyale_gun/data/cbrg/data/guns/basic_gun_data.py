import os
import re

def bulk_update_weapon_data(root_dir):
    target_suffix = "_data.json"
    # 定义允许的父目录名
    allowed_parents = {"gun", "guns"}
    
    # 定义需要检查和修改的目标数值
    target_values = {
        "life": 2,
        "gravity": 0.0245,
        "knockback": 0,
        "friction": 0.03322,
        "draw_time": 0.58,
        "put_away_time": 0.4,
        "aim_time": 0.2,
        "sprint_time": 0.2,
        "weight": 0
    }

    count = 0

    for root, dirs, files in os.walk(root_dir):
        # --- 新增判断逻辑 ---
        # 获取当前所在的文件夹名称
        parent_dir_name = os.path.basename(root).lower()
        if parent_dir_name not in allowed_parents:
            continue
        # ------------------

        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                modified = False
                new_content = content

                for key, target_val in target_values.items():
                    # 正则匹配格式: "key": value
                    pattern = re.compile(rf'"{key}"\s*:\s*([^,}}\s]+)')
                    
                    def replacement(match):
                        nonlocal modified
                        current_val_str = match.group(1).strip()
                        try:
                            # 转换为 float 进行数学比较
                            if float(current_val_str) != float(target_val):
                                modified = True
                                return f'"{key}": {target_val}'
                        except ValueError:
                            # 如果不是数字（比如 null 或 字符串），也强制修改
                            modified = True
                            return f'"{key}": {target_val}'
                        
                        return match.group(0)

                    new_content = pattern.sub(replacement, new_content)

                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"已校准数值: {file_path}")
                    count += 1

    print(f"\n处理完成！共修复了 {count} 个文件的参数。")

if __name__ == "__main__":
    path_to_search = input("请输入目标目录路径: ").strip()
    if os.path.exists(path_to_search):
        bulk_update_weapon_data(path_to_search)
    else:
        print("路径不存在。")