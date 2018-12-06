import pymssql
import random
import tkinter as tk
import designconn as dc
import userinterface
import interfacebeer
import interfacecat

def createConnection(dba):
    conn = pymssql.connect(server='(local)',user='sa',password='123',database=dba)
    return conn

def closeConnection(conn):
    conn.close

def checkout(e1,e2):
    int(e1)
    int(e2)
    conn = pymssql.connect(server='(local)', user='sa', password='123', database='cat')
    cursor = conn.cursor()
    cursor.execute('select integral from userdata where id=%s and password=%s' % (e1, e2))
    row1 = cursor.fetchone() #第一组
    print(row1)
    row = row1
    if row !=None:
        interfacecat.cat(e1,e2,row)
        return
    else:
        t1 = tk.Tk()
        tk.Label(t1, text='账号或密码错误').grid(row=1)

    row = None

    conn = pymssql.connect(server='(local)', user='sa', password='123', database='beer')
    cursor = conn.cursor()
    cursor.execute('select integral from userdata where id=%s and password=%s' % (e1, e2))
    row2 = cursor.fetchone()  # 第二组
    row = row2
    if row != None:
        interfacebeer.bear(e1, e2, row)
        return
    else:
        t1 = tk.Tk()
        tk.Label(t1, text='账号或密码错误').grid(row=1)

    row = None


    conn = pymssql.connect(server='(local)', user='sa', password='123', database='vildae')
    cursor = conn.cursor()
    cursor.execute('select integral from userdata where id=%s and password=%s' % (e1, e2))
    row3 = cursor.fetchone()  # 第三组

    row = row3
    if row != None:
        userinterface.vildae(e1, e2, row)
        return
    else:
        t1 = tk.Tk()
        tk.Label(t1, text='账号或密码错误').grid(row=1)
    row = None








    conn.close





