# This script is licensed under BSD License, see file LICENSE.txt.
#
# (c) TASKING Germany GmbH, 2023
 
"""
This script shows recommended way to connect to specific version of winIDEA
at known location.
"""
 


try:
    import isystem.connect as ic
    import time
except ImportError:
    try:
        import subprocess
    except ImportError:
        subprocess.check_call(["pip", "install", "subprocess"])
    subprocess.check_call(["pip", "install", "isystem.connect"])
    subprocess.check_call(["pip", "install", "time"])
    
TIMEOUT_S = 15  
POLL_INTERVAL_S = 0.5
 
 
def test_connect():
    conn_mgr = ic.ConnectionMgr()
    cfg = ic.CConnectionConfig()
    cfg.start_always()
 
    conn_mgr.connect(cfg)
 
    if conn_mgr.isConnected():
        print("Connected to winIDEA!")
    else:
        print("Could not connect to winIDEA in the specified time.")
 
   
    
   
if __name__ == "__main__":
    test_connect()