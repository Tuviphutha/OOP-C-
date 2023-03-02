def func_1_congchuoi (dict_func):
    return dict_func["string1"] + dict_func["string2"] 

def func_2_saochepchuoi (dict_func):
    str3 = str(dict_func["string1"])
    return str3

def func_3_tinhdodaichuoi (dict_func):
    print("Do dai cua str1 la: ", len(dict_func["string1"]))
    print("Do dai cua str2 la: ", len(dict_func["string2"]))

def func_4_sosanhchuoi (dict_func):
    if (dict_func["string1"] == dict_func["string2"]):
        print("hai chuoi giong nhau")
    else: 
        print("hai chuoi khac nhau")

def func_5_sosanh1phanchuoi (dict_func):
    print ("Nhap so n:")
    n = int(input())
    str3 = dict_func["string1"][0:n]
    str4 = dict_func["string2"][0:n]
    if (str3 == str4):
        print("n phan tu dau cua hai chuoi giong nhau")
    else: 
        print("n phan tu dau cua hai chuoi khac nhau")
        
       
def func_6_timvitrixuathienchuoi1 (dict_func):
   print ('Nhap tu can tim:', end =' ')
   tu = input()
   if (dict_func["string1"].find(tu) != -1):
       print('Vi tri xuat hien trong str1 la: ', end = '')
       print (dict_func["string1"].find(tu))
       
def func_7_timvitrixuathienchuoi2 (dict_func):
   print ('Nhap tu can tim:', end =' ')
   tu = input()
   if (dict_func["string2"].find(tu)):
       print('Vi tri xuat hien trong str2 la: ', end = '')
       print (dict_func["string2"].find(tu))
     

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-str1',help="Nhap chuoi thu nhat", required=True) 
    #help: phần thông tin mô tả , required: các tham số phải được truyển theo đúng thứ tự 
    parser.add_argument('-str2',help="Nhap chuoi thu hai",required=True)
    parser.add_argument('-func',metavar="{1 2 3 4 5 6 7}", help="Ten cua cac funcion", required=True)
    try:
        args=parser.parse_args()
    except :
        print("Vui lòng nhật đúng form!")
        parser.print_help() 
        #in ra output theo chuan mac dinh 
        exit()
        
    dict_func = dict(func=args.func, string1=args.str1, string2=args.str2)
    
    if (dict_func["func"] == '1') :
        print(func_1_congchuoi(dict_func))
    
    if (dict_func["func"] == '2') :
        print(func_2_saochepchuoi(dict_func))
        
    if (dict_func["func"] == '3') :
        func_3_tinhdodaichuoi(dict_func)
    
    if (dict_func["func"] == '4') :
        func_4_sosanhchuoi(dict_func)
    
    if (dict_func["func"] == '5') :
        func_5_sosanh1phanchuoi(dict_func)
        
    if (dict_func["func"] == '6') :
        func_6_timvitrixuathienchuoi1(dict_func)
        
    if (dict_func["func"] == '7') :
        func_7_timvitrixuathienchuoi2(dict_func)
if __name__ == "__main__":
        main()