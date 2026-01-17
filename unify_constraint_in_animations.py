import os
import json
import glob
from collections import OrderedDict

# ================= 配置区域 =================
# X 判定阈值与修正目标
LIMIT_X = 0.2
TARGET_X = 0.2

# Y 判定阈值与修正目标
LIMIT_Y = 0.2
TARGET_Y = 0.2

# Z 判定阈值与修正目标
LIMIT_Z = 0.1
TARGET_Z = 0.08

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

def process_position_value(pos, limit_vec, target_vec, mode="clamp"):
    if isinstance(pos, list) and len(pos) >= 3:
        new_pos = list(pos)
        for i in range(3):
            if mode == "clamp":
                if pos[i] > limit_vec[i]:
                    new_pos[i] = target_vec[i]
            elif mode == "sync":
                new_pos[i] = min(pos[i], target_vec[i])
        return [round(x, 5) for x in new_pos]
    
    elif isinstance(pos, dict):
        new_dict = OrderedDict()
        for timestamp, coords in pos.items():
            new_dict[timestamp] = process_position_value(coords, limit_vec, target_vec, mode)
        return new_dict
    
    return pos

def process_animations():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    print("="*60)
    print("脚本功能：动画 Constraint 自由度压低 (支持关键帧字典格式)")
    print(f"1. 逻辑：X > {LIMIT_X}->{TARGET_X} | Y > {LIMIT_Y}->{TARGET_Y} | Z > {LIMIT_Z}->{TARGET_Z}")
    print(f"2. 同步：Shoot 关键帧将逐一对比 Idle 基准并压低")
    print(f"3. 排除：跳过目录 {SKIP_LIST}")
    print("="*60)

    prompt = f"请输入动画目录路径 (直接回车取当前目录 {current_dir}): "
    target_path = input(prompt).strip()
    target_path = target_path if target_path else current_dir

    files = []
    for root, dirs, _ in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in SKIP_LIST]
        if "assets" in dirs:
            all_anims = glob.glob(os.path.join(root, "assets", "**", "animations", "*.animation.json"), recursive=True)
            for p in all_anims:
                # 新增：文件名黑名单过滤
                fname_base = os.path.basename(p).lower()
                if any(black.lower() in fname_base for black in FILE_BLACK_LIST):
                    continue
                
                if not any(skip in p for skip in SKIP_LIST):
                    files.append(p)

    logs = []
    limit_vec = [LIMIT_X, LIMIT_Y, LIMIT_Z]
    target_vec = [TARGET_X, TARGET_Y, TARGET_Z]

    for file_path in files:
        fname = os.path.relpath(file_path, target_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f, object_pairs_hook=OrderedDict)

            animations = data.get("animations", {})
            if "static_idle" not in animations:
                continue

            modified = False
            changes_before, changes_after = [], []

            idle_bones = animations["static_idle"].setdefault("bones", OrderedDict())
            if "constraint" not in idle_bones:
                base_idle_pos = target_vec
                idle_bones["constraint"] = OrderedDict([("rotation", [0, 0, 0]), ("position", base_idle_pos)])
                changes_before.append("Idle:Missing")
                changes_after.append(f"Idle:Created{base_idle_pos}")
                modified = True
            else:
                old_pos = idle_bones["constraint"].get("position", [0, 0, 0])
                new_pos = process_position_value(old_pos, limit_vec, target_vec, "clamp")
                if old_pos != new_pos:
                    idle_bones["constraint"]["position"] = new_pos
                    changes_before.append(f"Idle:Changed")
                    changes_after.append(f"Idle:Clamped")
                    modified = True
                base_idle_pos = new_pos

            if "shoot" in animations:
                shoot_bones = animations["shoot"].get("bones", {})
                if "constraint" in shoot_bones:
                    old_s_pos = shoot_bones["constraint"].get("position", [0, 0, 0])
                    ref_vec = base_idle_pos
                    if isinstance(base_idle_pos, dict):
                        first_key = next(iter(base_idle_pos))
                        ref_vec = base_idle_pos[first_key]

                    new_s_pos = process_position_value(old_s_pos, None, ref_vec, "sync")
                    if old_s_pos != new_s_pos:
                        shoot_bones["constraint"]["position"] = new_s_pos
                        changes_before.append("Shoot:Changed")
                        changes_after.append("Shoot:Synced")
                        modified = True

            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent="\t", ensure_ascii=False)
                logs.append([fname, " | ".join(changes_before), " | ".join(changes_after)])
                print(f"已更新: {fname}")

        except Exception as e:
            print(f"解析失败 {fname}: {e}")

    output_table(logs, ["路径", "修改项", "结果摘要"], "unify_constraint_in_animations_log.txt")

def output_table(logs, headers, log_name):
    if not logs:
        print("\n[结果] 无动画修改。")
        return
    col_widths = [max(len(str(x)) for x in col) for col in zip(*([headers] + logs))]
    fmt = " | ".join(["{:<" + str(w) + "}" for w in col_widths])
    table_content = "\n".join([fmt.format(*headers), "-+-".join(["-"*w for w in col_widths])] + [fmt.format(*row) for row in logs])
    print("\n" + table_content)
    with open(log_name, 'w', encoding='utf-8') as f: f.write(table_content)

if __name__ == "__main__":
    process_animations()