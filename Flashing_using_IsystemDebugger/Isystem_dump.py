import subprocess
 
 
try:
    from intelhex import IntelHex
except ImportError:
    subprocess.check_call(["pip", "install", "IntelHex"])

 
try:
    import isystem.connect as ic
 
except ImportError:
    subprocess.check_call(["pip", "install", "isystem.connect"])
winidea_id = ''
def test_readMemory():
    connMgr = ic.ConnectionMgr()
    connMgr.connect(ic.CConnectionConfig().instanceId(winidea_id))
    dataCtrl = ic.CDataController(connMgr)
    addCtrl = ic.CAddressController(connMgr)
    START_ADDRESS = 0x11000000
    NUM = 32768
    print(f"Reading {NUM} bytes, starting at address: {hex(START_ADDRESS)}")
    rData = dataCtrl.readMemory(ic.IConnectDebug.fRealTime,
                                0,
                                START_ADDRESS,
                                NUM, 1)
 
    # Create an IntelHex object
    ih = IntelHex()
 
    # Populate the IntelHex object with the read data
    for index, data in enumerate(rData[:NUM]):
        ih[START_ADDRESS + index] = data  
 
    # Save the IntelHex object to a file
    ih.write_hex_file("ITCM.hex")
 
    
    START_ADDRESS = 0x20400000
    NUM = 32768
    print(f"Reading {NUM} bytes, starting at address: {hex(START_ADDRESS)}")
    rData = dataCtrl.readMemory(ic.IConnectDebug.fRealTime,
                                0,
                                START_ADDRESS,
                                NUM, 1)
 
    # Create an IntelHex object
    ih = IntelHex()
 
    # Populate the IntelHex object with the read data
    for index, data in enumerate(rData[:NUM]):
        ih[START_ADDRESS + index] = data  
 
    # Save the IntelHex object to a file
    ih.write_hex_file("SRAM.hex")

    START_ADDRESS = 0x00400000
    NUM = 524288
    print(f"Reading {NUM} bytes, starting at address: {hex(START_ADDRESS)}")
    rData = dataCtrl.readMemory(ic.IConnectDebug.fRealTime,
                                0,
                                START_ADDRESS,
                                NUM, 1)
 
    # Create an IntelHex object
    ih = IntelHex()
 
    # Populate the IntelHex object with the read data
    for index, data in enumerate(rData[:NUM]):
        ih[START_ADDRESS + index] = data  
 
    # Save the IntelHex object to a file
    ih.write_hex_file("Flash_0.hex")

    START_ADDRESS = 0x00480000
    NUM = 524288
    print(f"Reading {NUM} bytes, starting at address: {hex(START_ADDRESS)}")
    rData = dataCtrl.readMemory(ic.IConnectDebug.fRealTime,
                                0,
                                START_ADDRESS,
                                NUM, 1)
 
    # Create an IntelHex object
    ih = IntelHex()
 
    # Populate the IntelHex object with the read data
    for index, data in enumerate(rData[:NUM]):
        ih[START_ADDRESS + index] = data  
 
    # Save the IntelHex object to a file
    ih.write_hex_file("Flash_1.hex")
if __name__ == "__main__":
    test_readMemory()