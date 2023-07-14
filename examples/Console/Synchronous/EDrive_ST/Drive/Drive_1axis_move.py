'''
Drive - Drive_1axis_move.py with synchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EDrive_ST()

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
        target_position = 10000
        relative_position_mode = 1
        stop_decel = 0
        timeout = 3  ## second

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        en_forward = 0
        en_reverse = 0
        orginal_direction = 0

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## EDrive-ST open
        err = dev.Drive_open(port, timeout=timeout)
        print(f"Drive_open: {err}")

        ## EDrive-ST configure
        err = dev.Drive_cfgAxisMove(port, relative_position_mode, target_position, timeout=timeout)
        print(f"Drive_cfgAxisMove: {err}")

        err = dev.Drive_cfgAxisDirection(port, orginal_direction, timeout=timeout)
        print(f"Drive_cfgAxisDirection: {err}")

        err = dev.Drive_cfgEncoderDirection(port, orginal_direction, timeout=timeout)
        print(f"Drive_cfgEncoderDirection: {err}")

        err = dev.Drive_cfgLimit(port, en_forward, en_reverse, active_low, timeout=timeout)
        print(f"Drive_cfgLimit: {err}")

        ## EDrive-ST reset
        err = dev.Drive_rstEncoderPosi(port, timeout=timeout)
        print(f"EDST_reset: {err}")

        ## EDrive-ST Servo on
        err = dev.Drive_enableServoOn(port, timeout=timeout)
        print(f"Drive_enableServoOn: {err}")

        ## EDrive-ST start
        err = dev.Drive_start(port, timeout=timeout)
        print(f"Drive_start: {err}")

        move_status = 0
        while move_status == 0:
            move_status = dev.Drive_getMoveStatus(port, timeout=timeout)
            posi = dev.Drive_readEncoderPosition(port, timeout=timeout)
            print(f"encoder_posi: {posi[0]}, logical_posi: {posi[1]}")

        ## EDrive-ST Stop
        err = dev.Drive_stop(port, stop_decel, timeout=timeout)
        print(f"Drive_stop: {err}")

        ## EDrive-ST Servo off
        err = dev.Drive_enableServoOff(port, timeout=timeout)
        print(f"Drive_enableServoOff: {err}")

        ## EDrive-ST close
        err = dev.Drive_close(port, timeout=timeout)
        print(f"Drive_close: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()