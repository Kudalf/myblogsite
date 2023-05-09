import os
import shutil

# Set the source and destination directories
src_dir = "C:/Users/13564/Documents/Blog Essays/Static"
dst_dir = "F:/MyProjects/myblogsite/static/images"

# Copy the contents of the source directory to the destination directory
for filename in os.listdir(src_dir):
    src_path = os.path.join(src_dir, filename)
    dst_path = os.path.join(dst_dir, filename)
    if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path)
    elif os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
