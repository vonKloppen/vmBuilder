#!/usr/bin/env python

import sys


def title():
    
    print ('''\033[1;33;40m
VM machine builder script
CopyLeft by Marian
    ''')
    return

def menu_main():
    
    print ('''\033[1;32;40m
    Please make your selection or press any other key to exit:\n
    1. Create default VM
    2. Create custom VM
    3. Set default VM parameters
    4. Set VCenter parameters
    \33[02;37;40m''')
    choice = input ('> ')
    return choice

def menu_1():
    
    from conf.vmDefaults import vmHOSTNAME, vmVLAN, vmNETWORK

    hostname = input ('\033[0;31;40mHostname [%s]:\033[1;36;40m ' % vmHOSTNAME)
    hostname = hostname or vmHOSTNAME
    
    vlan = input ('\033[0;31;40mVLAN [%s]:\033[1;36;40m ' % vmVLAN)
    vlan = vlan or vmVLAN
    
    network = input ('\033[0;31;40mNETWORK {dhcp, static} [%s]:\033[1;36;40m ' % vmNETWORK)
    network = network or vmNETWORK
    
    if network == 'static':
        
        from conf.vmDefaults import vmIP, vmNETMASK, vmGATEWAY, vmNAMESERVERS
        
        ip = input ('\033[0;31;40mIP [%s]:\033[1;36;40m ' % vmIP)
        ip = ip or vmIP
        
        netmask = input ('\033[0;31;40mNetmask [%s]:\033[1;36;40m ' % vmNETMASK)
        netmask = netmask or vmNETMASK
        
        gateway = input ('\033[0;31;40mGATEWAY [%s]:\033[1;36;40m ' % vmGATEWAY)
        gateway = gateway or vmGATEWAY
        
        nameservers = input ('\033[0;31;40mNameservers [%s]:\033[1;36;40m ' % vmNAMESERVERS)
        nameservers = nameservers or vmNAMESERVERS
        
    
    return

def menu_2():
    
    
    return

def menu_3():
    
    
    return

def menu_4():
    
    
    return


title()
choice = menu_main()

if choice == '1':
    
    menu_1()
    
elif choice == '2':
    
    menu_2()
    
elif choice == '3':
    
    menu_3()
    
elif choice == '4':
    
    menu_4()
    
else:
    
    print ('Bye')
    sys.exit
    
    
    
    
    
    
    
