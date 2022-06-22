# Noun-scraper
Removes all articles, verbs, adjectives, adverbs etc, leaving only a list of nouns mentioned in a text file

This is a python script that when executed will prompt the user to enter the name of a text file which should reside in the directory of the script. 

When the user enters a file name (including the .txt), the script will retrieve all of the words in that file. It will then cross reference them with a library of English nouns. This library consists of over 6800 nouns which cover 99% of spoken language. Unfortunately this does not cover names of people or places however I may consider adding this at a later date.

To account for noun plurals, I have simply added an 's' to the search. This will cover the vast majority of plurals but it is not a perfect solution. I have also not accounted for nouns that have been used as verbs or vice versa as this is beyond the scope of a simple text scraper. For example, I have included a short sentence example that can be used (shortExample.txt). In this sentence, the word 'hate' is used as a verb, however this word can also exist as a noun. Because of this, the text scraper has falsely identified this as a noun. 

After various sample tests, I have found that this scraper should retrieve anywhere between 80% and 95% of the nouns included in a text file (not including names of people or places). This is highly dependent on the source material i.e. its length, complexicity and especially its genre. Non-fiction materials use a plethora of jargon that which remains beyond the scope of the embedded noun library. I have not tested this scraper on academic sources but I anticipate less than 40% accuracy and would not recommend it in that regard.

All duplicates of nouns used in the text file will be removed before presenting a final list. The results will include all nouns in the text file, the amount of nouns and the time it took to return the results.

                                                      Future improvements:
                                                      
Add more libraries for people and places, inc. specific genre domains e.g. psychology

As stated before, verbs and nouns may share the same word however the way in which they appear within a sentence structure differs for the vast majority of the time. For example, the word 'play/plays' is both a noun and verb. I can set a condition where if 'play/plays' is preceded by a pronoun then it will be considered a verb and excluded from the results (i.e. {verbs} He plays, I play, they play, it plays vs {nouns} the play, a good play, fair play). This may increase the time it takes to return results.
