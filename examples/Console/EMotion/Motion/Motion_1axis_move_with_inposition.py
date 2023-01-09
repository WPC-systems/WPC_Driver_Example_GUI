'''
Motion - Motion_1axis_move_with_inposition.py
 
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
        active_high = 1
        stop_deceleration = 0 

        err = await dev.Motion_open_async(port)
        print("open_async:", err)

        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, dir_cw, dir_cw, active_low)
        print("cfgAxis_async:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis, int(True), int(True), active_high)
        print("cfgLimit_async:", err)

        err = await dev.Motion_cfgInposi_async(port, axis, int(False), active_low)
        print("cfgInposi_async:", err)
            
        err = dev.Motion_cfgAxisMove_async(port, axis, relative_position, 5000)
        print("cfgAxisMove_async:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis)
        print("rstEncoderPosi_async:", err)

        err = await dev.Motion_enableServoOn_async(port, axis, int(True))
        print("enableServoOn_async:", err)

        err = await dev.Motion_startSingleAxisMove_async(port, axis)
        print("startSingleAxisMove_async:", err)

        move_status = 0; 
        while move_status == 0:
            move_status = await dev.Motion_getMoveStatus_async(port, axis)
            print("getMoveStatus:", move_status) 
            
        err = await dev.Motion_stop_async(port, axis, stop_deceleration)
        print("stop_async:", err)

        err = await dev.Motion_enableServoOn_async(port, axis, int(False))
        print("enableServoOn_async:", err)
        
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