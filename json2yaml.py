#!/usr/bin/python3
import yaml, json, sys
json_object = open('blue-green-service.json')
sys.stdout.write(yaml.dump(json.load(json_object)))
