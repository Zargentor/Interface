import os

from os.path import basename
import re

dict = []  # массив для записи отдельных предложений
directory = ""
word = ""


def corr():
    global dirr
    global dict
    global directory
    for adress, dirs, files in os.walk(os.path.normpath(directory)):
        for file in files:
            if file.endswith('.txt'):
                dict.append(os.path.join(adress, file))


def perebor_corr():
    global dict
    global word
    dictionary = {}
    for files_txt in dict:
        word_text = open(files_txt, 'r', encoding='utf-8',
                         errors='ignore').read().lower()  # считывает весь текст из всех текстовых документов
        len_all = len(word_text)
        len_curr = len(word)
        filename = os.path.splitext(basename(files_txt)[:-4])  # отрезает у названий файлов .txt
        split_regex = re.compile(r'[.]')  # для деления словаря на предложения по точкам
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(word_text)])
        readydictionary = ""
        wordcountbeforeword = ""
        wordcountafterword = ""
        trash = ""
        for i in sentences:
            if word in i:
                readydictionary = (filename[0], ":", i)
                wordcountbeforeword = ("Количество символов до слова", word, "=", word_text.index(word))
                wordcountafterword = ("Количество символов после слова", word, "=", len_all - word_text.index(word) - len_curr)
                trash = (readydictionary , "\n", wordcountbeforeword, "\n", wordcountafterword)
                return trash

def interface(s, dirpath):
    global word
    global directory
    shere = ""
    shere = s
    word = str(shere)
    directory = dirpath
    corr()
    perebor_corr()
