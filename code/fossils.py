try: 
    from commonlib import *
except: raise Exception('could not import commonlib.py')

# new update -> new mmm -> new script
# and yet same old headaches

cl()

printn('calling hypixel api...')
hp = callhp()
print(' +')
data=hp['products']

x50=['FOOTPRINT_FOSSIL', 'UGLY_FOSSIL', 'SPINE_FOSSIL', 'CLUBBED_FOSSIL', 'WEBBED_FOSSIL', 'TUSK_FOSSIL']
x25=['HELIX', 'CLAW_FOSSIL', 'GLACITE_SHARD']       # i was slightly surprised that helix is not a fossil apparently
x25ah=['FOSSIL_THE_FISH', 'PREHISTORIC_EGG']

dust='ESSENCE_FOSSIL'
dust_price={'sell':data[dust]['quick_status']['sellPrice'], 'buy':fcut(data[dust]['quick_status']['buyPrice'])}

printn('organizing hypixel api data...')
total = []
for i in x50:
    i_buy  = fcut(data[i]['quick_status']['buyPrice'])
    i_sell = fcut(data[i]['quick_status']['sellPrice'])

    total.append({'id':i, 'buy':i_buy, 'sell':i_sell, 'val':50})

for i in x25:
    i_buy  = fcut(data[i]['quick_status']['buyPrice'])
    i_sell = fcut(data[i]['quick_status']['sellPrice'])

    total.append({'id':i, 'buy':i_buy, 'sell':i_sell, 'val':25})
print(' +')

printn('calling coflnet api...')                    # thanks coflnet.com for ur extra free auction api i honestly would have used the hypixel one if i knew if it even existed (i actually have no idea where the data comes from)
for i in x25ah:
    x = callcofl(i)
    if x == []:
        total.append({'id':i, 'min':0, 'avg':0, 'val':25})
        break
    tmp=0
    tmpmin=[]
    for j in x:
        tmp += j['startingBid']
        tmpmin.append(j['startingBid'])
        i_avg = fcut(tmp/len(x))
    i_min = min(tmpmin)

    total.append({'id':i, 'min':i_min, 'avg':i_avg, 'val':25})
    print(' +')

printn('calculating...')
numbers = []
for i in total:
    try:
        numbers.append(i['buy'])
        numbers.append(i['sell'])
    except KeyError:                        # stuff for padding
        numbers.append(i['min'])
        numbers.append(i['avg'])

max_id_len = len(max(x50+x25+x25ah, key=len))
max_number_len = len(str(max(numbers, key=lambda x : len(str(x)))))+1

for i,j in enumerate(total):
    try:
        po_buy  = fcut(dust_price['buy']*j['val']-j['buy'])
        po_sell = fcut(dust_price['buy']*j['val']-j['sell'])
        total[i]['profit_order']={'buy':po_buy, 'sell':po_sell}
        pi_buy  = fcut(dust_price['sell']*j['val']-j['buy'])
        pi_sell = fcut(dust_price['sell']*j['val']-j['sell'])
        total[i]['profit_insta']={'buy':pi_buy, 'sell':pi_sell}
    except KeyError:                                                    # profits
        po_buy  = fcut(dust_price['buy']*j['val']-j['min'])
        po_sell = fcut(dust_price['buy']*j['val']-j['avg'])
        total[i]['profit_order']={'buy':po_buy, 'sell':po_sell}
        pi_buy  = fcut(dust_price['sell']*j['val']-j['min'])
        pi_sell = fcut(dust_price['sell']*j['val']-j['avg'])
        total[i]['profit_insta']={'buy':pi_buy, 'sell':pi_sell}

numbers = []
for i,j in enumerate(total):
    try:
        if j['min'] <= 0:
            break
    except KeyError: pass                                               # not sure if i could have used lambda for that but it seems to work fine

    numbers.append(j['profit_order']['sell']/j['val'])
    numbers.append(j['profit_insta']['sell']/j['val'])
candidate = max(numbers)

for i,j in enumerate(total):
    if (j['profit_order']['sell']/j['val']==candidate) or (j['profit_insta']['sell']/j['val']==candidate):
        best = total[i]['id']
print(' +')

