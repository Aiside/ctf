#python3.9.1 
#auther:aiside for HUC
#base64\base32\base16、rot13、Caesar cipher、Fence code
#version：1.0

def help():
    language_choose=input('中文(please input zn) or ENGLISH(please input en)\n')
    if language_choose=="zn":
        print("作者：Aiside\n请在菜单栏中选择您需要使用的模块的序列号，并根据程序提示输入，您将得到所需的一切\n\n第一项偏移加密，包含凯撒加密(偏移量为3)、rot13加密（偏移量为13），都属与偏移加密。\n\n第二项base16/32/64加密包含如你所见\n\n第三项FENCE code 是栅栏密码")
    elif language_choose=="en":
        print("Auther:aiside\nPlease select the serial number of the module you need to use in the menu bar, and input it according to the program prompt, you will get everything you want\n\nThe first offset encryption, including Caesar encryption and rot13 encryption, belongs to offset encryption\n\nThe second base16 / 32 / 64 encryption contains as you can see\n\n")
    else :
        print("ERROR input")
def Offset_encryption():
    def crypto_main(cip,shift):
        crypto_rot13_lst=[] 
        cip=cip.replace(' ','')
        if len(cip)==0:
            print("your input have some error please check")
        else:
            shift=int(shift)
            crypto_rot13_lst=[]
            for n in cip:
                ord_n=ord(n)
                judge_isalpha=n.isalpha()
                if judge_isalpha==1:
                    ord_n=ord(n)
                    ord_n=ord_n-shift
                    if ord_n in range (65,91) :
                        crypto_rot13_lst.append(chr(ord_n))
                        continue
                    elif ord_n in range (97,122):
                        crypto_rot13_lst.append(chr(ord_n))
                    else :
                        if ord_n>90 and ord_n<97:
                            ord_n=64+(ord_n-90)
                            crypto_rot13_lst.append(chr(ord_n))
                        elif ord_n>122:
                            ord_n=96+(ord_n-122)
                            crypto_rot13_lst.append(chr(ord_n))
                else:
                    crypto_rot13_lst.append(n)
        crypto_rot13_lst_join=("".join(crypto_rot13_lst))
        print ("the crypto bits ",shift,"\nThe decryption result is:")
        print (crypto_rot13_lst_join,'\n')
    def nomal_crypto(cip):
        shift=input('please enter the encryption bits\n')
        crypto_main(cip,shift)
        print("successed")
    def brute_force_crypto(cip):
        for shift in range (26):
            crypto_main(cip,shift)
        print ("successed")

    print('hello,this is rot13 crypto/encryption\n')
    choose=input('if you want brote force please input \'b\' , if you just want nomal crypto please input \'n\' ')
    cip=input('please,input your ciphertext')
    if choose=='b':
        brute_force_crypto(cip)
    if choose=='n':
        nomal_crypto(cip)

def base_crypto():#无爆破模块

    import base64
    i=0
    print ("Hello,this is base64/32/16 crypto\n")
    cip=input('please input your ciphertext\n')
    if cip%4!=0:
        print ("this ciphertext maybe not be base64 encrypto")
    else:
        while len(cip)==0:
                cip=input('please input your ciphertext again\n')
        type_num=input('please choose you want to do , like \'16\' or \'32\' or \'64\'\n')                
        try:
            while i!=1:
                if type_num == "16":
                    i=1
                    crypto_16_continue=str(base64.b16decode(cip),"UTF-8")
                    print("ctypto result:\n")
                    print(crypto_16_continue)
                elif type_num=="32":
                    i=1
                    crypto_32_continue=str(base64.b32decode(cip),"UTF-8")
                    print("ctypto result:\n")
                    print(crypto_32_continue)
                elif type_num=="64":
                    i=1
                    crypto_64_continue=str(base64.b64decode(cip),"UTF-8")
                    print("ctypto result:\n")
                    print(crypto_64_continue)
                else:
                    print("please,try input crypto type again! like \'16\' or \'32\' or \'64\'")
                    type_num=input()
        except Exception as e:
            print('ERROR:The data you entered is not of the selected encryption type\n',e)

