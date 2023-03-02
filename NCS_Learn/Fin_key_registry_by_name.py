import binascii
from regipy import RegistryHive
from regipy.plugins.plugin import Plugin
from regipy.exceptions import RegistryKeyNotFoundException
from regipy.registry import Subkey
import yarp.Registry
with open(r'C:\\Users\\tungt\\Downloads\\NTUSER.DAT', 'rb+' ) as fp:
        hive = yarp.Registry.RegistryHive(fp)
 
        print(hive.registry_file.baseblock.get_hbins_data_size())
        print(hive.root_key())
# Mở tệp ntuser.dat ở chế độ ghi
# with open('C:\\Users\\tungt\\Pictures\\NTUSER.DAT', 'r+b') as f:
# Đi đến offset để ghi khóa mới vào
#     f.seek(0x5E0)

# hex_str = "A0FFFFFF6E6B2000627676C58DBDD80100000000280900000000000000000000FFFFFFFFFFFFFFFF02000000680A0000C8020000FFFFFFFF00000000000000000C0000001A000000000000000A0000005573657243686F696365000000000000F0FFFFFF6C6601008009000055736572E0FFFFFF766B060014000000100A0000010000000100000050726F6749440000E8FFFFFF42007200610076006500480054004D004C000000E0FFFFFF766B04001A000000480A000001000000010004004861736801000000E0FFFFFF680039003100440043005400560037006500420077003D0000006E00F0FFFFFFF0090000280A000000000000A0FFFFFF6E6B2000E6B3855754DED40100000000F00100000000000000000000FFFFFFFFFFFFFFFF00000000FFFFFFFF78000000FFFFFFFF00000000000000000000000000000000000000000A000000696E7369646572687562000000000000A8FFFFFF6E6B200084ABB1AD53DED40100000000F00100000100000000000000C00B0000FFFFFFFF00000000FFFFFFFF78000000FFFFFFFF1400000000000000000000000000000000000000060000006D61696C746F0000"
# hex_bytes = binascii.unhexlify(hex_str)

# with open("C:\\Users\\tungt\\Downloads\\NTUSER.DAT", 'rb+') as f:
#     f.seek(0xA9D10)
    
#     f.write(hex_bytes)


#Add the key to the hive
hive = RegistryHive(r"C:\\Users\\tungt\\Downloads\\NTUSER.DAT")

# Get the key you want to retrieve subkeys from
print("Nhap ten key: ")
key_path= str(input())
print(hive.header
)
parent_key = hive.get_key(key_path)
# print(parent_key.get_security_key_info())


# Get all subkeys of the key
subkeys = hive.recurse_subkeys()
# print(subkeys)

# subkeys2 = parent_key.sub_keys
i = 1
for subkey in subkeys:
#     if i==1:
#     print(subkey)
#     i+=1
    if (subkey.subkey_name == key_path):
        print("key_name:", subkey.subkey_name)
        print("key_path:", subkey.path)
        print("key_timstamp:", subkey.timestamp)
        print("key_values_count:", subkey.values_count)
        print("key_values:", subkey.values)
        print("key_actual_path:", subkey.actual_path)
        break


# # def convert_wintime(wintime: int, as_json=False) -> Union[dt.datetime, str]:
# #     """
# #     Get an integer containing a FILETIME date
# #     :param wintime: integer representing a FILETIME timestamp
# #     :param as_json: whether to return the date as string or not
# #     :return: datetime
# #     """
# #     # http://stackoverflow.com/questions/4869769/convert-64-bit-windows-date-time-in-python
# #     us = wintime / 10
# #     try:
# #         date = dt.datetime(1601, 1, 1, tzinfo=pytz.utc) + \
# #             dt.timedelta(microseconds=us)
# #     except OverflowError:
# #         # If date is too big, it is probably corrupted' let's return the smallest possible windows timestamp.
# #         date = dt.datetime(1601, 1, 1, tzinfo=pytz.utc)
# #     return date.isoformat() if as_json else date