'''
AIO - AIO_all_channels_loopback.py

This example demonstrates how to write AIO loopback in all channels from USBDAQF1AOD.
Use AO pins to send signals and use AI pins to receive signals on single device also called "loopback".

First, it shows how to open AO and AI in port.
Second, write all digital signals to AO and read AI ondemand data.
Last, close AO and AI in port.

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
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0

        ## Open AI
        err = dev.AI_open(port)
        print("AI_open:", err)

        ## Open AO
        err = dev.AO_open(port)
        print("AO_open:", err)

        ## Set AI port and data acquisition
        data = dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Set AO port and write data simultaneously
        err = dev.AO_writeAllChannels(port, [0,1,2,3,4,5,4,3])
        print("AO_writeAllChannels:", err)

        ## Sleep
        time.sleep(1) ## delay(second) 

        ## Set AI port and data acquisition
        data = dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Close AI
        err = dev.AI_close(port)
        print("AI_close:", err)

        ## Close AO
        err = dev.AO_close(port)
        print("AO_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()