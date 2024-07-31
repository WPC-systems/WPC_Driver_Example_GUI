
'''
SNTP - SNTP configure.py with synchronous mode.

This example demonstrates how to configure SNTP from EthanT.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc
import time

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanT()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        ip_addr = "255.255.255.255" ## Automatic search
        period = 5 ## second
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Set SNTP server IP
        err = dev.SNTP_setServerIP(ip_addr, timeout)
        print(f"SNTP_setServerIP, status: {err}")

        ## Set SNTP period
        err = dev.SNTP_setPeriod(period, timeout)
        print(f"SNTP_setPeriod, status: {err}")

        ## Sync now
        err = dev.SNTP_syncNow(timeout)
        print(f"SNTP_syncNow, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()