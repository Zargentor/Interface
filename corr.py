from tkinter import *
from tkinter import filedialog
import billing
from billing import interface,perebor_corr
from functools import partial
from tkinter import ttk
import time


root = Tk()
# Указываем фоновый цвет
root['bg'] = ''
# Указываем название окна
root.title('Поиск по слову')
# Указываем размеры окна
root.geometry('1000x800')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

couttext = ""

def ButtonOne():
    dirpath = filedialog.askdirectory(
        parent=textworkgroup,
        title='Выберите директорию поиска'
    )
    label = Label(textworkgroup, text="Выбранная директория: " + dirpath, anchor='w')
    label.place(width=690, height=25)
    textpool = Entry(textworkgroup)
    textpool.place(width=690, height=20, y=45)

    phraseforword = Label(textworkgroup, text="Введите слово для поиска", anchor='w', )
    phraseforword.place(width=690, height=20, y=25)
    s = textpool
    other = partial(ButtonTwo, dirpath, s)
    btn_two = Button(buttonworkgroup, text="Начать поиск", command=other)
    btn_two.place(width=100, height=25, y=50)
    return dirpath

def ButtonTwo(dirpath, s):
    v = s.get()
    if v != None:
        interface(v, dirpath)
    text = perebor_corr()
    Table(text)


def Table(text):
    valueVar = IntVar()
    Tree = ttk.Treeview(textworkgroup, columns=columns, show="headings")
    Tree.place(width=700, height=500, y=95)
    Tree.heading("filename", text="Имя файла", anchor=W)
    Tree.heading("word", text="Искомое слово", anchor=W)
    Tree.heading("sentence", text="Предложение", anchor=W)
    Tree.heading("wordcountbeforeword", text="Сдвиг от начала", anchor=W)
    Tree.heading("wordcountafterword", text="Сдвиг от конца", anchor=W)
    Tree.column("#1", stretch=YES, width=20)
    Tree.column("#2", stretch=YES, width=40)
    Tree.column("#3", stretch=YES, width=200)
    Tree.column("#4", stretch=YES, width=30)
    Tree.column("#5", stretch=YES, width=30)
    Progressbar = ttk.Progressbar(textworkgroup,orient="horizontal", mode="determinate",maximum=100)
    Progressbar.place(width=700, y=595)
    for i in range(len(text)):
        Tree.insert("", END, values=text[i])
        Progressbar.configure(value=i)
        time.sleep(0.05)
        Progressbar.update()




textworkgroup = Frame(root,  background='')
textworkgroup.place(width=690, height=800, x=15, y=15)

buttonworkgroup = Frame(root, background='')
buttonworkgroup.place(width=200, height=120, x=720, y=15)
columns = ("filename", "word","sentence","wordcountbeforeword","wordcountafterword")

btn_one = Button(buttonworkgroup, command=ButtonOne, text="Выберите \n директорию \n поиска")
btn_one.place(width=100, height=45)





root.mainloop()
