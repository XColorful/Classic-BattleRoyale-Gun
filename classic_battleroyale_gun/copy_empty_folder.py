import os

def create_empty_files(source_dir, destination_dir):
    """
    读取源目录下所有文件名，并在目标目录下创建相应的空文件，不复制任何元数据。

    Args:
        source_dir (str): 源目录的路径。
        destination_dir (str): 目标目录的路径。
    """
    # 检查源目录是否存在
    if not os.path.isdir(source_dir):
        print(f"错误: 源目录 '{source_dir}' 不存在。")
        return

    # 如果目标目录不存在，则创建它
    if not os.path.exists(destination_dir):
        print(f"目标目录 '{destination_dir}' 不存在，正在创建...")
        os.makedirs(destination_dir)

    # 遍历源目录下的所有文件和文件夹
    for item_name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item_name)

        # 仅处理文件，忽略子目录
        if os.path.isfile(source_path):
            destination_path = os.path.join(destination_dir, item_name)

            try:
                # 以写入模式打开并立即关闭，即可创建一个空的同名文件
                with open(destination_path, 'w') as f:
                    pass
                print(f"已在目标目录中创建空文件: '{item_name}'")
            except IOError as e:
                print(f"创建文件 '{item_name}' 时发生错误: {e}")

# 脚本执行入口
if __name__ == "__main__":
    source_directory = input("请输入源目录路径：")
    destination_directory = input("请输入目标目录路径：")
    
    create_empty_files(source_directory, destination_directory)