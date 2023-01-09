'''
Motion - Motion_save_configuration_file.py
 
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
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        axis = 0
        two_pulse_mode = 1
        relative_position = 1
        dir_cw = 0
        active_low = 0

        err = await dev.Motion_open_async(port)
        print("open_async:", err)
 
        err = await dev.Motion_opencfgFile_async('Emotion.ini')
        print("opencfgFile_async:", err)
 
        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, dir_cw, dir_cw, active_low)
        print("cfgAxis_async:", err)

        err = await dev.Motion_cfgAxisMove_async(port, axis, relative_position, 5000)
        print("cfgAxisMove_async:", err)

        err = await dev.Motion_saveCfgFile_async()
        print("saveCfgFile_async:", err)

        err = await dev.Motion_close_async(port)
        print("close_async:", err) 
         
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return

if __name__ == '__main__':
    asyncio.run(main())