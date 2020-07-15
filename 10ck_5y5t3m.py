import ctypes 

option = raw_input('Do you wish to lock your system? (Y/N) ')
if option == 'N':
    print('Scared? Aren\'t we all? (;')
    exit()
else:
    user32 = ctypes.cdll.LoadLibrary("user32.dll") 
    user32.LockWorkStation()