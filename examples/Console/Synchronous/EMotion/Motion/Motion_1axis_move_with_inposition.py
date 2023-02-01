'''
Motion - Motion_1axis_move_with_inposition.py
 
For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import time

## WPC

from wpcsys import pywpc

def main():
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
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        axis = 0
        two_pulse_mode = 1
        rel_posi_mode = 1
        stop_decel = 0
        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0
        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1
        inposi_enable_false = 0
  
        ## Motion open
        err = dev.Motion_open(port)
        print("open_async:", err)

        ## Motion configure
        err = dev.Motion_cfgAxis(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print("Motion_cfgAxis:", err)
            
        err = dev.Motion_cfgLimit(port, axis, forward_enable_true, reverse_enable_true, active_high)
        print("Motion_cfgLimit:", err)

        err = dev.Motion_cfgInposi(port, axis, inposi_enable_false, active_low)
        print("Motion_cfgInposi:", err)
            
        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_position = 5000)
        print("Motion_cfgAxisMove:", err)

        err = dev.Motion_rstEncoderPosi(port, axis)
        print("Motion_rstEncoderPosi:", err)

        err = dev.Motion_enableServoOn(port, axis, int(True))
        print("Motion_enableServoOn:", err)

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis)
        print("Motion_startSingleAxisMove:", err)

        move_status = 0; 
        while move_status == 0:
            move_status = dev.Motion_getMoveStatus(port, axis)
            print("Motion_getMoveStatus:", move_status) 

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel)
        print("Motion_stop:", err)

        err = dev.Motion_enableServoOn(port, axis, int(False))
        print("Motion_enableServoOn:", err)

        ## Motion close
        err = dev.Motion_close(port)
        print("Motion_close:", err) 
         
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return
if __name__ == '__main__':
    main()