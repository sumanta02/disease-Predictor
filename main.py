from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


diseases = ["Covid-19", "Breast Cancer", "Parkinsons", "Diabetes"]
parameters = [["param 1", "param2"], ["param 1", "param 2", "param 3", "param 4"], ["param 1", "param 2", "param 3"], ["param 1", "param 2", "param 3", "param 4", ]]

mainWindow = Tk()
mainWindow.title("Disease Predictor")
mainWindow.geometry("600x600")

mainFrame = ttk.Frame(mainWindow, padding = "12 12 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

selectorLabel = Label (mainFrame, text="Select the disease to predict", justify=CENTER, font='Arial 14 bold')
selectorLabel.place(relx=0.5, rely=0, anchor=CENTER)
disease = StringVar()
disease.set(diseases[0])
SelectorMenu = OptionMenu(mainFrame, disease, *diseases)
SelectorMenu.place(relx=0.5, rely=0.1, anchor=CENTER)

def getParams():
    return

def collectInfo(disease):
    global diseases
    mainFrame.grid_forget()
    mainWindow.title("Input Parameters")
    infoFrame = ttk.Frame(mainWindow, padding="12 12 12 12")
    infoFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    infoFrame.columnconfigure(0, weight=1)
    infoFrame.rowconfigure(0, weight=1)
    paramSet = parameters[diseases.index(disease)]
    params = []
    paramInputs = []
    paramLabels = []
    count = 0
    for i in paramSet:
        temp = Label (infoFrame, text="Input " + str(paramSet[count]), justify=CENTER, font='Arial 10 bold')
        temp.pack(padx=5, pady=10)
        paramInputs.append(Entry(infoFrame, width=30, relief=SUNKEN))
        paramInputs[-1].pack(padx=5, pady=10)
        count += 1
    submitButton = Button(infoFrame, text="Get Results", command=lambda: getParams)



proceedButton = Button(mainFrame, text="Enter Information", width=15, height=3, command=lambda: collectInfo(disease.get()))
proceedButton.place(relx=0.5, rely=0.2, anchor=CENTER)


mainWindow.mainloop()