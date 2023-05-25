'''
AI - AI_on_demand_in_loop.py with asynchronous mode.

This example demonstrates how to get AI data in on demand mode.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels STEM.

First, it shows how to open AI port and configure AI parameters.
Second, read AI ondemand data.
Last, close AI port.

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

async def loop_func(handle, port, delay=0.05, exit_loop_time=3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## data acquisition
        data = await handle.AI_readOnDemand_async(port)
        if len(data) > 0:
            print(f"data in port {port}: {data}")

        ## Wait
        await asyncio.sleep(delay)  ## delay [s]
        time_cal += delay

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.STEM()

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
        port = 1 ## Depend on your device
        mode = 0
        chip_select = [0, 1]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        
        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode: ", port_mode)

        if port_mode != "AIO":
            ## Set port to AIO mode
            err = await dev.Sys_setPortAIOMode_async(port)
            print(f"Sys_setPortAIOMode_async in port {port}: {err}")

        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode: ", port_mode)

        ## Open port
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}: {err}")

        ## Enable CS
        err = await dev.AI_enableCS_async(port, chip_select)
        print(f"AI_enableCS_async in port {port}: {err}")
        

        ## Set AI port and acquisition mode to on demand mode (0)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}: {err}")

        ## Set loop parameters
        delay = 0.05
        exit_loop_time = 3

        ## Start loop
        await loop_func(dev, port, delay=delay, exit_loop_time=exit_loop_time)

        ## Close port
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}: {err}")
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