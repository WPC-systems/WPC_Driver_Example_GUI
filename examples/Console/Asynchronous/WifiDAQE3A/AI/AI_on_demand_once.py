'''
AI - AI_on_demand_once.py with asynchronous mode.

This example demonstrates how to get AI data in on demand mode.
Also, it gets AI data in once with 8 channels from WifiDAQE3A.

First, it shows how to open AI port.
Second, read AI ondemand data.
Last, close AI port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        mode = 0

        ## Open port
        err = await dev.AI_open_async(port)
        print("AI_open_async:", err)

        ## Set AI port and acquisition mode to on demand mode (0)
        err = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async:", err)

        ## Set AI port and data acquisition
        data =  await dev.AI_readOnDemand_async(port)
        print("data :" + str(data))

        ## Close port
        err = await dev.AI_close_async(port)
        print("AI_close_async:", err)
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