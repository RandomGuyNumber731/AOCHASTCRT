try: 
    from commonlib import *
except: raise Exception('could not import commonlib.py')

if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)                                                                                                     # im not sure where i found that
    mode = ctypes.c_ulong()                                                                                                                 # i actually dont know if it works
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0001 | 0x0004)

print(echo())