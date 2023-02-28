import os

from os.path import basename
import re

dict = []  # массив для записи отдельных предложений
directory = ""
word = ""
count = ""
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
    global trash
    res_list = []
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
        for i in sentences:
            if word in i:
                readydictionary = (filename[0], ":", i)
                wordcountbeforeword = word_text.index(word)
                wordcountafterword = (len_all - word_text.index(word) - len_curr)
                # trash = (readydictionary + '\n', wordcountbeforeword, '\n', wordcountafterword)
                dictionary = (filename[0], word,i, wordcountafterword, wordcountbeforeword)
                # res_list[filename[0]] = dictionary
                res_list.append(dictionary)
                # dictionary["sentences"].append(i)
                # dictionary["wordcountbeforeword"].append(wordcountbeforeword)
                # dictionary["wordcountafterword"].append(wordcountafterword)
    return res_list

def interface(v, dirpath):
    global word
    global directory
    shere = ""
    shere = v
    word = str(shere).lower()
    directory = dirpath
    corr()
    perebor_corr()
