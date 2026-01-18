import os
import re

def reset_armor_ignore(root_dir):
    target_suffix = "_data.json"
    # 允许的父级目录列表
    allowed_parents = {"gun", "guns"}
    
    # 正则表达式解释：
    # "armor_ignore"\s*:\s* 匹配键名和冒号，允许有空格
    # ([^,}\s]+)            捕获冒号后的值，直到遇到逗号、花括号或空格
    pattern = re.compile(r'("armor_ignore"\s*:\s*)([^,}\s]+)')
    
    count = 0

    for root, dirs, files in os.walk(root_dir):
        # 获取当前所在目录的名称（即文件的父级目录）
        parent_dir_name = os.path.basename(root).lower()
        
        # 检查当前目录名是否在允许的列表中
        if parent_dir_name not in allowed_parents:
            continue

        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 定义替换逻辑
                def replacement_func(match):
                    prefix = match.group(1) # "armor_ignore": 
                    value = match.group(2).strip()
                    
                    # 如果值不是 0 (考虑到可能是 "0", "0.0", "0.00")
                    try:
                        if float(value) != 0:
                            return f'{prefix}0'
                    except ValueError:
                        # 如果值不是数字（比如是变量名或 null），也建议重置
                        return f'{prefix}0'
                    
                    return match.group(0) # 保持原样

                new_content = pattern.sub(replacement_func, content)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"已重置护甲穿透: {file_path}")
                    count += 1

    print(f"\n处理完成！共重置了 {count} 个文件的护甲穿透数值。")

if __name__ == "__main__":
    # 使用 input 接收路径
    path_to_search = input("请输入目标目录路径: ").strip()
    if os.path.exists(path_to_search):
        reset_armor_ignore(path_to_search)
    else:
        print("路径不存在。")