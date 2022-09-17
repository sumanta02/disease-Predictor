from tkinter import ttk
from tkinter import *
from parkinsonsfunc import Parkinsons
from BreastCancerFunc import BreastCancer
from DiabetesFunc import Diabetes
from HeartDiseaseFunc import HeartDisease


diseases = ["Heart Disease", "Breast Cancer", "Parkinsons", "Diabetes"]
parameters = [["Age", "Sex", "Chest pain type", "BP", "Cholesterol", "FBS over 120", "EKG results", "Max HR", "Exercise angina" , "ST depression", "Slope of ST", "Number of vessels fluro", "Thallium"], ["param 1", "param 2", "param 3", "param 4"], ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA","NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"], ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]

paramInputEntries = []
inputParams = []
paramLabels = []

mainWindow = Tk()
mainWindow.title("Disease Predictor")
mainWindow.geometry("600x600")

mainFrame = ttk.Frame(mainWindow, padding = "12 12 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

infoFrame  = ttk.Frame(mainWindow, padding="12 12 12 12")
infoCanvas = Canvas(infoFrame)

resultFrame = ttk.Frame(mainWindow, padding="12 12 12 12")

selectorLabel = Label (mainFrame, text="Select the disease to predict", justify=CENTER, font='Arial 14 bold')
selectorLabel.place(relx=0.5, rely=0, anchor=CENTER)
disease = StringVar()
disease.set(diseases[0])
Img = PhotoImage(file="drop-down-arrow.png")
SelectorMenu = OptionMenu(mainFrame, disease, *diseases)
SelectorMenu.config(indicatoron=0, compound='right', image=Img)
SelectorMenu.place(relx=0.5, rely=0.1, anchor=CENTER)

def resDisp(pred_arr):
    global resultFrame
    if pred_arr[0] in [1,"Presence"]:
        result = "Positive"
    else:
        result = "Negative"
    return result

def startProc(inputParams):
    global disease
    diseaseIndex = diseases.index(disease.get())
    if diseaseIndex == 0:
        accuracy, pred_arr = HeartDisease([inputParams])
    if diseaseIndex == 1:
        accuracy, pred_arr = BreastCancer([inputParams])
    if diseaseIndex == 2:
        accuracy, pred_arr = Parkinsons([inputParams])
    if diseaseIndex == 3:
        accuracy, pred_arr = Diabetes([inputParams])
    infoFrame.pack_forget()
    infoCanvas.pack_forget()
    resultFrame.pack(fill=BOTH, expand=True)
    resultFrame.columnconfigure(0, weight=1)
    resultFrame.rowconfigure(0, weight=1)
    resultEntry = Label(resultFrame, text="Result", font="Arial 17 bold", justify=CENTER)
    resultEntry.pack()
    result = resDisp(pred_arr)
    result_disp = Label(resultFrame, text = disease.get() + ": " + result, font="Arial 14 bold", justify=CENTER)
    result_disp.pack()
    acc = Label(resultFrame, text="Accuracy: " + str(accuracy) + "%", font="Arial 14 bold", justify=CENTER)
    acc.pack()


def getParams(inputParams, paramSet):
    for i in range(len(paramSet)):
        inputParams.append(paramInputEntries[i].get())
    input = [eval(i) for i in inputParams]
    startProc(input)

def collectInfo(disease):
    global diseases
    mainFrame.grid_forget()
    mainWindow.title("Input Parameters")
    
    scroll = ttk.Scrollbar(infoFrame, orient=VERTICAL, command=infoCanvas.yview)
    scrollable_frame = ttk.Frame(infoCanvas)
    scrollable_frame.bind("<Configure>", lambda e: infoCanvas.configure(scrollregion=infoCanvas.bbox("all")))
    infoCanvas.create_window((0, 0), window=scrollable_frame, anchor=CENTER)
    infoCanvas.configure(yscrollcommand=scroll.set)
    infoFrame.pack(fill=BOTH, expand=True)
    infoCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)
    paramSet = parameters[diseases.index(disease)]
    count = 0
    for i in paramSet:
        temp = Label (scrollable_frame, text="Input " + str(paramSet[count]), justify=CENTER, font='Arial 10 bold')
        temp.pack(padx=5, pady=10, anchor=N)
        paramInputEntries.append(Entry(scrollable_frame, width=30, relief=SUNKEN, justify=CENTER))
        paramInputEntries[-1].pack(padx=5, pady=10)
        count += 1
    submitButton = Button(scrollable_frame, text="Get Results", command=lambda: getParams(inputParams, paramSet))
    submitButton.pack()
    



proceedButton = Button(mainFrame, text="Enter Information", width=15, height=3, command=lambda: collectInfo(disease.get()))
proceedButton.place(relx=0.5, rely=0.25, anchor=CENTER)


mainWindow.mainloop()