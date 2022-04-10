#モジュールを読み込む
from tkinter import *
import tkinter as tk

#GUI画面を作成・タイトル
sample2 = tk.Tk()
sample2.geometry('500x300')
sample2.title('Sample2')

#ラジオボタンに表示する文字列
item = ['A','B','C','D']
# Intvarオブジェクトを作成して変数に代入
val = tk.IntVar()
#ラジオボタンの作成と配置
#itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # 親要素を指定
    tk.Radiobutton(sample2,value = i,variable = val,text = item[i]).pack(anchor = tk.W)

#ラジオボタンの状態を通知する関数
def choice():
    #Intvarオブジェクトの値を取得
    ch = val.get()
    #リストitemのインデックスをchに指定して要素を出力
    print(item [ch] + 'を選択しました。')

#ボタンの作成と配置
button = tk.Button(sample2,text = 'OK',command = choice).pack(side = tk.LEFT)

#GUI画面を出力
sample2.mainloop()