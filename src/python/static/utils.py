import os
from datetime import datetime


now = datetime.now()

timestamp = now.strftime("%b-%d-%Y:%H-%M-%S")
logger_header = "[" + timestamp + "_logger]: "

def join_to_relative_path(filepath):
    sep = '\\python'
    stripped = __file__.split(sep, 1)[0]
    dirname = os.path.dirname(stripped)
    filepath = os.path.join(dirname, filepath).replace("\\", "/")
    return filepath
