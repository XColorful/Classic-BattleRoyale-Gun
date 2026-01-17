import os
import json
import glob

# ================= 配置区域 =================
# 期望相对于 scope_pos 的偏移量
OFFSET_X = 0
OFFSET_Y = 2
OFFSET_Z = 8

# 判定修改的阈值（任意轴差距大于此值则覆写）
DIST_THRESHOLD = 0.6

# 忽略名单：tacz 目录下不需要遍历的文件夹名称
SKIP_LIST = [
    "classic_battleroyale_gun",
    "suffuse_gunsmoke_pack",
    "infinite_origin" # P90
]
FILE_BLACK_LIST = [
    # suffuse_gunsmoke_pack
    "svd",
    "gm6"
]
# ===========================================

def process_geo_models():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    print("="*60)
    print("脚本功能：模型 Constraint 坐标对齐 + 自动补全缺失组")
    print(f"1. 逻辑：若缺失 constraint 则根据 scope_pos 父级自动创建")
    print(f"2. 对齐：XYZ 任意轴距离目标超过 {DIST_THRESHOLD} 则覆写")
    print(f"3. 排除：跳过目录 {SKIP_LIST}")
    print("="*60)

    prompt = f"请输入模型目录路径 (直接回车取当前目录 {current_dir}): "
    target_path = input(prompt).strip()
    
    if not target_path:
        target_path = current_dir
        print(f"已选择目录: {target_path}")

    files = []
    for root, dirs, _ in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in SKIP_LIST]
        if "assets" in dirs:
            p1 = glob.glob(os.path.join(root, "assets", "**", "geo_models", "gun", "*_geo.json"), recursive=True)
            p2 = glob.glob(os.path.join(root, "assets", "**", "geo_models", "guns", "*_geo.json"), recursive=True)
            for p in (p1 + p2):
                # 新增：文件名黑名单过滤
                fname_base = os.path.basename(p).lower()
                if any(black.lower() in fname_base for black in FILE_BLACK_LIST):
                    continue
                
                if not any(skip in p for skip in SKIP_LIST):
                    files.append(p)

    logs = []
    for file_path in files:
        fname = os.path.relpath(file_path, target_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if "minecraft:geometry" not in data: continue

            file_modified = False

            for geo in data["minecraft:geometry"]:
                bones = geo.get("bones", [])
                bone_map = {b.get("name"): b for b in bones}
                
                constraint = bone_map.get("constraint")
                scope_pos = bone_map.get("scope_pos")

                if scope_pos and constraint:
                    c_pivot = constraint.get("pivot", [0, 0, 0])
                    s_pivot = scope_pos.get("pivot", [0, 0, 0])
                    expected = [
                        round(s_pivot[0] + OFFSET_X, 5), 
                        round(s_pivot[1] + OFFSET_Y, 5), 
                        round(s_pivot[2] + OFFSET_Z, 5)
                    ]

                    diffs = [abs(c_pivot[i] - expected[i]) for i in range(3)]
                    if any(d > DIST_THRESHOLD for d in diffs):
                        logs.append([fname, str(c_pivot), str(expected)])
                        constraint["pivot"] = expected
                        file_modified = True

                elif scope_pos and not constraint:
                    s_pivot = scope_pos.get("pivot", [0, 0, 0])
                    expected = [
                        round(s_pivot[0] + OFFSET_X, 5), 
                        round(s_pivot[1] + OFFSET_Y, 5), 
                        round(s_pivot[2] + OFFSET_Z, 5)
                    ]
                    
                    parent_name = scope_pos.get("parent")
                    grandparent_name = None
                    if parent_name in bone_map:
                        grandparent_name = bone_map[parent_name].get("parent")
                    
                    new_constraint = {
                        "name": "constraint",
                        "pivot": expected
                    }
                    if grandparent_name:
                        new_constraint["parent"] = grandparent_name
                    
                    bones.append(new_constraint)
                    logs.append([fname, "Missing", f"Created (Parent: {grandparent_name})"])
                    file_modified = True

            if file_modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent="\t", ensure_ascii=False)
                print(f"已处理: {fname}")
            else:
                print(f"无需修改: {fname}")

        except Exception as e:
            print(f"错误 {fname}: {e}")

    output_table(logs, ["路径", "原状态", "处理结果"], "unify_geo_model_constraint_pos_log.txt")

def output_table(logs, headers, log_name):
    if not logs:
        print("\n[结果] 无文件修改。")
        return
    str_logs = [[str(cell) for cell in row] for row in logs]
    col_widths = [max(len(x) for x in col) for col in zip(*([headers] + str_logs))]
    fmt = " | ".join(["{:<" + str(w) + "}" for w in col_widths])
    table_content = "\n".join([fmt.format(*headers), "-+-".join(["-"*w for w in col_widths])] + [fmt.format(*row) for row in str_logs])
    print("\n" + table_content)
    with open(log_name, 'w', encoding='utf-8') as f: f.write(table_content)

if __name__ == "__main__":
    process_geo_models()