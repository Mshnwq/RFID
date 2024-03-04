import multiprocessing
import platform
import ctypes
from ctypes import *
from copy import deepcopy
import os
import time
import clr
from threading import Thread, Lock
from multiprocessing import Process, Queue
from queue import Empty


absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
if platform.system() == 'Windows':
    clr.AddReference(
        fileDirectory + '\\lib\\RFIDReaderAPI.dll') # load dll object
    import RFIDReaderAPI
    from RFIDReaderAPI import *
    from RFIDReaderAPI.Interface import IAsynchronousMessage
    from RFIDReaderAPI.Models import Tag_Model
    # from RFIDReaderAPI import GpiModel
    # import RFIDReaderAPI.GPI_Model

class MyAsynchronousMessage(IAsynchronousMessage):
    __namespace__ = "MyNameSpace"
    tagsQs = None
    currentQ = None # pointer to a Q
    tagsList = []

    '''Tags Management'''

    def dump_queue(q):
        """
        Empties all pending items in a queue and returns them in a list.
        """
        result = []
        q.put('STOP')

        for i in iter(q.get, 'STOP'):
            result.append(i)
        time.sleep(.1)
        return result
        # q.put(None)
        # return list(iter(lambda : q.get(timeout=0.00001), None))

    @classmethod
    def getTagsList(cls):
        return cls.tagsList

    @classmethod
    def getTagsQ(cls):
        return cls.tagsQs

    @classmethod
    def setTagsQ(cls, tagsQs_dict):
        cls.tagsQs = tagsQs_dict

    @classmethod
    def getCurrentQ(cls):
        print(cls.currentQ)
        return cls.dump_queue(cls.currentQ)

    @classmethod
    def setCurrentQ(cls, ant):
        print(f"seted a Q {ant}")
        cls.currentQ = cls.tagsQs[ant]

    @classmethod
    def transferListToQ(cls):
        for tag in cls.tagsList:
            cls.currentQ.put(tag)

    @classmethod
    def clearTagsList(cls):
        cls.tagsList.clear()

    @classmethod
    def appendTagsList(cls, tag):
        if tag not in cls.tagsList:
            cls.tagsList.append(tag)

    '''Callback Functions'''

    def OutPutTags(self, tag: Tag_Model):
        # print(f"Tag: {tag.EPCData}\n")
        print(f"Tag: {tag.EPC}\n")
        # self.appendTagsList(tag=tag.EPCData)
        self.appendTagsList(tag=tag.EPC)

    def OutPutTagsOver(self):
        # print("No more tags.\n")
        ...

    def WriteDebugMsg(self, msg: str):
        # print(f"Debug: {msg}\n")
        ...

    def WriteLog(self, msg: str):
        print(f"Log: {msg}\n")

    def PortConnecting(self, connID: str):
        print(f"Connecting to {connID}\n")
        
    def PortClosing(self, connID: str):
        print(f"Closing {connID}\n")

    # def GPIControlMsg(self, gpi_model: GPI_Model):
    def GPIControlMsg(self, gpi_model: str):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"GPI Model: {gpi_model}\n")
        print(f"GPI Index: {gpi_model.GpiIndex}\n")
        print(f"GPI State: {gpi_model.gpiState}\n")
        print(f"GPI OR: {gpi_model.StartOrStop}\n")
        print(f"GPI Time: {gpi_model.Utc_Time}\n")


