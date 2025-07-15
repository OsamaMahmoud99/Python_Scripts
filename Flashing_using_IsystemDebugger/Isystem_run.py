import isystem.connect as ic

winidea_id = ''

def test_run():
    connMgr = ic.ConnectionMgr()
    connMgr.connect(ic.CConnectionConfig().instanceId(winidea_id))
    execCtrl = ic.CExecutionController(connMgr)
    execCtrl.run()
    isRunning = execCtrl.getCPUStatus(False).isRunning()
    print(f"Is CPU in `RUN` state: {isRunning}")

if __name__ == "__main__":
    test_run()