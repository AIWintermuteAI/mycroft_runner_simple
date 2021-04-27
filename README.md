# Precise Wrapper

A lightweight Python module for using Mycroft Precise. The main difference of this fork is simplified installation procedure.

#### Supported platforms:
Linux

#### Supported architectures:

x86_64
armv7l
aarch64

## Installation

```
git clone 
sudo apt-get install portaudio19-dev
cd 
pip install .
```

Alternatively, you can simply install the latest stable version of this package from PyPi

```
sudo apt-get install portaudio19-dev
pip install .
```

## Usage

#### CLI:

```
mycroft-precise --model hey-mycroft
```
This command will run hot word detection ith default engine and default key word model. You can supply the following additional arguments

```
:-m --model str -
    TensorFlow (.pb) model to run

:-c --chunk-size int 2048
    Samples between inferences

:-l --trigger-level int 3
    Number of activated chunks to cause an activation

:-s --sensitivity float 0.5
    Network output required to be considered activated

:-b --basic-mode
    Report using . or ! rather than a visual representation

:-d --save-dir str -
    Folder to save false positives

:-p --save-prefix str -
    Prefix for saved filenames
```

#### As Python module:

You can create a program as follows, passing in the location of
the executable and model to PreciseEngine(), or leaving them empty if you want to use the default engine and default model (responds to "hey-mycroft", speak clearly and with clean accent):

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


PreciseEngine() class init accepts the following parameters:

```
exe_file (Union[str, list]): Either filename or list of arguments
                                (ie. ['python', 'precise/scripts/engine.py'])

model_file (str): Location to .pb model file to use (with .pb.params)

chunk_size (int): Number of *bytes* per prediction. Higher numbers
                    decrease CPU usage but increase latency
```

On the first run, if no engine path or model path arguments are specified, it will automatically download the engine and use default model, supplied with the package.

PreciseRunner class init accepts the following parameters:

```
engine (Engine): Object containing info on the binary engine

trigger_level (int): Number of chunk activations needed to trigger on_activation. Higher values add latency but reduce false positives

sensitivity (float): From 0.0 to 1.0, how sensitive the network should be 

stream (BinaryIO): Binary audio stream to read 16000 Hz 1 channel int16
audio from. If not given, the microphone is used

on_prediction (Callable): callback for every new prediction

on_activation (Callable): callback for when the wake word is heard
```

You can stop runner instance with stop() method, e.g.

```runner.stop()```

or pause it with pause() method, e.g.

```runner.pause()```

then resume with 

```runner.play()```
