import configparser


class search_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('data\search_config.cfg')

    # Access values from the configuration file
    correction = int(config.get('General', 'search correction %'))
    related = int(config.get('General', 'search related %'))
    directory = config.get('General', 'database directory')


class website_config():
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('data\website_config.cfg')

    # Access values from the configuration file
    IP = config.get('General', 'ip')
    PORT = config.get('General', 'port')
