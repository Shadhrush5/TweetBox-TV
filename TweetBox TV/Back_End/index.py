import logging, sys
logging.disable(sys.maxsize)

import lucene
import os
from org.apache.lucene.store import MMapDirectory, SimpleFSDirectory, NIOFSDirectory
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader
from org.apache.lucene.search import IndexSearcher, BoostQuery, Query
from org.apache.lucene.search.similarities import BM25Similarity
import json

# Load the JSON file
with open('data.json', 'r') as file:
    sample_doc = json.load(file)

def create_index(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    store = SimpleFSDirectory(Paths.get(dir))
    analyzer = StandardAnalyzer()
    config = IndexWriterConfig(analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
    writer = IndexWriter(store, config)

    metaType = FieldType()
    metaType.setStored(True)
    metaType.setTokenized(False)

    contextType = FieldType()
    contextType.setStored(True)
    contextType.setTokenized(True)
    contextType.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

    for sample in sample_doc:
        title = sample['title']
        created_at = sample['created_at']
        followers_count = sample['followers_count']
        friends_count = sample['friends_count']
        text = sample['text']
        latitude = sample['latitude']
        longitude = sample['longitude']

        doc = Document()
        doc.add(Field('title', str(title), metaType))
        doc.add(Field('text', str(text), contextType))
        doc.add(Field('created_at', str(created_at), metaType))
        doc.add(Field('followers_count', str(followers_count), metaType))
        doc.add(Field('friends_count', str(friends_count), metaType))
        doc.add(Field('latitude', str(latitude), metaType))
        doc.add(Field('longitude', str(longitude), metaType))
        writer.addDocument(doc)
    writer.close()

#import sys

#query = sys.argv[1:]
lucene.initVM(vmargs=['-Djava.awt.headless=true'])
create_index('tv_shows_lucene_index/')
