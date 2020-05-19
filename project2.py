#!/usr/bin/python3

import sys
import os
import time

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
      {colors.CBLUE2} ver:{colors.CRED2} 1.0
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

   {colors.CRED2} Updates:{colors.CBEIGE2}
   1. Make it faster by using for loop instead
      of While loop
   2. Add ETA for the process to end

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
 start = input("[+] Enter number to start the loooop: ")
 end = input("[+] Enter number to end the loooop: ")

 if int(end) == 0:
  print("\n[__________ETA: 0 m 0 s__________]")
 else:

  # This for approximate
  int_start_appro = int(start)
  int_end_appro = int(end)
  approximate_a_appro = int_end_appro - int_start_appro
  approximate_b_appro = approximate_a_appro * 0.0000087 # Approximate time for each looop 0.0000090 second Example 1000000 * 0.0000085
  seconds_appro = approximate_b_appro # Seconds Example 8.5s
  minutes_appro = seconds_appro / 60 # Minutes 0.14166667 m

  str_a_appro = str(minutes_appro)
  str_find_appro = str_a_appro.find(".") # 0.14166667 ==> 1

  minutes_a_appro = int(str_a_appro[:str_find_appro])
  seconds_a_appro = minutes_appro - minutes_a_appro
  seconds_b_appro = seconds_a_appro * 60
  seconds_c_appro = str(seconds_b_appro)
  seconds_e_appro = seconds_c_appro.find(".")
  size3 = approximate_a_appro * 9
  size4 = size3
  size5 = size4 / 1024
  size6 = size5 / 1024
  size7 = int(size6)
  print(f"\n[__________ETA: {minutes_a_appro} m {seconds_c_appro[:seconds_e_appro]} s Size: {size7} MB__________]")
 def __init__(self, key):
  i = int(PSK.start)
  self.key = key + i
 def txtpwd(self):
  with open(PSK.path, "w") as file:
   startt = int(PSK.start)
   endd = int(PSK.end) + 1
   #for dot in range(start, end):
    #print("Loading...  Approximate size will be ")
   for self.key in range(startt, endd):
    if len(str(self.key)) == switch.case[1]:
     val = str(self.key)
     file.write("0000000" +  val + "\n") # 7 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[2]:
     val = str(self.key)
     file.write("000000" +  val + "\n") # 6 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[3]:
     val = str(self.key)
     file.write("00000" +  val + "\n") # 5 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[4]:
     val = str(self.key)
     file.write("0000" +  val + "\n") # 4 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[5]:
     val = str(self.key)
     file.write("000" +  val + "\n") # 3 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[6]:
     val = str(self.key)
     file.write("00" +  val + "\n") # 2 zeros
     self.key = self.key + 1
    elif len(str(self.key)) == switch.case[7]:
     val = str(self.key)
     file.write("0" +  val + "\n") # 1 zeros
     self.key = self.key + 1
    else:
     val = str(self.key)
     file.write(val + "\n") # 0 zeros
     self.key = self.key + 1

rslt = PSK(0)
rslt.txtpwd()
size_bit0 = os.path.getsize(rslt.path) * 8
size_bit1 = str(size_bit0)
size0 = os.path.getsize(rslt.path) / 1024 # Kilobyte
size1 = size0 / 1024
size1 = int(size1)
print(f"""


           Done!
           File name & path: {os.path.abspath(rslt.path)}
           Size: {size1} MB ({size_bit1} Bit)
           Size in Byte: {os.path.getsize(rslt.path)}

""")

