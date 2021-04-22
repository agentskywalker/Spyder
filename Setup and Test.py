#%%
import math
import os
import sys

import requests

print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


r = requests.get("https://debashish.info")
print(r.status_code)

name = input("Your Name ?? ")
print(greet(name))


# %%
