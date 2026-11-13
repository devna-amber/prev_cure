# PreCure (`ErgoGuard`) — Automated Ergonomic & Eye-Strain Guardian

A lightweight, zero-dependency Python utility that delivers periodic posture and eye-strain micro-break reminders based on **OSHA neutral-spine guidelines** and the **American Academy of Ophthalmology (AAO) 20-20-20 rule**.

## Key Features
* **Zero External Dependencies**: Built strictly with Python's standard library (`shutil`, `subprocess`, `time`).
* **Cross-Platform Desktop Alerts**: Automatically detects **WSL2** (`powershell.exe` pop-ups), **Ubuntu Desktop** (`notify-send`), or standard CLI terminals.
* **Evidence-Based Micro-Breaks**: Cycles through four 20-second resets every 20 minutes—eye relaxation, neutral neck alignment, shoulder release, and circulation check.

## Quick Start

```bash
# Run interactively in your terminal
python3 ergoguard.py

# Or run silently in the background while studying/coding
python3 ergoguard.py &
```
