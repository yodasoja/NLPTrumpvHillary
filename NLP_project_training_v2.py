import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

input1 = open('tweet_training_set.txt', 'r')
trainingSet = input1.readlines()

#print(trainingSet)

size1 = len(trainingSet)

trainingSetLower = []

for i in range(size1):
    tempTweet = trainingSet[i].lower()
    trainingSetLower.append(tempTweet)

# print(trainingSetLower)

D_hashtag = ['strongertogether', 'voteforhillary', 'imwithher']
R_hashtag = ['draintheswamp', 'makeamericagreatagain']
feature_hashtag = []

D_keyword = ['grope', 'kkk']
R_keyword = ['benghazi', 'foundation']
feature_keyword = []

D_JJ = ['disgusting', 'racist']
R_JJ = ['dishonest', 'corrupt']
feature_JJ = []

D_beneficiary = ['top 1', 'white supremacist']
R_beneficiary = ['illegal immigrant', 'muslim immigrant']
feature_beneficiary = []


def hashtag(tweet1):
    len1 = len(tweet1)
    for i in range(len1-1):
        temp1 = tweet1[i]
        temp2 = tweet1[i+1]

        if ('#' == temp1) and ((temp2 == D_hashtag[0]) or (temp2 == D_hashtag[1]) or (temp2 == D_hashtag[2])):
            flag1 = 1
            break
        elif ('#' == temp1) and ((temp2 == R_hashtag[0]) or (temp2 == R_hashtag[1])):
            flag1 = -1
            break
        else:
            flag1 = 0

    return flag1


def keyword(tweet1):
    len1 = len(tweet1)
    for i in range(len1):
        temp1 = tweet1[i]

        if (temp1 == D_keyword[0]) or (temp1 == D_keyword[1]):
            flag2 = 1
            break
        elif (temp1 == R_keyword[0]) or (temp1 == R_keyword[1]):
            flag2 = -1
            break
    else:
        flag2 = 0

    return flag2


def jj(tweet_tokens, tweet_pos_tags):
    len1 = len(tweet_tokens)
    jj_list = []
    for myi in range(len1):
        if 'JJ' == tweet_pos_tags[myi][1]:
            jj_list.append(tweet_pos_tags[myi][0])

    len2 = len(jj_list)
    for myi in range(len1):
        if ('donald' == tweet_tokens[myi]) or ('trump' == tweet_tokens[myi]):
            name1 = 1
            break
        elif ('hillary' == tweet_tokens[myi]) or ('clinton' == tweet_tokens[myi]):
            name1 = -1
            break
        else:
            name1 = 0

    jj1 = 0
    for myi in range(len2):
        if (jj_list[myi] == D_JJ[0]) or (jj_list[myi] == D_JJ[1]):
            jj1 = 1
            break
        elif (jj_list[myi] == R_JJ[0]) or (jj_list[myi] == R_JJ[1]):
            jj1 = -1
            break
        else:
            jj1 = 0

    #print(JJ_list)

    if (1 == name1) and (1 == jj1):
        flag3 = 1
    elif (-1 == name1) and (-1 == jj1):
        flag3 = -1
    else:
        flag3 = 0

    return flag3


def beneficiary(tweet1):
    len_tweet=len(tweet1)
    beneTemp1=[]

    for i in range(len_tweet-2):
        if 'for' == tweet1[i]:
            beneTemp1.append(tweet1[i+1])
            beneTemp1.append(tweet1[i+2])
    # print(beneTemp1)

    if len(beneTemp1)>1:
        search_str1 = beneTemp1[0] + ' ' + beneTemp1[1]

        print('The beneficiaries are: ' + search_str1 + '.')

        for ss in wn.synsets(beneTemp1[0]):
            temp_str1=ss.hypernyms()
            print('The hypernymy of the '+str(beneTemp1[0])+' are:')
            print(temp_str1)
            temp_str11 = ss.hyponyms()
            print('The hyponymy of the ' + str(beneTemp1[0]) + ' are:')
            print(temp_str11)
            search_str1 = search_str1+' '+str(temp_str1)+' '+str(temp_str11)

        for ss in wn.synsets(beneTemp1[1]):
            temp_str2 = ss.hypernyms()
            print('The hypernymy of the ' + str(beneTemp1[1]) + ' are:')
            print(temp_str2)
            temp_str21 = ss.hyponyms()
            print('The hyponymy of the ' + str(beneTemp1[1]) + ' are:')
            print(temp_str21)
            search_str1 = search_str1+' '+str(temp_str2)+' '+str(temp_str21)

        # print(search_str1)

        if ('top 1' in search_str1) or ('white supremacist' in search_str1):
            flag5 = 1
        elif ('illegal immigrant' in search_str1) or ('muslim immigrant' in search_str1):
            flag5 = -1
        else:
            flag5 = 0

    else:
        print('The beneficiaries are N/A.')
        print('The hypernymy of the beneficiaries are N/A.')
        print('The hyponymy of the beneficiaries are N/A.')
        flag5 = 0

    return flag5


