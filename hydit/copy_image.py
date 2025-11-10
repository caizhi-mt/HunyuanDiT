import os
import shutil
from pathlib import Path

def batch_copy_images_with_incremental_naming(source_images, source_dir, target_dir, start_number=159, total_copies=10000):
    """
    批量复制图片并从指定数字开始递增命名
    
    参数:
        source_images: 源图片文件名列表
        source_dir: 源图片所在目录
        target_dir: 目标目录
        start_number: 起始编号
        total_copies: 需要复制的总张数
    """
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"创建目标目录: {target_dir}")

    # 计算每个源图片需要复制的次数
    num_source_images = len(source_images)
    copies_per_image = total_copies // num_source_images
    remainder = total_copies % num_source_images
    
    print(f"源图片数量: {num_source_images}")
    print(f"每张图片大致复制次数: {copies_per_image}")
    print(f"起始编号: {start_number}")
    print(f"目标总张数: {total_copies}")
    print("-" * 50)
    
    current_number = start_number
    total_copied = 0
    
    # 复制图片直到达到目标数量[1,2](@ref)
    while total_copied < total_copies:
        for image_name in source_images:
            if total_copied >= total_copies:
                break
                
            # 构建完整的源文件路径[6](@ref)
            source_path = os.path.join(source_dir, image_name)
            
            # 检查源文件是否存在
            if not os.path.exists(source_path):
                print(f"警告: 源文件不存在，跳过: {source_path}")
                continue
            
            # 生成新文件名[2,8](@ref)
            new_filename = f"{current_number}.png"
            target_path = os.path.join(target_dir, new_filename)
            
            try:
                # 复制文件[7](@ref)
                shutil.copy2(source_path, target_path)
                total_copied += 1
                current_number += 1
                
                # 每复制1000张打印一次进度
                if total_copied % 1000 == 0:
                    print(f"已复制 {total_copied}/{total_copies} 张图片，当前编号: {current_number-1}")
                    
            except Exception as e:
                print(f"复制失败: {source_path} -> {target_path}, 错误: {e}")
    
    print("-" * 50)
    print(f"复制完成！总共复制了 {total_copied} 张图片")
    print(f"文件编号范围: {start_number} 到 {current_number-1}")

def main():
    # 配置参数
    source_directory = "/home/mccxadmin/caizhi/dataset/porcelain/images/"  # 请修改为您的源图片目录
    target_directory = "/home/mccxadmin/caizhi/dataset/porcelain/images/"  # 请修改为您的目标目录
    start_number = 159  # 起始编号
    total_copies = 10000  # 需要复制的总张数
    
    # 图片文件名列表（您提供的列表）
    image_files = [
        "0.png", "104.png", "110.png", "117.png", "123.png", "13.png", "136.png", "142.png", "149.png", "155.png", "19.png", "25.png", "31.png", "38.png", "44.png", "50.png", "57.png", "63.png", "7.png", "76.png", "82.png", "89.png", "95.png",
        "1.png", "105.png", "111.png", "118.png", "124.png", "130.png", "137.png", "143.png", "15.png", "156.png", "2.png", "26.png", "32.png", "39.png", "45.png", "51.png", "58.png", "64.png", "70.png", "77.png", "83.png", "9.png", "96.png",
        "10.png", "106.png", "112.png", "119.png", "125.png", "131.png", "138.png", "144.png", "150.png", "157.png", "20.png", "27.png", "33.png", "4.png", "46.png", "52.png", "59.png", "65.png", "71.png", "78.png", "84.png", "90.png", "97.png",
        "100.png", "107.png", "113.png", "12.png", "126.png", "132.png", "139.png", "145.png", "151.png", "158.png", "21.png", "28.png", "34.png", "40.png", "47.png", "53.png", "6.png", "66.png", "72.png", "79.png", "85.png", "91.png", "98.png",
        "101.png", "108.png", "114.png", "120.png", "127.png", "133.png", "14.png", "146.png", "152.png", "16.png", "22.png", "29.png", "35.png", "41.png", "48.png", "54.png", "60.png", "67.png", "73.png", "8.png", "86.png", "92.png", "99.png",
        "102.png", "109.png", "115.png", "121.png", "128.png", "134.png", "140.png", "147.png", "153.png", "17.png", "23.png", "3.png", "36.png", "42.png", "49.png", "55.png", "61.png", "68.png", "74.png", "80.png", "87.png", "93.png",
        "103.png", "11.png", "116.png", "122.png", "129.png", "135.png", "141.png", "148.png", "154.png", "18.png", "24.png", "30.png", "37.png", "43.png", "5.png", "56.png", "62.png", "69.png", "75.png", "81.png", "88.png", "94.png"
    ]
    sorted_image_files = sorted(image_files, key=lambda x: int(x.split('.')[0]))
    
    print("开始批量复制图片...")
    print(f"源目录: {source_directory}")
    print(f"目标目录: {target_directory}")
    print(f"起始编号: {start_number}")
    print(f"目标总张数: {total_copies}")
    
    # 执行复制操作[1,2](@ref)
    batch_copy_images_with_incremental_naming(
        sorted_image_files, 
        source_directory, 
        target_directory, 
        start_number, 
        total_copies
    )

