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


def retrieve(storedir, query):
    searchDir = NIOFSDirectory(Paths.get(storedir))
    searcher = IndexSearcher(DirectoryReader.open(searchDir))

    parser = QueryParser('text', StandardAnalyzer())
    parsed_query = parser.parse(query)

    topDocs = searcher.search(parsed_query, 10).scoreDocs
    topkdocs = []
    for hit in topDocs:
        doc = searcher.doc(hit.doc)
        topkdocs.append({
            "score": hit.score,
	    "title": doc.get("title"),
            "text": doc.get("text"),
	    "created_at": doc.get("created_at"),
            "lat": doc.get("latitude"),
            "lon": doc.get("longitude"),
	    "followers_count": doc.get("followers_count"),
	    "friends_count": doc.get("friends_count")
        })

    print(topkdocs)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sentence", help="Sentence to be processed")
args = parser.parse_args()

query = args.sentence
#print("Query passed as argument:", query)

lucene.initVM(vmargs=['-Djava.awt.headless=true'])
retrieve('tv_shows_lucene_index/', query)

