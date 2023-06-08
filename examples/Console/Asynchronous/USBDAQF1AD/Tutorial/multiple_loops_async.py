'''
Tutorial - multiple_loops_async.py with asynchronous mode.

This example project demonstrates how to use two async thread to get RTC & print string from USBDAQF1AD.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def readRTC_loop(handle, delay=1):
    while True:
        rtc = await handle.Sys_getRTC_async()
        print(f"RTC Time: {rtc}")
        await asyncio.sleep(delay)  ## delay(second)

async def printString_loop(handle, delay=1):
    while True:
        print("WPC Systems Ltd")
        await asyncio.sleep(delay)  # delay(second)

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        await asyncio.gather(readRTC_loop(dev, delay=1), printString_loop(dev, delay=2)) ## delay (second)
    except Exception as err:
        pywpc.printGenericError(err)

    ## This part never execute because the async thread.

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))

if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder