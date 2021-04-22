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

import urllib.request
import os
import tarfile
import time 

engine_path = os.path.join(os.path.expanduser("~"), '.local', 'share', 'mycroft-precise')
engine_url = "https://github.com/MycroftAI/mycroft-precise/releases/download/v0.2.0/precise-engine_0.2.0_"
default_model_path = os.path.join("..", os.path.dirname(__file__), 'models', 'hey-mycroft_original.pb')

def get_binary(arch_name):
    """Download engine file and extract it"""
    
    print("Downloading engine binary from Github (50Mb)")
    url = engine_url + arch_name + ".tar.gz"
    file_tmp = urllib.request.urlretrieve(url, filename=None)[0]
    tar = tarfile.open(file_tmp)
    tar.extractall(engine_path)
    print("Downloaded and extracted engine binary to {}".format(engine_path))
    time.sleep(1)  
    
def activate_notify():
    """Play some sound to indicate a wakeword activation when testing a model"""
    audio = 'data/activate.wav'
    audio = os.path.join(os.path.dirname(__file__) ,audio)
    play_audio(audio)

def play_audio(filename: str):
    """
    Args:
        filename: Audio filename
    """
    import platform
    from subprocess import Popen

    if platform.system() == 'Darwin':
        Popen(['afplay', filename])
    else:
        Popen(['aplay', '-q', filename])

