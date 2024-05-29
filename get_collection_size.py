import csv
import sys
from pyPreservica import *

client = EntityAPI()

root_folder = client.folder(sys.argv[1])
with open(file=f'{root_folder.title}.csv', mode='x', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for asset in filter(only_assets, client.all_descendants(root_folder.reference)):
        print(asset.title)
        for r in client.representations(asset):
            for co in client.content_objects(r):
                for generation in client.generations(co):
                    for bs in generation.bitstreams:
                            writer.writerow([root_folder.title, asset.title, bs.filename, bs.length])
                            print(root_folder.title, bs.filename)
