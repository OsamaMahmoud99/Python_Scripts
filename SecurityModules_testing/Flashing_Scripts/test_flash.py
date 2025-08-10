import subprocess

try:
    import isystem.connect as ic

except ImportError:
    subprocess.check_call(["pip", "install", "isystem.connect"])


winidea_id = ''


def test_download():
    conn_mgr = ic.ConnectionMgr()
    conn_mgr.connect(ic.CConnectionConfig().instanceId(winidea_id))

    load_ctrl = ic.CLoaderController(conn_mgr)

    if load_ctrl.download() == 0:
        print("Download finished successfully.")
    else:
        print("Download finished with warnings.")


if __name__ == "__main__":
    test_download()