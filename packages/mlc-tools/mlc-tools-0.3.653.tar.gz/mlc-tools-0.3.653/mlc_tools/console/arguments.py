import sys


class Arguments:
    def __init__(self):
        self.command = 'run'
        self.mode = 'debug'
        self.config = 'project.yaml'
        self.project_name = 'mlc_app'

        args = sys.argv[1:]
        if args:
            self.set_command(args[0])

        self.set_option('mode')
        self.set_option('config')

    def set_command(self, command):
        valid = [
            'init', 'clean', 'run', 'build'
        ]
        if command not in valid:
            raise RuntimeError('Unknown command: ' + command)
        self.command = command

        if self.command == 'init':
            if len(sys.argv) < 3:
                raise RuntimeError('Error:\n  - mlc init [name]. Parameter name is skipped')
            self.project_name = sys.argv[2]

    def set_option(self, option):
        if not self.__getattribute__(option):
            raise RuntimeError('Unknown option: ' + option)

        arg = '--' + option
        if arg not in sys.argv:
            return
        index = sys.argv.index(arg)
        if index > len(sys.argv) - 2:
            raise RuntimeError('Error parse option: ' + arg)

        value = sys.argv[index + 1]
        self.__setattr__(option, value)
