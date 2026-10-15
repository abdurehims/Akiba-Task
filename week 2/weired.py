#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    is_weird = n % 2 != 0 or 6 <= n <= 20

    print("Weird" if is_weird else "Not Weird")