# 高级版本：支持循环复制和更好的错误处理
def advanced_cyclic_copy():
    """高级版本：支持循环复制模式"""
    import time
    
    # 配置参数
    source_dir = "path/to/source"
    target_dir = "path/to/target"
    start_num = 159
    total_needed = 10000
    
    
    image_files = [
        "0.png", "104.png", "110.png", "117.png", "123.png", "13.png", "136.png", "142.png", "149.png", "155.png", "19.png", "25.png", "31.png", "38.png", "44.png", "50.png", "57.png", "63.png", "7.png", "76.png", "82.png", "89.png", "95.png",
        "1.png", "105.png", "111.png", "118.png", "124.png", "130.png", "137.png", "143.png", "15.png", "156.png", "2.png", "26.png", "32.png", "39.png", "45.png", "51.png", "58.png", "64.png", "70.png", "77.png", "83.png", "9.png", "96.png",
        "10.png", "106.png", "112.png", "119.png", "125.png", "131.png", "138.png", "144.png", "150.png", "157.png", "20.png", "27.png", "33.png", "4.png", "46.png", "52.png", "59.png", "65.png", "71.png", "78.png", "84.png", "90.png", "97.png",
        "100.png", "107.png", "113.png", "12.png", "126.png", "132.png", "139.png", "145.png", "151.png", "158.png", "21.png", "28.png", "34.png", "40.png", "47.png", "53.png", "6.png", "66.png", "72.png", "79.png", "85.png", "91.png", "98.png",
        "101.png", "108.png", "114.png", "120.png", "127.png", "133.png", "14.png", "146.png", "152.png", "16.png", "22.png", "29.png", "35.png", "41.png", "48.png", "54.png", "60.png", "67.png", "73.png", "8.png", "86.png", "92.png", "99.png",
        "102.png", "109.png", "115.png", "121.png", "128.png", "134.png", "140.png", "147.png", "153.png", "17.png", "23.png", "3.png", "36.png", "42.png", "49.png", "55.png", "61.png", "68.png", "74.png", "80.png", "87.png", "93.png",
        "103.png", "11.png", "116.png", "122.png", "129.png", "135.png", "141.png", "148.png", "154.png", "18.png", "24.png", "30.png", "37.png", "43.png", "5.png", "56.png", "62.png", "69.png", "75.png", "81.png", "88.png", "94.png"
    ]
    sorted_image_files = sorted(image_files, key=lambda x: int(x.split('.')[0]))

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    current_number = start_num
    copied_count = 0
    image_index = 0
    
    start_time = time.time()
    
    print("开始循环复制图片...")
    
    while copied_count < total_needed:
        # 循环使用源图片列表
        image_name = sorted_image_list[image_index]
        source_path = os.path.join(source_dir, image_name)
        
        if os.path.exists(source_path):
            new_filename = f"{current_number}.png"
            target_path = os.path.join(target_dir, new_filename)
            
            try:
                shutil.copy2(source_path, target_path)
                copied_count += 1
                current_number += 1
                
                if copied_count % 500 == 0:
                    elapsed = time.time() - start_time
                    speed = copied_count / elapsed if elapsed > 0 else 0
                    remaining = (total_needed - copied_count) / speed if speed > 0 else 0
                    
                    print(f"进度: {copied_count}/{total_needed} "
                          f"({copied_count/total_needed*100:.1f}%) "
                          f"速度: {speed:.1f} 文件/秒 "
                          f"预计剩余时间: {remaining/60:.1f} 分钟")
                          
            except Exception as e:
                print(f"错误: 复制 {source_path} 失败 - {e}")
        else:
            print(f"警告: 源文件不存在 - {source_path}")
        
        # 移动到下一个图片，循环使用
        image_index = (image_index + 1) % len(sorted_image_list)
    
    print(f"\n复制完成！总共生成 {copied_count} 个文件")
    print(f"编号范围: {start_num} 到 {current_number-1}")

if __name__ == "__main__":
    # 运行基本版本
    main()
    
    # 如果需要更高级的循环复制功能，可以取消注释下面的行
    # advanced_cyclic_copy()
