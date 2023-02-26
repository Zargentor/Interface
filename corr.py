from tkinter import *
from tkinter import filedialog
import billing
import os
from billing import interface,perebor_corr

root = Tk()
# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Поиск по слову')
# Указываем размеры окна
root.geometry('1200x1000')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

couttext = ""
global dirpath
def ButtonOne():
    dirpath = filedialog.askdirectory(
        parent=textworkgroup,
        title='Выберите директорию поиска'
    )
    label = Label(textworkgroup, text="Выбранная директория: " + dirpath, anchor='w')
    label.place(width=500, height=25)

    phraseforword = Label(textworkgroup, text="Введите слово для поиска", anchor='w', )
    phraseforword.place(width=500, height=20, y=25)

    textpool = Entry(textworkgroup)
    textpool.place(width=500, height=50, y=45)

    btn_two = Button(buttonworkgroup, text="Начать поиск", command=lambda:ButtonTwo(dirpath,s))
    btn_two.place(width=100, height=25, y=50)
    phraseforword = Label(textworkgroup, text="Введите слово для поиска", anchor='w', )
    phraseforword.place(width=500, height=20, y=25)
    textpool = Entry(textworkgroup)
    textpool.place(width=500, height=50, y=45)
    s = textpool

def ButtonTwo(dirpath, s):
    v = s.get()
    if v != None:
        interface(v, dirpath)
    cout = Text(textworkgroup, font=12)
    cout.insert(0.2,billing.count)
    cout.place(height=500, width=500, y=95)
    bb=cout.get()
    scrollright = Scrollbar(cout, command=cout.yview)
    scrollright.pack(side=LEFT, fill=Y)



textworkgroup = Frame(root, highlightbackground="black", highlightthickness=1, background='')
textworkgroup.place(width=500, height=800, x=15, y=15)

buttonworkgroup = Frame(root, highlightbackground="black", highlightthickness=1, background='')
buttonworkgroup.place(width=200, height=120, x=525, y=15)

btn_one = Button(buttonworkgroup, command=ButtonOne, text="Выберите \n директорию \n поиска")
btn_one.place(width=100, height=45)




root.mainloop()
