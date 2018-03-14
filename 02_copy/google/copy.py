#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import json
import sys

input = json.load(sys.stdin)

with open("input.txt", "w") as file:
  json.dump(input,file, indent=4)

print("Content-type: application/json\n\n")
output = {
  "speech": u"こんにちは"
}
json.dump(output, sys.stdout)