from tkinter import *
from tkinter import filedialog
import main
import os


dirpath = ""
root = Tk()
# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Поиск по слову')
# Указываем размеры окна
root.geometry('800x600')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

def ButtonOne():
    global dirpath
    dirpath = filedialog.askdirectory(
        parent=textworkgroup,
        title='Выберите директорию поиска'
    )
    label = Label(textworkgroup, text=dirpath, anchor='w')
    label.place(width=500, height=25)

textworkgroup = Frame(root, highlightbackground="black", highlightthickness=1, background='')
textworkgroup.place(width=500, height=400, x=15, y=15)

buttonworkgroup = Frame(root, highlightbackground="black", highlightthickness=1, background='')
buttonworkgroup.place(width=100, height=60, x=525, y=15)



btn_one = Button(buttonworkgroup, command=ButtonOne)
btn_one.place(width=100, height=25)
btn_two = Button(buttonworkgroup)
btn_two.place(width=100, height=25, y=30)

# textpool = Text(textworkgroup)
# textpool.place(width=500, height=25)



root.mainloop()