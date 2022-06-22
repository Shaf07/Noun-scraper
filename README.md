# Noun-scraper
Removes all articles, verbs, adjectives, adverbs etc, leaving only a list of nouns mentioned in a text file

This is a python script that when run will prompt the user to enter the name of a text file which should reside in the directory of the script. 

When the user enters a file name (including the .txt), the script will retrieve all of words in that file. It will then cross reference them with a preset list of English nouns. This library consists of over 6800 nouns which cover 99% of spoken language. Unfortunately this does not cover names of people or places however I may consider adding this at a later date.

To account for noun plurals, I have simply added an 's' to the search. This will cover the vast majority of plurals but it is not a perfect solution. I have also not accounted for nouns that have been used as verbs or vice versa as this is beyond the scope of a simple text scraper. After various sample tests, I have found that this scraper should retrieve anywhere between 85% and 95% of the nouns included in a text file (not including names of people or places).

All duplicates of nouns used in the text file will be removed before presenting a final list. The results will include all nouns, the amount of nouns returned and the time it took to retrieve the results.
