#!/usr/bin/python
import csv
import json
from elasticsearch import Elasticsearch, helpers
import warnings

warnings.filterwarnings("ignore")

question_number = "5.4"

with open('types.csv') as f :
    types = f.readline().strip().split(',')
    field_types = f.readline().strip().split(',')

# Connexion au cluster
client = Elasticsearch(hosts="http://@localhost:9200")

# Mapping pour l'index "eval"
mapping = {
    "mappings": {
        "properties": {
            types[i]:{'type':field_types[i]} for i in range(len(types))
        }
    }
}

# Création de l'index "eval" avec le mapping cohérent
client.indices.create(index="eval", body=mapping)

# Importations du fichier csv 
with open('Womens_Clothing.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(client, reader, index='eval')

# Recherche "match_all" dans l'index "eval"

query = {
        "query":{
            "range":{
                "Rating":{
                    "lt":2
                }
            }
        }
        
    }    
    





response = client.search(index="eval", body=query)

# Sauvegarde de la requête et la réponse dans un fichier json
with open("./{}.json".format("q_" + question_number + "_response"), "w") as f:
    json.dump(dict(response), f, indent=2)

with open("./{}.json".format("q_" + question_number + "_request"), "w") as f:
    json.dump(query, f, indent=2)
