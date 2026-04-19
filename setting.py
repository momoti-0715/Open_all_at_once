import os
import subprocess

file_name = os.path.splitext(os.path.basename(__file__))[0] # 実行しているこのファイル名(拡張子を除く)を取得
subprocess.Popen(['python', "open_all_at_once.py", file_name])