import os
import re

def unify_crawl_recoil(root_dir):
    target_suffix = "_data.json"
    key = "crawl_recoil_multiplier"
    target_val = 0.703
    
    # 正则匹配 "crawl_recoil_multiplier": 数值
    pattern = re.compile(rf'"{key}"\s*:\s*([^,}}\s]+)')
    count = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replacement(match):
                    current_val_str = match.group(1).strip()
                    try:
                        # 只有当数值不等于 0.703 时才修改
                        if float(current_val_str) != target_val:
                            return f'"{key}": {target_val}'
                    except ValueError:
                        return f'"{key}": {target_val}'
                    return match.group(0)

                new_content = pattern.sub(replacement, content)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"已校准爬行后坐力系数: {file_path}")
                    count += 1

    print(f"\n处理完成！共修改了 {count} 个文件。")

if __name__ == "__main__":
    path_to_search = input("请输入目标目录路径: ").strip()
    if os.path.exists(path_to_search):
        unify_crawl_recoil(path_to_search)
    else:
        print("路径不存在。")