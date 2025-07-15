import subprocess
 
try:
    import isystem.connect as ic
 
except ImportError:
    subprocess.check_call(["pip", "install", "isystem.connect"])

 

winidea_id = ''

def test_stop():
    connMgr = ic.ConnectionMgr()
    connMgr.connect(ic.CConnectionConfig().instanceId(winidea_id))
    execCtrl = ic.CExecutionController(connMgr)
    execCtrl.stop()
    isStopped = execCtrl.getCPUStatus(False).isStopped()
    print(f"Is CPU in `STOP` state: {isStopped}")

if __name__ == "__main__":
    test_stop()