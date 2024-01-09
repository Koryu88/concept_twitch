import yaml


class YamlReader:
    DATA = {}

    @staticmethod
    def read_property():
        if len(YamlReader.DATA) == 0:
            YamlReader.DATA = yaml.safe_load(open('resources/config.yml'))
        return YamlReader.DATA
