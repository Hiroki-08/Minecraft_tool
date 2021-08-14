from tkinter.constants import CENTER, CURRENT

import pyautogui , keyboard
import tkinter as tk
from tkinter import StringVar, ttk
import time
import threading

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

label4 = tk.Label( text= "F8 or クリック ： 実行/停止")
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


# 変数取得
key = box1.get()
mouse = box2.get().lower()
limit_time = int( box3.get() )

after_id = None
# イベント
def start():
    global after_id , win
    button1_text.set( "停止" )      # ボタン更新
    # pyautogui.keyDown( key )	    # キーを押したままにする
    # pyautogui.mouseDown( button = mouse )	# マウスボタンを押したままにする
    after_id = win.after( 60000 * limit_time , stop )     # ms
    time.sleep( 1 )

def stop():
    global after_id , win
    button1_text.set( "実行" )      # ボタン更新
    # pyautogui.keyUp( key )	        # キーを離す
    # pyautogui.mouseUp( button = mouse )      # マウスボタンを離す
    win.after_cancel( after_id )
    after_id = None

button1_text = tk.StringVar()
button1_text.set( "実行" )

def func():
    if ( str( button1_text.get() ) == "実行" ):
        start()
    else:
        stop()

# ボタン
def button():
    button1 = ttk.Button( win , textvariable= button1_text , command = func )
    button1.grid( row=4, column=1 , ipadx=10, ipady=7 , pady=20 )

# F8
def control():
    while True:
        if keyboard.read_key() == "f8":
            time.sleep( 0.3 )
            func()


thread1 = threading.Thread( target = button )
thread2 = threading.Thread( target = control )

thread2.setDaemon(True)

thread1.start()
thread2.start()

win.mainloop()
