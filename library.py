import argparse, configparser, grp, pwd, hashlib, os, re, sys, zlib
from datetime import datetime
from fnmatch import fnmatch
from math import ceil

argparser = argparse.ArgumentParser(description = "Command-line parser")
argsubparser = argparser.add_argument(title = "Command", dest = "command")
argsubparser.required = True