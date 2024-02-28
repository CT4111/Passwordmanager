import customtkinter as ctk
from customtkinter import CTk
import json

def AddNewCredential(Labletext,num,scrollableFrame):
    global array
    try:
        if len(array) >= 3:
            array = []
    except:
        array=[]
    dialog = ctk.CTkInputDialog(text = Labletext,title="TEST")
    array.append(dialog.get_input())
    if num <2:
        num += 1
        if(num == 1):
            Labletext = "Test2"
        elif (num == 2):
            Labletext = "Test3"
        AddNewCredential(Labletext, num,scrollableFrame)
    else:
        AppendToJson(array[0],array[1],array[2])
        AppendElementsToList(scrollableFrame)

def AddingCredentialsToList(array,scrollableFrame,counter):
    global r
    r = ctk.IntVar()
    newEntry = ctk.CTkLabel(scrollableFrame,text=f"{counter} {array[0]} Username: {array[1]} Password: {array[2]}")
    newEntry.pack()

def Setup():
    ctk.set_appearance_mode("Dark")
    app = CTk()
    # app.title()
    # app.iconbitmap()
    app.geometry("500x400")
    return app
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def AppendToJson(name,username,password):
    newdata = {name: {
        "Username": username,
        "Password": password}
    }
    filename = "Credentials.json"
    with open(filename) as fp:
        listObj = json.load(fp)

    listObj.update(newdata)

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file,
                  indent=4,
                  separators=(',', ': '))
def SaveJsonInArray():
    with open("Credentials.json", 'r') as jsFile:
        data = json.load(jsFile)
    CredentialsArray = [[], [], []]
    for i in data:
        CredentialsArray[0].append(i)
    #sortArray
    CredentialsArray[0]=qsort(CredentialsArray[0])
    for i in CredentialsArray[0]:
        for x, jData in enumerate(data[i]):
            CredentialsArray[x + 1].append(data[i][jData])
    return CredentialsArray
def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
def AppendElementsToList(scrollFrame):
    clearFrame(scrollFrame)
    credentials = SaveJsonInArray()
    for i in range(len(credentials[0])):
        array = [credentials[0][i],credentials[1][i],credentials[2][i]]
        AddingCredentialsToList(array,scrollFrame,i)

def GUI():
    app = Setup()
    mainFrame = ctk.CTkFrame(app)
    scrollableFrame = ctk.CTkScrollableFrame(mainFrame)
    AddInformationButton = ctk.CTkButton(mainFrame, text="Add credentials",
                                         command=lambda: AddNewCredential("Test1", 0, scrollableFrame))
    scrollableFrame.pack(fill="both", expand=True, pady=10, padx=100)
    AddInformationButton.pack(padx=20)
    mainFrame.pack(fill="both", expand=True, pady=10, padx=10)
    AppendElementsToList(scrollableFrame)
    app.mainloop()
GUI()