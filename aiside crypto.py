#python3.9.1 
#auther:aiside for HUC
#base64\base32\base16、rot13、Caesar cipher、Fence code
#version：1.2
def help():
    language_choose=input('中文(please input zn) or ENGLISH(please input en)\n')
    if language_choose=="zn":
        print("作者：Aiside\n输入您要破解的密文，程序将自动开始解码，目前支持base系列解密，偏移位密码解密，栅栏密码解密，维吉尼亚密码解密")
    elif language_choose=="en":
        print("Auther:aiside\nEnter the ciphertext you want to crack, the program will automatically start decoding, currently support base series decryption, offset decryption, fence decryption, Virginia decryption\n\n")
def Offset_encryption(cip):
    def crypto_main(cip,shift):
        crypto_rot13_lst=[] 
        cip=cip.replace(' ','')
        if len(cip)==0:
            print("error,can not decrypto!")
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
    def brute_force_crypto(cip):
        for shift in range (26):
            crypto_main(cip,shift)
        print ("successed")


    brute_force_crypto(cip)

def base_crypto(cip):
    import base64
    while len(cip)==0:
            cip=input('please input your ciphertext again\n')      

    judge_type=0
    for i in cip :
        cup=i.isalpha()
        cup_2=i.isdigit()
        if cup!=1 and cup_2!=1:
            judge_type=64
            break
        else :
            for m in cip :
                if ord(m) in range (97,123):
                    judge_type=64
                    break
                else:
                    continue
            continue
    if judge_type==0:
        for i in cip :
            if ord(i) in range(70,91):
                judge_type=32
                break
            else :
                continue
    if judge_type==0 :
        judge_type=16
    i=0
    try:
        while i!=1:
            if judge_type == 16:
                i=1
                crypto_16_continue=str(base64.b16decode(cip),"UTF-8")
                print("ctypto result:\n")
                print(crypto_16_continue)
            elif judge_type==32:
                i=1
                crypto_32_continue=str(base64.b32decode(cip),"UTF-8")
                print("ctypto result:\n")
                print(crypto_32_continue)
            elif judge_type==64:
                i=1
                crypto_64_continue=str(base64.b64decode(cip),"UTF-8")
                print("ctypto result:\n")
                print(crypto_64_continue)
            else:
                print("please,try input crypto type again! like \'16\' or \'32\' or \'64\'")
                judge_type=input()
    except Exception as e:
        print('ERROR:The data you entered is not of the selected encryption type\n',e)
            


def fence_code(cip):
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
        
    def decrypt_fence(encrypted_str,fence_length):
        encrypted_str = add_num(encrypted_str,fence_length)
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
    def main(cip):
            encrypted_str=cip
            fence_length=len(encrypted_str)+1
            for i in range (1,fence_length):
                decrypt_fence(encrypted_str,i)


    print("fence code was run!")
    main(cip)
    

def Bacon_cipher(cip):
    print("bacon cipher running")
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

def Vigenere_Cipher():
    cip=input('please input the crypto text\n')
    secret_key=input('please input the key\n')
    if secret_key.isupper()==1:
        next
    else:
        secret_key=secret_key.upper()
    if cip.isupper()==1:
        next
    else:
        cip=cip.upper()
    secret_key_list=list(secret_key)
    continue_text=[]
    for i in range(9999):
        for i in secret_key:
            if len(cip)>len(secret_key_list):
                secret_key_list.append(i)
            else:
                break
        if len(cip)>len(secret_key_list):
            next
        else :
            break

    #print (secret_key_list)     #key补全

    num_key=0
    for i in cip:
        cup_2=''.join(secret_key_list[num_key:(num_key+1)])
        cup=ord(cup_2)
        i=ord(i)-cup
        if i<0 :
            i=26+i
        num_judge=0
        crypto_continue=65
        while num_judge!=i:
            if crypto_continue==90:
                crypto_continue+=1
                num_judge=num_judge+1
            else:
                crypto_continue+=1
                num_judge+=1
        continue_text.append(chr(crypto_continue))
        num_key=num_key+1
    continue_text_join="".join(continue_text)
    print('decreypto succsses')
    print('decrypto result:\n')
    print(continue_text_join)


#def 

##########################################################################################功能调用模块
def main(command):
    if command==104:
        help()
    elif command==86 or command==118:
        Vigenere_Cipher(cip)
    elif command ==65 or command==97:
        cip=input('please input the cip\n请输入密文')
        print("\n")
        print("Offset_encryption will run \n\n\n")
        Offset_encryption(cip)
        print("\n")
        print("base_crypto will run \n\n\n")
        base_crypto(cip)
        print("\n")
        print("fence_code will run \n\n\n")
        fence_code(cip)
        print("\n")
        print("Bacon_cipher will run\n\n\n")
        Bacon_cipher(cip)
        

    



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
    print("if you want use Vigenere Cipher please input \'v\'\n or input \'a\' for brute force ")
    print("please choose the servise if you want,or input h and \"enter\" to get help \n")
    command=ord(input('please input your choose\n'))
    main(command)
############################################################################################
title_of()
menu_of()
    


        

        




        
