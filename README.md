# Coding Challenge

### 1. Python script to check the [“Getting to Philosophy”](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) law.
Requirements:
  - Python 3.x
  - bs4 package (BeautifulSoup)

Clicking on the first link in the main body of a Wikipedia article and repeating the process for subsequent articles would usually lead to the article Philosophy.

The program should receive a Wikipedia link as an input, go to another normal link and repeat this process until either Philosophy page is reached, or we are in an article without any outgoing wikilinks, or stuck in a loop.

A “normal link” is a link from the main page article, not in a box, is blue (red is for non-existing articles), not in parentheses, not italic and not a footnote. You don’t have to check style tables or other fancy things, it is enough that the script works with current wikipedia style (for example you can use ‘class’ attribute in Wikipedia tags). For easy validation, please print all visited links to the standard output.

Use a 0.5 second timeout between queries to avoid heavy load on Wikipedia (sleep function from time module).

#### How to use
Run the script `wiki_loop_philosophy.py` with up to 2 arguments (if not stated then default value will be used):
  - 1st: starting Wikipedia URL (default: [random](https://en.wikipedia.org/wiki/Special:Random))
  - 2nd: max loop before program is terminated (default: 100)

Example:
```sh
$ python wiki_loop_philosophy.py 'https://en.wikipedia.org/wiki/Character_actor' 150
```

Output:


![N|Solid](https://i1.wp.com/joshsteveth.files.wordpress.com/2018/09/wiki_loop.png?ssl=1&w=450)

If Philosophy page can't be reached (either because of infinite loop between 2 pages or max loop or absence of normal links), an error will be raised accordingly.

Example:
```sh
$ python wiki_loop_philosophy.py 'https://en.wikipedia.org/wiki/American_football'
```
Output:


![N|Solid](https://i1.wp.com/joshsteveth.files.wordpress.com/2018/09/wiki_loop_error.png?ssl=1&w=450)



### 2. Create a Jupyter notebook with a simple analysis based on [Twitter Sentiment Analysis Training Corpus](http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/):.

Dataset: [Twitter Sentiment Analysis Dataset](http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip)

Tasks:

— Show the top-10 most positive words, top-10 negative words (words more frequent with positive and negative labels respectively). 

— Check the Zipf law (https://en.wikipedia.org/wiki/Zipf%27s_law: the frequency of any word is inversely proportional to its rank in the frequency table), show it using a plot. 

— Write a simple classifier to predict sentiment, describe your approach and what can be done to improve the results.
