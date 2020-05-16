#!/usr/bin/python3

import sys, os


#colors
class colors:

 CGREY    = '\33[90m'
 CRED2    = '\33[91m'
 CGREEN2  = '\33[92m'
 CYELLOW2 = '\33[93m'
 CBLUE2   = '\33[94m'
 CVIOLET2 = '\33[95m'
 CBEIGE2  = '\33[96m'
 CWHITE2  = '\33[97m'


print(f"""


                  {colors.CBLUE2} Wi-Fi numeric Passwords Creator
                  {colors.CBLUE2} ver:{colors.CRED2} 0.4
                  {colors.CBLUE2} By:{colors.CRED2} y053f01
                  {colors.CGREEN2} Proudly written in nano

           {colors.CBEIGE2} Introduction
           {colors.CRED2} +++++++++++++++++++++++++++++++++++++++++++++++
            +                                             +
              {colors.CBEIGE2} This code will help you to create
               passwords and store it in Text file
               for Wi-Fi that use numbers in password

              {colors.CRED2} Remember:{colors.CBEIGE2}
               The file that created will be useful after
               hacking the Wi-Fi networks and capturing
               the (.cap) file and use text file in
                  Aircrack-ng tool in Kali Linux

               File exmaple:
               Text.txt ===> Include:
               00000000
               00000001
               00000002
               ...
               99999999
               999999999... Endless
           {colors.CRED2} +                                             +
            +++++++++++++++++++++++++++++++++++++++++++++++{colors.CWHITE2}


""")

input("Press enter to continue...")
# this CLASS only waste the time HAHAHAHAH
class switch:
 case = {
 0:0,
 1:1,
 2:2,
 3:3,
 4:4,
 5:5,
 6:6,
 7:7
 }

class PSK:
 text = input("[+] Enter file name to store the data in TXT: ")
 path = text + '.txt'
 def __init__(self, key):
  i = input("[+] Enter number to start the loooop: ")
  i = int(i)
  self.key = key + i
 def txtpwd(self):
  with open(PSK.path, "w") as file:
   loooop = input("[+] Enter number to end the loooop: ")
   print("Loading...")
   loooop = int(loooop)
   while self.key <= loooop:
    if len(str(self.key)) == switch.case[1]:
     val = str(self.key)
     file.write("0000000" +  val) # 7 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[2]:
     val = str(self.key)
     file.write("000000" +  val) # 6 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[3]:
     val = str(self.key)
     file.write("00000" +  val) # 5 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[4]:
     val = str(self.key)
     file.write("0000" +  val) # 4 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[5]:
     val = str(self.key)
     file.write("000" +  val) # 3 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[6]:
     val = str(self.key)
     file.write("00" +  val) # 2 zeros
     file.write("\n")
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[7]:
     val = str(self.key)
     file.write("0" +  val) # 1 zeros
     file.write("\n")
     self.key = self.key + 1
    else:
     val = str(self.key)
     file.write(val) # 0 zeros
     file.write("\n")
     self.key = self.key + 1

rslt = PSK(0)
rslt.txtpwd()

size = os.path.getsize(rslt.path) / 1000 # Kilobyte

print(f"""


           Done!
           File name & path: {os.path.abspath(rslt.path)}
           Size: {size} KB


""")
