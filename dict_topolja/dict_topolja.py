from tkinter import *
from module1 import *

dict=dict()
dict=readFile("riigid_pealinnad.txt",dict)
print(dict)

def main(event):
	buttonNew.place(x=3000,y=3000)
	inputWord2.place(x=0,y=18000)
	input=str(inputWord.get())
	if input in dict:
		result=dict[input]
		lblResult.config(text=result)
	elif type(get_key(dict, input))==str:
		result=get_key(dict, input)
		print('Result: ',result)
		lblResult.config(text=result)
	else:
		buttonNew.pack(side=LEFT)
		inputWord2.place(x=0,y=180)
		lblResult.config(text="Слово отсутствует")

def newWord(event):
	input1=str(inputWord.get())
	lblResult.config(text="Введите столицу/страну")
	input2=str(inputWord2.get())
	dict[input1]=input2
	fileSave("riigid_pealinnad.txt",input1,input2)

window=Tk()
window.title("Euroopa riigid")
window.geometry("700x300")

lbl=Label(window,text="Euroopa Riigid",font="Arial 25",height=2,width=35,bg="blue",fg="white")
lbl.pack()
lblResult=Label(window,text="",font="Arial 20",height=2,width=20,bg="blue",fg="white")
lblResult.pack(side=BOTTOM)

inputWord=Entry(window,bg="green",fg="white",font="Arial 30",width=10,justify=LEFT)
inputWord.pack(side=LEFT)
inputWord.bind("<Return>",main)

inputWord2=Entry(window,bg="yellow",fg="black",font="Arial 30",width=10,justify=LEFT)
inputWord2.place(x=0,y=18000)
inputWord2.bind("<Return>",main)

buttonSolve=Button(window,text="Найти",font="Arial 20",width=8,bg="blue",fg="white")
buttonSolve.pack(side=LEFT)
buttonSolve.bind("<Button-1>",main)

buttonNew=Button(window,text="Добавить Слово",font="Arial 20",width=20,bg="blue",fg="white")
buttonNew.place(x=3000,y=3000)
buttonNew.bind("<Button-1>",newWord)

window.mainloop()