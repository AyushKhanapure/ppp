from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_db'] 
collection = db['test_collection'] 

def create_document(data):
    result = collection.insert_one(data)
    print("Document created with id:", result.inserted_id)

def read_documents(query={}):
    documents = collection.find(query)
    for doc in documents:
        print(doc)

def update_document(query, new_data):
    result = collection.update_one(query, {"$set": new_data})
    print("Document updated:", result.modified_count)

def delete_document(query):
    result = collection.delete_one(query)
    print("Document deleted:", result.deleted_count)

if __name__ == "__main__":
    create_document({"name": "John", "age": 25})
    
    print("Documents in the collection:")
    read_documents()
    
    update_document({"name": "John"}, {"age": 26})
    
    print("Documents in the collection after update:")
    read_documents()
    
    delete_document({"name": "John"})
    
    print("Documents in the collection after delete:")
    read_documents()
