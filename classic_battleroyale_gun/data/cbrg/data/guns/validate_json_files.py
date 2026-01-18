import os
import json

def validate_json_files(root_dir):
    target_suffix = "_data.json"
    invalid_count = 0
    total_checked = 0

    print("开始校验 JSON 格式...\n")

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(target_suffix):
                total_checked += 1
                file_path = os.path.abspath(os.path.join(root, file))
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 尝试加载 JSON
                        json.load(f)
                except json.JSONDecodeError as e:
                    # 如果解析失败，打印完整路径和错误详情
                    invalid_count += 1
                    print(f"❌ [格式错误]: {file_path}")
                    print(f"    错误原因: {e}\n")
                except Exception as e:
                    invalid_count += 1
                    print(f"⚠️ [未知读取错误]: {file_path}")
                    print(f"    错误描述: {e}\n")

    print("--- 校验结束 ---")
    print(f"共检查文件: {total_checked} 个")
    if invalid_count == 0:
        print("✅ 所有 JSON 文件格式正确！")
    else:
        print(f"🚨 发现 {invalid_count} 个损坏的文件，请根据上方路径进行修复。")

if __name__ == "__main__":
    path_to_search = input("请输入要校验的目录路径: ").strip()
    if os.path.exists(path_to_search):
        validate_json_files(path_to_search)
    else:
        print("路径不存在。")