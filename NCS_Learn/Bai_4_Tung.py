import ctypes
import sys
from ctypes import *
import win32api
import win32con
import win32process
from ctypes.wintypes import *
from ctypes import POINTER
from ctypes.wintypes import HANDLE, HLOCAL, LPVOID, WORD, DWORD, BOOL, ULONG, LPCWSTR
LPDWORD = POINTER(DWORD)
LPHANDLE = POINTER(HANDLE)
ULONG_PTR = POINTER(ULONG)

class STARTUPINFO(ctypes.Structure):
    _fields_ = [("cb", DWORD),
                ("lpReserved", LPCWSTR),
                ("lpDesktop", LPCWSTR),
                ("lpTitle", LPCWSTR),
                ("dwX", DWORD),
                ("dwY", DWORD),
                ("dwXSize", DWORD),
                ("dwYSize", DWORD),
                ("dwXCountChars", DWORD),
                ("dwYCountChars", DWORD),
                ("dwFillAttribute", DWORD),
                ("dwFlags", DWORD),
                ("wShowWindow", WORD),
                ("cbReserved2", WORD),
                ("lpReserved2", LPVOID),
                ("hStdInput", HANDLE),
                ("hStdOutput", HANDLE),
                ("hStdError", HANDLE)]
LPSTARTUPINFO = POINTER(STARTUPINFO)

def GetCurrentProcess():
    return ctypes.windll.kernel32.GetCurrentProcess()

def GetCurrentProcessId():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetCurrentProcessId = windll.kernel32.GetCurrentProcessId
    _GetCurrentProcessId.argtypes = []
    _GetCurrentProcessId.restype = ctypes.c_uint
    ID = _GetCurrentProcessId()
    return _GetCurrentProcessId()

def terminate_process(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hProcess = params["hProcess"]
    uExitCode = params["uExitCode"]
    kernel32.TerminateProcess(hProcess, uExitCode)

def create_process(params):
    kernel32 = ctypes.windll.kernel32
    lpApplicationName = params["lpApplicationName"]
    lpCommandLine = params["lpCommandLine"]
    lpEnvironment = params["lpEnvironment"]
    bInheritHandles = params["bInheritHandles"]
    dwCreationFlags = params["dwCreationFlags"]
    lpStartupInfo = params["lpStartupInfo"]
    lpCurrentDirectory = params["lpCurrentDirectory"]
    lpProcessAttributes = params["lpProcessAttributes"]
    lpThreadAttributes = params["lpThreadAttributes"]
    # if (type(lpFileName) == type(u"")):
    hProcess, hThread, dwProcessId, dwThreadId  = win32process.CreateProcess(lpApplicationName,lpCommandLine, lpProcessAttributes, lpThreadAttributes, bInheritHandles, dwCreationFlags, lpEnvironment, lpCurrentDirectory, lpStartupInfo)
    return hProcess, hThread, dwProcessId, dwThreadId 

def open_process(params):
    kernel32 = ctypes.windll.kernel32
    dwDesiredAccess = params["dwDesiredAccess"]
    idProcess = params["idProcess"]
    bInherit = params["bInherit"]
    hProcess = kernel32.OpenProcess(dwDesiredAccess, idProcess, bInherit)
    return hProcess

def get_process_heap(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    return kernel32.GetProcessHeap()

def process32_next(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hSnapshot = params["hSnapshot"]
    lppe = params["lppe"]
    return kernel32.Process32NextW(hSnapshot, lppe)

def process32_first(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hSnapshot = params["hSnapshot"]
    lppe = params["lppe"]
    return kernel32.Process32FirstW(hSnapshot, lppe)

def get_exit_code_process(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hProcess = params["hProcess"]
    lpExitCode = params["lpExitCode"]
    return kernel32.GetExitCodeProcess(hProcess, lpExitCode)

def write_process_memory(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hProcess = params["hProcess"]
    lpBaseAddress = params["lpBaseAddress"]
    lpBuffer = params["lpBuffer"]
    nSize = params["nSize"]
    return kernel32.WriteProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize)

def read_process_memory(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hProcess = params["hProcess"]
    lpBaseAddress = params["lpBaseAddress"]
    lpBuffer = params["lpBuffer"]
    nSize = params["nSize"]
    return kernel32.ReadProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize)

def get_process_id(params):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    hProcess = params["hProcess"]
    return kernel32.GetProcessId(hProcess)

def main():
    params= dict()
    params["hProcess"] = GetCurrentProcessId()
    params["uExitCode"] = 0
    pid = GetCurrentProcessId()
    print(pid)
    rv = terminate_process(params)
    if (rv != 0):
        print("Terminated")
    else:
        print("Failed to terminate")

    params.clear()    
    params["lpApplicationName"] = "C:\masm32\Wiin32\Bai43.exe"
    params["lpCommandLine"] = "Bai43.exe"
    params["lpProcessAttributes"] = None
    params["lpThreadAttributes"] = None
    params["bInheritHandles"] = 0
    params["dwCreationFlags"] = win32process.CREATE_NEW_CONSOLE
    params["lpEnvironment"] = None
    params["lpCurrentDirectory"] = None
    params["lpStartupInfo"] = win32process.STARTUPINFO()
    hProcess, hThread, dwProcessId, dwThreadId  = create_process(params)

    params.clear()    
    params["dwDesiredAccess"] = win32con.PROCESS_TERMINATE
    params["bInherit"] = True 
    params["idProcess"] = GetCurrentProcessId()
    h_process = open_process(params)

    params.clear()
    ph = get_process_heap(params)
    if (ph == 0):
        print("Failed to get process heap")
    else:
        print("Got process heap")

    params.clear()
    # CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
    # hProcessSnap = CreateToolhelp32Snapshot(0x00000002, 0)
    # params["hSnapshot"] = hProcessSnap
    # params["lppe"] = 0
    params["hSnapshot"] = 0
    params["lppe"] = 0
    pf = process32_first(params)

    params.clear()
    params["hSnapshot"] = 0
    params["lppe"] = 0
    pf = process32_next(params)

    params.clear()
    params["hProcess"] = GetCurrentProcessId()
    params["lpExitCode"] = 0
    ecp = get_exit_code_process(params)
    if (ecp == None):
        print("Failed to get exit code process")
    else:
        print("Got exit code process")
    
    params.clear()
    params["hProcess"] = GetCurrentProcessId()
    params["lpBaseAddress"] = 0
    params["lpBuffer"] = b""
    params["nSize"] = 0
    wm = write_process_memory(params)
    
    
    params.clear()
    params["hProcess"] = GetCurrentProcessId()
    params["lpBaseAddress"] = 0
    params["lpBuffer"] = "NCSGroup".encode("UTF-8")
    params["nSize"] = 0
    wm = read_process_memory(params)
    

    params.clear()
    params["hProcess"] = GetCurrentProcessId()
    pid = get_process_id(params)
    print(pid)
main()
