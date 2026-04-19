import os
import sys
import subprocess

file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

# このpyファイルがあるフォルダ
# base_dir = os.path.dirname(os.path.abspath(__file__)) # これはpython用
base_dir = os.path.dirname(sys.executable)
# 1つ上のフォルダ
parent_dir = os.path.dirname(base_dir)

# exeのパス
file_path = os.path.join(parent_dir, "open_all_at_once.exe")

print(file_path)
subprocess.run([file_path, file_name])