def fence_code():
    import math
    def add_num(encrypted_str,fence_length):    
        str_len = len(encrypted_str)
        fence_count = math.ceil(str_len/ fence_length)  
        target_length = fence_count*fence_length
        jiequ = []
        while str_len<target_length:
            encrypted_str = encrypted_str + '*'
            jiequ.append(encrypted_str[-fence_count :])
            encrypted_str = encrypted_str[:-fence_count]
            str_len += 1
        jiequ.reverse()
        s = ''
        for i in jiequ:
            s = s + i
        result = encrypted_str + s
        return result
        
    def decrypt_fence(encrypted_str,fence_length,choose):
        encrypted_str = add_num(encrypted_str,fence_length)
        if fence_length>=len(encrypted_str) or fence_length<1:
            if choose=="1":
                print("The fence is too long or too small to decrypt")
                return
            if choose=="2":
                print("crypto finish")
                return
        fence_count = math.ceil(len(encrypted_str)/fence_length)
        elen=len(encrypted_str)
        result = {x: '' for x in range(fence_count)}
        for i in range(elen):  
            a = i % fence_count
            result.update({a: result[a] + encrypted_str[i]}) 
        d = ''
        for i in range(len(result)):
            d += result[i]
        d = d.replace("*", '')
        print(f'your :{fence_length}，result：{d}')  
    def main(choose):
        if choose =='1'or choose == '2':
            if choose =='1':
                encrypted_str=input ('please,input your encryhtertext\n')
                fence_length=input('please,input the crypto bits\n')
                decrypt_fence(encrypted_str,fence_length,choose)
            elif choose == '2':
                encrypted_str=input('please input your encryhertext\n')
                fence_length=len(encrypted_str)+1
                for i in range (1,fence_length):
                    decrypt_fence(encrypted_str,i,choose)
        else :
            print("EEROR:please try again")

    print("please,choose what you want\n")
    print("1、you know this message Encryption process（General decryption） or 2、you don't know (brute force)\n")
    choose=int(input('please , input the number in menu\n'))
    main(choose)
    

def Bacon_cipher():
    print("Hello,this is Bacon cipher")
    cip=input('please input your ciphertext')
    lst_crypto_a=['AAAAA', 'AAAAB', 'AAABA', 'AAABB', 'AABAA', 'AABAB', 'AABBA', 'AABBB', 'ABAAA', 'ABAAB', 'ABABA', 'ABABB', 'ABBAA', 'ABBAB', 'ABBBA', 'ABBBB', 'BAAAA', 'BAAAB', 'BAABA', 'BAABB', 'BABAA', 'BABAB', 'BABBA', 'BABBB', 'BBAAA', 'BBAAB']
    lst_crypto_A=[ "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA","AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA","ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA","BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB"]
    lst_crypto_1=['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    lst_crypto_2=['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    dict_crypto_Plaintext_1=dict(zip(lst_crypto_A,lst_crypto_2))
    dict_crypto_Plaintext_2=dict(zip(lst_crypto_a,lst_crypto_1))
    crypto_handle=[]
    crypto_continue=[]    
    all_num=0
    all_alpha=len(cip)/5
    if (int(len(cip))%5!=0) and (cip.isalpha())==1:
        print("ERROR : This TEXT maybe is not isn't encrypted like this")
    for i in range (0,len(cip),5):
        crypto_handle.append(cip[i:i+5])
    try:
        for i in crypto_handle:
            cup=dict_crypto_Plaintext_2[i]
            crypto_continue.append(cup)
            all_num=all_num+1
            if all_num==all_alpha:
                print("successed")
                crypto_continue_join=''.join(crypto_continue)
                print("result:",crypto_continue_join)
            else:
                print("try to another bacon crypto")
    except :
            crypto_continue=[]
            for i in crypto_handle:
                if i in lst_crypto_A:
                    cup=dict_crypto_Plaintext_1[i]
                    crypto_continue.append(cup)
                    all_num=all_num+1
                    if all_num==all_alpha:
                        print("successed")
                        crypto_continue_join=''.join(crypto_continue)
                        print("result:",crypto_continue_join)
                else :
                    print("ERROR : This TEXT maybe is not isn't encrypted like this")

#def Vigenere_Cipher():
 #   all_alpha=[]
  #  for i in range (65,91):
   #     all_alpha.append(chr(i))
    #print(all_alpha)

##########################################################################################功能调用模块
def main(command):
    if command==49:
        Offset_encryption()
    elif command==50:
        base_crypto()
    elif command==51:
        fence_code()
    elif command==52: 
        Bacon_cipher()
#    elif comande==53:
 #       offset_encryption()
  #      base_crypto()
   #     fence_code()
    #    Bacon_cipher
    elif command==104:
        help()
    else:
        print("ERROR input")


##########################################################################################美化模块
def title_of():
    print("version 1.0\n\n")
    print("ccccccccccccc                tttttttttttttttt                 ffffffffffffff")
    print("cc                                 tt                         ff            ")
    print("cc                                 tt                         ff            ")
    print("cc                                 tt                         ffffffffffffff")
    print("cc                                 tt                         ff            ")
    print("cc                                 tt                         ff            ")
    print("cc                                 tt                         ff            ")
    print("ccccccccccccc                      tt                         ff          \n")

def menu_of():
    print("menu")
    print("*************************************************************************************************************\n")
    print("1、Offset encryption            2、base16/32/64           3、Fence code         4、Bacon cipher      \n")
    print("*************************************************************************************************************\n")
    print("please choose the servise if you want,or input h and \"enter\" to get help \n")
    command=ord(input('please input your choose\n'))
    main(command)
############################################################################################
title_of()
menu_of()
    


        

        




        
