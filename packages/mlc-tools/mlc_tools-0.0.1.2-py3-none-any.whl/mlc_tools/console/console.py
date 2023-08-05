import os
import shutil
import subprocess
from mlc_tools import Mlc
from mlc_tools.utils.fileutils import normalize_path, write


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

        self.built = False
        self.generator = Mlc(configs_directory=self.root + 'src',
                             data_directory=self.root + 'data',
                             out_directory=self.root + 'build/gen',
                             out_data_directory=self.root + 'build/data',
                             generate_intrusive=True,
                             generate_factory=True,
                             generate_tests=False,
                             language='cpp',
                             php_validate=False,
                             join_to_one_file=True,
                             auto_registration=True,
                             formats='xml')
        self.generator.generate()
        if os.path.isdir(self.generator.model.data_directory):
            self.generator.generate_data()

    def build(self):
        self.built = True
        self._create_cmake()
        self._copy_third_party()
        self._create_main()
        self._build()

    def run(self):
        if not self.built:
            self.build()
        self._run()

    def _copy_third_party(self):
        if not os.path.isdir(self.root + 'build/external/jsoncpp'):
            shutil.copytree(self.root + '../simple_test/external/jsoncpp', self.root + 'build/external/jsoncpp')
        if not os.path.isdir(self.root + 'build/external/pugixml'):
            shutil.copytree(self.root + '../simple_test/external/pugixml', self.root + 'build/external/pugixml')

    def _create_main(self):
        content = '''#include "Main.h"
int main(int argc, char ** args){ mg::Main::main(); return 0; }
'''
        write(self.root + 'build/__main.cpp', content)


    def _create_cmake(self):
        content = '''cmake_minimum_required(VERSION 3.6.2)
SET(ROOT ${CMAKE_SOURCE_DIR})
project(mlc_app)
file(GLOB_RECURSE SRC ${ROOT}/gen/*.cpp ${ROOT}/external/*.cpp)
if(WIN32)
    add_definitions(-W1 -std=c++14)
else()
    add_definitions(-Wall -std=c++14)
endif()
include_directories(${ROOT}/gen ${ROOT}/external)
add_executable(${PROJECT_NAME} ${SRC} ${ROOT}/__main.cpp)
target_link_libraries(${PROJECT_NAME})'''
        write(self.root + 'build/CMakeLists.txt', content)

    def _build(self):
        process = SubprocessWrapper(f'cmake -S {self.root}build/ -B {self.root}build/')
        if process.call() != 0:
            raise RuntimeError('Error on cmake')

        process = SubprocessWrapper(f'make -C {self.root}build/')
        if process.call() != 0:
            raise RuntimeError('Error on make')

    def _run(self):
        process = subprocess.Popen(['./build/mlc_app'])
        process.communicate()
        if process.returncode != 0:
            raise RuntimeError('Error on run')


def main():
    try:
        print(os.path.abspath(os.path.curdir))
        console = Console(os.path.curdir)
        console.run()
    except RuntimeError as exception:
        print(exception)
        exit(1)
    exit(0)


if __name__ == '__main__':
    main()