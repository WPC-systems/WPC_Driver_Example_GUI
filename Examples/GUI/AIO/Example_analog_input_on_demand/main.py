##  main.py
##  Example_analog_input_on_demand
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import sys
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_AI_on_demand import Ui_MainWindow 

## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        ## Material path
        self.trademark_path = os.getcwd() + "\Material\WPC_trademark.jpg" 
        self.blue_led_path = os.getcwd() + "\Material\WPC_Led_blue.png"
        self.red_led_path = os.getcwd() + "\Material\WPC_Led_red.png"
        self.green_led_path = os.getcwd() + "\Material\WPC_Led_green.png"

        ## Set trademark path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))

        ## Get Python driver version
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

        ## Wifi DAQ AI port
        self.AI_port = 1 

        ## Connection flag
        self.connect_flag = 0

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.btn_onDemand.clicked.connect(self.onDemandEvent)

    def closeEvent(self, event):
        ## Disconnect network device
        dev.disconnect()
        
        ## Release device handle
        dev.close()
 
    @asyncSlot()      
    async def onDemandEvent(self):  
        ## Set AI port to 1 and data acquisition
        data_list =  await dev.AI_readOnDemand(self.AI_port)
        for i in range(8):
            obj_lineEdit= getattr(self.ui, 'lineEdit_AI%d' %i)
            obj_lineEdit.setText(str(data_list[i]))

    @asyncSlot()      
    async def connectEvent(self): 
        # Get ip from UI
        self.ip = self.ui.lineEdit_IP.text()
        try: 
            ## Connect to network device
            dev.connect(self.ip)

            ## Open AI port
            await dev.AI_open(self.AI_port)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))

            ## Change connection flag
            self.connect_flag = 1
        except pywpc.Error as err: 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## close AI port
        await dev.AI_close(self.AI_port)

        ## Disconnect network device
        dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
        
        ## Change connection flag
        self.connect_flag = 0

def main(): 
    app = QtWidgets.QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    with loop: 
        loop.run_forever()

if __name__ == "__main__":
    ## Create device handle
    dev = pywpc.WifiDAQE3A()
    main()