from tkinter import ttk
from tkinter import *
from customtkinter import *
from parkinsonsfunc import Parkinsons
from BreastCancerFunc import BreastCancer
from DiabetesFunc import Diabetes
from HeartDiseaseFunc import HeartDisease


diseases = ["Heart Disease", "Breast Cancer", "Parkinsons", "Diabetes"]
parameters = [["Age", "Sex", "Chest pain type", "BP", "Cholesterol", "FBS over 120", "EKG results", "Max HR", "Exercise angina" , "ST depression", "Slope of ST", "Number of vessels fluro", "Thallium"], ["param 1", "param 2", "param 3", "param 4"], ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA","NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"], ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]

paramInputEntries = []
inputParams = []
paramLabels = []


set_default_color_theme("blue")
set_appearance_mode("dark")
mainWindow = CTk()
mainWindow.title("Disease Predictor")
mainWindow.geometry("600x600")



mainFrame = CTkFrame(mainWindow)
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

infoFrame  = CTkFrame(mainWindow, fg_color="#2a2d2e")
infoCanvas = CTkCanvas(infoFrame)

resultFrame = CTkFrame(mainWindow, fg_color="#2a2d2e")

selectorLabel = CTkLabel (master=mainFrame, text="Select the disease to predict", justify=CENTER, text_font=("Arial", 14))
selectorLabel.pack(anchor=CENTER)
disease = StringVar()
disease.set(diseases[0])
SelectorMenu = CTkOptionMenu(master=mainFrame, variable=disease, values=diseases, corner_radius=5)

SelectorMenu.pack(anchor=CENTER, padx=20, pady=10)


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
        accuracy, pred_arr = HeartDisease([[float(x) for x in inputParams]])
    if diseaseIndex == 1:
        accuracy, pred_arr = BreastCancer([[float(x) for x in inputParams]])
    if diseaseIndex == 2:
        accuracy, pred_arr = Parkinsons([[float(x) for x in inputParams]])
    if diseaseIndex == 3:
        accuracy, pred_arr = Diabetes([[float(x) for x in inputParams]])
    infoFrame.pack_forget()
    infoCanvas.pack_forget()
    resultFrame.pack(fill=BOTH, expand=True)
    resultFrame.columnconfigure(0, weight=1)
    resultFrame.rowconfigure(0, weight=1)
    resultEntry = CTkLabel(resultFrame, text="Result", text_font=("Arial", 17), justify=CENTER)
    resultEntry.pack()
    result = resDisp(pred_arr)
    result_disp = CTkLabel(resultFrame, text = disease.get() + ": " + result, text_font=("Arial", 14), justify=CENTER)
    result_disp.pack()
    acc = CTkLabel(resultFrame, text="Accuracy: " + str(accuracy) + "%", text_font=("Arial", 14), justify=CENTER)
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
    
    scroll = CTkScrollbar(infoFrame, orientation=VERTICAL, command=infoCanvas.yview)
    scrollable_frame = CTkFrame(infoCanvas, fg_color="#2a2d2e", bg_color="#2a2d2e")
    scrollable_frame.bind("<Configure>", lambda e: infoCanvas.configure(scrollregion=infoCanvas.bbox("all")))
    infoCanvas.create_window((0, 0), window=scrollable_frame, anchor=CENTER)
    infoCanvas.configure(yscrollcommand=scroll.set)
    infoCanvas.configure(bg="#2a2d2e")
    infoFrame.pack(fill=BOTH, expand=True)
    infoCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)
    paramSet = parameters[diseases.index(disease)]
    count = 0
    for i in paramSet:
        temp = CTkLabel (scrollable_frame, text="Input " + str(paramSet[count]), justify=CENTER, text_font=("Arial", 10), bg_color="#2a2d2e")
        temp.pack(padx=5, pady=10, anchor=N)
        paramInputEntries.append(CTkEntry(scrollable_frame, justify=CENTER, bg_color="#2a2d2e", width=120, height=25))
        paramInputEntries[-1].pack(padx=5, pady=10)
        count += 1
    submitButton = CTkButton(scrollable_frame, text="Get Results", command=lambda: getParams(inputParams, paramSet), corner_radius=5)
    submitButton.pack(anchor=CENTER, padx=20, pady=10)
    



proceedButton = CTkButton(mainFrame, text="Enter Information", width=15, height=3, command=lambda: collectInfo(disease.get()), corner_radius=5)
proceedButton.pack(anchor=CENTER)


mainWindow.mainloop()