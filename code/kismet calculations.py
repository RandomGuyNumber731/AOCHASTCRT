import requests, os, math, keyboard

if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    mode = ctypes.c_ulong()                                                                                                                 # bruh imagine using windows like bruh
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))                                                                                     # déjà vu eh?
    kernel32.SetConsoleMode(handle, mode.value | 0x0001 | 0x0004)

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

datbz={}

handle='NECRON_HANDLE'
scroll_1='WITHER_SHIELD_SCROLL'
scroll_2='IMPLOSION_SCROLL'
scroll_3='SHADOW_WARP_SCROLL'
rec='RECOMBOBULATOR_3000'

feather='KISMET_FEATHER'

odds_handle=0.001094
odds_scroll=0.001459
odds_rec=0.029184

names=[handle, scroll_1, scroll_2, scroll_3, rec]
odds=[odds_handle, odds_scroll, odds_scroll, odds_scroll, odds_rec]

def getit():
    while True:
        key=keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN:                # man i hate it
            return key.name


def callbz():
    print('fetching bazaar...')
    global datbz
    api='https://api.hypixel.net/skyblock/bazaar'
    out=requests.get(api)
    datbz=out.json()

def callah():
    print('fetching auction...')
    global datah
    api='https://sky.coflnet.com/api/auctions/tag/NECRON_HANDLE/active/bin'
    out=requests.get(api)
    datah=out.json()

def call():
    try:
        cl()
        callbz()
        callah()
    except Exception as e:
        cl()
        print(f'got an error while fetching api: \033[31m{e}\033[0m')
        quit()
        
def doings():
    call()
    cl()
    avrg=0
    prices={}
    print("IIWITUAKF?\n\n")
    print('PRICES:')
    for i, j in enumerate(names):
        if j in datbz['products']:
            item_data=datbz['products'][j]
            prc=item_data['quick_status']['buyPrice']
            print(f' {j:<25} - sell order: {prc/1000000:.2f}M')
            prices[j]=float(f'{prc:.2f}')
        elif j == handle:
            for l, k in enumerate(datah):
                avrg+=datah[l]['startingBid']
            hndlp=avrg/len(datah)
            print(f' {j:<25} - BIN average price: {hndlp/1000000:.2f}M\n{' '*27}\\ BIN cheapest: {datah[0]['startingBid']/1000000:.2f}M\n')
            prices[j]=float(f'{hndlp:.2f}')
    item_data=datbz['products'][feather]
    fprice=item_data['quick_status']['sellPrice']
    print(f'\n {feather:<25} - buy order: {fprice/1000000:.2f}M\n{' '*27}\\ bits: 1350')
    print('-'*69)

    print(f'ODDS:{' '*23}USUAL:{' '*17}WITH KISMET:')
    for i, j in enumerate(odds):
        print(f' {names[i]:<25} - {j*100}% (1/{1/j:.2f}){' '*(3 if i!=4 else 4)}| {j*100*2}% (1/{1/j/2:.2f})')
    print('\nPROFIT:')
    for i, j in enumerate(names):
        nok=prices[j]/math.ceil(1/odds[i])
        yesk=(prices[j]-fprice*math.ceil(1/odds[i]/2))/math.ceil(1/odds[i]/2)
        print(f' {j:<25} - {nok/(1000 if abs(nok)<1000000 else 1000000):.2f}{'k' if abs(nok)<1000000 else 'M'} per run{'':<5}| {yesk/(1000 if abs(yesk)<1000000 else 1000000):.2f}{'k' if abs(yesk)<1000000 else 'M'} per run')
    print('\npress any key to exit', end='', flush=True)
    getit()
    cl()
    exit



doings()
