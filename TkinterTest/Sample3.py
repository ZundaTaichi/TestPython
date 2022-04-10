#モジュールを読み込む
from tkinter import *
import tkinter as tk

#チェックボタンに表示する文字列を用意
item = ['A','B','C','D']
check = {}

#GUI画面を作成・タイトル
sample3 = tk.Tk()
sample3.geometry('800x500')
sample3.title('Sample3')

#itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    #BooleanVarオブジェクトを作成しリストのcheck要素に追加
    check[i] = tk.BooleanVar()
    # チェックボタンの作成と配置
    tk.Checkbutton(sample3,variable = check[i],text = item[i]).pack(anchor = tk.W)

#チェックボタンの状態を通知する関数
def select():
    # 辞書check要素の数だけ繰り返す
    for i in check:
        if check[i].get() == True:
            print(item[i] + 'チェックしました')

# ボタンの作成と配置
button = tk.Button(sample3,text = 'OK',command = select).pack(anchor = tk.W)

#GUI画面を出力
sample3.mainloop()