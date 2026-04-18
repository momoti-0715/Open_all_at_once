import subprocess
import webbrowser
import json
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        print(f"ファイルが存在しません: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"JSONの読み込みに失敗しました: {e}")
        return None


def web_open(u_data):
    """urlをまとめて開く"""
    if(u_data["is_open"] == "False"):
        return
    
    b_path = u_data["browser"]
    if not b_path is None:
        print(b_path)
        browser = webbrowser.get(f'"{b_path}" %s')

    
    url_list = u_data["url_list"]
    for url in url_list:
        browser.open(url)

    return 0

def cmd_open(c_data):
    if(c_data["is_open"] == "False"):
        return

    p_c_list = c_data["p_c_list"]
    for p_c in p_c_list:
        path = p_c.get("path")
        command = p_c.get("command")
        if not path is None:
            if not command is None:
                subprocess.Popen(['start','/d', path, command], shell=True)
            subprocess.Popen(['start','/d', path], shell=True)
        elif not command is None:
            subprocess.Popen(['start', command], shell=True)
        else:
            subprocess.Popen(['start'], shell=True)



def task_open(t_data):
    """タスクをまとめて開く"""
    if(t_data["is_open"] == "False"):
        return

    task_list = t_data["task_list"]
    for task in task_list:
        try:
            subprocess.Popen(task, shell=True) # taskをまとめて開く
        except:
            print(f"{task}を開けませんでした")

    return 0

if __name__ == '__main__':
    file_path = "setting.json"  # JSONファイル名
    data = load_json(file_path)

    if data:
        task_open(data["task_open"])
        cmd_open(data["cmd_open"])
        web_open(data["web_open"])