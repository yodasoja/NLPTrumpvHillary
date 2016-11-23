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

I collected 48 pro-Clinton tweets, 8 tweets for each feature. Similarly, I collected 48
pro-Trump tweets, 8 tweets for each feature. In addition, I collected 30 neutral tweets. This is saved as the original_tweets.txt.

For the training set (tweet_training_set.txt), I included 30 out of the 48 pro-Clinton tweets, 5 tweets for each feature. Similarly, I included 30 out of the 48 pro-Trump tweets, 5 tweets for each feature. In addition, I included 20 out of the 30 neutral tweets.

For the NLP_project_v1, for each feature, we will write a function. So far, I have finished the hashtag, keyword and JJ functions, which use and display three mandatory NLP features (tokenization, lemmatization and POS tagging). The results will be displayed for the project demo. I also write the vector results for each feature into an external txt file (feature1_hashtag.txt, feature2_keyword.txt and feature3_JJ.txt). These vectors will be used for the machine learning process (Naive Bayesian Analysis).

Next, I will write codes for the naive analysis which simply use names "Hillary CLinton" and "Donald Trump".

I will also revise my NLP_project_v1.py to include the syntactic parsing feature and the external feature file.

I will also help write the Machine Learning training/testing code.

You can focus on the features (5) and (6), which essentially one semantic function for labeling of Beneficiaries and Agents.

