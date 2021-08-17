from tkinter.constants import CENTER, CURRENT

import pyautogui , keyboard
import tkinter as tk
from tkinter import StringVar, ttk
import time
import threading

# 画面作成
win = tk.Tk()
win.title("自動採掘")
win.geometry("305x240") # ウィンドウサイズ
win.resizable(0,0)      # ウインドウサイズ変更禁止

# ラベル
label0 = ttk.Label( text= "　" )
label0.grid( row=0, column=0 )

label1 = ttk.Label( text= "入力するキー" )
label1.grid( row=1, column=1 , padx=10, pady=5 )

label2 = ttk.Label( text= "入力するマウスのボタン")
label2.grid( row=2, column=1 , padx=10, pady=5 )

label3 = ttk.Label( text= "実行時間 (分)")
label3.grid( row=3, column=1 , padx=10, pady=5 )

label4 = tk.Label( text= "状態")
label4.grid( row=4, column=1 , padx=10, pady=20 )

label4_1 = tk.Label( text= "停止中")
label4_1.grid( row=4, column=2 , padx=10, pady=20 )

label5 = tk.Label( text= "F8 or クリック ： 実行/停止")
label5.grid( row=5, column=1 , padx=10, pady=5 )

# テキストボックス
box1 = ttk.Entry( width=13 )
box1.insert( 0 , "w" )
box1.grid( row=1, column=2 , padx=10, pady=5 )

list1 = [ "Left" , "Right" ]
box2 = ttk.Combobox( width = 10 , values = list1 ,
                    state = 'readonly' , justify = CENTER )
box2.set( list1[0] )
box2.grid( row=2, column=2 , padx=10, pady=5 )

list2 = [ 1,2,3,4,5,6,7,8,9,10 ]
box3 = ttk.Combobox( width = 10 , values = list2 ,
                    state = 'readonly' , justify = CENTER )
box3.set( list2[4] )
box3.grid( row=3, column=2 , padx=10, pady=5 )

# 変数取得
def value():
    global key, mouse, limit_time
    key = str( box1.get() )
    mouse = box2.get().lower()
    limit_time = int( box3.get() )

after_id = None
#actions = ActionChains()
# イベント
def start():
    value()
    global after_id , win
    button1_text.set( "停止" )      # ボタン更新
    label4_1[ 'text' ] = "動作中"
    label4_1[ 'fg' ] = '#ffffff'
    label4_1[ 'bg' ] = '#dc143c'

    # pyautogui.keyDown( 'ctrl' )
    pyautogui.keyDown( key )	    # キーを押したままにする


    # actions.key_down(Keys.LEFT_CONTROL)
    # actions.key_down( key )
    # actions.perform()

    # pyautogui.mouseDown( button = mouse )	# マウスボタンを押したままにする
    after_id = win.after( 60000 * limit_time , stop )     # ms
    time.sleep( 1 )

def stop():
    global after_id , win
    button1_text.set( "実行" )      # ボタン更新
    label4_1[ 'text' ] = "停止中"
    label4_1[ 'fg' ] = '#000000'
    label4_1[ 'bg' ] = '#f2f2f2'
    pyautogui.keyUp( key )	        # キーを離す
    pyautogui.keyUp( 'ctrl' )

    # actions.key_up( key )

    pyautogui.mouseUp( button = mouse )      # マウスボタンを離す
    win.after_cancel( after_id )
    after_id = None
    time.sleep( 1 )

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
    button1.grid( row=5 , column=2 , ipadx=10, ipady=7 , pady=3 )

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
