import os
from pathlib import Path

# --- 配置区域：白名单文件夹名称或路径 ---
# 获取脚本文件所在的目录
SCRIPT_DIR = Path(__file__).resolve().parent

whitelist_raw = [
    "./remove_unused_content"
]

def delete_empty_files():
    # 1. 获取用户输入
    raw_input = input(f"请输入要清理的目录路径 (直接回车默认使用脚本所在目录: {SCRIPT_DIR}): ").strip()
    
    # 2. 确定目标路径
    if not raw_input:
        target_dir = SCRIPT_DIR
    else:
        target_dir = Path(raw_input).expanduser().resolve()

    # 将白名单转换为绝对路径对象，基于脚本所在目录计算
    whitelist = [(SCRIPT_DIR / p).resolve() if p.startswith(".") else Path(p).resolve() for p in whitelist_raw]
    # ---------------------------------------

    if not target_dir.exists():
        print(f"错误: 路径 '{target_dir}' 不存在。")
        return

    print(f"正在扫描: {target_dir}")
    print(f"排除名单: {whitelist_raw}")
    print("-" * 30)

    count = 0
    # os.walk 处理递归
    for root, dirs, files in os.walk(target_dir):
        current_path = Path(root).resolve()

        # 检查白名单过滤
        if any(current_path == w or w in current_path.parents for w in whitelist):
            # 只有当白名单目录在扫描路径下时才打印跳过信息
            try:
                rel_path = current_path.relative_to(target_dir)
                print(f"跳过白名单目录: {rel_path if str(rel_path) != '.' else '当前目录'}")
            except ValueError:
                pass 
            dirs[:] = []  # 停止递归
            continue

        for name in files:
            file_path = current_path / name
            try:
                # 检查是否为文件且大小为 0
                if file_path.is_file() and file_path.stat().st_size == 0:
                    file_path.unlink() # 删除文件
                    print(f"已删除: {file_path.relative_to(target_dir)}")
                    count += 1
            except Exception as e:
                print(f"无法处理 {name}: {e}")

    print("-" * 30)
    print(f"清理完成！共删除 {count} 个空文件。")

if __name__ == "__main__":
    delete_empty_files()