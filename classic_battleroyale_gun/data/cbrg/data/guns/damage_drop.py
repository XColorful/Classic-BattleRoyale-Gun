import math

def calculate_damage_adjust():
    try:
        start_distance = float(input("请输入 start_distance: "))
        end_distance = float(input("请输入 end_distance: "))
        start_damage = float(input("请输入 start_damage: "))
        end_damage = float(input("请输入 end_damage: "))
    except ValueError:
        print("输入无效。请确保所有输入都是有效的数字。")
        return

    # 计算总伤害差值
    total_drop = round(start_damage - end_damage, 2)

    # 根据total_drop计算split值
    # 规则：2.04 -> 20, 2.05 -> 21
    # 逻辑为 (total_drop * 10) 四舍五入取整
    split = round(total_drop * 10)

    print(f"\n计算结果：")
    print(f"总伤害差值 (total_drop): {total_drop}")
    print(f"分割步数 (split): {split}")
    print("\n--- 逐行验证数据 ---")

    json_lines = []

    for i in range(split + 1):
        distance = start_distance + i * (end_distance - start_distance) / split
        damage = start_damage - i * total_drop / split

        rounded_distance = round(distance, 2)
        rounded_damage = round(damage, 2)

        if rounded_distance == int(rounded_distance):
            distance_str = str(int(rounded_distance))
        else:
            distance_str = f"{rounded_distance}"
        
        if rounded_damage == int(rounded_damage):
            damage_str = str(int(rounded_damage))
        else:
            damage_str = f"{rounded_damage}"

        # 打印用于人工验证的数据
        print(f"{distance_str}\t\t{damage_str}")

        # 将数据格式化为一行JSON字符串
        line = f'{{"distance": {distance_str}, "damage": {damage_str}}}'
        json_lines.append(line)

    last_line = json_lines[-1]
    json_lines[-1] = last_line.rstrip('}') + '},'
    infinite_item = f'{{"distance": "infinite", "damage": {damage_str}}}'
    json_lines.append(infinite_item)


    print("{")
    print("  \"bullet\": {")
    print("    \"extra_damage\": {")
    print('      "damage_adjust": [')
    
    for i, line in enumerate(json_lines):
        print(f'        {line}{"," if i < len(json_lines) - 2 else ""}')

    print('      ]')

calculate_damage_adjust()