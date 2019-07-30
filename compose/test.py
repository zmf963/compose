from __future__ import absolute_import
from __future__ import unicode_literals
import sys
sys.path.append("/opt/compose/")
from compose.cli.main import main

main()

# import compose.config.config as config

# ret = config.load_yaml("/opt/compose/docker-compose.yml")
# print(ret)