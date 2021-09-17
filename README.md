# pyRemoteScreen
Control your computer anywhere through web browser remotely! 

# Achievements
1. Screen Streaming (Captured by _PyScreeze_)

# Requirements
**pyRemoteScreen only supports Windows.**

* Flask
* PyScreeze

You can all requirements by `requirements.txt`.
```bash
pip install -r requirements.txt
```

# Usage
All configuraions are configure by default. Just run `pyremote.py`.
```bash
python pyremote.py
```

Host is `0.0.0.0` by default. However, the host can be changed by `--host` option.
```bash
python pyremote.py --host <an address to desire>
```

Service port is `4000` by default. However, the port can be changed by `--port` option.
```bash
python pyremote.py --port <a number to desire>
```
