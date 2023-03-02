import ctypes

# Định nghĩa các hằng số
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
MEM_RELEASE = 0x8000
PAGE_READWRITE = 0x04
LPVOID = ctypes.c_void_p
SIZE_T = ctypes.c_size_t
HANDLE = ctypes.c_void_p
DWORD = ctypes.c_uint32
LPCTSTR = ctypes.c_wchar_p

# memset - Thiết lập tất cả các byte của một vùng nhớ liên tiếp thành một giá trị được chỉ định.

def hook_memset(params):
    dest = params["dest"]
    value = params["value"]
    count = params["count"]
    ctypes.memset(dest, value, count)

# memcpy - Sao chép nội dung của một vùng nhớ liên tiếp đến vùng nhớ khác.

def hook_memcpy(params):
    dest = params["dest"]
    src = params["src"]
    count = params["count"]
    ctypes.memmove(dest, src, count)

# memcmp - So sánh hai vùng nhớ liên tiếp để xác định liệu chúng có bằng nhau không.

def hook_memcmp(params):
    buf1 = params["buf1"]
    buf2 = params["buf2"]
    count = params["count"]
    return ctypes.memcmp(buf1, buf2, count)

# memmove - Sao chép nội dung của một vùng nhớ liên tiếp đến vùng nhớ khác, có thể xử lý các trường hợp trùng nhau.

def hook_memmove(params):
    dest = params["dest"]
    src = params["src"]
    count = params["count"]
    ctypes.memmove(dest, src, count)

# memchr - Tìm kiếm trong vùng nhớ liên tiếp xem giá trị đã cho có xuất hiện trong nó không.

def hook_memchr(params):
    buf = params["buf"]
    value = params["value"]
    count = params["count"]
    ctypes.memchr(buf, value, count)

# VirtualAlloc - Cấp phát một vùng nhớ ảo.

def hook_VirtualAlloc(params):
    lpAddress = params["lpAddress"]
    dwSize = params["dwSize"]
    flAllocationType = params["flAllocationType"]
    flProtect = params["flProtect"]
    return ctypes.windll.kernel32.VirtualAlloc(lpAddress, dwSize, flAllocationType, flProtect)

# HeapAlloc - Cấp phát một vùng nhớ từ Heap.

def hook_HeapAlloc(params):
    hHeap = params["hHeap"]
    dwFlags = params["dwFlags"]
    dwBytes = params["dwBytes"]
    return ctypes.windll.kernel32.HeapAlloc(hHeap, dwFlags, dwBytes)

# malloc - Cấp phát một vùng nhớ từ Heap của hệ thống.
def malloc(size):
    return ctypes.windll.msvcrt.malloc(size)

def hook_malloc(params):
    size = params["size"]
    return ctypes.windll.msvcrt.malloc(size)

# LocalAlloc - Cấp phát một vùng nhớ từ Local Heap.

def hook_LocalAlloc(params):
    uFlags = params["uFlags"]
    uBytes = params["uBytes"]
    return ctypes.windll.kernel32.LocalAlloc(uFlags, uBytes)

# GlobalAlloc - Cấp phát một vùng nhớ từ Global Heap.

def hook_GlobalAlloc(params):
    uFlags = params["uFlags"]
    uBytes = params["uBytes"]
    return ctypes.windll.kernel32.GlobalAlloc(uFlags, uBytes)

# VirtualAllocEx - Cấp phát một vùng nhớ ảo từ một quá trình khác.
def VirtualAllocEx(hProcess, lpAddress, dwSize, flAllocationType, flProtect):
    return ctypes.windll.kernel32.VirtualAllocEx(hProcess, lpAddress, dwSize, flAllocationType, flProtect)

def hook_VirtualAlloc(params):
    hProcess = params["hProcess"]
    lpAddress = params["lpAddress"]
    dwSize = params["dwSize"]
    flAllocationType = params["flAllocationType"]
    flProtect = params["flProtect"]
    return ctypes.windll.kernel32.VirtualAllocEx(hProcess, lpAddress, dwSize, flAllocationType, flProtect)

def main():
    params = dict()
    params["dest"] = bytearray(10)
    params["value"] = 0xFF
    params["count"] = 5
    hook_memset(params)

    params.clear()
    params["dest"] = bytearray(1024)
    params["src"] = bytearray(b'\x01\x02\x03\x04\x05\x06')
    params["count"] = len(src)
    hook_memcpy (params)
    if (dest == src):
        print("Succces!")
    else:
        print("Fail!")

    params.clear()
    params["buf1"] = bytearray(b'\x01\x02\x03\x04\x05')
    params["buf2"] = bytearray(b'\x01\x02\x03\x04\x06')
    params["count"] = 3
    check = hook_memcmp (params)
    if (check == 0):
        print("Same!")
    else:
        print("Different!")    

    params.clear()
    params["dest"] = bytearray(b'\x01\x02\x03\x04\x05')
    params["src"] = bytearray(b'\x01\x02\x03\x04\x05')
    params["count"] = len(dest)
    buff = hook_memmove (params) 
    if(buff == bytearray(b'\x02\x03\x04\x05\x05')):
        print("Succces!")
    else:
        print("Fail!")

    params.clear()
    params["buf"] = bytearray(b'\x01\x02\x03\x04\x05')
    params["value"] = 0x03
    params["count"] = len(buf)
    str1 = hook_memchr (params)
    if (str1 == buf[2:3]):
        print("Yes!")
    else: 
        print("No!")

    params.clear()
    params["lpAddress"] = 0
    params["dwSize"] = 1024
    params["flAllocationType"] = MEM_COMMIT
    params["flProtect"] = PAGE_READWRITE
    result = hook_VirtualAlloc(params)
    if (result != 0):
        print("Succces!")
    else:
        print("Succes!")

    params.clear()
    params["hHeap"] = ctypes.windll.kernel32.GetProcessHeap()
    params["dwFlags"] = 0
    params["dwSize"] = 1024
    result = hook_HeapAlloc(params)
    if (result != 0):
        print("Succces!")
    else:
        print("Succes!")

    params.clear()
    params["size"] = 1024
    result = hook_malloc(params)
    if (result == None):
        print("Succces!")
    else:
        print("Succes!")

    params.clear()
    params["uFlags"] = MEM_COMMIT
    params["uBytes"] = 1024
    result = hook_LocalAlloc(params)
    if (result == None):
        print("Succces!")
    else:
        print("Succes!")

    params.clear()
    params["uFlags"] = MEM_COMMIT
    params["uBytes"] = 1024
    result = hook_GlobalAlloc(params)
    if (result == None):
        print("Succces!")
    else:
        print("Succes!")

    params.clear()
    params["hProcess"] = ctypes.windll.kernel32.GetCurrentProcess()
    params["lpAddress"] = 0
    params["dwSize"] = 1024
    params["flAllocationType"] = MEM_COMMIT
    params["flProtect"] = PAGE_READWRITE
    result = hook_VirtualAllocEx(params)
    if (result != 0):
        print("Succces!")
    else:
        print("Succes!")

main()


    

