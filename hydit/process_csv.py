import os
import shutil

def process_dataset_txt(input_file, output_file, total_lines=10000):
    """
    处理数据集TXT文件，从第二行开始循环复制，递增图片序号
    
    参数:
        input_file: 输入TXT文件路径
        output_file: 输出TXT文件路径  
        total_lines: 需要生成的总行数
    """
    # 读取原始文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 检查文件是否包含数据
    if len(lines) < 2:
        print("错误：文件行数不足")
        return
    
    # 提取标题行和数据行
    header = lines[0].strip()  # 第一行标题
    data_lines = [line.strip() for line in lines[1:] if line.strip()]  # 从第二行开始的数据行
    
    print(f"读取到标题行: {header}")
    print(f"读取到 {len(data_lines)} 行数据")
    
    # 处理数据行
    processed_data = []
    
    for i in range(total_lines):
        # 计算当前应该使用哪一行原始数据（循环使用）
        original_index = i % len(data_lines)
        original_line = data_lines[original_index]
        
        # 分割路径和文本
        if ',' in original_line:
            parts = original_line.split(',', 1)  # 只分割第一个逗号
            if len(parts) == 2:
                image_path, text_zh = parts
                
                # 提取原始序号并计算新序号
                original_filename = os.path.basename(image_path.strip())
                if original_filename.endswith('.png'):
                    # 生成新的序号（从0开始递增）
                    new_filename = f"{i}.png"
                    # 构建新的图片路径（保持原始目录结构）
                    new_image_path = os.path.join(os.path.dirname(image_path.strip()), new_filename)
                    
                    # 构建新行
                    new_line = f"{new_image_path},{text_zh}"
                    processed_data.append(new_line)
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入标题行
        f.write(header + '\n')
        # 写入处理后的数据行
        for line in processed_data:
            f.write(line + '\n')
    
    print(f"处理完成！生成 {len(processed_data)} 行数据")
    print(f"输出文件: {output_file}")

def main():
    # 配置参数
    input_txt = "/home/mccxadmin/caizhi/dataset/porcelain/csvfile/image_text_bk.csv"  # 输入TXT文件路径
    output_txt = "/home/mccxadmin/caizhi/dataset/porcelain/csvfile/image_text.csv"  # 输出TXT文件路径
    total_lines = 10159  # 需要生成的总行数
    
    
    print("开始处理TXT文件...")
    # 处理TXT文件
    process_dataset_txt(input_txt, output_txt, total_lines)
    
if __name__ == "__main__":
    # 运行基本版本
    main()
