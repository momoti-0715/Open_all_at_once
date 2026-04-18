import subprocess
import webbrowser

def web_open():
    """urlをまとめて開く"""
    url_list = []

    for url in url_list:
        webbrowser.open(url)

    return 0

def cmd_open():
    subprocess.Popen('start /d "C:\\Users\\User\\Desktop" conda activate py39', shell=True) #/d ファイルのパス　でカレントディレクトリを指定


def task_open():
    """タスクをまとめて開く"""
    vscode = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    task_scheduler = "C:\\windows\\system32\\taskschd.msc"
    task_manager = "C:\\windows\\system32\\Taskmgr.exe"

    tasklist = [vscode, task_scheduler, task_manager]

    for task in tasklist:
        try:
            subprocess.Popen(task, shell=True) # taskをまとめて開く
        except:
            print(f"{task}を開けませんでした")

    return 0

if __name__ == '__main__':
    task_open()
    cmd_open()
    web_open()