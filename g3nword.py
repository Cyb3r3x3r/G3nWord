
import os, random
import sys
from math import log

#Developed by cyb3r3xr..........Free to develop this code
#but don't copy.....cause it makes you LOL xd

try:
    from colorama import Fore, Back, Style
    g = Fore.GREEN
    r = Fore.RED
    m = Fore.MAGENTA
    y = Fore.YELLOW
except ImportError:
    print('[-] Cannot find module colorama')
    print(' [*] Install by pip install colorama')
    sys.exit()

class G3nWord():
    def __init__(self):
        try:
            choice2 = sys.argv[1]
            if choice2 == '-n':
                self.logo()
                choice1 = input(y + '   [!]Do you want to use spcl characters[y/N] : ')
                print(g + '---------------------------------------------------')
                for x in range(0,10):
                    print('')
                    print(g + ' [+]GENERATED :           ',self.num_gen(choice1))
                print(g + '---------------------------------------------------')
            elif choice2 == '-l':
                self.logo()
                print(y + '  [!]Do you want to include your own string[y/N]')
                choice1 = input('> ')
                if choice1 == 'y' or choice1 == 'Y':
                    name = input(y + '  [!] Enter a name >')
                    str1 = input(y + '  [!] Enter any other string u want >')
                    print(g + '---------------------------------------------------')
                    for x in range(0,10):
                        print('')
                        print(g + ' [+]GENERATED :           ',self.word_str(name,str1))
                    print(g + '---------------------------------------------------')
                else:
                    print(g + '---------------------------------------------------')
                    for x in range(0,10):
                        print('')
                        print(g + ' [+]GENERATED :           ',self.word_gen())
                    print(g + '---------------------------------------------------')
            elif choice2 == '-m':
                self.logo()
                name = input(y + '  [!] Enter a name >')
                str1 = input(y + '  [!] Enter any other string u want >')
                print(g + '---------------------------------------------------')
                for x in range(0,10):
                    print('')
                    print(g + ' [+]GENERATED :           ',self.mix_gen(name,str1))
                print(g + '---------------------------------------------------')
            else:
                sys.logo()
                sys.help()
                sys.exit()
        except IndexError:
            self.logo()
            self.erro1()
            self.help()
            sys.exit()
    def clscr(self):
        linux = 'clear'
        win = 'cls'
        os.system([linux,win][os.name == 'nt'])
    def logo(self):
        print(m + """
         ######################################################
               _____ ____    __          __           _ 
              / ____|___ \   \ \        / /          | |
             | |  __  __) |_ _\ \  /\  / /__  _ __ __| |
             | | |_ ||__ <| '_ \ \/  \/ / _ \| '__/ _` |
             | |__| |___) | | | \  /\  / (_) | | | (_| |
              \_____|____/|_| |_|\/  \/ \___/|_|  \__,_|
                  Developed by Cyb3r3x3r - ICG                          
         ######################################################                                   
""")
    def erro1(self):
        print(r + '     [-]--------------------------------------------')
        print(r + '     [-]' + r + 'You must use an arguement in syntax')
    def help(self):
        print('')
        print(m + '[!]  -n   =             generate only from numbers')
        print(m + '[!]  -l   =             generate only from letter')
        print(m + '[!]  -m   =             generate from both letter nd numbers')
    def num_gen(self,choice1):
        spcl_ch = ['@', '-', '$', '%', '&', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        only_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if choice1 == 'y' or choice1 == 'Y':
            num_list = []
            ab = ''
            for x in range(0,14):
                num_list.append(random.choice(spcl_ch))
            snum_list = [str(a) for a in num_list]
            nm = ''.join(snum_list)
            return nm
        else:
            re = 0;
            for x in range(0,14):
                numm = random.choice(only_num)
                re = re*10 + numm
            return re
    def word_gen(self):
        spc_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&']
        w_list = []
        for x in range(0,18):
            w_list.append(random.choice(spc_letter))
        wl_list = ''.join(w_list)
        return wl_list
    def word_str(self,name,str1):
        spc_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&']
        w_list = []
        for x in range(0,12):
            w_list.append(random.choice(spc_letter))
        name1 = name.lower()
        str1 = str1.lower()
        name1 = name1.replace('b','6').replace('a','4').replace('i','1').replace('e','3').replace('l','!').replace('t','7').replace('s','$').replace('o','0')
        str1 = str1.replace('b','6').replace('a','4').replace('i','1').replace('e','3').replace('l','!').replace('t','7').replace('s','$').replace('o','0')
        pwd = name1 + ''.join(w_list) + str1
        return pwd
    def mix_gen(self,name,str1):
        all_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        w_list = []
        for x in range(0,15):
            w_list.append(random.choice(all_char))
        name1 = name.lower()
        str1 = str1.lower()
        name1 = name1.replace('b','6').replace('a','4').replace('i','1').replace('e','3').replace('l','!').replace('t','7').replace('s','$').replace('o','0')
        str1 = str1.replace('b','6').replace('a','4').replace('i','1').replace('e','3').replace('l','!').replace('t','7').replace('s','$').replace('o','0')
        pwd = name1 + ''.join(w_list) + str1
        return pwd
cyb = G3nWord()
cyb
