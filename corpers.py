import os
import time
#cores
Ve = '\033[1;31m'
Vd = '\033[1;32m'
Am = '\033[1;33m'
Az = '\033[1;34m'
Br = '\033[1;37m'

ban = f'''{}
_________                __________                        
\_   ___ \   ____ _______\______   \  ____ _______  ______ 
/    \  \/  /  _ \\_  __ \|     ___/_/ __ \\_  __ \/  ___/ 
\     \____(  <_> )|  | \/|    |    \  ___/ |  | \/\___ \  
 \______  / \____/ |__|   |____|     \___  >|__|  /____  > 
        \/                               \/            \/  
                                                           '''
op = f'''
_______________
{Ve}"Vermelho"    {Br}-
{Vd}"Verde"       {Br}=
{Am}"Amarelo"     {Br}-
{Az}"Azul"        {Br}=
_______________\n\n
>>> 
'''

os.system('clear')
print(f'{ban}')
cor = input(f'{op}')


if cor == 'Vermelho' or 'vermelho':
    os.chdir('/data/data/com.termux/files/home/Corlux/Colors/')
    os.system('cp Vermelho /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/files/usr/etc/')
    os.system('rm -fr bash.bashrc')
    os.system('mv Vermelho bash.bashrc')
    print(f'{Ve}[{Br}i{Ve}]Pronto!!{Ve}[{Br}i{Ve}]')
elif cor == 'Verde' or 'verde':
    os.chdir('/data/data/com.termux/files/home/Corlux/Colors/')
    os.system('cp Verde /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/files/usr/etc/')
    os.system('rm -fr bash.bashrc')
    os.system('mv Verde bash.bashrc')
    print(f'{Vd}[{Br}i{Vd}]Pronto!!{Vd}[{Br}i{Vd}]')
elif cor == 'Amarelo' or 'amarelo':
    os.chdir('/data/data/com.termux/files/home/Corlux/Colors/')
    os.system('cp Verde /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/files/usr/etc/')
    os.system('rm -fr bash.bashrc')
    os.system('mv Amarelo bash.bashrc')
    print(f'{Am}[{Br}i{Am}]Pronto!!{Am}[{Br}i{Am}]')
elif cor == 'Azul' or 'azul':
    os.chdir('/data/data/com.termux/files/home/Corlux/Colors/')
    os.system('cp Azul /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/files/usr/etc/')
    os.system('rm -fr bash.bashrc')
    os.system('mv Azul bash.bashrc')
    print(f'{Az}[{Br}i{Az}]Pronto!!{Az}[{Br}i{Az}]')
else:
    os.system('clear')
    print(f'{ban}')
    print(f'''
_______________
{Ve}"Vermelho"    {Br}-
{Vd}"Verde"       {Br}=
{Am}"Amarelo"     {Br}-
{Az}"Azul"        {Br}=
_______________\n\n
>>> 
'''
    time.sleep(1)
    print(f'{Br}Command not found!')
    time.sleep(2)
    os.system('python corpers.py')