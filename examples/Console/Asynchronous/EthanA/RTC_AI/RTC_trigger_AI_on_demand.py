
'''
RTC_AI - RTC_trigger_AI_on_demand.py with asynchronous mode.

This example demonstrates how to use RTC to trigger AI with on demand mode from EthanA.

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

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanA()

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
        port = 0 ## Depend on your device
        mode = 3 ## 3 : RTC On demand, 4 : RTC N-samples, 5 : RTC Continuous
        mode_alarm = 0
        month = 4
        day = 2
        hour = 15
        minute = 8
        second = 50

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}, status: {err}")

        ## Set AI mode
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}, status: {err}")

        ## Set RTC
        err = await dev.Sys_setRTC_async(2024, month, day, hour, minute, second-10)
        print(f"Set RTC to 2024-{month}-{day}, {hour}:{minute}:{second-10} , status: {err}")

        ## Start RTC alarm after 10 seconds
        err = await dev.Sys_startRTCAlarm_async(mode_alarm, day, hour, minute, second)
        print(f"Alarm RTC to 2024-{month}-{day}, {hour}:{minute}:{second} , status: {err}")

        for i in range(15):
            print(f"Get RTC {await dev.Sys_getRTC_async()}")
            await asyncio.sleep(1) ## delay [s]

        ## Read AI
        ai_list = await dev.AI_getData_async(port)
        print(f"Data in port {port}: {ai_list}")

        ## Close AI
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}, status: {err}")
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