##  example_multiple_loops_thread.py
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import threading
import time

## WPC
from wpcsys import pywpc

async def getRSSI(handle, delay = 1):
    data = await handle.Wifi_readRSSI_async()
    print("RSSI: " + str(data) + " dBm")
    await asyncio.sleep(delay)  # delay(second)

async def getBattery(handle, delay = 1):
    data = await handle.Wifi_readBattery_async()
    print("Battery: "+ str(data) + " mV")
    await asyncio.sleep(delay)  # delay(second)

def Battery_thread(handle, delay): 
    while True: 
        asyncio.run(getBattery(handle, delay))
        time.sleep(1) 

def RSSI_thread(handle, delay):
    while True: 
        asyncio.run(getRSSI(handle, delay))
        time.sleep(1)

async def main():   
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)
    
    ## Perform two sync thread to query data
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        _threadRSSI = threading.Thread(target = RSSI_thread, args=[dev, 0.5])
        _threadRSSI.start()

        _threadBattery = threading.Thread(target = Battery_thread, args=[dev, 0.5])
        _threadBattery.start()
    except Exception as err:
        pywpc.printGenericError(err) 

    ## This part will execute immediately because the sync thread is running in parallel.
    '''
    # Disconnect network device
    dev.disconnect()
    
    # Release device handle
    dev.close()
    '''

    print("End example code...")
    return

if __name__ == '__main__': 
    asyncio.run(main())
