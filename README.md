# BSOD-Python

<img width="1920" height="1080" alt="bsod1" src="https://github.com/user-attachments/assets/22ef0db1-009c-432e-9e4c-f0fff4e0e093" />

# BSOD Prank

Fullscreen fake Blue Screen of Death written in Python. Captures a screenshot of the desktop, displays it fullscreen, and on click runs through a sequence of fake BSOD images with matching sound effects. Strictly for pranks — not malware.

## How it works

1. Minimizes all windows (`Win+D`) and takes a screenshot of the desktop.
2. Opens a fullscreen, always-on-top window using the screenshot as its background, so the user thinks they're still looking at their normal desktop.
3. A left click triggers the sequence: 9 BSOD images (blue, red, black variants, fake Windows XP shutdown, etc.) cycle through while `winsound` plays the corresponding audio clips.
4. Blocks `Ctrl`, `Alt`, and `Win` so the usual escape shortcuts (`Ctrl+Alt+Del`, `Alt+F4`) don't work.

## Requirements

- Windows (required for `winsound` and the key blocking behavior)
- Python 3.x
- Packages:
  - `pyautogui`
  - `Pillow`
  - `keyboard`

## File structure

```
.
├── main.py
├── bsod1.png ... bsod9.png
├── noise1.wav
├── error.wav
├── error2.wav
├── bass-boost-discord-call.wav
├── dexter-meme.wav
├── windows-xp-distorted.wav
└── windows-xp-startup.wav
```

All assets must sit in the same folder as `main.py`.

## Usage

```bash
python main.py
```

After launch, a left click starts the sequence. Once it finishes, restart your PC or press ctrl + alt + del then "Task Manager" and then alt + tab and move your mouse to the tkinter window and press "x"

## Notes

- Windows only.
- The `keyboard` module often needs admin privileges to block keys reliably.
- No built-in exit hotkey. If you want one, add `keyboard.add_hotkey('esc', root.destroy)` before `mainloop`.
