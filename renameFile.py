import csv
import os
import tkinter.filedialog
def getDeviceName(file):

    file = open(file) #open file
    
    csvreader = csv.reader(file) #idk what this does i found it online

    #generates header and finds index that device name is stored at
    header = []
    header = next(csvreader)
    headerIndex = header.index('Device')

    #grabs rows
    rows = []
    for row in csvreader:
        rows.append(row)

    #grabs device name by using previously found index
    row0 = rows[0]
    deviceName = row0[headerIndex]
    deviceName = deviceName.lower()

    file.close() #close file

    return deviceName #return device name to be used with renameFile method

def renameFile(file, fileType, deviceName):
    
    #rename file

    oldName = os.path.abspath(file) #find directory of file (long path thing)
    fileName = os.path.basename(file) #find the file name (i.e. "Example.json")

    #get index of file name and replace it with the new file name
    index1 = oldName.index(fileName) 
    newName = oldName[0:index1] + deviceName + fileType

    os.rename(oldName, newName) #actually rename the file

    print("Renamed " + oldName[index1: ] + " to " + newName[index1: ]) #tells us what the files are now named