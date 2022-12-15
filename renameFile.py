from tkinter.filedialog import askopenfile
import csv
import os

def getDeviceName(file):
    #idk what this does i found it online
    csvreader = csv.reader(file)

    #generates header
    header = []
    header = next(csvreader)
    print(header)
    headerIndex = header.index('Device')


    rows = []
    for row in csvreader:
        rows.append(row)

    row0 = rows[0]
    deviceName = row0[headerIndex]
    deviceName = deviceName.lower()

    return deviceName

def renameFile(file, fileType, deviceName):
    
    #rename file

    oldName = os.path.abspath(file)
    fileName = os.path.basename(file)
    index1 = oldName.index(fileName)
    newName = oldName[0:index1] + deviceName + fileType

    os.rename(oldName, newName)

    print("Renamed " + oldName[index1: ] + " to " + newName[index1: ])

#file = askopenfile(filetypes=[("CSV files", "*.csv")])
#getDeviceName(file)