import sys

def solve_rpm_logic():
    print("=== TaC-Z 射速计算工具 ===")
    print("说明：输入 [目标RPM] [拉栓时间]，用空格隔开（例如: 32.46 0.9）")
    print("输入 'exit' 或 'q' 退出程序\n")

    while True:
        try:
            user_input = input("请输入数据 > ").strip().lower()
            
            if user_input in ['exit', 'q']:
                print("程序已退出。")
                break
            
            # 解析输入
            parts = user_input.split()
            if len(parts) != 2:
                print("错误：请输入两个数字（目标RPM 和 拉栓时间），中间用空格隔开。")
                continue
            
            target_rpm = float(parts[0])
            bolt_time = float(parts[1])

            if target_rpm <= 0:
                print("错误：目标RPM必须大于0。")
                continue

            # 1. 计算目标总周期 (T_target)
            target_total_interval = 60.0 / target_rpm
            
            # 2. 逻辑验证
            if bolt_time >= target_total_interval:
                max_possible_rpm = 60.0 / bolt_time
                print(f"❌ 警告：拉栓时间 ({bolt_time}s) 已超过或等于目标总周期 ({target_total_interval:.4f}s)！")
                print(f"   这意味着即便 RPM 设为无限大，实际射速也无法达到 {target_rpm}。")
                print(f"   当前拉栓动作限制下的最高理论射速为: {max_possible_rpm:.3f} RPM")
            else:
                # 3. 计算配置文件应填写的 RPM
                # 公式: 60 / (总周期 - 拉栓时间)
                required_fire_interval = target_total_interval - bolt_time
                config_rpm = 60.0 / required_fire_interval
                
                print(f"✅ 计算完成：")
                print(f"   目标总周期: {target_total_interval:.4f} 秒/发")
                print(f"   应填入配置文件的 'rpm': {config_rpm:.3f}")
                print(f"   (逻辑: {required_fire_interval:.4f}s 射击间隔 + {bolt_time}s 拉栓 = {target_total_interval:.4f}s 总间隔)")
            
            print("-" * 40)

        except ValueError:
            print("错误：请输入有效的数字！")
        except KeyboardInterrupt:
            print("\n程序已退出。")
            break

if __name__ == "__main__":
    solve_rpm_logic()