import requests, os, math

if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()                                                                                                                 # bruh imagine using windows like bruh
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0001 | 0x0004)

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')                                                                                        # my fav thingy


item='smth went wrong eh?'
headitem='smth went wrong eh?'
subitem='smth went wrong eh'
subsubitem='smth went wrong eh'

ovoid='NULL_OVOID'
ovoid_headitem='NULL_SPHERE'
ovoid_subitem="ENCHANTED_OBSIDIAN"
ovoid_subsubitem='OBSIDIAN'

viscera='REVENANT_VISCERA'
viscera_headitem='REVENANT_FLESH'
viscera_subitem='ENCHANTED_STRING'                                                                                                          # this took awhile
viscera_subsubitem='STRING'

silk='TARANTULA_SILK'
silk_headitem='TARANTULA_WEB'
silk_subitem='ENCHANTED_FLINT'
silk_subsubitem='FLINT'

tooth='GOLDEN_TOOTH'
tooth_headitem='WOLF_TOOTH'
tooth_subitem='ENCHANTED_GOLD'
tooth_subsubitem='GOLD_INGOT'

nope='\033[2mno orders\033[0m'

got={}
amnt=1
lastdat={}
m=1000000

def call(IsCraft=False):
    
    cl()
    print('fetching...')
    global data
    des='https://api.hypixel.net/skyblock/bazaar'
    out=requests.get(des)    
    data=out.json()
    put() if not IsCraft else craftput()

def put():
    
    cl()
    global i    
    i=input('MENU\n| 1 - viscera\n| 2 - silk\n| 3 - tooth\n| 4 - ovoid\n-| r - recall api\n-| c - crafts\n-| q - exit\n\ninput: ')                
    match i:                                                                                                                                # dont judge im not fond of lists
        case '1':
            check(viscera_headitem, viscera_subitem, viscera_subsubitem, viscera, True)
        case '2':
            check(silk_headitem, silk_subitem, silk_subsubitem, silk, True)
        case '3':
            check(tooth_headitem, tooth_subitem, tooth_subsubitem, tooth, True)
        case '4':
            check(ovoid_headitem, ovoid_subitem, ovoid_subsubitem, ovoid, True)
        case 'r':
            call()
        case 'c':
            craftput()
        case 'q':
            cl()
            exit
        case _:
            put()

def craftput():
    
    cl()
    global i
    i=input('CRAFTS\n| 1 - viscera\n| 2 - silk\n| 3 - tooth\n| 4 - ovoid\n-| r - recall api\n-| q - exit\n-| else - back\n\ninput: ')
    match i:
        case '1':
            craft(check(viscera_headitem, viscera_subitem, viscera_subsubitem, viscera))
        case '2':
            craft(check(silk_headitem, silk_subitem, silk_subsubitem, silk))                                                                # still not fond 😔
        case '3':
            craft(check(tooth_headitem, tooth_subitem, tooth_subsubitem, tooth))
        case '4':
            craft(check(ovoid_headitem, ovoid_subitem, ovoid_subsubitem, ovoid))
        case 'r':
            call(True)
        case 'q':
            cl()
            exit
        case _:
            put()

def check(x=headitem, y=subsubitem, z=subsubitem, target=item, IsVerb=False):
    
    cl()
    global got, amnt
    amnt=1
    got={}
    j=0
    get={}
    items=[target, x, y, z]
    for i in items:
        if i in data['products']:
            if target not in got: got[target]=[]
            j+=1
            get={}; get['name']=''; get['buy']=0; get['sell']=0
            item_data = data['products'][i]
            buy=float(f"{item_data['quick_status']['buyPrice']:.2f}")                                                                       # yay api!!!
            sell=float(f"{item_data['quick_status']['sellPrice']:.2f}")
            if IsVerb: print(f'{i}\nbuy: {nope if buy==0 else buy}\nsell: {nope if sell==0 else sell}', end='')
            if i == y:
                ic=float(f"{160*data['products'][z]['quick_status']['buyPrice']:.2f}")
                oc=float(f"{160*data['products'][z]['quick_status']['sellPrice']:.2f}")
                if IsVerb: print(f'\n| instabuy craft: {nope if ic==0 else ic}\n| order craft: {nope if oc==0 else oc}\n\n')
            elif IsVerb: print('\n\n')
            get['name']=i; get['buy']=buy; get['sell']=sell; got[target].append(get)
            # print(get)
        else:
            if IsVerb: print(f'item not found\nthe value is: {[i]}\n')
    # print(got)
    if IsVerb: input('press enter to continue'); put()
    if not IsVerb: return got


