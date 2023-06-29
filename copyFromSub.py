import os
import shutil

subdir_path = os.getcwd()+'/'+os.listdir()[1]

# Get a list of all files in the subdirectory
subdir_files = os.listdir(subdir_path)
# print(subdir_files)

# Copy each file from the subdirectory to the current directory
for file in subdir_files:
    src_path = os.path.join(subdir_path, file)
    dst_path = os.path.join(os.getcwd(), file)
    shutil.copy(src_path, dst_path)
print("copied",len(subdir_files),"files Successfully!!")
# os.rmdir(subdir_path)