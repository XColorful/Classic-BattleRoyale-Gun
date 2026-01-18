import os
import re

def find_decimal_rpm():
    # 获取用户输入的目录路径
    target_dir = input("请输入要搜索的目录路径 (直接回车表示当前目录): ").strip()
    if not target_dir:
        target_dir = "."

    # 验证路径是否存在
    if not os.path.exists(target_dir):
        print(f"错误: 路径 '{target_dir}' 不存在。")
        return

    # 定义允许的父目录名
    allowed_parents = {"gun", "guns"}

    # 正则表达式说明：匹配键名 rpm 且数值带小数点的行
    pattern = re.compile(r'"rpm"\s*:\s*\d+\.\d+')

    found_files = []

    print(f"正在扫描目录: {os.path.abspath(target_dir)} ...")
    print(f"限制父目录为: {allowed_parents}")
    
    for root, dirs, files in os.walk(target_dir):
        # --- 新增判断逻辑 ---
        # 获取当前文件夹名称并转为小写
        parent_dir_name = os.path.basename(root).lower()
        if parent_dir_name not in allowed_parents:
            continue
        # ------------------

        for file in files:
            if file.endswith('_data.json'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 逐行读取，对大文件更友好
                        for line_num, line in enumerate(f, 1):
                            if pattern.search(line):
                                found_files.append((file_path, line_num, line.strip()))
                                # 找到第一个匹配就跳出该文件，避免重复记录同一个文件
                                break 
                except Exception as e:
                    print(f"无法读取文件 {file_path}: {e}")

    # 输出结果
    print("\n" + "="*50)
    if found_files:
        print(f"找到以下包含小数 rpm 的文件 (共 {len(found_files)} 个):")
        for path, line_no, content in found_files:
            print(f"- 文件: {path}")
            print(f"   位置: 第 {line_no} 行 -> {content}")
    else:
        print("未发现匹配的小数 rpm 数据（或所在目录不匹配）。")
    print("="*50)

if __name__ == "__main__":
    find_decimal_rpm()