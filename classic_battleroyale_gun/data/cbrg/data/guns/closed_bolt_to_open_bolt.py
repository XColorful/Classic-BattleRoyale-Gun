import os

def update_bolt_status(root_dir):
    # 目标后缀和需要替换的内容
    target_suffix = "_data.json"
    old_text = '"bolt": "closed_bolt"'
    new_text = '"bolt": "open_bolt"'
    
    count = 0

    # os.walk 会递归遍历所有子目录
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(target_suffix):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查是否包含目标字符串，避免不必要的写入
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    
                    # 写回文件
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"已更新: {file_path}")
                    count += 1

    print(f"\n处理完成！共修改了 {count} 个文件。")

if __name__ == "__main__":
    # 在这里输入你想遍历的目录路径
    path_to_search = input("请输入目标目录路径: ").strip()
    
    if os.path.exists(path_to_search):
        update_bolt_status(path_to_search)
    else:
        print("路径不存在，请检查后重试。")