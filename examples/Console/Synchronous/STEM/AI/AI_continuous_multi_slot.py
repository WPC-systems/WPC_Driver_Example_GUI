
'''
AI - AI_continuous_multi_slot.py.

This example demonstrates the process of obtaining AI data in continuous mode with multi slot from STEM.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
Finally, it concludes by explaining how to close the AI.

Please invoke the function `Sys_setAIOMode_async`and `AI_enableCS_async`.
Example: AI_enableCS_async is {0, 2}
Subsequently, the returned value of AI_readOnDemand_async and AI_readStreaming_async will be displayed as follows.
data:
          CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7
          |                                     |                                      |
          |---------------- CS0-----------------|---------------- CS2------------------|
[sample0]
[sample1]
   .
   .
   .
[sampleN]

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.STEM()

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
        slot_list = [1, 2] ## Connect AIO module to slot
        chip_select = [0, 1]
        mode = 2 ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 200
        read_points = 200
        read_delay = 2 ## second
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        for slot in slot_list:
            ## Get slot mode
            slot_mode = dev.Sys_getMode(slot, timeout)
            print("Slot mode:", slot_mode)

            ## If the slot mode is not set to "AIO", set the slot mode to "AIO"
            if slot_mode != "AIO":
                err = dev.Sys_setAIOMode(slot, timeout)
                print(f"Sys_setAIOMod in slot {slot}: {err}")

            ## Get slot mode
            slot_mode = dev.Sys_getMode(slot, timeout)
            print("Slot mode:", slot_mode)

            ## Open AI
            err = dev.AI_open(slot, timeout)
            print(f"AI_open in slot {slot}: {err}")

            ## Enable CS
            err = dev.AI_enableCS(slot, chip_select, timeout)
            print(f"AI_enableCS in slot {slot}: {err}")

            ## Set AI acquisition mode to continuous mode (2)
            err = dev.AI_setMode(slot, mode, timeout)
            print(f"AI_setMode {mode} in slot {slot}: {err}")

            ## Set AI sampling rate
            err = dev.AI_setSamplingRate(slot, sampling_rate, timeout)
            print(f"AI_setSamplingRate {sampling_rate} in slot {slot}: {err}")

            ## Start AI
            err = dev.AI_start(slot, timeout)
            print(f"AI_start in slot {slot}: {err}")

        data_len = 1
        while data_len > 0:
            for slot in slot_list:
                ## Read data acquisition
                ai_2Dlist = dev.AI_readStreaming(slot, read_points, read_delay)
                print(f"Slot{slot}: data len {len(ai_2Dlist)}" )

                ## Update data len and counter
                data_len = len(ai_2Dlist)

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        for slot in slot_list:
            ## Stop AI
            err = dev.AI_stop(slot, timeout)
            print(f"AI_stop in slot {slot}: {err}")

            ## Close AI
            err = dev.AI_close(slot, timeout)
            print(f"AI_close in slot {slot}: {err}")

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()
