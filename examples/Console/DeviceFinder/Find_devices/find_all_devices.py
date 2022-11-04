'''
Find_devices - find_all_devices.py

This example demonstrates how to find all available USB and ethernet devices.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.DeviceFinder()

    ## Connect to network device
    try:
        dev.connect()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform USB device information
    print("Find all USB devices....")
    try:
        dev_list = dev.Bcst_enumerateUSBDevices()
        for device in dev_list:
            print(device)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform network device information
    print("Find all network devices....")
    try:
        dev_list = await dev.Bcst_enumerateNetworkDevices_async()
        for device in dev_list:
            print(device)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())