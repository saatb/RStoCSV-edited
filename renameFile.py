from tkinter.filedialog import askopenfilename
import csv
import os

def getDeviceName(file):
    #idk what this does i found it online
    csvreader = csv.reader(file)

    #generates header
    header = []
    header = next(csvreader)
    #print(header)
    headerIndex = header.index("Device")


    rows = []
    for row in csvreader:
        rows.append(row)

    row0 = rows[0]
    deviceName = row0[headerIndex]
    deviceName = deviceName.lower()

    return deviceName

def renameFile(file, deviceName, fileType):
    
    #rename file

    oldName = os.path.abspath(file.name)
    fileName = os.path.basename(file.name)
    index1 = oldName.index(fileName)
    newName = oldName[0:index1] + deviceName + fileType

    file.close()
    os.rename(oldName, newName)

    print("Renamed " + oldName[index1: ] + " to " + newName[index1: ])