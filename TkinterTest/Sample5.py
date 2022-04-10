#モジュールを読み込む
from tkinter import *
import tkinter as tk

def btn_click():
    #最初のGUIの画面に戻る
    def return_view():
        sample5_new_csv.destroy()
 
    sample5_new_csv = tk.Tk()
    #GUIの画面サイズ
    sample5_new_csv.geometry('300x200')
    #GUIの画面タイトル
    sample5_new_csv.title('次の画面')
    #ボタン
    btn_return = tk.Button(sample5_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    sample5_new_csv.mainloop()
 
sample5 = tk.Tk()
#GUIの画面サイズ
sample5.geometry('300x200')
#GUIの画面タイトル
sample5.title('最初の画面')
 
#ボタン
btn = tk.Button(sample5, text='次の画面に移動', command=btn_click)
btn.place(x=120, y=140)
 
 
#表示
sample5.mainloop()