import os
# https://pypi.douban.com/simple  # 豆瓣镜像
# https://pypi.tuna.tsinghua.edu.cn/simple  # 清华镜像

mirror = " -i https://pypi.douban.com/simple"
#os.system("python -m pip install --upgrade pip" + mirror)  #更新pip

# os.system("python -m pip install pytest" + mirror)  #安装pytest
# os.system("python -m pip install pywinauto" + mirror)  #安装pywinauto
# os.system("python -m pip install pypiwin32" + mirror)  #安装pypiwin32 和 pywin32
# os.system("python -m pip install pyautogui" + mirror)  #安装pyautogui

location = os.system("C:\\Program Files\\Python38\\Lib\\site-packages")
'''
if location:
    os.system("python -m pip install pytest-sugar" + mirror) 


'''