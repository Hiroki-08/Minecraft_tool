from tkinter.constants import CENTER, CURRENT

import pyautogui , keyboard
import tkinter as tk
from tkinter import StringVar, ttk
# pyautogui.mouseDown()	# マウスボタンを押したままにする
# pyautogui.mouseUp()     # マウスボタンを離す

# pyautogui.keyDown()	    # キーボードの()を押したままにする
# pyautogui.keyUp('shift')

# while True:
#     if keyboard.read_key() == "f8":
#         print("\nYou pressed F8")

# 画面作成
win = tk.Tk()
win.title("自動採掘")
win.geometry("300x200")

# ラベル
label0 = ttk.Label( text= "" )
label0.grid( row=0, column=0 )

label1 = ttk.Label( text= "入力するキー" )
label1.grid( row=1, column=0 , padx=10, pady=5 )

label2 = ttk.Label( text= "入力するマウスのボタン")
label2.grid( row=2, column=0 , padx=10, pady=5 )

label3 = ttk.Label( text= "実行時間 (分)")
label3.grid( row=3, column=0 , padx=10, pady=5 )

label4 = tk.Label( text= "クリック or F8 ： 実行/停止")
label4.grid( row=4, column=0 , padx=10, pady=5 )

# テキストボックス
box1 = ttk.Entry( width=13 )
box1.insert( 0 , "w" )
box1.grid( row=1, column=1 , padx=10, pady=5 )

Value = [ "Left" , "Right" ]
box2 = ttk.Combobox( width=10 , values=Value ,
                    state='readonly' , justify=CENTER )
box2.set( Value[0] )
box2.grid( row=2, column=1 , padx=10, pady=5 )

box3 = ttk.Entry( width=13 )
box3.insert( 0 , 5 )
box3.grid( row=3, column=1 , padx=10, pady=5 )

# イベント
def start():

    button1_text.set( "停止" )

    # 変数取得
    key = box1.get()
    mouse = box2.get()
    time = box3.get()



    # pyautogui.keyDown( key )	    # キーを押したままにする
    # pyautogui.keyUp( key )	        # キーを離す

    # pyautogui.mouseDown( mouse )	# マウスボタンを押したままにする
    # pyautogui.mouseUp( mouse )     # マウスボタンを離す


# ボタン
button1_text = StringVar()
button1_text.set( "実行" )
button1 = ttk.Button( win , textvariable= button1_text , command = start() )
button1.grid( row=4, column=1 , ipadx=15, ipady=7 , pady=20 )




win.mainloop()