import can
import socket
import threading
import time
 
# ========== Configuration ==========
TARGET_IP = "10.49.0.23"      # Windows CANoe IP (run `ipconfig` on Windows)
SEND_PORT = 16000             # CAPL script receives on this port
RECEIVE_PORT = 17000          # CAPL sends UDP to this port
# ===================================
 
# Set up CAN interfaces
bus_send = can.interface.Bus(channel='vcan0', bustype='socketcan')
bus1 = can.interface.Bus(channel='vcan0', bustype='socketcan')
bus2 = can.interface.Bus(channel='vcan1', bustype='socketcan')
 
# UDP sockets
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(("0.0.0.0", RECEIVE_PORT))
recv_sock.settimeout(1.0)
 
# ========== Function to Parse UDP to CAN ==========
def parse_and_send(line: str):
    parts = line.strip().split(',')
    if len(parts) != 5:
        return
    bus_name, timestamp_us, can_id_str, dlc_str, data_hex = parts
    try:
        can_id = int(can_id_str, 16)
        dlc = int(dlc_str)
        data = bytes.fromhex(data_hex[:dlc * 2])
        msg = can.Message(arbitration_id=can_id, data=data, is_extended_id=False)
    
        print(f"[CAN RX] {bus_name} ID=0x{can_id:X} Data={data.hex().upper()}")
    except Exception as e:
        print(f"[ERROR] Failed to parse/send: {e}")
# ================================================
 
# ========== UDP Receiver Thread ==========
def udp_receiver():
    print(f"[UDP RX] Listening on UDP port {RECEIVE_PORT} for CANoe frames...")
    while True:
        try:
            row, addr = recv_sock.recvfrom(256)
            line = row.decode()
            print(f"[UDP RX] From {addr}: {line.strip()}")
            parse_and_send(line)
        except socket.timeout:
            continue
        except Exception as e:
            print(f"[ERROR] UDP receive failed: {e}")
            break
# =========================================
 
# ========== UDP Sender ==========
def send_from_vcan0():
    print(f"[CAN TX] Forwarding vcan0 → UDP {TARGET_IP}:{SEND_PORT}")
    try:
        for msg in bus_send:
            data_hex = msg.data.hex().upper()
            line = f"CAN1,{int(msg.timestamp * 1_000_000)},{msg.arbitration_id:03X},{msg.dlc},{data_hex}\n"
            send_sock.sendto(line.encode(), (TARGET_IP, SEND_PORT))
            print(f"[UDP TX] Sent: {line.strip()}")
    except KeyboardInterrupt:
        print("Sender stopped.")
# =========================================
 
# ========== Main ==========
if __name__ == "__main__":
    try:
        recv_thread = threading.Thread(target=udp_receiver, daemon=True)
        recv_thread.start()
        send_from_vcan0()
    except KeyboardInterrupt:
        print("Program terminated.")