#モジュールを読み込む
from tkinter import *
import tkinter as tk

#GUI画面を作成
sample1 = tk.Tk()
sample1.geometry('500x300')

#タイトル
sample1.title('Sample1')

#メニューの配置#
def callback():
    print('プログラムを閉じる')

menubar = tk.Menu(sample1)
sample1.config(menu = menubar)

file = tk.Menu(menubar)
menubar.add_cascade(label = 'ファイル',menu = file)

file.add_command(label = '閉じる',command = callback)

edit = tk.Menu(menubar)
menubar.add_cascade(label = 'エディット',menu = edit)


#ウィジェット作成#

#ボタン
buttonA = tk.Button(sample1, text = 'ボタンA').grid(row = 1, column = 1)
buttonB = tk.Button(sample1,text = 'ボタンB').grid(row = 1, column = 2)
buttonC = tk.Button(sample1,text = 'ボタンC').grid(row = 1, column = 3)
#ラベル
label = tk.Label(text = 'ラベル').grid(row = 2, column = 1)
#テキストボックス
txtBox = tk.Entry(width = 20).grid(row = 3, column = 1)
TextBox = tk.Text(width = 30,height = 15).grid(row = 4, column = 1)
#ラベル
label2 = tk.Label(text = 'スピンボックス').grid(row = 5,column = 1)
#スピンボックス
spinbox = tk.Spinbox(sample1,values = ('ボックス1','ボックス2','ボックス3','ボックス4')).grid(row = 5,column = 2)


#GUI画面を出力
sample1.mainloop()