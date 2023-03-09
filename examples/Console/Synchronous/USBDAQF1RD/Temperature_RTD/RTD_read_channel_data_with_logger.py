'''
Temperature_RTD - RTD_read_channel_data_with_logger.py with synchronous mode.

This example demonstrates how to read RTD data in two channels and save data into csv file from USBDAQF1RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data and save them.
Last, close thermal port.

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

    ## Create datalogger handle
    dev_logger = pywpc.DataLogger()

    ## Open file with WPC_test.csv
    dev_logger.Logger_openFile("WPC_test.csv")

    ## Write header into CSV file
    dev_logger.Logger_writeHeader(["RTD CH0","RTD CH1"])

    ## Create device handle
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 1 ## Depend on your device
        ch0 = 0
        ch1 = 1
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open RTD
        err = dev.Thermal_open(port, timeout)
        print(f"Thermal_open in port{port}: {err}")

        ## Wait for at least 100 ms
        time.sleep(0.1) ## delay [s]

        ## Set RTD port and read RTD in channel 0
        data = dev.Thermal_readSensor(port, ch0, timeout)
        print(f"Read sensor in channel {ch0} in port{port}: {data}°C")

        ## Set RTD port and read RTD in channel 1
        data = dev.Thermal_readSensor(port, ch1, timeout)
        print(f"Read sensor in channel {ch1} in port{port}: {data}°C")

        ## Write data into CSV file
        dev_logger.Logger_writeList([data0, data1])

        ## Close RTD
        err = dev.Thermal_close(port, timeout)
        print(f"Thermal_close in port{port}: {err}")

        ## Close File
        dev_logger.Logger_closeFile()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()