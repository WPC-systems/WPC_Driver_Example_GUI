'''
Drive - Drive_servo_on.py with synchronous mode.

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
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## EDrive-ST open
        err = dev.Drive_open(port, timeout=timeout)
        print(f"Drive_open: {err}")

        ## EDrive-ST servo on
        err = dev.Drive_enableServoOn(port, timeout=timeout)
        print(f"Drive_enableServoOn: {err}")

        ## Wait for 5 seconds
        time.sleep(5) ## delay [s]

        ## EDrive-ST servo off
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