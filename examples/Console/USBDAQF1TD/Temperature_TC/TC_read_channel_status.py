'''
Temperature_TC - TC_read_channel_status.py

This example demonstrates how to get status from USBDAQF1TD.

First, it shows how to open thermal port
Second, get status from channel 0 and channel 1
Last, close thermal port.

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
    dev = pywpc.USBDAQF1TD()

    ## Connect to device
    try:
        dev.connect("21JA1239")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 1
        channel_0 = 0
        channel_1 = 1

        ## Open thermo
        status = await dev.Thermal_open_async(port)
        print("Thermal_open_async status: ", status)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port and get status in channel 0
        status = await dev.Thermal_getStatus_async(port, channel_0)
        print("Thermal_getStatus in chaannel 0: ", status)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port and get status in channel 1
        status = await dev.Thermal_getStatus_async(port, channel_1)
        print("Thermal_getStatus in chaannel 1: ", status)

        ## Close thermo
        status = await dev.Thermal_close_async(port)
        print("Thermal_close_async status: ", status)
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