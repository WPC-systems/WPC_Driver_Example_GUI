'''
Temperature-RTD - example_RTD_read_channel_data.py

This example demonstrates how to read RTD data in two channels from WPC-USB-DAQ-F1-RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data
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
    dev = pywpc.USBDAQF1RD()

    ## Connect to USB device
    try:
        dev.connect('21JA1385')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 1
        channel_0 = 0 
        channel_1 = 1 

        ## Open RTD port1
        status = await dev.Thermal_open(port)
        if status == 0: print("Thermal_open: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set RTD port to 1 and read RTD in channel 0
        data = await dev.Thermal_readSensor(port, channel_0)
        print("Read channel 0 data:", data, "°C")

        ## Set RTD port to 1 and read RTD in channel 1
        data = await dev.Thermal_readSensor(port, channel_1)
        print("Read channel 1 data:", data, "°C")

        ## Close RTD port1
        status = await dev.Thermal_close(port)
        if status == 0: print("Thermal_close: OK")   
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return
    
if __name__ == '__main__':
    asyncio.run(main())