def craft(dat=lastdat):

    cl()

    global amnt, lastdat

    awe=dat[list(dat.keys())[0]]
    target=awe[0]
    head=awe[1]
    sub=awe[2]
    subsub=awe[3]

    hia=amnt*32*4
    sia=amnt*32
    ssia=amnt*32*160

    hio=math.floor(hia/71680)
    sio=math.floor(sia/71680)
    ssio=math.floor(ssia/71680)

    hir=hia-hio*71680
    sir=sia-sio*71680
    ssir=ssia-ssio*71680

    iam=[None, hia, sia, ssia]
    ior=[None, hio, sio ,ssio]
    ire=[None, hir, sir, ssir]

    ttcsiffoiussiwpcab=70    #"time to craft sub item from full order if using subsub items with personal compactor and bags (rough estimate)" 🥀🥀🥀🥀🥀
    opbbopi=ssio*5    #"order placement bias based on personal experience"
    tcvtttftafctiussistywkiiwion=ssia/71680*ttcsiffoiussiwpcab+opbbopi if ssia>71680 else ssia/1024    #"the convinient variable that tweaks the formula to adjust for craft time if using subsub items so that you will know if it woth it or not" 😭😭😭😭🥀🥀🥀🥀🥀🥀🥀

    tpso=target['buy']
    tpis=target['sell']

    hpib=head['buy']
    hpbo=head['sell']

    spib=sub['buy']
    spbo=sub['sell']

    sspib=subsub['buy']
    sspbo=subsub['sell']

    ccib=round(hpib*hia+spib*sia, 2)
    ccbo=round(hpbo*hia+spbo*sia, 2)

    ccibwss=round(hpib*hia+sspib*ssia, 2)   # "craft cost instabuy with subsub item" 🥀🥀
    ccbowss=round(hpbo*hia+sspbo*ssia, 2)

    bigos=[tpso,tpis,ccib,ccbo,ccibwss,ccbowss]

    IsProfit = True if any(a>b for a in (tpso*amnt,tpis*amnt) for b in(ccib,ccbo)) else False
    IsBetterWithSS = True if any(a>b for a in (tpso*amnt,tpis*amnt) for b in (ccibwss,ccbowss)) else False
    IsActuallyBetterWithSS = True if amnt*15*(opbbopi/4)/tcvtttftafctiussistywkiiwion<100 else False    # thats actually just my opinion u may ignore it
    IsBazaarOrderCapped = True if hio+sio>21 else False                                        # NOBODY CARES ABOUT SS
    IsBazaarOrderCappedButYouAreRich = True if hio+sio>28 else False

    cl()

    ipco=round(amnt*tpso/ccib*100, 2)
    opco=round(amnt*tpso/ccbo*100, 2)
    ipci=round(amnt*tpis/ccib*100, 2)
    opci=round(amnt*tpis/ccbo*100, 2)

    for i, j in enumerate(awe):
        if i>0:
            print(f'{'\033[90m' if ior[i]>25 else ''}{j["name"]}\n| total amount: {iam[i]:<10}full orders: {ior[i]:<5}partial order: {ire[i]:<5}\n\033[0m')
        else:
            print(f'{j["name"]}\n\n| sell order:  {amnt:5} * {tpso} = {(round(amnt*tpso, 2) if amnt*tpso<m else f'{round(amnt*tpso/m,2)}M'):<{7 if amnt*tpso>m else 14}} (i - {'\033[31;2m' if ipco<100 else '\033[33;2m' if ipco<=105 and ipco>=100 else '\033[32m'}{ipco:6}%\033[0m) (o - {'\033[31;2m' if opco<100 else '\033[33;2m' if opco<=105 and opco>=100 else '\033[32m'}{opco:6}%\033[0m)\n| instasell:   {amnt:5} * {tpis} = {(round(amnt*tpis, 2) if amnt*tpis<m else f'{round(amnt*tpis/m, 2)}M'):<{7 if amnt*tpis>m else 14}} (i - {'\033[31;2m' if ipci<100 else '\033[33;2m' if ipci<=105 and ipci>=100 else '\033[32m'}{ipci:6}%\033[0m) (o - {'\033[31;2m' if opci<100 else '\033[33;2m' if opci<=105 and opci>=100 else '\033[32m'}{opci:6}%\033[0m)')      # srry thats the only way i could think of
            print(f'\ntotal price:\n| order - {ccbo if ccbo<m else f'{round(ccbo/m,2)}M'}\n| insta - {ccib if ccib<m else f'{round(ccib/m,2)}M'}\n\ntotal price (ss):\n| order - {ccbowss if ccbowss<m else f'{round(ccbowss/m,2)}M'}\n| insta - {ccibwss if ccibwss<m else f'{round(ccibwss/m,2)}M'}\n')                                                                                                                                                                                                                                                                                                                                                                                                                                                                       # i love them one-liners
            for i in range(255,235,-1):
                print(f'\033[38;5;{i}m---\033[0m', end='')
            print('\033[0m')
    for i in range(255,235,-1):
        print(f'\033[38;5;{i}m---\033[0m', end='')
    print('\033[0m')
    print(f'| IsProfit = {isit(IsProfit)}\n| IsBetterWithSS = {isit(IsBetterWithSS)}\n| IsActuallyBetterWithSS = {isit(IsActuallyBetterWithSS):}\n| IsBazaarOrderCapped = {isit(IsBazaarOrderCapped, True)}\n| IsBazaarOrderCappedButYouAreRich = {isit(IsBazaarOrderCappedButYouAreRich, True)}\n')
    k=input('type in any number for amount (max 20000) | q - go back: ')
    lastdat=dat
    try:
        k=math.floor(float(k))
        if k>20000: k=20000
    except: k=k    # seems about right eh?
    match k:
        case 'q':
            craftput()
        case _:
            if isinstance(k, (int,float)): amnt=k; craft(lastdat)
            else: craft(lastdat)

def isit(i, op=False):
    if op: j = '\033[32mNah\033[0m' if not i else '\033[31mYeah\033[0m'  
    else: j = '\033[32mYeah\033[0m' if i else '\033[31mNah\033[0m'
    return j

call()
