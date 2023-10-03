from dom_api import domo_connector

import logging
import random
import configparser
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType, Policy
from pydomo.datasets import PolicyFilter, FilterOperator, PolicyType, Sorting
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType


domoapi = configparser.ConfigParser()
domoapi.read_file(open(r'./cfg/config.txt'))

# Connection Info
## add the connection info here
