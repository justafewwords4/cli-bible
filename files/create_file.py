#!/usr/bin/env python

import os

base_name = "sparv60_02_GEN_"
chapters = 50

for index in range(1, chapters + 1):
    os.system(f"touch {base_name}{index:02d}.md")
