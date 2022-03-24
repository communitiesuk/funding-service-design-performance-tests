import configparser


class Configs:

    config = configparser.ConfigParser()
    config.read("./config.ini")
