import tkinter as tk
import pymssql


def vildae(e1,e2,row):
    ca = tk.Tk()
    ca.title('用户界面')
    ca.geometry('1000x500')


    conn = pymssql.connect(server='(local)', user='sa', password='123', database='vildae') #链接数据库
    cursor = conn.cursor()
    cursor.execute('select integral from userdata where id=%s and password=%s' % (e1, e2))
    vintegra3 = cursor.execute
    print(vintegra3)




    tk.Label(ca,text='用户名').grid(row=1)
    tk.Label(ca,text=e1).grid(row=1,column=1)
    tk.Label(ca,text='积分').grid(row=2)
    tk.Label(ca,text=row).grid(row=2,column=1)
    tk.Label(ca,text='等级').grid(row=3)
    tk.Label(ca,text='大豚鼠').grid(row=3,column=1)


    tk.Button(ca,text='浏览博客',command=ca.quit).grid(row=4,column=1,pady=4)


    ca.mainloop()