# feature 4
def syntactic_parse_np(tweet_tokens, tweet_pos_tags):
    #parse and look for key noun phrases
    len1 = len(tweet_tokens)
    np_list = []
    for myi in range(len1):
        if 'NP' == tweet_pos_tags[myi][1]:
            np_list.append(tweet_pos_tags[myi][0])

    len2 = len(np_list)
    for myi in range(len1):
        if ('donald' == tweet_tokens[myi]) or ('trump' == tweet_tokens[myi]):
            name1 = 1
            break
        elif ('hillary' == tweet_tokens[myi]) or ('clinton' == tweet_tokens[myi]):
            name1 = -1
            break
        else:
            name1 = 0

    jj1 = 0
    for myi in range(len2):
        if (np_list[myi] == D_JJ[0]) or (np_list[myi] == D_JJ[1]):
            jj1 = 1
            break
        elif (np_list[myi] == R_JJ[0]) or (np_list[myi] == R_JJ[1]):
            jj1 = -1
            break
        else:
            jj1 = 0

    # print(JJ_list)

    if (1 == name1) and (1 == jj1):
        flag4 = 1
    elif (-1 == name1) and (-1 == jj1):
        flag4 = -1
    else:
        flag4 = 0

    return flag4

for i in range(size1):
    tempTweet1 = trainingSetLower[i]
    tokens = nltk.word_tokenize(tempTweet1)
    print('The tokens are:')
    print(tokens)

    lmtzr = WordNetLemmatizer()
    len_tokens = len(tokens)
    lemmas = []
    pos_tags = []
    for j in range(len_tokens):
        temp_str1 = lmtzr.lemmatize(tokens[j])
        lemmas.append(temp_str1)

    print('The lemmas are:')
    print(lemmas)

    pos_tags = pos_tag(tokens)
    print('The POS tags are:')
    print(pos_tags)

    flag1_output = hashtag(tokens)
    flag2_output = keyword(lemmas)
    flag3_output = jj(tokens, pos_tags)
    flag5_output = beneficiary(tokens)

    feature_hashtag.append(flag1_output)
    feature_keyword.append(flag2_output)
    feature_JJ.append(flag3_output)
    feature_beneficiary.append(flag5_output)


#print(feature_hashtag)
#print(feature_keyword)
#print(feature_JJ)
#print(feature_beneficiary)

agent=['N/A', 'the electoral college', 'N/A', 'N/A', 'N/A',
       'N/A', 'N/A', 'N/A', 'N/A', 'i',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
       'the racist trump supporters', 'N/A', 'kareem abdul-jabbar', 'racist trump fans', 'N/A',
       'donald', 'trump', 'trump', 'N/A', 'N/A',
       'women', 'intelligent women', 'southern women', 'women', 'latino',
       'N/A', 'the islamist 5th column', 'N/A', 'N/A', 'N/A',
       'N/A', 'hillary clinton', 'N/A', 'N/A', 'hillary clinton',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
       'crooked hillary', 'N/A', 'N/A', 'N/A', 'N/A',
       'N/A', 'N/A', 'democrats', 'someone', 'she',
       'veterans', 'veterans', '10000 veterans', 'all military and veterans', 'cops',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
       'N/A', 'N/A', 'N/A', 'N/A', 'N/A']

len_list1 = len(agent)

feature_agent = []

for i in range(len_list1):
    temp1 = agent[i]
    #print(temp1)

    if 'N/A' == temp1:
        print('The agents are N/A.')
        print('The hypernymy of the agents are N/A.')
        print('The hyponymy of the agents are N/A.')
        flag6 = 0
        feature_agent.append(flag6)

    else:
        search_str1 = temp1
        print('The agents are: ' + str(temp1) + '.')
        temp2 = temp1.split()
        #print(temp2)
        len_temp2 = len(temp2)
        for j in range(len_temp2):
            temp3 = temp2[j]
            #print(temp3)

            for ss in wn.synsets(temp3):
                temp_str1 = ss.hypernyms()
                print('The hypernymy of the ' + str(temp3) + ' are:')
                print(temp_str1)
                temp_str11 = ss.hyponyms()
                print('The hyponymy of the ' + str(temp3) + ' are:')
                print(temp_str11)
                search_str1 = search_str1 + ' ' + str(temp_str1) + ' ' + str(temp_str11)

    # print(search_str1)

        if ('women' in search_str1) or ('latinos' in search_str1):
            flag6 = 1
            feature_agent.append(flag6)
        elif ('veterans' in search_str1) or ('cops' in search_str1):
            flag6 = -1
            feature_agent.append(flag6)
        else:
            flag6 = 0
            feature_agent.append(flag6)

output1 = open('feature1_hashtag.txt', 'w')
for i in range(size1):
    temp1 = feature_hashtag[i]
    output1.write(str(temp1)+" ")
output1.close()

output2 = open('feature2_keyword.txt', 'w')
for i in range(size1):
    temp2 = feature_keyword[i]
    output2.write(str(temp2)+" ")
output2.close()

output3 = open('feature3_JJ.txt', 'w')
for i in range(size1):
    temp3 = feature_JJ[i]
    output3.write(str(temp3)+" ")
output3.close()

output5 = open('feature5_BENEFICIARY.txt', 'w')
for i in range(size1):
    temp5 = feature_beneficiary[i]
    output5.write(str(temp5)+" ")
output5.close()

output6 = open('feature6_AGENT.txt', 'w')
for i in range(size1):
    temp6 = feature_agent[i]
    output6.write(str(temp6)+" ")
output6.close()
