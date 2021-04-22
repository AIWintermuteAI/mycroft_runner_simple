# Python 3
# Copyright 2019 Mycroft AI Inc.
# Modified 2021 Seeed Studio STU, Dmitry Maslov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Run a model on microphone audio input

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
"""

import numpy as np
import os
from prettyparse import Usage
from random import randint
from shutil import get_terminal_size
from threading import Event

from precise_runner.scripts.base_script import BaseScript
from precise_runner import PreciseEngine, PreciseRunner
from precise_runner.util import activate_notify

class MycroftScript(BaseScript):
    usage = Usage(__doc__)

    def __init__(self, args):
        super().__init__(args)

        if args.model == 'hey-mycroft': 
            args.model = None
            
        self.engine = PreciseEngine(exe_file = None, model_file = args.model, chunk_size= args.chunk_size)
        self.runner = PreciseRunner(self.engine, args.trigger_level, sensitivity=args.sensitivity,
                                    on_activation=self.on_activation, on_prediction=self.on_prediction)
        self.session_id, self.chunk_num = '%09d' % randint(0, 999999999), 0

    def on_activation(self):
        activate_notify()

        if self.args.save_dir:
            nm = join(self.args.save_dir, self.args.save_prefix + self.session_id + '.' + str(self.chunk_num) + '.wav')
            save_audio(nm, self.audio_buffer)
            print()
            print('Saved to ' + nm + '.')
            self.chunk_num += 1

    def on_prediction(self, conf):
        if self.args.basic_mode:
            print('!' if conf > 0.7 else '.', end='', flush=True)
        else:
            max_width = 80
            width = min(get_terminal_size()[0], max_width)
            units = int(round(conf * width))
            bar = 'X' * units + '-' * (width - units)
            cutoff = round((1.0 - self.args.sensitivity) * width)
            print(bar[:cutoff] + bar[cutoff:].replace('X', 'x'))


    def run(self):
        self.runner.start()
        Event().wait()  # Wait forever

main = MycroftScript.run_main

if __name__ == '__main__':
    main()
