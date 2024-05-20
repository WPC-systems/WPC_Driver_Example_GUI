
'''
RTC_AI - RTC_trigger_AI_N_samples.py with synchronous mode.

This example demonstrates how to use RTC to trigger AI with on demand mode from EthanA.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''
## WPC

from wpcsys import pywpc
import time

def main():
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
        mode = 3 ## RTC On demand, 4 : RTC N-samples, 5 : RTC Continuous
        timeout = 3 ## second
        mode_alarm = 0
        month = 4
        day = 2
        hour = 15
        minute = 8
        second = 50

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port {port}, status: {err}")

        ## Set AI mode
        err = dev.AI_setMode(port, mode, timeout)
        print(f"AI_setMode {mode} in port {port}, status: {err}")

        ## Set RTC
        err = dev.Sys_setRTC(2024, month, day, hour, minute, second-10, timeout)
        print(f"Set RTC to 2024-{month}-{day}, {hour}:{minute}:{second-10}, status: {err}")

        ## Start RTC alarm
        err = dev.Sys_startRTCAlarm(mode_alarm, day, hour, minute, second, timeout)
        print(f"Alarm RTC to 2024-{month}-{day}, {hour}:{minute}:{second}, status: {err}")

        for i in range(15):
            print(f"Get RTC {dev.Sys_getRTC()}")
            time.sleep(1)

        ## Read AI
        ai_list = dev.AI_readOnDemand(port, timeout)
        print(f"Data in port {port}: {ai_list}")

        ## Close AI
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()