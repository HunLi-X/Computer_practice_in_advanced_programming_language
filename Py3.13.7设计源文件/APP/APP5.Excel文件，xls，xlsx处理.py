# ==========================================
# App5. Excel 自动化处理程序 (修改版)
# 功能: 读取指定Excel，按"部门"拆分成多个小文件
# ==========================================

import pandas as pd
import os  # 用于检查文件是否存在


def main():
    print("=== App5 Excel 自动化处理启动 ===")

    # Step 0: 设置源文件名
    # 数据文件路径
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_file = os.path.join(script_dir, 'DATA', 'groupby_test_auto_中原工学院教职工名单.xlsx')

    # 检查文件是否存在，防止报错
    if not os.path.exists(source_file):
        print(f"❌ 错误: 找不到文件 '{source_file}'")
        print("请检查文件名是否正确，或者文件是否放在了DATA目录下。")
        return

    # Step 1: 读取 Excel 文件
    print(f"\n1. 正在读取源文件: {source_file} ...")
    try:
        # 知识点: read_excel 读取本地文件
        df_source = pd.read_excel(source_file)
        print("   -> 读取成功！")

        # 打印前5行看看数据长什么样
        print(f"   -> 数据预览:\n{df_source.head()}")
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return

    # 检查是否有“部门”这一列
    if '部门' not in df_source.columns:
        print(f"❌ 错误: 表格中没有找到 '部门' 这一列。")
        print(f"   -> 当前表头是: {list(df_source.columns)}")
        return

    # Step 2: 自动分析有哪些部门
    # 知识点: unique() 比 set() 更直接，pandas 自带方法
    all_departments = df_source['部门'].unique()
    print(f"\n2. 自动识别到 {len(all_departments)} 个部门: {all_departments}")

    # Step 3: 按部门拆分并保存
    print("\n3. 开始自动拆分...")

    # 设置输出目录为DATA目录
    output_dir = os.path.join(script_dir, 'DATA')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 使用 groupby 进行分组
    grouped = df_source.groupby('部门')

    for dept in all_departments:
        # 处理部门名称可能为空的情况
        if pd.isna(dept):
            dept_name = "未知部门"
        else:
            dept_name = str(dept)

        # 获取该部门数据
        sub_df = grouped.get_group(dept)

        # 生成文件名 (使用 f-string)
        new_filename = os.path.join(output_dir, f'App5_分表_{dept_name}.xlsx')

        # 保存文件
        sub_df.to_excel(new_filename, index=False)
        print(f"   -> 成功导出: {new_filename} (包含 {len(sub_df)} 人)")

    print("\n=== 处理完成！请在DATA文件夹中查看生成的文件 ===")
    input("按回车键退出...")


if __name__ == '__main__':
    main()
