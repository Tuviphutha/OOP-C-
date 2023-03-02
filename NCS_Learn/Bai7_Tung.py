import win32api
import win32inet
import ctypes
import sys

def InternetCloseHandle(params) -> bool:
    hInternet = params["hInternet"]
    ich = win32inet.InternetCloseHandle(hInternet)
    return ich

def InternetReadFile(params):
    hFile = params["hFile"]
    lpBuffer = params["lpBuffer"]
    dwNumberOfBytesToRead = params["dwNumberOfBytesToRead"]
    lpdwNumberOfBytesToRead = params["dwNumberOfBytesToRead"]
    idf = win32inet.InternetReadFile(hFile, lpBuffer, dwNumberOfBytesToRead, lpdwNumberOfBytesToRead)
    return idf
    
def InternetOpen(params):
    lpszAgentName = params["lpszAgentName"]
    dwAccessType = params["dwAccessType"]
    lpszProxy = params["lpszProxy"]
    lpszProxyBypass = params["lpszProxyBypass"]
    dwFlags = params["dwFlags"]
    io = win32inet.InternetOpen(lpszAgentName, dwAccessType, lpszProxy, lpszProxyBypass, dwFlags)
    return io
    
def InternetConnect(params):
    hInternet = params["hInternet"]
    lpszServername = params["lpszServername"]
    nServerPort = params["nServerPort"]
    lpszUsername = params["lpszUsername"]
    lpszPassword = params["lpszPassword"]
    dwService = params["dwService"]
    dwFlags = params["dwFlags"]
    dwContext = params["dwContext"]
    ic = win32inet.InternetConnect(hInternet, lpszServername, nServerPort, lpszServername, nServerPort, lpszUsername, lpszPassword, dwService, dwFlags, dwContext)
    return iC

def OpenRequest(params):
    hConnection = params["hConnection"]
    lpszVerb = params["lpszVerb"]
    lpszObject = params["lpszObject"]
    lpszVersion = params["lpszVersion"]
    lpszReference = params["lpszReference"]
    lplpszAcceptTypes = params["lplpszAcceptTypes"]
    dwFlags = params["dwFlags"]
    dwContext = params["dwContext"]
    or = win32inet.OpenRequest(hConnection, lpszVerb, lpszObject, lpszVersion, lpszReference, lplpszAcceptTypes, dwFlags, dwContext)
    # win32inet.OpenRequest(hInternet, verb, objectName, version=HTTP_VERSION, referer=None, accept=None, flags=0)
    return or

def HttpSendRequest(params):
    hRequest = params["hRequest"]
    lpszHeader = params["lpszHeader"]
    dwHeader = params["dwHeader"]
    lpOptional = params["lpOptional"]
    dwOptionalLength = params["dwOptionalLength"]
    hsr = win32inet.HttpSendRequest(hRequest, lpszHeader, dwHeader, lpOptional, dwOptionalLength)
    return hsr
        
def InternetErrorDlg(params):
    hWnd = params["hWnd"]
    hRequest = params["hRequest"]
    dwError = params["dwError"]
    dwFlags = params["dwFlags"]
    lppvData = params["lppvData"]
    ied = win32inet.InternetErrorDlg(hWnd, hRequest, dwError, dwFlags, lppvData)
    return ied

def InternetSetOption(params):
    hInternet = params["hInternet"]
    dwOption = params["Option"]
    lpBuffer = params["lpBuffer"]
    dwBufferLength = params["dwBufferLength"]
    isp = win32inet.InternetSetOption(hInternet, dwOption, lpBuffer, dwBufferLength)
    return isp

def InternetQueryOption(params):
    hInternet = params["hInternet"]
    dwOption = params["Option"]
    lpBuffer = params["lpBuffer"]
    dwBufferLength = params["dwBufferLength"]
    iqp = win32inet.InternetQueryOption(hInternet, dwOption, lpBuffer, dwBufferLength)
    return iqp

