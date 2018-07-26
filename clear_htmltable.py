import re
from tkinter import *
from tkinter.messagebox import *
import win32clipboard as w
import win32con
root = Tk()
fm = []
root.title("html标签清洗")
width, height = 400, 500  # 窗口大小
for color in [0,1,2,3,4,5,6,7,8,9]:
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    fm.append(Frame(height =height,width =width))

root.geometry('%dx%d+%d+%d' % (width,height,(root.winfo_screenwidth() - width ) / 2, (root.winfo_screenheight() - height) / 2))#窗口居中显示

lableSign = Label(fm[0], text="请粘贴要转换的内容")
lableSign.pack()
textinput = Text(fm[0], width=40, height=10)
textinput.pack()

def print_file():
    showinfo(title="文件输出", message="成功" )
    web = open("./end.txt", "w+")
    dd=textend.get("0.0", "end")
    dd.encode('gbk')
    web.write(dd)
    web.close()
def print_Clipboard():
    dd = str(textend.get("0.0", "end"))
    print_settext(dd)
def print_settext(aString):
     w.OpenClipboard()
     w.EmptyClipboard()
     w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
     w.CloseClipboard()
def clear_html():
    textend.delete(0.0, 'end')
    html=textinput.get("0.0", "end")
    dr = re.compile(r'<[^>]+>',re.S)
    html=str(html)
    dd = dr.sub('',html)
    textend.insert(END, dd)
    fm[1].pack()
bottonSign_input = Button(fm[0], text="转换", command=clear_html)
bottonSign_input.pack()
bottonClipboard = Button(fm[1],text = "输出到剪切板",command = print_Clipboard)
bottonClipboard.pack()
bottonfile = Button(fm[1],text = "输出到文件",command = print_file)
bottonfile.pack()
textend = Text(fm[0], width=40, height=13)
textend.pack()
fm[0].pack()
mainloop()