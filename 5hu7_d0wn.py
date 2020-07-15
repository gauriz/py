import os 
  
shutdown = raw_input("Do you wish to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 1") 