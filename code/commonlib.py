
# somewhat common functions i use in my stuff
# that i grouped into a single file
# so i could just import them
#
# all credits go to me and some stack overflow fellars

import requests, os, math, time

# MISC
def echo():
    return 'ping!'

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')                                                                                        # bet it works really good

def check_size():
    i=os.get_terminal_size()
    out=[i.columns, i.lines]
    return out


# API
def callhp():
    i='https://api.hypixel.net/skyblock/bazaar'
    j=requests.get(i)    
    l=j.json()
    return l

def callcofl(x=None):
    if x==None: raise Exception('no value provided')                                                                                        # thanks coflnet for existing and making checking auction alot easier
    i=f'https://sky.coflnet.com/api/auctions/tag/{x}'
    j=requests.get(i)
    l=j.json()
    return l


# QOL/VISUAL
def short(x=None):
    i = str(f'{x/1000000000:.2f}')+'B' if abs(x)>=1000000000 else str(f'{x/1000000:.2f}')+'M' if abs(x)>=1000000 else str(f'{x/1000:.2f}')+'k' if abs(x)>=1000 else x
    return i

def smol(col, row):
    cl()
    ohno='window too small!!'
    uneed='u need {} by {}'.format(col, row)
    size = check_size()
    if size[0]>=col and size[1]>=row:
        return
    while size[0]<col or size[1]<row:
        size = check_size()
        ohnomid=math.ceil(size[0]/2)-math.ceil(len(ohno)/2)
        uneedmid=math.ceil(size[0]/2)-math.ceil(len(uneed)/2)
        mid=math.ceil(size[0]/2)
        space=' '*(mid-1)
        up=f'{space}^\n{space}|\n{' '*(mid-len(str(size[1]))//2)}{size[1]}'
        down=f'{size[1]}\n{space}|\n{space}V'
        hor=f'<-{size[0]}{' '*(size[0]-4-len(str(size[0])*2))}{size[0]}->'
        print(f'{'\033[32m' if row<=size[1] else ''}{up}\033[0m\n{'\n'*(math.ceil(size[1]/2)-4)}{' '*ohnomid}{ohno}\n{'\033[32m' if col<=size[0] else ''}{hor}\033[0m\n{' '*uneedmid}{uneed}{'\n'*(size[1]-(math.ceil(size[1]/2))-4)}{' '*(mid-len(str(size[1]))//2)}{'\033[32m' if row<=size[1] else ''}{down}\033[0m', end='', flush=True)    # i have a bad habit of making those...
        time.sleep(0.05)
        cl()
    size = check_size()
    print(f'{'\n'*int(size[1]/2)}{' '*int(size[0]/2-5)}well done!!\n')
    time.sleep(0.7)
    cl()