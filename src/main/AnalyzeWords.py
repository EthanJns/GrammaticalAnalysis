from GrammarDriver import GrammarWebDriver as GWDriver
from resources.ConfigEnum import ConfigEnum as CE

def build_config():
    config_dict = {}
    config_file = open('./resources/config.txt', 'r')
    for line in config_file.readlines():
        key_value = line.split('=')
        if len(key_value) == 2:
            config_dict[key_value[0]] = key_value[1]
    return config_dict

gd = GWDriver(build_config())
gd.get_driver().get("https://google.com")
