import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to network device
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
        port = 2
        baudrate = 9600 
        data_bit_mode = 0  ## 0 : 8-bit data, 1 : 9-bit data.
        parity_mode = 0    ## 0 : None, 2 : Even parity, 3 : Odd parity.
        stop_bit_mode = 0  ## 0 : 1 bit, 1 : 0.5 bits, 2 : 2 bits, 3 : 1.5 bits  
       
        ## Open port 2
        status = await dev.UART_open(port) 
        if status == 0: print("UART_open: OK")

        ## Set baudrate to 9600
        status = await dev.UART_setBaudRate(port, baudrate)
        if status == 0: print("UART_setBaudRate: OK")
 
        ## Set data bit to 8-bit data
        status = await dev.UART_setDataBit(port, data_bit_mode)
        if status == 0: print("UART_setDataBit: OK")
        
        ## Set parity to None
        status = await dev.UART_setParity(port, parity_mode)
        if status == 0: print("UART_setParity: OK")

        ## Set stop bit to 8-bit data
        status = await dev.UART_setNumStopBit(port, stop_bit_mode)
        if status == 0: print("UART_setNumStopBit: OK")

        ## Sleep
        await asyncio.sleep(10) ## delay(second)
        
        ## Read 20 bytes
        data = await dev.UART_read(port, 20) 
        print("data: ", data)

        ## Close port 2
        status = await dev.UART_close(port) 
        if status == 0: print("UART_close: OK")

    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())
