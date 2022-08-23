##  example_TC_read_channel_status.py
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import sys

## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

    ## Connect to USB device
    try:
        dev.connect('21JA1239')
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
        
        ## Open thermo port1
        status = await dev.Thermal_open(port)
        if status == 0: print("Thermal_open: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port to 1 and get status in channel 0 
        status = await dev.Thermal_getStatus(port, channel_0)
        if status == 0: print("Thermal_getStatus in chaannel 0: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port to 1 and get status in channel 1
        status = await dev.Thermal_getStatus(port, channel_1)
        if status == 0: print("Thermal_getStatus in chaannel 1: OK")

        ## Close thermo port1
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