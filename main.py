import time
import random
import string
import os
import pickle
from colorama import init, Fore
init(convert=True)
import subprocess, requests

x = 10


def source(size=x, char=string.digits + string.ascii_lowercase + string.ascii_uppercase + "@" + "#" + "!" + "-"):
    return "".join(str(random.choice(char)) for _ in range(x))

f = open("pass.txt", "a")
f.write(source())
f.close

