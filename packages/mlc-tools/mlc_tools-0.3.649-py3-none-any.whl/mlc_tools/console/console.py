import os
import shutil
import subprocess
from mlc_tools import Mlc
from mlc_tools.console.config import ProjectConfig
from mlc_tools.utils.fileutils import normalize_path, write
from mlc_tools.console.cmake_file import *


class SubprocessWrapper(object):
    def __init__(self, arguments):
        assert isinstance(arguments, list) or isinstance(arguments, str)

        if isinstance(arguments, str):
            arguments = arguments.split(' ')

        assert len(arguments) > 0

        self.arguments = arguments
        self.process = subprocess.Popen(arguments)
        self.code = 0

    def call(self):
        self.process.communicate()
        self.code = self.process.returncode
        return self.code


class Console(object):
    def __init__(self, root):
        self.root = normalize_path(root)
        if not os.path.isdir(self.root):
            raise RuntimeError("Unknown path: " + self.root)

        self.config = ProjectConfig(self.root)
        self.config.parse()

        self.built = False
        self.generator = Mlc(configs_directory=self.config.src_directory,
                             data_directory=self.config.data_directory,
                             out_directory=self.config.build_directory + 'gen',
                             out_data_directory=self.config.build_directory + 'data',
                             generate_intrusive=True,
                             generate_factory=True,
                             generate_tests=False,
                             language='cpp',
                             php_validate=False,
                             join_to_one_file=True,
                             auto_registration=True,
                             formats='xml')

    def clean(self):
        self._clean()

    def build(self):
        self.built = True
        self._generate()
        self._create_cmake()
        self._copy_third_party()
        self._create_main()
        self._build()

    def run(self):
        if not self.built:
            self.build()
        self._run()

    def _clean(self):
        shutil.rmtree(self.config.build_directory)

    def _generate(self):
        self.generator.generate()
        if os.path.isdir(self.generator.model.data_directory):
            self.generator.generate_data()

    def _copy_third_party(self):
        destination = self.config.build_directory + 'external'
        if not os.path.isdir(destination):
            git_clone_command = 'git clone --branch {tag} {url} {path}'.format(
                tag=self.config.third_party_release,
                url=self.config.third_party_source_url,
                path=destination
            )
            process = SubprocessWrapper(git_clone_command)
            if process.call() != 0:
                raise RuntimeError('Error on clone external source from: {}, release: {}'.format(
                    self.config.third_party_source_url, self.config.third_party_release
                ))

    def _create_main(self):
        write(self.config.build_directory + '__main.cpp', MAIN_CPP)

    def _create_cmake(self):
        content = CMAKE
        content = content.replace('@{project_name}', self.config.name)
        write(self.config.build_directory + 'CMakeLists.txt', content)

    def _build(self):
        process = SubprocessWrapper(f'cmake -S {self.config.build_directory} -B {self.config.build_directory}')
        if process.call() != 0:
            raise RuntimeError('Error on cmake')

        process = SubprocessWrapper(f'make -C {self.config.build_directory}')
        if process.call() != 0:
            raise RuntimeError('Error on make')

    def _run(self):
        process = subprocess.Popen([f'./{self.config.build_directory}/' + self.config.name])
        process.communicate()
        if process.returncode != 0:
            raise RuntimeError('Error on run')


def main():
    try:
        print(os.path.abspath(os.path.curdir))
        console = Console(os.path.curdir)
        # console.clean()
        console.run()
    except RuntimeError as exception:
        print(exception)
        exit(1)
    exit(0)


if __name__ == '__main__':
    main()
