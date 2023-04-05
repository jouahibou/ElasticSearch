import csv 
fields = [
    {"name": "Clothing ID", "type": "integer"},
    {"name": "Age", "type": "integer"},
    {"name": "Title", "type": "text"},
    {"name": "Review Text", "type": "keyword"},
    {"name": "Rating", "type": "integer"},
    {"name": "Recommended IND", "type": "integer"},
    {"name": "Positive Feedback Count", "type": "integer"},
    {"name": "Division Name", "type": "keyword"},
    {"name": "Department Name", "type": "keyword"},
    {"name": "Class Name", "type": "keyword"}
]

with open ("types.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([field["name"] for field in fields]) 
    writer.writerow([field["type"] for field in fields]) 
csvfile.close()      