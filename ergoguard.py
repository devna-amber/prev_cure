#!/usr/bin/env python3
"""
ErgoGuard — Hands-Free Ergonomic Reminder grounded in OSHA/Mayo Clinic & AAO guidelines.
Works natively on WSL2 (Windows Desktop Pop-up), Ubuntu Desktop, and CLI terminals.
"""

import shutil
import subprocess
import sys
import time

ERGONOMIC_CUES = [
    ("20-20-20 Eye Reset (AAO)", "Look at something 20 feet away for 20 seconds to relax eye focusing muscles."),
    ("Neutral Neck Check (OSHA)", "Gently tuck your chin back so your ears align directly over your shoulders."),
    ("Shoulder & Wrist Release", "Drop your shoulders away from your ears and keep wrists flat, not bent upward."),
    ("Posture & Circulation Reset", "Uncross your legs, plant both feet flat on the floor, or stand up for 30 seconds."),
]


def send_desktop_alert(title: str, message: str) -> None:
    """Sends a native Windows pop-up on WSL2, notify-send on Linux, or terminal bell."""
    print(f"\a[{time.strftime('%I:%M %p')}] {title}: {message}", flush=True)

    if shutil.which("notify-send"):
        subprocess.run(["notify-send", "-u", "normal", "-t", "8000", title, message], check=False)
    elif shutil.which("powershell.exe"):
        ps_cmd = (
            f"Add-Type -AssemblyName PresentationFramework; "
            f"[System.Windows.MessageBox]::Show('{message}', '{title}', 'OK', 'Information') | Out-Null"
        )
        subprocess.Popen(["powershell.exe", "-NoProfile", "-Command", ps_cmd],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> int:
    interval_minutes = 20
    print("ErgoGuard active (20-min clinical micro-break cycle). Minimize this window and study!", flush=True)
    send_desktop_alert("ErgoGuard Active", "Screen top at eye level, feet flat. First micro-break in 20 mins.")

    idx = 0
    try:
        while True:
            time.sleep(interval_minutes * 60)
            title, msg = ERGONOMIC_CUES[idx % len(ERGONOMIC_CUES)]
            send_desktop_alert(title, msg)
            idx += 1
    except KeyboardInterrupt:
        print("\nErgoGuard stopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
