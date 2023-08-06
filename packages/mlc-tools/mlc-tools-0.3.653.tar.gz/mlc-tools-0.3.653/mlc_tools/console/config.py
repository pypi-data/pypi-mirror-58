from os.path import isfile
import yaml
from mlc_tools.utils.fileutils import normalize_path


class ProjectConfig:
    def __init__(self, root, arguments):
        self.arguments = arguments
        self.name = 'app'
        self.root = normalize_path(root)
        self.src_directory = normalize_path(self.root + 'src')
        self.data_directory = normalize_path(self.root + 'data')
        self.build_directory = normalize_path(self.root + 'build/' + arguments.mode)
        self.third_party_source_url = 'https://github.com/mlc-tools/third_party.git'
        self.third_party_release = 'master'

    def parse(self):
        config_file = self.root + self.arguments.config
        if not isfile(config_file):
            return
        with open(config_file) as stream:
            try:
                data = yaml.safe_load(stream)
                self.parse_dict(data)
            except yaml.YAMLError as exc:
                print(exc)

    def parse_dict(self, dictionary):
        try:
            self.name = dictionary['project']
        except KeyError as error:
            print('Project data has not key')
            print(error)
            raise RuntimeError('Cannot parse project data')
