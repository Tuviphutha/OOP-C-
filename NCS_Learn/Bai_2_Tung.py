import sys
import json
import magic
import platform
import pefile
# ham check format file
def check_file_File_format(file_path):
    File_format= ""
    File_p1 = str(magic.Magic(mime=True, magic_file= None, uncompress=True).from_file(file_path))
    File_p2 = magic.from_file(file_path, mime=True)
    #print(File_p2)
# kiem tra File_format cua file
    if "text/plain" in File_p1:
        File_format = "txt"
    elif "application/pdf" in File_p1:
        File_format = "pdf"
    elif "application/aac, adt, adts" in File_p1:
        File_format = "audio"
    elif "application/accdb" in File_p1:
        File_format = "Microsoft Access database file"
    elif "application/accde" in File_p1:
        File_format = "Microsoft Access execute-only file"
    elif "application/accdr" in File_p1:
        File_format = "Microsoft Access runtime database"
    elif "application/aif, aifc, aiff" in File_p1:
        File_format = "Audio Interchange File format file"
    elif "application/aspx" in File_p1:
        File_format = "ASP.NET Active Server page"
    elif "application/avi" in File_p1:
        File_format = "Audio Video Interleave movie or sound file"
    elif "application/bat" in File_p1:
        File_format = "PC batch file"
    elif "application/bin" in File_p1:
        File_format = "Binary compressed file"
    elif "application/bmp" in File_p1:
        File_format = "Bitmap file"
    elif "application/x-dosexec" in File_p1:
        File_format = "exe"
    elif "application/cab" in File_p1:
        File_format = "Windows Cabinet file"
    elif "application/gif" in File_p1:
        File_format = "gif"
    elif "application/iso" in File_p1:
        File_format = "ISO-9660 disc image"
    elif "application/octet-stream" in File_p1:
        File_format = "bin"
    elif "application/x-dosexec" in File_p2:
        File_format = "exe"
        vt= File_p2.find("GUI")
        vt2= File_p2.find(",",vt+1)
        # print(vt,vt2)
        arch=File_p2[vt+5:vt2]
    else:
        vt = File_p1.find("\\")
        File_format = File_p1[vt+1:len(File_p1)]
    
    return File_format
# ham check arch cua file
def check_arch(file_path):
    file_File_format = magic.from_file(file_path, mime=True)
    if "application/x-dosexec" in file_File_format:
        pe = pefile.PE(file_path)
        if pe.NT_HEADERS.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_I386']:
            return 'x32'
        elif pe.NT_HEADERS.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64']:
            return'x64'
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_ALPHA']:
            return pe.ARCH_ARM_MODE_ALPHA
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_ALPHA64']:
            return pe.ARCH_ARM_MODE_ALPHA64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_ARM']:
            return'ARM'
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_ARM64']:
            return pe.ARCH_ARM_MODE_ARM64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_ARMNT']:
            return pe.ARCH_ARM_MODE_ARMNT
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AXP64']:
            return pe.ARCH_ARM_MODE_AXP64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_EBC']:
            return pe.ARCH_ARM_MODE_EBC
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_IA64']:
            return pe.ARCH_ARM_MODE_IA64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_LOONGARCH32']:
            return pe.ARCH_ARM_MODE_LOONGARCH32
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_LOONGARCH64']:
            return pe.ARCH_ARM_MODE_LOONGARCH64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_M32R']:
            return pe.ARCH_ARM_MODE_M32R
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_MIPS16']:
            return pe.ARCH_ARM_MODE_MIPS16
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_MIPSFPU']:
            return pe.ARCH_ARM_MODE_MIPSFPU
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_MIPSFPU16']:
            return pe.ARCH_ARM_MODE_MIPS16
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_POWERPCFP']:
            return pe.ARCH_ARM_MODE_POWERPCFP
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_POWERPC']:
            return pe.ARCH_ARM_MODE_POWERPC
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_THUMB']:
            return pe.ARCH_ARM_MODE_THUMB
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_R4000B']:
            return pe.ARCH_ARM_MODE_R4000B
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_RISCV32']:
            return pe.ARCH_ARM_MODE_RISCV32
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_RISCV64']:
            return pe.ARCH_ARM_MODE_RISCV64
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_RISCV128']:
            return pe.ARCH_ARM_MODE_RISCV128
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_SH3']:
            return pe.ARCH_ARM_MODE_SH3
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_SH3DSP']:
            return pe.ARCH_ARM_MODE_SH3DSP
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_SH4']:
            return pe.ARCH_ARM_MODE_SH4
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_SH5']:
            return pe.ARCH_ARM_MODE_SH5
        elif pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_WCEMIPSV2']:
            return pe.ARCH_ARM_MODE_WCEMIPSV2
        else:
            return"Machine not supported"
    else:
        return platform.machine()
    
# ham check os     
def check_os(file_path):
    try:
        file_File_format = magic.from_file(file_path, mime=True)
        if "application/x-dosexec" in file_File_format:
            if "x86-64" in file_File_format:
                return "linux"
            else:
                return "Window"
        elif "application/x-apple-diskimage" in file_File_format:
            return "macOS"
        elif "application/x-deb" in file_File_format:
            return "linux"
        elif "application/vnd.android.package-archive" in file_File_format:
            return "Android"
        else:
            return "Windows"
    except Exception as e:
        print("Error: ", e)
        return "unknown os"
    
# #<-------------------------------------------------------------------->  
  
if __name__ == "__main__":
    # kiem tra form khi goi chuong trinh (5 la danh sach tham so khi goi)
    if len(sys.argv) != 5:
        print("Usage: python bai_x_Ten.py -fi [file_input] -fo [file_output]")
        sys.exit(1)
    # Tham so duoc truyen vao (2, 4 la vi tri tham so)
    file_input = sys.argv[2]
    file_output = sys.argv[4]

    result = {}
    result["File_format"] = check_file_File_format(file_input)
    result["os"] = check_os(file_input)
    result["arch"] = check_arch(file_input)

    with open(file_output, "w") as outfile:
                json.dump(result, outfile)
    print("Done!")
