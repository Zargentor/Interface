import os

from os.path import basename
import re
from corr import *

dict = []  # массив для записи отдельных предложений
directory = ""
word = ""
dirr = []
def corr():
    global dirr
    global dict
    global directory
    for adress, dirs, files in os.walk(os.path.normpath(directory)):
        for file in files:
            if file.endswith('.txt'):
                dict.append(os.path.join(adress,file))

def perebor_corr():
    global dict
    global word
    dictionary = {}
    for files_txt in dict:
        word_text = open(files_txt, 'r', encoding='utf-8', errors='ignore').read().lower()  # считывает весь текст из всех текстовых документов
        len_all = len(word_text)
        len_curr = len(word)
        filename = os.path.splitext(basename(files_txt)[:-4])   # отрезает у названий файлов .txt
        split_regex = re.compile(r'[.]')  # для деления словаря на предложения по точкам
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(word_text)])
        for i in sentences:
            if word in i:
                print(filename[0], ":",i)
                print("Количество символов до слова",word,"=",word_text.index(word))
                print("Количество символов после слова",word,"=", len_all - word_text.index(word) - len_curr)



def interface():
    global word
    global directory
    global dirpath
    global textpool
    word = textpool
    directory = dirpath
    corr()
    perebor_corr()
