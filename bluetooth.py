
# save as bt_proximity_lock.py
import asyncio
import time
from collections import deque
from bleak import BleakScanner
from win10toast import ToastNotifier
import ctypes

# ====== CONFIG ======
DEVICE_NAME = "OPPO F27 PRO+ 5G"      # ya device ka BLE name (case-sensitive). Tum MAC address bhi use kar sakte ho agar available.
# On Windows, bleak may show addresses like "AA:BB:CC:DD:EE:FF" for some adapters.
USE_ADDRESS = None            # set to "AA:BB:CC:DD:EE:FF" if you prefer matching by address. Else keep None.
RSSI_LOCK_THRESHOLD = -85     # below this (dBm) consider 'far' (tune kar sakte ho)
SMOOTH_WINDOW = 4             # average RSSI calculation window
CHECK_INTERVAL = 5            # seconds between scans
CONSECUTIVE_LOCK_COUNT = 3    # must be 'far' for this many checks before locking
# ======================

toaster = ToastNotifier()

def lock_windows():
    """Locks the Windows workstation."""
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception as e:
        print("Lock failed:", e)

async def scan_once(timeout=3):
    """Perform a BLE scan for `timeout` seconds."""
    devices = await BleakScanner.discover(timeout=timeout)
    return devices

def pick_device_from_list(devices, name=None, address=None):
    for d in devices:
        if address and (d.address.lower() == address.lower()):
            return d
        if name and d.name and (d.name == name):
            return d
    return None

async def monitor_loop():
    print("Starting BT proximity monitor...")
    rssi_history = deque(maxlen=SMOOTH_WINDOW)
    far_count = 0
    locked = False

    while True:
        try:
            devices = await scan_once(timeout=3)
        except Exception as e:
            print("Scan error:", e)
            devices = []

        dev = pick_device_from_list(devices, name=DEVICE_NAME if not USE_ADDRESS else None, address=USE_ADDRESS)
        if dev:
            # got device - use RSSI if available
            rssi = dev.rssi if hasattr(dev, "rssi") else None
            print(f"[{time.strftime('%H:%M:%S')}] Found device: {dev.name} ({dev.address}), RSSI={rssi}")
            if rssi is not None:
                rssi_history.append(rssi)
                avg_rssi = sum(rssi_history)/len(rssi_history)
            else:
                # if RSSI not available, consider it 'near' because it's detected
                avg_rssi = -40

            # if previously locked and device is back, we cannot auto-unlock.
            if locked:
                toaster.show_toast("Phone nearby", "Phone detected. Please unlock Windows (use PIN/fingerprint).", duration=5, threaded=True)
                locked = False
                far_count = 0
            else:
                # just reset far counter
                far_count = 0

            # debug print
            print(f" Avg RSSI (smoothed): {avg_rssi:.1f} dBm")
        else:
            # device not seen in this scan
            print(f"[{time.strftime('%H:%M:%S')}] Device not detected in scan.")
            # treat as very far
            avg_rssi = -999
            rssi_history.clear()
            far_count += 1
            print(f" Far count: {far_count}/{CONSECUTIVE_LOCK_COUNT}")

        # decide lock
        if (avg_rssi != -999 and avg_rssi < RSSI_LOCK_THRESHOLD) or (avg_rssi == -999 and far_count >= CONSECUTIVE_LOCK_COUNT):
            # lock the workstation
            print("Proximity considered FAR. Locking Windows...")
            toaster.show_toast("Locking PC", "Device away — locking your PC.", duration=4, threaded=True)
            lock_windows()
            locked = True
            # after locking, wait a bit longer before next scans
            await asyncio.sleep(CHECK_INTERVAL * 2)
        else:
            # no lock, normal wait
            await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        asyncio.run(monitor_loop())
    except KeyboardInterrupt:
        print("Exiting...")
