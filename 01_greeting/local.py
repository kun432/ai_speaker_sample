import json
import sys

print("Content-type: application/json\n\n")

output = {
  "speech": "Hello."
}

json.dump(output, sys.stdout)