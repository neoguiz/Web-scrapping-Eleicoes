import subprocess
import sys

def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--user"])

install("python-twitter-v2")
install("snscrape")
install("pandas")

# INICIO DO CODIGO

import snscrape.modules.twitter as dados
import pandas as pandas
import datetime






