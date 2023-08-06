from os.path import isfile
import yaml
from mlc_tools.utils.fileutils import normalize_path


class ProjectConfig:
    def __init__(self):
        self.name = None
        self.format = None
        self.src_directory = None
        self.data_directory = None
        self.build_directory = None
        self.third_party_source_url = None
        self.third_party_release = None
        self.set_defaults('')

    def set_defaults(self, root, arguments=None):
        self.name = 'app'
        self.format = 'xml'
        self.src_directory = normalize_path(root + 'src')
        self.data_directory = normalize_path(root + 'data')
        self.build_directory = normalize_path(root + 'build/' + arguments.mode if arguments else 'debug')
        self.third_party_source_url = 'https://github.com/mlc-tools/third_party.git'
        self.third_party_release = 'master'

    def parse(self, root, arguments):
        self.set_defaults(root, arguments)
        root = normalize_path(root)
        config_file = root + arguments.config
        if not isfile(config_file):
            return
        with open(config_file) as stream:
            try:
                data = yaml.safe_load(stream)
                self._parse_dict(data)
            except yaml.YAMLError as exception:
                print(exception)
                raise RuntimeError('Cannot parse project.yaml file')

    def _parse_dict(self, dictionary):
        try:
            self.name = dictionary.get('project')
            self.format = dictionary.get('format', 'xml')
        except KeyError as error:
            print('Project data has not key')
            print(error)
            raise RuntimeError('Cannot parse project data')
