import tkinter as tk
import designconn as dc


    conn = dc.createConnection('cat')
    id1 = e3
    password1 = e4
    cursor = conn.cursor()
    cursor.executemany(
        "insert into dbo.userdata VALUES (%s,%s,%d)",
        [(id1,password1,0)]
    )
    conn.commit()
    conn.close()



def create():
    topr=tk.Tk()
    topr.title('注册界面')
    tk.Label(text='请输入id').grid(row=0) #标签
    tk.Label(text='请输入密码').grid(row=1)#标签
    rid = tk.Entry()#输入框
    rid.grid(row=0, column=1)
    rpassword = tk.Entry()#输入框
    rpassword.grid(row=1, column=1)
    tk.Button(text='返回', command=topr.quit).grid(row=2, column=0, pady=4)#按钮
    tk.Button(text='提交', command=register).grid(row=2, column=1, pady=4)
    topr.mainloop()


