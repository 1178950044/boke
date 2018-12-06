import tkinter as tk
import pymssql

def bear(e1,e2,row):
    be = tk.Tk()
    be.title('用户界面')
    be.geometry('1000x500')



    conn = pymssql.connect(server='(local)', user='sa', password='123', database='beer') #链接数据库
    cursor = conn.cursor()
    cursor.execute('select integral from userdata where id=%s and password=%s' % (e1, e2))
    vintegra2 = cursor.execute
    print(vintegra2)

    tk.Label(be, text='用户名').grid(row=1)  # 标签们
    tk.Label(be, text=e1).grid(row=1, column=1)
    tk.Label(be, text='积分').grid(row=2)
    tk.Label(be, text=row).grid(row=2, column=1)
    tk.Label(be, text='等级').grid(row=3)
    tk.Label(be, text='树懒熊').grid(row=3, column=1)


    tk.Button(be,text='浏览博客',command=be.quit).grid(row=4,column=1,pady=4)
    tk.Button(be,text='上传日志',command=be.quit).grid(row=4,column=0,pady=4)


    be.mainloop()