import os
import re

def unify_crawl_recoil(root_dir):
    target_suffix = "_data.json"
    key = "crawl_recoil_multiplier"
    target_val = 0.703
    # 定义允许的父目录名
    allowed_parents = {"gun", "guns"}
    
    # 正则匹配 "crawl_recoil_multiplier": 数值
    pattern = re.compile(rf'("{key}"\s*:\s*)([^,}}\s]+)')
    count = 0

    for root, dirs, files in os.walk(root_dir):
        # --- 新增判断逻辑 ---
        # 获取当前文件夹的名称并转为小写
        parent_dir_name = os.path.basename(root).lower()
        if parent_dir_name not in allowed_parents:
            continue
        # ------------------

        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replacement(match):
                    prefix = match.group(1)        # 这一部分是 '"crawl_recoil_multiplier": '
                    current_val_str = match.group(2).strip() # 只有数值
                    try:
                        if float(current_val_str) != target_val:
                            return f'{prefix}{target_val}' # 拼接前缀和新值，原数值后的逗号不受影响
                    except ValueError:
                        return f'{prefix}{target_val}'
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