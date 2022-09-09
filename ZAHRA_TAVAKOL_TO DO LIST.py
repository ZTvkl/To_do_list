import tkinter
import tkinter.messagebox
import pickle
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.title("To do list by Zahra Tavakol")
root.resizable(0,0)
tasks=[]



def add_task():
    task = entry_task.get()
    if task!= "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task.")

def Delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_task():
   tasks = listbox_tasks.get(0, listbox_tasks.size())
   pickle.dump(tasks, open("tasks.dat", "wb"))


def exit_task():
    confex = messagebox.askquestion('Quit Confirmation', 'Are you sure you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass

def  info_task():
     messagebox.showinfo("info", "This is Todolist 1 \ncreated by Zahra Tavakol ",)

def Deleteall_task():
    conf = messagebox.askquestion("delete all?", "Are you sure you want to delete all tasks?")
    print(conf)
    if conf.upper() == "YES":
        listbox_tasks.delete(0, tkinter.END)


    else:
        pass
    

def number_task():

    label_dsply.config(state=NORMAL)
    label_dsply.delete(0, tkinter.END)
    listbox_tasks.index("end")
    count = listbox_tasks.index("end")
    print (count)
    
    label_dsply.insert(tkinter.END, count)
    label_dsply.config(state=DISABLED)




# creat GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()



listbox_tasks = tkinter.Listbox(frame_tasks, height = 10,width = 50,font=("Times New Roman",12),bd=5, relief=RIDGE, bg='#E6D5B8')
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50,font=("Times New Roman",12))
entry_task.pack()

button_add_task = tkinter.Button(root, text = "Add Task" ,font=("Times New Roman",12),bg='#E6DEDD',activebackground='#E0BB20', width=48, command = add_task)
button_add_task.pack()

button_Delete_task = tkinter.Button(root, text = "Delete Task" ,font=("Times New Roman",12),bg='#E6DEDD', width=48,activebackground='#E0BB20', command = Delete_task)
button_Delete_task.pack()

button_load_task = tkinter.Button(root, text = "Load Task" ,font=("Times New Roman",12),bg='#E6DEDD', width=48,activebackground='#E0BB20', command = load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text = "Save Task" ,font=("Times New Roman",12),bg='#E6DEDD',fg='black', width=48,activebackground='#E0BB20', command = save_task)
button_save_task.pack()

button_exit_task = tkinter.Button(root, text = "Exit" ,font=("Times New Roman",12),bg='#E6DEDD', width=48,activebackground='#E0BB20', command = exit_task)
button_exit_task.pack()

button_info_task = tkinter.Button(root, text = "Info" ,font=("Times New Roman",12),bg='#E6DEDD', width=48,activebackground='#E0BB20', command = info_task)
button_info_task.pack()

button_Deleteall_task = tkinter.Button(root, text = "Delete all" ,font=("Times New Roman",12),bg='#E6DEDD',activebackground='#E0BB20', width=48, command = Deleteall_task)
button_Deleteall_task.pack()

number_task = tkinter.Button(root, text="Number of Task",font=("Times New Roman",12),bg='#E6DEDD', width=48,activebackground='#E0BB20', command=number_task)
number_task.pack()

label_dsply = tkinter.Entry(root, text="",width=50, bg="white",state=DISABLED)
label_dsply.pack()



root.mainloop()