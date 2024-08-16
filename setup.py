import configparser


def search_config():
    config = configparser.ConfigParser()

    # Add sections and key-value pairs
    config['General'] = {'search correction %': 80,
                         'search related %': 70, 'database directory': 'data\crate_database'}

    # Write the configuration to a file
    with open('data\search_config.cfg', 'w') as configfile:
        config.write(configfile)


def website_config():
    config = configparser.ConfigParser()

    # Add sections and key-value pairs
    config['General'] = {'ip' : '0.0.0.0', 'port' : '5000'}

    # Write the configuration to a file
    with open('data\website_config.cfg', 'w') as configfile:
        config.write(configfile)


search_config()
website_config()
