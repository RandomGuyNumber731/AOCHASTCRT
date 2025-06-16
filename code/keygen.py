try: 
    from commonlib import *
except: raise Exception('could not import commonlib.py')
import math

if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)                                                                                                     # im not sure where i found that
    mode = ctypes.c_ulong()                                                                                                                 # i actually dont know if it works
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0001 | 0x0004)

name='{}_KEY'
main='ENCHANTED_{}'
mainsub='{}'
sub='BEJEWELED_HANDLE'
subsub='GLACITE_JEWEL'
data=None
tp=None
amnt=1

maina=192
mainsuba=30720
suba=1
subsuba=3

mul=[1,maina,mainsuba,suba,subsuba]

def recall():
    cl()
    print('fetching...', flush=True, end='')
    global data
    data = callhp()

def put():
    cl()
    global data, tp
    i=input('MENU\n| 1 - tungsten\n| 2 - umber\n-| r - recall api\n-| q - exit\n\ninput: ')
    match i[0]:
        case '1': tp='TUNGSTEN'; calc(tp)
        case '2': tp='UMBER'; calc(tp)
        case 'r': recall() ; put()
        case 'q': cl() ; quit()
        case   _: put()


def calc(target=None):
    cl()
    if target==None: raise Exception('no value provided')
    global name,main,mainsub,sub,subsub,mul,amnt
    name_=name.format(target)
    main_=main.format(target)
    mainsub_=target
    items=[name_,main_,mainsub_,sub,subsub]
    item_data, item_buy, item_sell={},{},{}
    print('\033[90m{:<22}{:<14}{:<14}{:<14}{:<10}{:<14}\033[0m'.format('name:','buy price:','sell price:','amount:','orders:','partial:'))
    for i,j in enumerate(items):
        item_data[j] = data['products'][j]['quick_status']
        item_buy[j] = float(f"{item_data[j]['buyPrice']:.2f}")
        item_sell[j] = float(f"{item_data[j]['sellPrice']:.2f}")
        pb = short(item_buy[j])
        ps = short(item_sell[j])
        if i!=0: need = amnt*mul[i] ; order = need//71680 ; part = need-order*71680
        else: need=amnt*mul[i]; order=part=''
        blk='\033[33m' if not isinstance(order, str) and 20<order<25 else '\033[31m' if not isinstance(order, str) and order>=25 else ''
        print(f'{blk} {j:<22}{pb:<14}{ps:<14}{need:<14}{order:<10}{part:<14}\033[0m')
    print('\n\033[90m{:<22}{:<14}{:<14}\033[0m'.format('','cost insta:','cost order:'))
    for i,j in enumerate(items):
            ci = short(item_buy[j]*amnt)
            co = short(item_sell[j]*amnt)
            print(f' {j:<22}{ci:<14}{co:<14}')
    ioocnfmv=['COST','INSTASELL','SELL ORDER']
    ioocnfmva=['',item_sell,item_buy]
    costo, costi={},{}
    for i,j in enumerate(items):
        if i!=0:
            costo[j]=item_sell[j]*mul[i]
            costi[j]=item_buy[j]*mul[i]
    print('\n\n\033[90m{:<18}{:<20}{:<20}{:<20}{:<20}\033[0m'.format('','full sub profit:','sub handle only:',f'sub {mainsub_.lower()} only:','no sub:'))
    for i,j in enumerate(ioocnfmv):
        if i==0:
            fsp=short(costo[mainsub_]*amnt+costo[subsub]*amnt)
            sho=short(costo[main_]*amnt+costo[subsub]*amnt)
            smo=short(costo[mainsub_]*amnt+costo[sub]*amnt)
            ns =short(costo[main_]*amnt+costo[sub]*amnt)
        else:
            fsp=short(ioocnfmva[i][name_]*amnt-costo[mainsub_]*amnt-costo[subsub]*amnt)
            sho=short(ioocnfmva[i][name_]*amnt-costo[main_]*amnt-costo[subsub]*amnt)
            smo=short(ioocnfmva[i][name_]*amnt-costo[mainsub_]*amnt-costo[sub]*amnt)
            ns =short(ioocnfmva[i][name_]*amnt-costo[main_]*amnt-costo[sub]*amnt)
        print(' {:<18}{:<20}{:<20}{:<20}{:<20}'.format(j,fsp,sho,smo,ns))
    print('\033[90mbying stuff instantly:\033[0m')
    for i,j in enumerate(ioocnfmv):
        if i==0:
            fsp=short(costi[mainsub_]*amnt+costi[subsub]*amnt)
            sho=short(costi[main_]*amnt+costi[subsub]*amnt)
            smo=short(costi[mainsub_]*amnt+costi[sub]*amnt)
            ns =short(costi[main_]*amnt+costi[sub]*amnt)
        else:
            fsp=short(ioocnfmva[i][name_]*amnt-costi[mainsub_]*amnt-costi[subsub]*amnt)
            sho=short(ioocnfmva[i][name_]*amnt-costi[main_]*amnt-costi[subsub]*amnt)
            smo=short(ioocnfmva[i][name_]*amnt-costi[mainsub_]*amnt-costi[sub]*amnt)
            ns =short(ioocnfmva[i][name_]*amnt-costi[main_]*amnt-costi[sub]*amnt)
        print(' {:<18}{:<20}{:<20}{:<20}{:<20}'.format(j,fsp,sho,smo,ns))


    l=input('\n\ntype in any number for amount (max 20000) | q - go back: ')
    try:
        l=math.floor(float(l))
        if l>20000: l=20000
    except: l=l
    match l:
        case 'q': amnt=1; put()
        case   _:
            if isinstance(l, (int,float)): amnt=l; calc(tp)
            else: calc(tp)

smol(101,29)
recall()
put()