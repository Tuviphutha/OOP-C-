import struct
# import bitstring

# Mở tệp NTUSER.DAT và đọc 4096 byte đầu tiên để lấy registry header/base block
with open("C:\\Users\\tungt\\Downloads\\NTUSER.DAT", "rb") as f:
    data = f.read(10000000000)
    # print(data)
#<-----------------------RegCreateKeyEx----------------------->
    # f.seek(0x3000)

    # # Dữ liệu khóa mới, ví dụ:
    # new_key = b'my_new_key'

    # # Ghi dữ liệu khóa vào tệp
    # f.write(new_key)

    # # Tính toán và cập nhật kích thước tệp
    # file_size = f.tell()
    # f.seek(0x4)
    # f.write(struct.pack('<I', file_size))

    # f.seek(0x4000)

    # # Dữ liệu khóa mới, ví dụ:
    # new_key = b'Manchester United'

    # # Ghi dữ liệu khóa vào tệp
    # f.write(new_key)

    # # Tính toán và cập nhật kích thước tệp
    # file_size = f.tell()
    # f.seek(0x4)
    # f.write(struct.pack('<I', file_size))
#<-----------------------RegOpenKeyEx----------------------->

#<-----------------------RegDeleteKey----------------------->

# Đọc signature và version của registry header
signature = data[0:4]
Primary_sequence_number = data[4:8]
Secondary_sequence_number = data[8:12]
Last_written_time = data[12:20]
major_version = data[20:24]
minor_version = data[24:28]
file_type = data[28:32]
file_format = data[32:36]
root_cell_offset = data[36:40]
hive_bins_offset = data[40:44]
clutering_factor = data[44:48]
file_name = data[48:112]
# Reserved = data[112:508]
checksum = data[508:512]

# Đọc offset và size của registry hive bins
Primary_sequence_number = struct.unpack("<I", data[4:8])[0]
Secondary_sequence_number = struct.unpack("<I", data[8:12])[0]
Last_written_time = struct.unpack("<Q", data[12:20])[0]
major_version = struct.unpack("<I", data[20:24])[0]
minor_version = struct.unpack("<I", data[24:28])[0]
file_type = struct.unpack("<I", data[28:32])[0]
file_format = struct.unpack("<I", data[32:36])[0]
root_cell_offset = struct.unpack("<I", data[36:40])[0]
hive_bins_offset = struct.unpack("<I", data[40:44])[0]
clutering_factor = struct.unpack("<I", data[44:48])[0]


# In ra các thông tin đã đọc được
print("Base block!")
print("----------------------------------------------------")
print("Signature: {}".format(signature.decode("utf-8")))
print("Primary_sequence_number: {}".format(Primary_sequence_number))
print("Secondary_sequence_number: {}".format(Secondary_sequence_number))
print("Last_written_time: {}".format(Last_written_time))
print("major_version: {}".format(major_version))
print("minor_version: {}".format(minor_version))
print("file_type: {}".format(file_type))
print("file_format: {}".format(file_format))
print("root_cell_offset: {}".format(root_cell_offset))
print("hive_bins_offset: {}".format(hive_bins_offset))
print("clutering_factor: {}".format(clutering_factor))
print("file_name: {}".format(file_name))
print("checksum: {}".format(checksum))

x = int(0)
k = int(4096)

# hive_bin_sigature = data[k:4100]
# hive_bins_offset = data[4100:4104]
# hive_bin_size = data[4104:4108]
# hive_bin_reserved = data[4108:4120]
# hive_bin_timestamp = data[4120:4128]
# hive_bin_size = struct.unpack("<I", data[4104:4108])[0]
# ive_bins_offset = struct.unpack("<I", data[4100:4104])[0]
# hive_bin_reserved = struct.unpack("<QI", data[4108:4120])[0]
# hive_bin_timestamp = struct.unpack("<Q", data[4120:4128])[0]
# print("hive_bin_signature: {}".format(hive_bin_sigature))
# print("hive_bins_offset: {}".format(hive_bins_offset))
# print("hive_bin_size: {}".format(hive_bin_size))
# print("ive_bin_reserved: {}".format(hive_bin_reserved))
# print("hive_bin_timestamp: {}".format(hive_bin_timestamp))

