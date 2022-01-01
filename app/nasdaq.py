# this python file is to findout more about stocks that meet a specific criteria.
import nasdaqdatalink
keys_file = open("../keys.txt")
nasdaqdatalink.ApiConfig.api_key = keys_file.readline().rstrip()
