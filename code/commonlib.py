
# somewhat common functions i use in my stuff
# that i grouped into a single file
# so i could just import them
#
# all credits go to me and some stack overflow fellars

import requests, os, math, time, json
# make sure u have those ↑



# PRERUN
root=os.path.dirname(os.path.abspath(__file__))
where=os.path.join(root,'__test__')
wherehp=os.path.join(where, 'hp.json')
wherecofl=os.path.join(where, 'cofl.json')              # so that i wont need to call api a billion times just to check if i didnt made a typo
try:
    os.mkdir(where)
except FileExistsError:
    pass
except Exception as e: raise(e)


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
def callhp(IsTest=False):
    IsThere=os.path.isfile(wherehp)
    i='https://api.hypixel.net/skyblock/bazaar'
    if not IsTest: j=requests.get(i); l=j.json()
    else:
        if IsThere:
            with open(wherehp) as file: l=json.load(file)
        else:
            j=requests.get(i); l=j.json()
            with open(wherehp,'w') as file: json.dump(l, file, indent=4)
    return l

def callcofl(target=None, IsTest=False):
    IsThere=os.path.isfile(wherecofl)
    if target==None: raise Exception('no value provided')                                                                                   # thanks coflnet for existing and making checking auction alot easier
    i=f'https://sky.coflnet.com/api/auctions/tag/{target}/active/bin'
    if not IsTest: j=requests.get(i); l=j.json()
    else:
        if IsThere:
            with open(wherecofl) as file: l=json.load(file)
        else:
            j=requests.get(i); l=j.json()
            with open(wherecofl,'w') as file: json.dump(l, file, indent=4)
    return l


# QOL/VISUAL
def short(target=None):
    i = str(f'{target/1000000000:.2f}')+'B' if abs(target)>=1000000000 else str(f'{target/1000000:.2f}')+'M' if abs(target)>=1000000 else str(f'{target/1000:.2f}')+'k' if abs(target)>=1000 else f'{target:.2f}'
    return i

def long(x=None):
    try:
        mul=[1000000000,1000000,1000]
        for i,j in enumerate(['b','m','k']):
            if str(x[len(str(x))-1]).lower() == j:
                x=list(x.replace(',','.'))
                x.pop(len(x)-1)                         # this was harder than the shortening one
                x.pop(0)
                x=float(''.join(x))*mul[i]
                return x
        return float(x[1:])
    except ValueError: return 1

def smol(col, row):
    cl()
    lastsize=[]
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
        if lastsize!=size:                                                      # probably fixes too much flickering    
            cl()
            print(f'{'\033[32m' if row<=size[1] else ''}{up}\033[0m\n{'\n'*(math.ceil(size[1]/2)-4)}{' '*ohnomid}{ohno}\n{'\033[32m' if col<=size[0] else ''}{hor}\033[0m\n{' '*uneedmid}{uneed}{'\n'*(size[1]-(math.ceil(size[1]/2))-4)}{' '*(mid-len(str(size[1]))//2)}{'\033[32m' if row<=size[1] else ''}{down}\033[0m', end='', flush=True)    # i have a bad habit of making those...
            time.sleep(0.05); lastsize=size
    cl()
    print(f'{'\n'*int(size[1]/2)}{' '*int(size[0]/2-5)}well done!!\n')
    time.sleep(0.7)
    cl()