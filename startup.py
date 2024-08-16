import _website as app
from _configs import website_config

app.app.run(host=website_config.IP, port=website_config.PORT)