def InternetOpenUrl(params):
    hInternet = params["hInternet"]
    lpszUrl = params["lpszUrl"]
    lpszHeaders = params["lpszHeaders"]
    dwHeadersLength = params["dwHeadersLength"]
    dwFlags = params["dwFlags"]
    dwContext = params["dwContext"]
    iou = win32inet.InternetOpenUrl(hInternet, lpszUrl, lpszHeaders, dwHeadersLength, dwFlags, dwContext)
    return iou

def InternetWriteFile(params):
    hfile = params["hfile"]
    lpBuffer = params["lpBuffer"]
    dwNumerberofBytesToWrite = params["dwNumerberofBytesToWrite"]
    lpdwBytesToWrite = params["lpdwBytesToWrite"]
    iw = win32api.WriteFile(hfile, lpBuffer, dwNumerberofBytesToWrite)
    return iw

def main():

    params = dict()
    params["lpszAgentName"] = 'My App'
    params["dwAccessType"] = win32inet.INTERNET_OPEN_TYPE_DIRECT
    params["lpszProxy"] = None
    params["lpszProxyBypass"] = None
    params["dwFlags"] = 0 
    hInternet = InternetOpen(params)
    if (hInternet == None):
        print ("Failed to open Internet")
    else:
        print ("Successfully opened Internet")

    params.clear()
    hInternet = win32inet.InternetOpen("MyApp" , win32inet.INTERNET_OPEN_TYPE_PRECONFIG, None, None, 0)
    params["hInternet"] = hInternet
    params["lpszUrl"] = 'http://www.google.com'
    params["lpszHeaders"] = None
    params["dwHeadersLength"] = 0
    params["dwFlags"] = 0
    params["dwContext"] = 0
    hUrl = InternetOpenUrl(params)
    if (hUrl == None):
        print ("Failed to open Internet URL")
    else:
        print (hUrl.message)
    params.clear()
    
    hInternet = win32inet.InternetOpen("MyApp", win32inet.INTERNET_OPEN_TYPE_DIRECT, None, None, 0)
    params["hFile"] = win32inet.InternetOpenUrl(hInternet, "http://www.example.com/", None, 0, 0, 0)
    params["lpBuffer"] = b"Hello World!"
    params["dwNumberOfBytesToRead"] = len(params["lpBuffer"])
    iw = InternetWriteFile(params)
    if (iw == None):
        print ("Failed to write to Internet file")
    else:
        print ("Successfully wrote to Internet file")

    params.clear()
    buff = str(1024)
    hInternet = win32inet.InternetOpen("MyApp", win32inet.INTERNET_OPEN_TYPE_DIRECT, None, None, 0)
    params["hFile"] = win32inet.InternetOpenUrl(hInternet, "http://www.example.com/", None, 0, 0, 0)
    params["lpBuffer"] = buff
    params["dwNumberOfBytesToRead"] = len(buff)
    params["lpdwNumberOfBytesToRead"] = len(buff)
    content = InternetReadFile(params)
    if (content == True):
        print ("Successfully read ")
    else:
        print ("Failed to read " + buff)
    
    params["hInternet"] = hInternet
    hclose = InternetCloseHandle(params)
    if (hclose == True):
        print ("Successfully closed Internet")
    else:
        print ("Failed to close!")

    params.clear()
    hInternet = win32inet.InternetOpen("MyApp" , win32inet.INTERNET_OPEN_TYPE_PRECONFIG, None, None, 0)
    params["lpszServername"] = "127.0.0.1"
    params["nServerPort"] = win32inet.INTERNET_DEFAULT_FTP_PORT
    params["lpszUserName"] = None
    params["lpszPassword"] = None
    params["dwService"] = win32inet.INTERNET_SERVICE_FTP
    params["dwFlags"] = 0
    params["dwContext"] = 0
    io = win32inet.InternetConnect(Params)
    if (io == None):
        print ("Failed to connect Internet")
    else:
        print ("Successfully connected Internet")
        
    params.clear()
    params["hWnd"] = None
    params["hRequest"] = None
    params["dwError"] = 0
    params["dwFlags"] = 0
    params["lppvData"] = None

    params.clear()
    params["hConnection"] = None
    params["lpszVerb"] = "GET"
    params["lpszObject"] = None
    
    

main()

        










