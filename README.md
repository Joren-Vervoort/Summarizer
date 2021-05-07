# Summarizer

- Type of challenge: Learning
- Duration: `2 weeks`
- Deadline : `07/05/2021 09:00 AM`
- Contributors: Joren Vervoort

## Mission objectives

- Use of tokenization, stemming and lemmatization for exploration of text-based datasets.
- Explore state-of-the-art algorithms for text summarization.
- Use of transformers.
- Evaluate the performance of pre-trained models.
- Development and deployment of the dashboard for text summarization.

### The Mission

A book publishing company is interested in increasing its online sales. The marketing department discovered the way people read is evolving and now rather than reading the full book, people prefer to get an overview of the main ideas expressed by the author. The digital era also means that customers want to get answers not from one book but from thousands immediately.

You have the task of developing an "AI-powered tool" able to "read" the content of any given book and make a summarization of the text. Also, the tool has to be deployed online since the company is looking to integrate the program into their website and connect it with the database where the books are stored.

## Description

### Installation

This project was designed to run in Google Colab. All installations that are needed, are within the .py files themselves. By this definition this repo should be downloaded and uploaded to your GoogleDrive in a map called: "Project_Algorhythm_Summarizer" in order to work.

### Files within the repository

A list of the following files are in this repo:
 - README.md
 - Webscraper.py
 - model_testing.py
 - app.py
 - templates (folder) containing: base.html, index.html & summary.html

#### README.md

This file contains an overal description of the project.

#### Webscraper.py

First a connection with your GoogleDrive will have to be made running the first two lines of code.

This file is used to scrape the html file of the text of any book you want from [Project Gutenberg](https://www.gutenberg.org/). Because there is no consistancy in html tag usage throughout the Gutenberg website for different books, the scraping of the text itself is customized for the following book: https://www.gutenberg.org/files/103/103-h/103-h.htm .

Ideas: A more global version could be maybe achieved by looking at the UTF-8 file instead of the html of each book. 

#### model_testing.py

First a connection with your GoogleDrive will have to be made running the first two lines of code.

Dataset

Because there was no clear result to compare a book summarization, I chose to go for a different dataset called: "News Summary". This dataset can be found on Kaggle following this link: https://www.kaggle.com/sunnysai12345/news-summary?select=news_summary.csv . This file contains news articles and their human-made summaries. In this way the evaluation of the models is not made on 1 book or example, but can be tracked on overall performance on a lot of articles, with different lengths.
! a map <<dataset>> should be created with downloaded file "news_summary.csv" inside !
 
File
 
This file first read and cleans the news_summary.csv file before usage. An df_ex will be created which contains only the cleaned text and summary of every article. (df_ab is also in this file BUT for now, remain unused. This is to check if a abstractive model would perform better is specialized cleaning of the text was performed)

A random article can be chosen by the user and will be summarized by the different extractive and abstractive summarization models included in this file.
extractive models: TextRank, LexRank, Luhn, LSA, KL-Sum
abstractive models: (T5), BART, GPT-2, XLM
This file is specially made so new models can be easily added for future exploration. 

The evaluation of the different models will be done based on the following metrics:
- the cosine spatial distance between the word embedded (BERT) human summary and the summary made by the different models
- ROUGE-1, ROUGE-2 and ROUGE-L
The ROUGE metrics are the most familiar used metrics in evaluating text summarization models. In these cases the ROUGE metrics are based on the 1-gram, 2-gram and l-gram overlay between the model-made summary and the human summary. This means comparing the words that are used in chunks of 1 word, 2 words and longest-matched words. The higher the score, the better. The problem with kind of metrics is it that it does not really check "text-similarity" but rather if two texts are identical or not. This is why I used a second metric called: "word embedded (BERT) cosine spatial distance". In this way the words of the human and model-made summary are embedded and checked for similarity in "meaning" rather than using the same words. This solves the problem of paraphrasing that often happen in summarizations. The lower the score of this metric, the more 2 summaries are simular in "meaning".

#### app.py

First a connection with your GoogleDrive will have to be made running the first two lines of code.

This file contains a prototype of the deployment of this project. It connects the different templates found in the templates folder to create a local webpage. In this prototype ngrok is used to run Flask in Google Colabs. clicking on the 2nd link (containing "...ngrok.io") you can reach the webpage. A GenSim (extractive) model is used to perform a text pasted in the "book title" input box. After submitting a summarization will be made by this model and shown on the webpage.
! This app is only to give a general idea of the deployement !

## Usage

## Result

Although this repo does not solve the problem, it is a great model evaluation method and a first stepping stone to achieve the desired result.

### Miscellaneous information

 [Project Gutenberg](https://www.gutenberg.org/) 



4. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - ⚠️**DATA SOURCES**
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)

## Evaluation criteria

### Technical

