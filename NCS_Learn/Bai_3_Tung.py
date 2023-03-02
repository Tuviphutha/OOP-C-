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
    if (type(lpFileName) == type(u"")):
        hFile = CreateFileW(lpFileName,dwDesiredAccess,dwShareMode,lpSecurityAttributes,dwCreationDisposition,dwFlagsAndAttributes,hTemplateFile) 
    else:
        hFile = CreateFileA(lpFileName,dwDesiredAccess,dwShareMode,lpSecurityAttributes,dwCreationDisposition,dwFlagsAndAttributes,hTemplateFile)
    return hFile

def hook_WriteFile(params):
    hFile = params["hFile"]
    lpBuffer = params['lpBuffer']
    nNumberOfBytesToWrite = params["nNumberOfBytesToWrite"]
    lpNumberOfBytesWrite = params["lpNumberOfBytesWrite"]
    lpOverlapped=params["lpOverlapped"]
    str1, Wfile = WriteFile(hFile, lpBuffer ,lpOverlapped)
    return str1, Wfile
    
def hook_ReadFile(params):
    hFile = params["hFile"]
    lpBuffer = params['lpBuffer']
    nNumberOfBytesToRead = params["nNumberOfBytesToRead"]
    lpNumberOfBytesRead = params["lpNumberOfBytesRead"]
    lpOverlapped=params["lpOverlapped"]
    ind1, ind2 = ReadFile(hFile, lpBuffer, lpOverlapped)
    return ind1, ind2
    
def hook_CopyFile(params):
    lpExistingFileName= params["lpExistingFileName"]
    lpNewFileName= params["lpNewFileName"]
    bFailIfExists= params["bFailIfExists"]
    CopyFile(lpExistingFileName, lpNewFileName, bFailIfExists)
    
def hook_CloseHandle(params):
    hObject = params["hObject"]
    CloseHandle(hObject)
    
def main():
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

    bufff=AllocateReadBuffer(1024)    
    dict3={
       "hFile":hFile,
       "lpBuffer": "tungtienti".encode("UTF-8"),
       "nNumberOfBytesToWrite":0,
       "lpNumberOfBytesWrite":None,
       "lpOverlapped":None, 
       }

    bFile= hook_WriteFile(dict3)
    if (bFile == False):
        print("WriteFile Failed!")
    else:
        print("WriteFile Susscessful!")

    dict2={
            "hFile":hFile,
            "lpBuffer": 30,
            "nNumberOfBytesToRead":128,
            "lpNumberOfBytesRead":None,
            "lpOverlapped":None, 
            }
    bFile = hook_ReadFile(dict2)
    if (bFile == False):
        print("ReadFile Failed!")
    else:
        print("ReadFile Susscessful!")  
         
    dict4={
        "lpExistingFileName":"D:\\Bai_3\\Bai3_3.txt",
        "lpNewFileName":"D:\\Bai_3\\Bai3_2.txt",
        "bFailIfExists": False,   
        }
    hook_CopyFile(dict4)
    
    dict5={
        "hObject":hFile, 
        }
    hook_CloseHandle(dict5)
main()