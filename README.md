
# Book Recommender System

This project implements a book recommender system based on user-based collaborative filtering. It utilizes Amazon's books dataset, which contains up to 76 thousand books. The recommender system suggests 5 similar books based on the user's selection.

## Project Structure

The repository contains the following files:

- `App.py`: Streamlit app for running the book recommender system.
- `Book Recommender System.ipynb`: Jupyter notebook describing the steps of building the recommender system.

## Dataset Description

The first **reviews** file contains feedback about 3M users on 212404 unique books the data set is part of the Amazon review Dataset it contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.
and this file has these attributes

|Features|	Description|
|---------|----------------|
|id|	The Id of Book|
|Title|	Book Title|
|Price|	The price of Book|
|User_id|	Id of the user who rates the book|
|profileName|	Name of the user who rates the book|
|review/helpfulness|	helpfulness rating of the| 
|review| e.g. 2/3|
|review/score|	rating from 0 to 5 for the book|
|review/time|	time of given the review|
|review/summary|	the summary of a text review|
|review/text|	the full text of a review|

The second file Books Details file contains details information about 212404 unique books it file is built by using
google books API to get details information about books it rated in the first file
and this file contains

|Features|	Description|
|--------|-------------|
|Title|	Book Title|
|Description|	decription of book|
|authors|	Neme of book authors|
|image|	url for book cover|
|previewLink|	link to access this book on google Books|
|publisher|	Name of the publisher|
|publishedDate|	the date of publish|
|infoLink|	link to get more information about the book on google books|
|categories|	genres of books|
|ratingsCount|	averaging rating for book|
