# TweetBox-TV
Discover TweetBox TV a TV Show Tweet Analyzer: Collect, index &amp; explore tweets about your favorite shows. Powerful search and captivating visuals bring TV show discussions to life. Dive into a world of tweets, insights, and connection.
<img width="562" alt="image" src="https://github.com/Shadhrush5/TweetBox-TV/assets/119898772/a5c2d378-2e9e-4546-a196-178536f78ad9">


# Backend
## Requirements to Run Twitter crawler
1. Python 3
2. Install Tweepy

## Twitter Crawling Architecture
<img width="405" alt="image" src="https://github.com/Shadhrush5/TweetBox-TV/assets/119898772/1d776995-444a-4d57-8bd5-4ee0902d5434">

## Components

### config.py
The configuration files for this application contain the API keys, consumer key, API/Consumer Secret, Access key, and Access key secret. These files are essential for accessing the Twitter API from our application. Please use your keys in the placeholder.

### twitter_api.py
This file performs the following steps:
1. Itimportsnecessarylibraries:csv,tweepy,pandas,andrandom.
2. It imports API keys and access tokens from a separate configuration file
named config.py.
3. It retrieves an integer value from command-line arguments, which
represents the index of the title of a TV show to search for in a CSV file named
tv_shows.csv.
4. It reads the CSV file using pandas and retrieves the TV show's title from the
column named "title" at the given index.
5. ItcreatesanewCSVfilewiththenameoftheTVshowfollowedby'.csv'.
6. It defines two functions, one to generate random latitude and longitude
coordinates (as a substitute for missing geolocations), and the other to
remove spaces from a string.
7. ItopensthenewlycreatedCSVfileandinitializesaCSVwriter.
8. It creates a Twitter API object and uses it to search for tweets that contain
the TV show's title as a query.
9. For each tweet returned in the search, it extracts the tweet's creation date,
user's follower count, friend count, and text content, as well as random
latitude and longitude coordinates.
10. It writes these extracted values as a new row in the CSV file.
11. Once all tweets have been processed, the CSV file is closed.

### script.sh
This shell scripts runs our scraper once in 15 minutes retrieving tweets for a particular TV show one by one present in the list. This ensured the process automatically continued without user intervention.

### tv_shows.csv
IMDB top 1000 TV shows data set

### csvtojson.py
Run to consolidate all the csv files to a single JSON
file named as data.json

### remove_duplicates.py
To remove duplicates in data.json, run remove_duplicates.py file in the
same directory as data.json

### Lucene
We index the tweets using Lucene's default settings for text analysis and indexing. We perform a search for the query "Game of Thrones" using Lucene's default scoring algorithm and retrieve the top 10 results. We evaluate the quality of the rankings by manually inspecting the top 10 results and checking how relevant they are to the query.

1. Executethefileindex.pyforindexingusinglucenewhichislocated in the same folder as data.json
2. Execute the file retrieve.py with argument as query enclosed in single quotes for retrieving the top tweet results.
(Example: python3 retreive.py 'What does the phrase winter is coming means?')

### BERT
<img width="465" alt="image" src="https://github.com/Shadhrush5/TweetBox-TV/assets/119898772/336da32b-ed4e-4c05-b8dc-8e8ee2798bd2">

We convert the query to an embedding using the same pre-trained BERT model and search the index for the closest embeddings to the query. We retrieve the top 10 tweets with the closest embeddings to the query. We evaluate the quality of the rankings by manually inspecting the top 10
results and checking how relevant they are to the query.

1. Import the necessary libraries and packages, including PyTorch, pandas, faiss, transformers.
2. Loads a pre-trained BERT model and tokenizer from the "bert-base- uncased" model, which is a version of BERT trained on a large corpus of text data.
3. Reads sentences from a JSON file and stores them in a pandas DataFrame called "sentences".
4. Defines a function called "embedding_creator" that takes as input a dictionary of tokenized sentences, generates embeddings for each sentence using the pre-trained BERT model, and returns the mean- pooled embeddings.
5. Defines a function called "process_batch" that takes as input a batch of sentences, tokenizes them using the BERT tokenizer, generates
embeddings for each sentence using the "embedding_creator" function, and returns a list of embeddings.
6. Divides the sentences into batches and processes each batch using the "process_batch" function, storing the resulting embeddings in a list called "result".
7. Creates an index using the Faiss library and adds the embeddings from the "result" list to the index.
8. Defines a function called "convert_to_embedding" that takes as input a query string, tokenizes it using the BERT tokenizer, generates an embedding using the "embedding_creator" function, and returns the embedding.
9. The purpose of this code is to use BERT to generate embeddings for a set of sentences and then use Faiss to create an index of those embeddings. The resulting index can then be used to perform similarity search on a new query sentence by converting it to an embedding using BERT and then searching the index for the closest embeddings.

# Front End

<img width="468" alt="image" src="https://github.com/Shadhrush5/TweetBox-TV/assets/119898772/9912686e-0f8c-4e96-b60e-788f61e9d9f4">

## Front-end Development with Angular

Angular is a popular JavaScript framework for building dynamic web applications. To start working with Angular on your macOS machine, follow these steps:

### Prerequisites
1. Install Node.js: Download and install the latest stable version of Node.js from the official website or use a package manager like Homebrew.

### Installing Angular CLI
1. Open the Terminal application.
2. Run the following command to install the Angular CLI globally:


### Running the Application
1. After the dependencies are installed, run the app.sh file to start the Angular server:
2. Open a web browser and visit `http://localhost:4200` to view the application.

### Additional Configuration
1. Adjust any required environment variables or configuration files as specified in the project documentation.
2. Explore the Angular documentation and guides to leverage the full potential of the framework.


**Note:** Make sure you have the required permissions and dependencies installed on your system to ensure a smooth development experience.

## Output would look like

<img width="468" alt="image" src="https://github.com/Shadhrush5/TweetBox-TV/assets/119898772/aeb70417-0cf8-4902-8af8-24b240431836">



