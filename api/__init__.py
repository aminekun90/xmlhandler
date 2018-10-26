'''api Module'''
#api module
from .handlers import XMLHandler
from .db_config import Config

session = Config().session
