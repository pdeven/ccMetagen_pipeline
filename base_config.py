import json
import os
import sys

script_path = os.path.dirname(__file__)

json_path = os.path.join(script_path, "config.json")
if os.path.isfile(json_path):
    with open(json_path, "r", encoding="utf8") as conf_json:
        configuration = json.load(conf_json)
else:
    sys.exit("Backend config.json is missing.")

RESOURCE_BASE_PATH = configuration["resources_base_path"]
KMA_INDEXED_DATABASE = os.path.join(RESOURCE_BASE_PATH,"database","ncbi_16s" )
CONTAINER_BASEPATH = os.path.join(RESOURCE_BASE_PATH, "container_resources" )
RESULTS_FOLDER = os.path.join(RESOURCE_BASE_PATH, "results" )
TEMPORARY_DIRECTORY = os.path.join(RESOURCE_BASE_PATH, "temp_directory" )
LOG_DIRECTORY = os.path.join(RESOURCE_BASE_PATH, "log_directory" )
MEMORY = configuration["memory"]
DISK = configuration["disk"]
CORES = configuration["cores"]

