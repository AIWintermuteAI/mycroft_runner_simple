# Python 3
# Copyright 2019 Mycroft AI Inc.
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

from abc import abstractmethod
from argparse import ArgumentParser, Namespace
from prettyparse import Usage

class BaseScript:
    """A class to standardize the way scripts are defined"""
    usage = Usage()

    def __init__(self, args):
        self.args = args

    @classmethod
    def create(cls, **args):
        values = {}
        for arg_name, arg_data in cls.usage.arguments.items():
            if arg_name in args:
                values[arg_name] = args.pop(arg_name)
            else:
                if 'default' not in arg_data and arg_name and not arg_data['_0'].startswith('-'):
                    raise TypeError('Calling script without required "{}" argument.'.format(arg_name))
                typ = arg_data.get('type')
                if arg_data.get('action', '').startswith('store_') and not typ:
                    typ = bool
                if not typ:
                    typ = lambda x: x
                values[arg_name] = typ(arg_data.get('default'))
        args = Namespace(**values)
        cls.usage.render_args(args)
        return cls(args)

    @abstractmethod
    def run(self):
        pass

    @classmethod
    def run_main(cls):
        parser = ArgumentParser()
        cls.usage.apply(parser)
        args = cls.usage.render_args(parser.parse_args())

        try:
            script = cls(args)
        except ValueError as e:
            parser.error('Error parsing args: ' + str(e))
            raise SystemExit(1)

        try:
            script.run()
        except KeyboardInterrupt:
            print()
