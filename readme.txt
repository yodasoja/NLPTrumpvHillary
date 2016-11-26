For the NLP project, we have collected 126 U.S. election-related tweets and our goal is to classify them as pro-Clinton, pro-Trump or neutral.
The 126 tweets were divided into two groups: the training set (80) and the testing set (46).

We proposed 6 features:
(1).hashtag
pro-Clinton: #strongertogether, #voteforhillary, #imwithher
pro-Trump: #draintheswamp, #makeamericagreatagain
(2).keyword
pro-Clinton: grope, KKK
pro-Trump: benghazi, foundation
(3).POS (JJ)
pro-Clinton: disgusting, racist, sexist (Donald Trump)
pro-Trump: dishonest, corrupt (Hillary Clinton)
(4).NP
pro-Clinton: racist Trump, narcissistic Trump
pro-Trump: crooked Hillary, dishonest Hillary
(5).Beneficiary
pro-Clinton: top 1%
pro-Trump: illegal immigrants, muslim immigrants
(6).Agent
pro-Clinton: women, latinos
pro-Trump: veterans, cops

For the training set (80 in total), 30 are pro-Clinton (5 tweets for each of the 6 features), 30 are pro-Trump (5 tweets for each of the 6 features), and 20 are neutral.
The 80 tweets are saved as tweet_training_set.txt. The classification results are saved in classification_training_set.txt.

For the testing set (46 in total), 18 are pro-Clinton (3 tweets for each of the 6 features), 18 are pro-Trump (3 tweets for each of the 6 features), and 10 are neutral.
The 46 tweets are saved as tweet_testing_set.txt. The classification results are saved in calssification_testing_set.txt.

Step 1: using naive name-based keyword search algorithm:
If a tweet contains 'hillary' or 'clinton', we classify it as pro-Clinton. If a tweet contains 'donald' or 'trump', we claddify it as pro-Trump.
The code is naive_name_algorithm. When we apply this algorithm on the tweet_testing_set.txt, the error rate is 65.2%.

Step 2: generating the 6 feature vectors for both training set and testing set:
The codes NLP_project_training_v2.py and NLP_project_testing_v2.py are written to extract the feature vectors for the training and testing sets.

(1). features 1 and 2:
In order to search for the hashtags and keywords, we have converted all tweets to lowercase, and then use NLTK library for tokenization (lexical feature 1) and lemmatization (lexical feature 2).
Both tokenization and lemmatization results will be displayed on the terminal for demonstration.
Also, the feature vectors 1 and 2 will be saved into external files, named as feature1_hashtag.txt and feature2_keyword.txt for the training set, and test_hashtag.txt and test_keyword.txt for the testing set.

(2). feature 3:
We used the NLTK library for the POS tagging (syntactic feature 1), which results will be displayed on the terminal for demonstration.
Also, the feature vectors 3 will be saved into external files, named as feature3_JJ.txt for the training set, and test_JJ.txt for the testing set.

(3). features 5 and 6:
We identified the Beneficiaries by extracting the lexical entities after the keyword "for", and also mannually identified the Agents and saved it into a list named as 'agent'.
It is hypothesized that the hypernyms and hyponyms of the beneficiaries and agents may fit our search target, such as 'women' and 'veteran'. Thus, we used the NLTK library to perform the hypernymy (semantic feature 1) and hyponymy (semantic feature 2).
Both hypernyms and hyponyms are displayed on the terminal for demonstration.
Also, the feature vectors 5 and 6 will be saved into external files, named as feature5_BENEFICIARY.txt and feature6_AGENT.txt for the training set, and test_BENEFICIARY.txt and test_AGENT.txt for the testing set.

Step 3: using naive Bayesian algorithm:
We then use the feature vectors for the training set to calculate all required conditional probabilities, and then applied it on the testing set.
The error rate for the testing set now has been reduced to 13.7%.

___
remaining work:
(1).Please use NLTK or Stanford CoreNLP to perform the syntactic parsing for both the training and testing sets, and then save the feature vectors 3 into the external files as feature4_NP.txt for the training set, and test_NP.txt for the testing set.
After that, I can re-run the naive Bayesian to update the error rate.

(2).Please use this readme as the starting materials to expand it to the final report. I can help later for updates and modifications such as potantial technical difficulties and alternative solutions.