class Controller_Driver():


    def __init__ (self, tcp):
        self.__setup_dll()
        self.__connect(tcp)
        self.readLock = Lock()
        self.selectorLock = Lock()
        # self.__setupProcesses()

    # def __setup_processes(self):



        '''2.1 Connect & Disconnect'''

        # print(self.rfidReader.OpenTcpServer(tcps, "9090", self.log))
        # while True:
            # time.sleep(2)
            # print(self.rfidReader.GetServerStartUp())
        # print(self.rfidReader.CheckConnect(tcp))
        # print(self.rfidReader.CloseTcpServer())
        # print(self.rfidReader.GetServerStartUp())
    


        # print(self.rfidReader.CloseConn(tcp))
        # print(self.rfidReader.CloseAllConnect())
        # from pywinauto.application import Application

        # app = Application().connect(process=pid)
        # current_window = app.top_window()
        # Handle = None

        # driverlist = self.rfidReader.GetUsbHidDeviceList()
        # ConnID = driverlist[0]
        # print(ConnID)
        # Handle = User32API.GetCurrentWindowHandle()
        # pid = win32api.GetCurrentProcessId()
        # print(pid)

        # with pyhandle.ProcessHandle(pid=pid) as process:
            # Handle = process.handle
        # Handle = str(win32api.OpenProcess(0x1F0FFF, False, pid))
        # print(Handle)
        # print(type(Handle))
        # print(win32api.GetHandleInformation(Handle))
        
        # user32 = ctypes.WinDLL('user32')
        # Handle = user32.GetForegroundWindow()
        # print(self.rfidReader.CreateUsbConn(ConnID, Handle, self.log))
        # print(self.rfidReader.CreateUsbConn(ConnID))
        


        # print(self.rfidReader.StartSearchDevice(None))
        # ret = self.rfidReader.StopSearchDevice() # says returns integer

        # ret = self.rfidReader.SetTimeOut(2000)

        # print(self.rfidReader._ReaderConfig.GetSN(tcp))
        # print(self.rfidReader._ReaderConfig.GetReaderMacParam(tcp))
        # print("TEMP: " + self.rfidReader._RFIDConfig.GetRFIDTemperature(tcp))
        # '''2.2 Device Config'''
        # print(self.rfidReader._ReaderConfig.SetReaderNetworkPortParam
        # (tcp, "192.168.8.80", "255.255.255.0", "192.168.8.1"))
        # print(self.rfidReader._ReaderConfig.GetReaderNetworkPortParam(tcp))
        # print(self.rfidReader._RFIDConfig.Stop(tcp))

        
        # '''not work'''
        # print(self.rfidReader._ReaderConfig.SetReaderUTC(tcp, "2023.01.12 05:15:02"))
        # print(self.rfidReader._ReaderConfig.GetReaderUTC(tcp))
        # print(self.rfidReader._ReaderConfig.GetReaderSerialPortParam(tcp))
        # print(self.rfidReader._ReaderConfig.SetReaderMacParam(tcp, "dddddd"))
        # print(self.rfidReader._ReaderConfig.GetReaderInformation(tcp))
        # print(self.rfidReader._ReaderConfig.GetReaderBaseBandSoftVersion(tcp))
        # print(self.rfidReader._ReaderConfig.GetDataOutPutFormat(tcp))
        # print(self.rfidReader._ReaderConfig.SetDataOutPutFormat(tcp))
        # print(self.rfidReader._ReaderConfig.ReSetReader(tcp)) # DONT

        ###################################
        # print(self.rfidReader._ReaderConfig.SetCustomCode(tcp, "dddddddd"))
        # print(self.rfidReader._ReaderConfig.GetCustomCode(tcp))
        # print(self.rfidReader._RFIDConfig.SetBuzzerControl(tcp, True, True))
        # print(self.rfidReader._RFIDConfig.SetBuzzerSwitch(tcp, "1"))
        ###################################

        '''2.3 RFID Config'''
        # from System.Collections.Generic import Dictionary
        # from System import Int32
        # d = Dictionary[Int32, Int32]()
        # d[2] = 20
        # print(self.rfidReader._RFIDConfig.SetANTPowerParam(tcp, d))
        # print(self.rfidReader._RFIDConfig.GetANTPowerParam(tcp)[1])

        # print(self.rfidReader._RFIDConfig.SetTagUpdateParam(tcp, 0, 0))
        # print(self.rfidReader._RFIDConfig.GetTagUpdateParam(tcp))

        # freq = self.rfidReader._RFIDConfig.GetReaderRF(tcp)
        # print(freq)
        # freq = self.rfidReader._RFIDConfig.GetReaderWorkFrequency(tcp)
        # print(freq)

        # sleep = self.rfidReader._RFIDConfig.SetReaderAutoSleepParam(tcp, False, '500')
        # print(sleep)
        # isSleep = self.rfidReader._RFIDConfig.GetReaderAutoSleepParam(tcp)
        # print(isSleep)

        # print(self.rfidReader._ReaderConfig.GetReaderSelfCheck(tcp))

        '''idk'''
        # ants = self.rfidReader._RFIDConfig.SetReaderANT(tcp)
        # print(ants)
        # print(self.rfidReader._RFIDConfig.GetReaderANT(tcp))
        # print(self.rfidReader._RFIDConfig.GetReaderANT2(tcp))
        


        '''2.4 GPIO'''

        '''2.5 Tag Ops'''

        # self.readTag(2, 0)

    def setupProcesses(self, antennas, timeout=2):
        '''
        Driver Constructor
        Args:
            timeout (int): queue timeout
        '''
        self.timeout = timeout # timeout of queue
        self.Q_dict = dict()
        self.Prc_dict = dict()
        self.Flag_dict = dict()
        # print(antennas)
        for ant, val in enumerate(antennas):
            if val == 1:
                self.Q_dict[str(ant+1)] = Queue()
                self.Flag_dict[str(ant+1)] = multiprocessing.Value('i', 0)
        # Queue object for read tags
        self.log.setTagsQ(self.Q_dict)

    def createProcess(self, ant):
        # print(self.Q_dict)
        # print(self.Flag_dict)
        # print(self.Prc_dict)
        # self.Prc_dict[ant] = Process(target=self.__reading_job, args=(self.Q_dict[ant],ant,)) # a process for the job
        self.Prc_dict[ant] = Thread(target=self.__reading_job, args=(ant, self.getAntID(ant), self.readLock,)) # a process for the job

    #### PROCESS CONTROL METHODS ####
    def run(self, ant):
        '''start the job'''
        self.Flag_dict[ant].value = 0
        self.Prc_dict[ant].start()

    def stop(self, ant):
        '''stop the job'''
        self.Flag_dict[ant].value = 1
        self.Prc_dict[ant].join()
        self.Prc_dict[ant].close()

    def clearQ(self, ant):
        '''Clear Job Queue'''
        while not self.Q_dict[ant].empty():
            # print(f"cleared: {self.Q_dict[ant].get()}")
            self.Q_dict[ant].get()

    def __connect(self, tcp):
        self.tcp = tcp
        self.log = MyAsynchronousMessage() # TODO
        print("##################")
        print(self.rfidReader.CreateTcpConn(tcp, self.log))
        print("##################")
        print(self.rfidReader.CheckConnect(tcp))

    def readEPC(self, antNo=1, readChoice=0):
        '''
        Static int GetEPC(string ConnID, eAntennaNo antNum, eReadType readType,
        eMatchCode matchType = eMatchCode.None, string matchCode = "", int
        matchWordStartIndex = -1, string accessPassword = "")
        // only read EPC
        // ConnID: connection identifier
        // antNum: Antenna number enumeration.
        Appoint Antenna 1 and 2 working at same time; e.g.: eAntennaNo._1|eAntennaNo._2
        // ReadType: read type enumeration, Single or Inventory (one-time or cyclically reading)
        '''
        match (antNo):
            case 1:
                antNum = self.eAntennaNo._1
            case 2:
                antNum = self.eAntennaNo._2
            case 3:
                antNum = self.eAntennaNo._3
            case 4:
                antNum = self.eAntennaNo._4
            case __:
                antNum = self.eAntennaNo._1
        
        if readChoice == 0:
            readType = self.eReadType.Single
        elif readChoice == 1:
            readType = self.eReadType.Inventory
        else:
            readType = self.eReadType.Single
        
        # print(antNum)
        # print(readType)
        print('--------------')
        print(self.rfidReader._Tag6C.GetEPC(self.tcp, antNum, readType))
        # print(self.rfidReader._Tag6C.GetEPC_EpcData(self.tcp, antNum, readType))
        # # print(rt)
        # time.sleep()
        # print("$$$$$")
        time.sleep(0.1)
        # print(self.rfidReader._Tag6C.Stop(self.tcp))
        # print('--------------')
        # print(self.rfidReader.CloseConn(tcp))
        # return None
        ...

    def __reading_job(self, ant, antID, lock):
        '''
        Process of reeading Tags and Enqueuing to Queue
        Args: 
            q (Queue): Queue being enqueued
        '''

        print(f"PID#{ant} Entering the Reading Loop, Flag = {self.Flag_dict[ant].value}")
        while self.Flag_dict[ant].value == 0:
            # print("getting lock")
            lock.acquire()
            # print(f"PID#{ant}: and acquired lock")
            # tagRead = self.readEPC(ant, 0)
            # self.readEPC(ant, 0)
            self.rfidReader._Tag6C.GetEPC(self.tcp, 
                antID, self.eReadType.Single)
            # self.rfidReader._Tag6C.GetEPC_EpcData(self.tcp, 
                # antID, self.eReadType.Single, )
            tagsRead = deepcopy(self.log.getTagsList())
            print(f"content of tags read before clear {tagsRead}")
            self.log.clearTagsList()
            print(f"content of tags read after clear {tagsRead}")
            time.sleep(0.1)
            lock.release()
            # print(f"PID#{ant}: released lock\n\n")
            for tagRead in tagsRead:
                print("what")
                print(tagRead)
                if tagRead != None:
                    print("PUTTING")
                    # tagbytes = hex(int('0x'+tagRead, 16))
                    tagbytes = bytes.fromhex(tagRead)
                    self.Q_dict[ant].put(tagbytes)
            time.sleep(0.1)
            # print("AAAAA")
        print(f"PID#{ant} Exiting the Reading Loop, Flag = {self.Flag_dict[ant].value}")
        '''So Stupid'''
        # self.log.setCurrentQ(ant)
        # time.sleep(0.2)
        # print(f'\ncurrent Q before transf {self.log.getCurrentQ()}')
        # print(f' tags before {self.log.getTagsList()}\n\n')
        # self.log.transferListToQ()
        # time.sleep(0.2)
        # print(f'current Q after transf {self.log.getCurrentQ()}')
        # time.sleep(0.2)
        # print(f' tags after clear {self.log.getTagsList()}')
        # print(f'Tags Q {self.log.getTagsQ()}')

    def readTag(self, ant):
        '''Dequeue a Tag Read from Queue'''
        try:
            tagValue = self.Q_dict[ant].get(block=True, timeout=self.timeout)
            # print("DEQU")
            # print(tagValue)
            # print("DEQU")
            # return tagValue
        except Empty: # TODO why?
            # print('empty')
            tagValue = None

        if tagValue and self.checkSum(tagValue) == 1: # TODO
        # print("RETURNING")
            return tagValue
        else: 
            return None

    def getAntID(self, antNo):
        match (int(antNo)):
            case 1:
                return self.eAntennaNo._1
            case 2:
                return self.eAntennaNo._2
            case 3:
                return self.eAntennaNo._3
            case 4:
                return self.eAntennaNo._4
            case __:
                return self.eAntennaNo._1

    def checkAntPwr(self, antNum=1):
        print(self.rfidReader._RFIDConfig.GetANTPowerParam(self.tcp)[antNum])

    def checkConn(self):
        return self.rfidReader.CheckConnect(self.tcp)

    def checkTemp(self):
        return self.rfidReader._RFIDConfig.GetRFIDTemperature(self.tcp)

    def close(self):
        return self.rfidReader.CloseConn(self.tcp)

    def reconnect(self):
        return self.rfidReader.CreateTcpConn(self.tcp, self.log)

    def setSelector(self, antNum):
        # TODO
        self.rfidReader._ReaderConfig.SetReaderWG(
            tcp, self.eWiegandSwitch.Open, self.eWiegandFormat.Wiegand34,
            self.eWiegandDetails.end_of_the_EPC_data, antNum);
        ...

    def setGPOState(self, antNum, state):
        from System.Collections.Generic import Dictionary
        gpoList = Dictionary[self.eGPO, self.eGPOSate]()
        # print(state)
        for i, val in enumerate(state.value):
            if val == 0:
                gpoList[getattr(self.eGPO, f"_{i + 1}")] = self.eGPOSate.Low
            elif val == 1:
                gpoList[getattr(self.eGPO, f"_{i + 1}")] = self.eGPOSate.High
        
        self.selectorLock.acquire()
        # ENTER CS
        # self.setSelector(antNum)
        result = self.rfidReader._ReaderConfig.SetReaderGPOState(self.tcp, gpoList)
        # EXIT CS
        self.selectorLock.release()
        # for gpo in gpoList:
        #     print(gpo)
        #     print(type(gpo))
        return result
        ...

    def getGPIParam(self, antNum):
        '''get GPI Setting Trigger Start'''
        gpiNum = getattr(self.eGPO, f"_{antNum}")
        print(gpiNum)
        print(type(gpiNum))
        return self.rfidReader._ReaderConfig.GetReaderGPIParam(self.tcp, gpiNum)
        # return self.rfidReader._ReaderConfig.GetReaderGPIState(self.tcp)
        ...

    ##### HELPER METHODS #####
    def checkSum(self, Data):
        '''sums all bytes previous of index 11 of arr'''
        desiredCheckSum = Data[11]
        checkSum = int(0)
        for i in range(0, 11):
            checkSum += Data[i]
        checkSumValByte = checkSum.to_bytes(2,'big')
        checkSumVal = checkSumValByte[1]

        if checkSumVal == desiredCheckSum: 
            return 1
        else:
            return 0

    def getAntennaImpedence(self, antNum):
        '''
        ConnID: connection identification, antNo: Antenna number enumeration
        Remark If the difference is greater than 25, the antenna is connected, otherwise, the antenna is not
        connecte
        '''
        return self.rfidReader._RFIDConfig.GetAntennaStandingWaveRatio(self.tcp, antNum)

    def getProperties(self):
        '''Minimum output power | maximum output power | number of antennas | band list | list of RFID protocols'''
        return self.rfidReader._RFIDConfig.GetReaderProperty(self.tcp)

    def __setup_dll(self):
        absolutepath = os.path.abspath(__file__)
        fileDirectory = os.path.dirname(absolutepath)
        if platform.system() == 'Windows':
            clr.AddReference(
                fileDirectory + '\\lib\\RFIDReaderAPI.dll') # load dll object
            import RFIDReaderAPI
            self.rfidReader = RFIDReaderAPI.RFIDReader()
            self.rfid_Option = RFIDReaderAPI.RFID_Option()
            self.param_Option = RFIDReaderAPI.Param_Option()
            self.test_Option = RFIDReaderAPI.Test_Option()

            self.interface = RFIDReaderAPI.Interface
            self.myConn = RFIDReaderAPI.MyConnect
            self.myHelp = RFIDReaderAPI.MyHelper

            self.eAntennaNo = RFIDReaderAPI.eAntennaNo
            self.eGPI = RFIDReaderAPI.eGPI
            self.eGPO = RFIDReaderAPI.eGPO
            self.eGPOSate = RFIDReaderAPI.eGPOState
            self.eReadType = RFIDReaderAPI.eReadType
            self.eMatchCode = RFIDReaderAPI.eMatchCode
            self.eWiegandSwitch = RFIDReaderAPI.eWiegandSwitch
            self.eWiegandFormat = RFIDReaderAPI.eWiegandFormat
            self.eWiegandDetails = RFIDReaderAPI.eWiegandDetails

            self.models = RFIDReaderAPI.Models
            self.tag_model = self.models.Tag_Model
            # self.tag_model = self.models.
            self.device_model = self.models.Device_Model

        elif platform.system() == 'Linux':
            # TODO someday with MONO
            self.Objdll = ctypes.windll.LoadLibrary(
                # Path 64 bit
                self.fileDirectory + '/lib/RFIDReaderAPI.so') # load dll object
        else:
            exit(f"Device does not support {platform.system()} OS")


if __name__ == "__main__":
    # simple test script
    print(__name__)
    tcp = "192.168.8.116:9090"
    gate_Driver = Controller_Driver(tcp)
    # print(gate_Driver.checkTemp())
    # print(gate_Driver.checkAntPwr(1))
    # print(gate_Driver.getAntennaImpedence(1))
    # print("Lllllllllllllllll")
    
    # print(gate_Driver.setGPOState(1, [1, 0, 1, 0]))
    # print(gate_Driver.getGPIParam(1))
    # print(gate_Driver.readEPC(2, 1))
    # print(gate_Driver.log.getTagsList())