import win32api
from win32file import *

def hook_CreateFileA(params):
    lpFileName= params["lpFileName"]
    dwDesiredAccess= params["dwDesiredAccess"]
    dwShareMode= params["dwShareMode"]
    lpSecurityAttributes= params["lpSecurityAttributes"]
    dwCreationDisposition=params["dwCreationDisposition"]
    dwFlagsAndAttributes=params["dwFlagsAndAttributes"]
    hTemplateFile=params["hTemplateFile"]
    CreateFile(lpFileName,dwDesiredAccess,dwShareMode,lpSecurityAttributes,dwCreationDisposition,dwFlagsAndAttributes,hTemplateFile) 
    
dict1={
       "lpFileName":"D:\\Bai_3\\Bai3.txt",
       "dwDesiredAccess":GENERIC_READ+GENERIC_WRITE,
       "dwShareMode":0,
       "lpSecurityAttributes":None,
       "dwCreationDisposition":OPEN_EXISTING,
       "dwFlagsAndAttributes":FILE_ATTRIBUTE_NORMAL,
       "hTemplateFile": 0    
       }
hFile = hook_CreateFileA(dict1)
if (hFile == INVALID_HANDLE_VALUE):
   print("CreateFile Failed!")
else:
   print("CreateFile Susscessful!")

def hook_ReadFile(params1):
    hFile = params1["hFile"]
    lpBuffer = params1['lpBuffer']
    nNumberOfBytesToRead = params1["nNumberOfBytesToRead"]
    lpNumberOfBytesRead = params1["lpNumberOfBytesRead"]
    lpOverlapped=params1["lpOverlapped"]
    ReadFile(hFile, lpBuffer, lpOverlapped)
    
dict2={
        "hFile":hook_CreateFileA(dict1),
        "lpBuffer":0,
        "nNumberOfBytesToRead":0,
        "lpNumberOfBytesRead":None,
        "lpOverlapped":None, 
        }
bFile = hook_ReadFile(dict2)
if (bFile == False):
    print("ReadFile Failed!")
else:
    print("ReadFile Susscessful!")
    
def hook_WriteFile(params1):
    hFile = params1["hFile"]
    lpBuffer = params1['lpBuffer']
    nNumberOfBytesToWrite = params1["nNumberOfBytesToWrite"]
    lpNumberOfBytesWrite = params1["lpNumberOfBytesWrite"]
    lpOverlapped=params1["lpOverlapped"]
    WriteFile(hFile, lpBuffer ,lpOverlapped)
    
dict3={
       "hFile":hook_CreateFileA(dict1),
       "lpBuffer":str2bytes("Hello\0there"),
       "nNumberOfBytesToWrite":0,
       "lpNumberOfBytesWrite":None,
       "lpOverlapped":None, 
       }
bFile = hook_WriteFile(dict3)
if (bFile == False):
    print("WriteFile Failed!")
else:
    print("WriteFile Susscessful!")
def hook_CopyFile(params):
    lpExistingFileName= params["lpExistingFileName"]
    lpNewFileName= params["lpNewFileName"]
    bFailIfExists= params["bFailIfExists"]
    CopyFile(lpExistingFileName, lpNewFileName, bFailIfExists)
    
dict4={
       "lpExistingFileName":"D:\\Bai_3\\Bai3.txt",
       "lpNewFileName":"D:\\Bai_3\\Bai3_2.txt",
       "bFailIfExists":None,   
       }
hook_CopyFile(dict4)
if (bFailIfExists == None):
    print("WriteFile Failed!")
else:
    print("WriteFile Susscessful!")
    
def hook_CloseHandle(params):
    hObject = params["hObject"]
    CloseHandle(hObject)
dict5={
       "hObject":hook_CreateFileA(dict1), 
       }
hook_CloseHandle(dict5)


        
    
    
    
    