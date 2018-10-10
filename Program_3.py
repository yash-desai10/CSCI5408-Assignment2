# os library gives operating system dependent functionality
# json library parses JSON into a Python data format
# csv library  read and write tabular data in CSV format
import os,json,csv

#provides elastic search functionality in python
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, streaming_bulk

#indexing to elastic search database
es = Elasticsearch(['https://admin:KJMFTEJIZENLGHZJ@portal-ssl1505-6.bmix-dal-yp-75c72e88-0f6b-4398-a24f-461c0f57eb12.3517592683.composedb.com:58045'])
es.indices.create(index='jfile', ignore=400)

#Read data from csv file
csv_file=open("file.csv","r")

#Writes new json file
json_file=open("file2.json","w")
print("JSON File is created")

#Declaring field names
fieldnames=("Tweet","Score","Sentiment")

#use CSV Dict reader to write data from json file
reader=csv.DictReader(csv_file,fieldnames)
for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')
json_file.close()

#Loads json data to elasticsearch database
def elasdata():

    for json_file in open("file2.json",'r'):
        data = json.loads(json_file)

        yield{

            "_index": "jfile",
            "_type":"doc",
            "_source":{

                "Tweet":data['Tweet'],
                "Score":data['Score'],
                "Sentiment":data['Sentiment']


            }

        }
bulk(es, elasdata())
json_file.close()
