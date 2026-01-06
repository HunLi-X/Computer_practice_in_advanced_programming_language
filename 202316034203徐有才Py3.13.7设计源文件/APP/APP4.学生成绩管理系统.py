# ==========================================
# App4. 学生成绩管理系统
# 知识点: 字典(Dict)操作 + while循环
# ==========================================

def main():
    # 1. 初始化成绩单 (使用字典)
    # 知识点来源: 00dict_read.py
    # 格式: {'姓名': 成绩}
    grades = {
        '小明': 95,
        '小智': 88,
        '小强': 60
    }

    print("=== 学生成绩管理系统 ===")

    # 2. 开启主循环 (类似 App2 的游戏循环)
    while True:
        print("\n" + "=" * 30)
        print("当前系统中的学生:", list(grades.keys()))  # 显示所有名字
        print("1. 查询成绩 (Query)")
        print("2. 修改/添加成绩 (Modify/Add)")
        print("3. 删除成绩 (Delete)")
        print("0. 退出 (Exit)")
        print("=" * 30)

        choice = input("请输入功能编号 (0-3): ")

        # === 功能 0: 退出 ===
        if choice == '0':
            print("系统已退出。")
            break

        # === 功能 1: 查询成绩 ===
        elif choice == '1':
            name = input("请输入要查询的学生姓名: ")
            # 检查名字是否在字典里
            if name in grades:
                # 核心知识: dict[key] 读取值
                print(f">>> {name} 的成绩是: {grades[name]}")
            else:
                print(f">>> 错误: 找不到名为 {name} 的学生。")

        # === 功能 2: 修改或添加成绩 ===
        elif choice == '2':
            name = input("请输入学生姓名: ")
            score = input("请输入考试成绩: ")

            # 核心知识: 字典赋值 (如果key存在就修改，不存在就新增)
            grades[name] = score
            print(f">>> 成功！已将 {name} 的成绩更新为 {score}。")

        # === 功能 3: 删除成绩 ===
        elif choice == '3':
            name = input("请输入要删除的学生姓名: ")
            if name in grades:
                # 核心知识: del 删除元素 (来源: 02list_del.py 的逻辑)
                del grades[name]
                print(f">>> 成功！已删除 {name} 的记录。")
            else:
                print(f">>> 错误: 找不到名为 {name} 的学生，无法删除。")

        else:
            print("输入无效，请输入 0-3 之间的数字。")


if __name__ == '__main__':
    main()