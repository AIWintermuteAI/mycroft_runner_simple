# Precise Wrapper

A simplified lightweight Python module for using Mycroft Precise. 

## Usage:
```
sudo apt-get install portaudio19-dev
pip install .
```
On the first run, if no engine path or model path arguments are specified, it will automatically download the engine and use default model, supplied with the package.

Finally, you can create a program as follows, passing in the location of
the executable as the first argument:

```python
from precise_runner import PreciseEngine, PreciseRunner

engine = PreciseEngine()
runner = PreciseRunner(engine, on_activation=lambda: print('Hello Seeed!'))
runner.start()

# Sleep forever
from time import sleep
while True:
    sleep(10)
```
