from tkinter import *

def readFile(f:str,d:dict):
    file = open(f)
    di = file.read().split("\n")[:-1]
    for item in di:
        country = item.split("-")[0]
        capital = item.split("-")[1]
        d[country] = capital
    file.close()
    return d

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def fileSave(f:str,i1:str,i2:str):
    l={}
    file=open(f,'w',encoding="utf-8-sig")
    file.write(f"{i1}-{i2}"+'\n')
    l=readFile(f,l)
    file.close()

def newWord(f:str,i1:str,i2:str):
    l={}
    with open(f,"a",encoding="utf-8-sig") as file:
        file.write(f"{i1}-{i2}"+'\n')
    l=readFile(f,l)
    return l

