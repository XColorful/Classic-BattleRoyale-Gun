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

    # 正则表达式说明：
    # "rpm"   : 匹配键名
    # \s*:\s* : 匹配冒号及其前后的空格
    # \d+\.\d+: 匹配至少带一位小数的数字（如 600.0, 5.5）
    pattern = re.compile(r'"rpm"\s*:\s*\d+\.\d+')

    found_files = []

    print(f"正在扫描目录: {os.path.abspath(target_dir)} ...")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('_data.json'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 逐行读取，对大文件更友好
                        for line_num, line in enumerate(f, 1):
                            if pattern.search(line):
                                found_files.append((file_path, line_num, line.strip()))
                                # 如果一个文件只需要记录一次，可以 break
                                break 
                except Exception as e:
                    print(f"无法读取文件 {file_path}: {e}")

    # 输出结果
    print("\n" + "="*50)
    if found_files:
        print(f"找到以下包含小数 rpm 的文件 (共 {len(found_files)} 个):")
        for path, line_no, content in found_files:
            print(f"- 文件: {path}")
            print(f"  位置: 第 {line_no} 行 -> {content}")
    else:
        print("未发现匹配的小数 rpm 数据。")
    print("="*50)

if __name__ == "__main__":
    find_decimal_rpm()