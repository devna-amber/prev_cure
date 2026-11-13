# ErgoGuard — Automated Ergonomic & Posture Micro-Break Notifier

A lightweight, zero-dependency Python background utility that delivers periodic ergonomic posture and eye-strain reminders based on **OSHA neutral-spine guidelines** and the **American Academy of Ophthalmology (AAO) 20-20-20 rule**.

## Features
* **Cross-Platform Native Alerts**: Automatically detects WSL2 (`powershell.exe`), Linux Desktop (`notify-send`), or CLI terminal environments.
* **Zero External Dependencies**: Uses only Python's standard library (`shutil`, `subprocess`, `time`).
* **Evidence-Based Micro-Breaks**: Cycles through eye relaxation, neutral neck alignment, shoulder release, and circulation resets every 20 minutes.

## Quick Start
```bash
python3 ergoguard.py
```