printn('organizing the data in a very neat way that i spent too much time on coding...')    # pretty self-explanatory
lines=[]
linecount=0
for i in total:
    if i['val']==50:
        rbool=True
        try:
            tmp=i['buy']
            esc1 = ESC.green if i['id'] == best else ESC.yellow if (i['buy'] <= 0 or i['sell'] <= 0) else ''
            lines.append(f'{esc1}{i['id']:>{max_id_len+1}}{ESC.clear} | (x{i['val']}){'buy':>{max_number_len}}{' '*(8)}sell    '+ESC.clear)                                                         ;linecount+=1
            lines.append(f'{' '*(max_id_len+2)};- price: {i['buy']:>{max_number_len}} | {i['sell']:<{max_number_len}}'+ESC.clear)                                                                   ;linecount+=1
        except KeyError:
            esc1 = ESC.green if i['id'] == best else ESC.yellow if i['min'] <= 0 else ''
            lines.append(f'{esc1}{i['id']:>{max_id_len+1}}{ESC.clear} | (x{i['val']}){'min':>{max_number_len}}{' '*(8)}avg     '+ESC.clear)                                                         ;linecount+=1
            lines.append(f'{' '*(max_id_len+2)};- price: {i['min']:>{max_number_len}} | {i['avg']:<{max_number_len}}'+ESC.clear)                                                                    ;linecount+=1
        
        esc1 = ESC.gray if i['profit_order']['buy'] < 0 else ESC.green if i['id'] == best else ''
        esc2 = ESC.gray if i['profit_order']['sell'] < 0 else ESC.green if i['id'] == best else ''
        esc3 = ESC.gray if i['profit_insta']['buy'] < 0 else ESC.green if i['id'] == best else ''           # u know the gist
        esc4 = ESC.gray if i['profit_insta']['sell'] < 0 else ESC.green if i['id'] == best else ''
        lines.append(f'{' '*(max_id_len-7)}{'profits -+- order: '}{esc1}{i['profit_order']['buy']:>{max_number_len}}{ESC.clear} | {esc2}{i['profit_order']['sell']:<{max_number_len}}'+ESC.clear)   ;linecount+=1
        lines.append(f'{' '*(max_id_len+1)}{' `- insta: '}{esc3}{i['profit_insta']['buy']:>{max_number_len}}{ESC.clear} | {esc4}{i['profit_insta']['sell']:<{max_number_len}}'+ESC.clear)           ;linecount+=1
    else:
        if rbool: linecount=0; rbool=False
                                                        # i swear to god this shit gets crazier every time like what the actual fuck is this??????
        try:
            tmp=i['buy']
            esc1 = ESC.green if i['id'] == best else ESC.yellow if (i['buy'] <= 0 or i['sell'] <= 0) else ''
            lines[linecount]+=(f'{esc1}{' '*8}{i['id']:>{max_id_len+1}}{ESC.clear} | (x{i['val']}){'buy':>{max_number_len}}{' '*(8)}sell    '+ESC.clear)                                                            ;linecount+=1
            lines[linecount]+=(f'{' '*8}{' '*(max_id_len+2)};- price: {i['buy']:>{max_number_len}} | {i['sell']:<{max_number_len}}'+ESC.clear)                                                                      ;linecount+=1
        except KeyError:
            esc1 = ESC.green if i['id'] == best else ESC.yellow if i['min'] <= 0 else ''
            lines[linecount]+=(f'{esc1}{' '*8}{i['id']:>{max_id_len+1}}{ESC.clear} | (x{i['val']}){'min':>{max_number_len}}{' '*(8)}avg     '+ESC.clear)                                                            ;linecount+=1
            lines[linecount]+=(f'{' '*8}{' '*(max_id_len+2)};- price: {i['min']:>{max_number_len}} | {i['avg']:<{max_number_len}}'+ESC.clear)                                                                       ;linecount+=1
        
        esc1 = ESC.gray if i['profit_order']['buy'] < 0 else ESC.green if i['id'] == best else ''
        esc2 = ESC.gray if i['profit_order']['sell'] < 0 else ESC.green if i['id'] == best else ''
        esc3 = ESC.gray if i['profit_insta']['buy'] < 0 else ESC.green if i['id'] == best else ''
        esc4 = ESC.gray if i['profit_insta']['sell'] < 0 else ESC.green if i['id'] == best else ''
        lines[linecount]+=(f'{' '*8}{' '*(max_id_len-7)}{'profits -+- order: '}{esc1}{i['profit_order']['buy']:>{max_number_len}}{ESC.clear} | {esc2}{i['profit_order']['sell']:<{max_number_len}}'+ESC.clear)      ;linecount+=1
        lines[linecount]+=(f'{' '*8}{' '*(max_id_len+1)}{' `- insta: '}{esc3}{i['profit_insta']['buy']:>{max_number_len}}{ESC.clear} | {esc4}{i['profit_insta']['sell']:<{max_number_len}}'+ESC.clear)              ;linecount+=1
print(' +')

cl()
smol(len(lines[0])-5, len(lines)+1+len(lines)//4)
for i,j in enumerate(lines):                            # this may be my new fav way to render things
    print(j)
    if i%4==3: print()










'''   RANDOM STUFF I SAVED FOR REFFERENCING   '''

# esc1 = ESC.gray if i['profit_order']['buy'] < 0 else ESC.green if i['id'] == best else ''
# esc2 = ESC.gray if i['profit_order']['sell'] < 0 else ESC.green if i['id'] == best else ''
# esc1 = ESC.gray if i['profit_insta']['buy'] < 0 else ESC.green if i['id'] == best else ''
# esc2 = ESC.gray if i['profit_insta']['sell'] < 0 else ESC.green if i['id'] == best else ''
# esc1 = ESC.green if i['id'] == best else ESC.yellow if i['min'] <= 0 else ''



# print(f'{i['id']:>{max_id_len+1}} | (x{i['val']}){'buy':>{max_number_len}}{' '*(8)}sell    ')
# print(f'{' '*(max_id_len+2)}|- price: {i['buy']:>{max_number_len}} | {i['sell']:<{max_number_len}}')
# print(f'{' '*(max_id_len-7)}{'profits -+- order: '}{fcut(dust_price['buy']*50-i['buy']):>{max_number_len}} | {fcut(dust_price['buy']*50-i['sell']):<{max_number_len}}')
# print()


# print(f'{i:>{funkymax}}:: (x50){'buy':>11}{' '*(8)}sell')
# print(f'{' '*(funkymax-5)}|=-=-=-=-=-=-=-  {i_buy:>10} | {i_sell}')
# print(f'{' '*(funkymax-5)}{'|- profit order: '}{fcut(dust_price['buy']*50-i_buy):>10} | {fcut(dust_price['buy']*50-i_sell)}')
# print(f'{' '*(funkymax-5)}{'`- profit insta: '}{fcut(dust_price['sell']*50-i_buy):>10} | {fcut(dust_price['sell']*50-i_sell)}\n')
