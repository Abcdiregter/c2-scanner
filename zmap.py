import sys
import os 

os.system('clear')
print('coded by hphong')


def scan():
    output = sys.argv[2]
    port = sys.argv[1]
    os.system(f'zmap -p {port} -o {output}')
    print ('scaning with zmap ctrl c to quit and exit')

if '_main_' == "_main_":
    scan()
else:
    print('usage python3 zmap.py port outputfile')