# test1 = data[327680:327684]
# print("test: {}".format(test1))

while (data[k:(k+4)] != b'\x00\x00\x00\x00'):

    x += 1
    k = 4096*x
    # print("k: ", k)
    hive_bin_sigature = data[k:(k+4)]
    hive_bins_offset = data[(k+4):(k+8)]
    hive_bin_size = data[(k+8):(k+12)]
    hive_bin_reserved = data[(k+12):(k+24)]
    hive_bin_timestamp = data[(k+24):(k+32)]
    hive_bin_size = struct.unpack("<I", data[(k+8):(k+12)])[0]
    ive_bins_offset = struct.unpack("<I", data[(k+4):(k+8)])[0]
    hive_bin_reserved = struct.unpack("<QI", data[(k+12):(k+24)])[0]
    hive_bin_timestamp = struct.unpack("<Q", data[(k+24):(k+32)])[0]
    print("hive_bin_signature: {}".format(hive_bin_sigature))
    print("hive_bins_offset: {}".format(hive_bins_offset))
    print("hive_bin_size: {}".format(hive_bin_size))
    print("hive_bin_reserved: {}".format(hive_bin_reserved))
    print("hive_bin_timestamp: {}".format(hive_bin_timestamp))
    
    x1 = 1
    cell_signature = data[k+24:k+26]
    cell_flag = data[k+26:k+28]
    cell_last_written_time = data[k+28:k+36]
    cell_access_bits = data[k+44:k+48]
    cell_parent = data[k+48:k+52]
    cell_Numberofsubkeys = data[k+52:k+56]
    cell_Numberofvolatilesubkeys = data[k+56:k+60]
    cell_subkeyslistoffset = data[k+60:k+64]
    cell_numberofkeyvalues = data[k+64:k+68]
    cell_keyvaluelistoffset = data[k+68:k+72]
    cell_keysecurityoffset = data[k+72:k+76]
    cell_classnameoffset = data[k+76:k+80]
    cell_largestsubkeynamelength = data[k+80:k+84]
    cell_largestsubkeyclassnamelength = data[k+84:k+88]   
    cell_largestsubkeyvaluenamelength = data[k+88:k+92]
    cell_largestvaluedatasize = data[k+92:k+96]
    cell_workvar = data[k+96:k+100]
    cell_keynamelength = data[k+100:k+104]
    cell_classnamelength = data[k+104:k+106]
    cell_keynamestring = data[k+106:k+108]

    cell_signature = struct.unpack("<H", data[k+24:k+26])[0]
    cell_flag = struct.unpack("<H", data[k+26:k+28])[0]
    cell_last_written_time = struct.unpack("<Q", data[k+28:k+36])[0]
    cell_access_bits = struct.unpack("<I", data[k+44:k+48])[0]
    cell_parent = struct.unpack("<I", data[k+48:k+52])[0]
    cell_Numberofsubkeys = struct.unpack("<I", data[k+52:k+56])[0]
    cell_Numberofvolatilesubkeys = struct.unpack("<I", data[k+56:k+60])[0]
    cell_subkeyslistoffset = struct.unpack("<I", data[k+60:k+64])[0]
    cell_numberofkeyvalues = struct.unpack("<I", data[k+64:k+68])[0]
    cell_keyvaluelistoffset = struct.unpack("<I", data[k+68:k+72])[0]
    cell_keysecurityoffset = struct.unpack("<I", data[k+72:k+76])[0]
    cell_classnameoffset = struct.unpack("<I", data[k+76:k+80])[0]
    cell_largestsubkeynamelength = struct.unpack("<I", data[k+80:k+84])[0]
    cell_largestsubkeyclassnamelength = struct.unpack("<I", data[k+84:k+88])[0] 
    cell_largestsubkeyvaluenamelength = struct.unpack("<I", data[k+88:k+92])[0]
    cell_largestvaluedatasize = struct.unpack("<I", data[k+92:k+96])[0]
    cell_workvar = struct.unpack("<I", data[k+96:k+100])[0]
    cell_keynamelength = struct.unpack("<I", data[k+100:k+104])[0]
    cell_classnamelength = struct.unpack("<H", data[k+104:k+106])[0]
    cell_keynamestring = struct.unpack("<H", data[k+106:k+108])[0]

    print("cell_signature: {}".format(cell_signature))
    print("cell_flag: {}".format(cell_flag))
    print("cell_last_written_time: {}".format(cell_last_written_time))
    print("cell_access_bits: {}".format(cell_access_bits))
    print("cell_Numberofsubkeys: {}".format(cell_Numberofsubkeys))
    print("cell_subkeyslistoffset: {}".format(cell_subkeyslistoffset))
    print("cell_numberofkeyvalues: {}".format(cell_numberofkeyvalues))
    print("cell_keyvaluelistoffset: {}".format(cell_keyvaluelistoffset))
    print("cell_keysecurityoffset: {}".format(cell_keysecurityoffset))
    print("cell_classnameoffset: {}".format(cell_classnameoffset))
    print("cell_largestsubkeynamelength: {}".format(cell_largestsubkeynamelength))
    print("cell_largestsubkeyclassnamelength: {}".format(cell_largestsubkeyclassnamelength))
    print("cell_largestsubkeyvaluenamelength: {}".format(cell_largestsubkeyvaluenamelength))
    print("cell_largestvaluedatasize: {}".format(cell_largestvaluedatasize))
    print("cell_workvar: {}".format(cell_workvar))
    print("cell_keynamelength: {}".format(cell_keynamelength))
    print("cell_classnamelength: {}".format(cell_classnamelength))
    print("cell_keynamestring: {}".format(cell_keynamestring))


