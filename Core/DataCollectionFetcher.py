from sentinelhub import DataCollection

for collection in DataCollection.get_available_collections():
    print(collection)
