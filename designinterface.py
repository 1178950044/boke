import pymssql
import random
import tkinter as tk
import designconn as dc
import userinterface
import interfacebeer
import interfacecat
import sys
import interfacedamin



def register():
    conn = dc.createConnection('cat')
    cursor = conn.cursor()
    id1 = random.randint(0,9999999)
    password1 = random.randint(0,9999999)
    cursor.executemany(
        "insert into dbo.userdata VALUES (%s,%s,%s)",
        [(id1,password1,0)])
    top = tk.Tk()
    tk.Label(top, text='你的id是%s'%id1).grid(row=0)  # 标签
    tk.Label(top, text='你的密码是%s'%password1).grid(row=1)  # 标签
    conn.commit()
    conn.close


def checkid():
    e1 = id.get()
    e2 = password.get()
    dc.checkout(e1,e2)

def checkadmin():
    e5 = id.get()
    e6 = password.get()
    if e5 == 'admin'and e6 == 'admin':
        interfacedamin.moveuser()





def create():
    topr=tk.Tk()
    topr.title('注册界面')
    tk.Button(topr,text='返回', command=topr.quit).grid(row=2, column=0, pady=4)#按钮
    tk.Button(topr,text='开始', command=register).grid(row=2, column=1, pady=4)
    topr.mainloop()



window = tk.Tk()
window.title('微博管理系统')
window.geometry('1000x500')
tk.Label(text='id').grid(row=0)
tk.Label(text='password').grid(row=1)


id = tk.Entry()
password = tk.Entry()
id.grid(row=0,column=1)
password.grid(row=1,column=1)

tk.Button(text='退出',command=window.quit).grid(row=3,column=0,pady=4)
tk.Button(text='登录',command=checkid).grid(row=3,column=1,pady=4)
tk.Button(text='注册',command=create).grid(row=3,column=2,pady=4)
tk.Button(text='管理员界面',command=checkadmin).grid(row=4,column=2,pady=4)




window.mainloop()
