'''
DIO - example_DIO_loopback_port.py

Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
Last, close DO and DI in port.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio
import sys
 
## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to USB device
    try:
        dev.connect('21JA1044')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port_DO = 0
        port_DI = 1

        ## Open all pins in port 0 with digital output 
        status = await dev.DO_openPort(port_DO)
        if status == 0: print("DO_openPort in port 0: OK")

        ## Set pin0, pin1 and pin2 to high, others to low
        status = await dev.DO_writePort(port_DO, [0,0,0,0,0,1,1,1])
        if status == 0: print("DO_writePort: OK")

        ## Open all pins in port 1 with digital input
        status = await dev.DI_openPort(port_DI)
        if status == 0: print("DI_openPort in port 1: OK")

        ## Read all pins state in port 1
        state_list = await dev.DI_readPort(port_DI)
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3)
        
        ## Close all pins in port 0 with digital output
        status = await dev.DO_closePort(port_DO)
        if status == 0: print("DO_closePort in port 0: OK")
        
        ## Close all pins in port 1 with digital input
        status = await dev.DI_closePort(port_DI)
        if status == 0: print("DI_closePort in port 1: OK")
    except Exception as err:
        pywpc.printGenericError(err)
        
    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())