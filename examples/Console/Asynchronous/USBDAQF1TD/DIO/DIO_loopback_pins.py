'''
DIO - DIO_loopback_pins.py with asynchronous mode.

This example demonstrates how to write DIO loopback in pins from USBDAQF1TD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in pins.
Second, write DO pin and read DI pin
Last, close DO and DI in pins.

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

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

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

        ## Parameters setting
        port = 0 ## Depend on your device

        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output
        err = await dev.DO_openPins_async(port, [0,1,2,3,4])
        print(f"DO_openPins_async in port{port}: {err}")

        ## Set pin0 and pin1 to high, others to low
        err = await dev.DO_writePins_async(port, [0,1,2,3,4], [1,1,0,0,0])
        print(f"DO_writePins_async in port{port}: {err}")

        ## Open pin5, pin6 and pin7 with digital output
        err = await dev.DI_openPins_async(port, [5,6,7])
        print(f"DI_openPins_async in port{port}: {err}")

        ## Read pin5, pin6 and pin7 state
        state_list = await dev.DI_readPins_async(port, [7,5,6])
        print(state_list)

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output
        err = await dev.DO_closePins_async(port, [0,1,2,3,4])
        print(f"DO_closePins_async in port{port}: {err}")

        ## Close pin5, pin6 and pin7 with digital input
        err = await dev.DI_closePins_async(port, [5,6,7])
        print(f"DI_closePins_async in port{port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

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