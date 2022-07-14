import sys 
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, timeout = 1, num_of_samples = 600, delay = 0.005):
    t = 0
    while t < timeout:
        ## data acquisition
        data = await handle.AI_readStreaming(num_of_samples, delay)
        if data is not None:
            print(data)
            print("Get data points: " + str(len(data)))
        t += delay

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

    ## Perform data acquisition
    try:
        await dev.AI_setMode(1) ## Set acquisition mode to N-samples mode (1)
        await dev.AI_setSamplingRate(5000) ## Set sampling rate to 5k (Hz)
        await dev.AI_setNumSamples(3000) ## Set # of samples to 3000 (pts)
        await dev.AI_start() ## Start acquisition
        await loop_func(dev, 1, 600, 0.005) ## Start async thread
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
