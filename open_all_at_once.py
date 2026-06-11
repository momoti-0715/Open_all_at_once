import subprocess
import webbrowser
import json
import os
import sys

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
    b_path = u_data["browser"]
    if not b_path is None:
        browser = webbrowser.get(f'"{b_path}" %s')
    else:
        browser = webbrowser.get()

    url_list = u_data["url_list"]
    if url_list is None:
        return

    for url in url_list:
        browser.open(url)

    return 0

def cmd_open(c_data):
    p_c_list = c_data["p_c_list"]
    if p_c_list is None:
        return
    
    for p_c in p_c_list:
        path = p_c.get("path")
        command = p_c.get("command")
        close = p_c.get("close")
        if not path is None:
            if not command is None:
                if close:
                    subprocess.Popen(['start','/d', path,'cmd','/c', command], shell=True)
                else:
                    subprocess.Popen(['start','/d', path,'cmd','/k', command], shell=True)
            else:
                subprocess.Popen(['start','/d', path], shell=True)
        elif not command is None:
            if close:
                subprocess.Popen(['start','cmd','/c', command], shell=True)
            else:
                subprocess.Popen(['start','cmd','/k', command], shell=True)
        else:
            subprocess.Popen(['start'], shell=True)



def task_open(t_data):
    """タスクをまとめて開く"""
    task_list = t_data["task_list"]
    if task_list is None:
        return

    for task in task_list:
        try:
            subprocess.Popen(task, shell=True) # taskをまとめて開く
        except:
            print(f"{task}を開けませんでした")

    return 0

if __name__ == '__main__':
    file_path = f"../Setting/{sys.argv[1]}.json"  # JSONファイル名
    data = load_json(file_path)

    if data:
        task_open(data["task_open"])
        cmd_open(data["cmd_open"])
        web_open(data["web_open"])