# #Test ghi file
    hex_str = "A0FFFFFF6E6B2000627676C58DBDD80100000000280900000000000000000000FFFFFFFFFFFFFFFF02000000680A0000C8020000FFFFFFFF00000000000000000C0000001A000000000000000A0000005573657243686F696365000000000000F0FFFFFF6C6601008009000055736572E0FFFFFF766B060014000000100A0000010000000100000050726F6749440000E8FFFFFF42007200610076006500480054004D004C000000E0FFFFFF766B04001A000000480A000001000000010004004861736801000000E0FFFFFF680039003100440043005400560037006500420077003D0000006E00F0FFFFFFF0090000280A000000000000A0FFFFFF6E6B2000E6B3855754DED40100000000F00100000000000000000000FFFFFFFFFFFFFFFF00000000FFFFFFFF78000000FFFFFFFF00000000000000000000000000000000000000000A000000696E7369646572687562000000000000A8FFFFFF6E6B200084ABB1AD53DED40100000000F00100000100000000000000C00B0000FFFFFFFF00000000FFFFFFFF78000000FFFFFFFF1400000000000000000000000000000000000000060000006D61696C746F0000"
    hex_bytes = binascii.unhexlify(hex_str)

with open("C:\\Users\\tungt\\Pictures\\NTUSER.DAT", 'rb+') as f:
    f.seek(0xA9E10)
    f.write(hex_bytes)

# tìm key theo tên trong Registry

from regipy import RegistryHive

# Load the hive
hive = RegistryHive(r"C:\\Users\\tungt\\Downloads\\NTUSER.DAT")

# Get the key you want to retrieve subkeys from
print("Nhap ten key: ")
key_path= str(input())
parent_key = hive.get_key(key_path)

    # Get all subkeys of the key
subkeys = hive.recurse_subkeys()
# print(dir(subkeys))

# subkeys2 = parent_key.sub_keys
i = 1
for subkey in subkeys:
    # if i==1:
    #     print(subkey.subkey_name)
    # i+=1
    if (subkey.subkey_name == key_path):
        print(subkey)
        break













