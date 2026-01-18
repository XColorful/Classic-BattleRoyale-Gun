import os
import re

def bulk_update_weapon_data(root_dir):
    target_suffix = "_data.json"
    allowed_parents = {"gun", "guns"}
    
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

    # 提前编译所有正则表达式
    compiled_patterns = {
        key: re.compile(rf'("{key}"\s*:\s*)([^,}}\s]+)')
        for key in target_values.keys()
    }

    count = 0

    for root, dirs, files in os.walk(root_dir):
        if os.path.basename(root).lower() not in allowed_parents:
            continue

        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                modified = False
                new_content = content

                for key, pattern in compiled_patterns.items():
                    target_val = target_values[key]
                    
                    def replacement(match):
                        nonlocal modified
                        prefix = match.group(1) # '"key": '
                        current_val_str = match.group(2).strip().lower()
                        
                        # --- 新增逻辑：跳过布尔值 ---
                        if current_val_str in ['true', 'false']:
                            return match.group(0) # 保持原样，不触发 modified
                        # ---------------------------

                        try:
                            # 转换为 float 进行数学比较
                            if float(current_val_str) != float(target_val):
                                modified = True
                                return f'{prefix}{target_val}'
                        except ValueError:
                            # 如果原值不是数字也不是布尔值（如 null），则进行覆盖替换
                            modified = True
                            return f'{prefix}{target_val}'
                        
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
        print("路径不存在，请检查后重试。")