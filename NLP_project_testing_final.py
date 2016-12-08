import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# create an array with tweets
input1 = open('tweet_testing_set.txt', 'r')
testingSet = input1.readlines()
size1 = len(testingSet)
testingSetLower = []
for i in range(size1):
    tempTweet = testingSet[i].lower()
    testingSetLower.append(tempTweet)

D_hashtag = ['strongertogether', 'voteforhillary', 'imwithher']
R_hashtag = ['draintheswamp', 'makeamericagreatagain']
feature_hashtag = []

D_keyword = ['grope', 'kkk']
R_keyword = ['benghazi', 'foundation']
feature_keyword = []

D_JJ = ['disgusting', 'racist']
R_JJ = ['dishonest', 'corrupt']
feature_JJ = []

D_NP = ['racist trump', 'narcissistic trump']
R_NP = ['crooked hillary', 'dishonest hillary']
feature_NP = []

D_beneficiary = ['top 1', 'white supremacist']
R_beneficiary = ['illegal immigrant', 'muslim immigrant']
feature_beneficiary = []

agent = ['N/A', 'republicans', 'N/A', 'trump', 'N/A', 'i',
         'i', 'N/A', 'trump supporters', 'narcissistic trump', 'we', 'a narcissistic trump',
         'trump', 'trump','N/A', 'latinos', 'latinos', 'latinos',
         'N/A', 'N/A', 'everyone', 'N/A', 'i', 'N/A',
         'lots of liars and cheaters', 'N/A', 'N/A', 'crooked hillary supporters', 'crooked hillary', 'N/A',
         'hard working americans', 'hillary', 'crooked hillary', 'cops', 'cops', 'cops',
         'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
         'N/A', 'N/A', 'N/A', 'N/A', 'N/A']

len_list1 = len(agent)

feature_agent = []


def hashtag(tweet1):
    len1 = len(tweet1)
    flag1 = 0
    for myi in range(len1 - 1):
        mytemp1 = tweet1[myi]
        mytemp2 = tweet1[myi + 1]

        if ((mytemp1 == '#') and ((mytemp2 == D_hashtag[0]) or (mytemp2 == D_hashtag[1]) or (mytemp2 == D_hashtag[2]))):
            flag1 += 1
            print('Hashtag found: ' + mytemp1 + mytemp2)
        elif ((mytemp1 == '#') and ((mytemp2 == R_hashtag[0]) or (mytemp2 == R_hashtag[1]))):
            flag1 -= 1
            print('Hashtag found: ' + mytemp1 + mytemp2)
        else:
            flag1 += 0

    if flag1 <= 1:
        flag1 = 1
    elif flag1 == 0:
        flag1 = 0
        print('Hashtag unidentified.')
    else:
        flag1 = -1

    return flag1


def keyword(tweet1):
    len1 = len(tweet1)
    flag2 = 0
    tempstring = ''
    for myi in range(len1):
        mytemp1 = tweet1[myi]

        if (mytemp1 == D_keyword[0]) or (mytemp1 == D_keyword[1]):
            flag2 += 1
            tempstring += mytemp1 + ', '
        elif (mytemp1 == R_keyword[0]) or (mytemp1 == R_keyword[1]):
            flag2 -= 1
            tempstring += mytemp1 + ', '
        else:
            flag2 += 0
    if len(tempstring) > 0:
        tempstring = tempstring[:-2]
        print('Keywords found: ' + tempstring)
    else:
        print('No keywords found.')

    if flag2 <= 1:
        flag2 = 1
    elif flag2 == 0:
        flag2 = 0
    else:
        flag2 = -1

    return flag2


def JJ(tweet_tokens, tweet_pos_tags):
    len1 = len(tweet_tokens)
    JJ_list = []
    for myi in range(len1):
        if tweet_pos_tags[myi][1] == 'JJ':
            JJ_list.append(tweet_pos_tags[myi][0])

    len2 = len(JJ_list)
    name1 = 0
    for myi in range(len1):
        if (tweet_tokens[myi] == 'donald') or (tweet_tokens[myi] == 'trump'):
            name1 += 1
        elif (tweet_tokens[myi] == 'hillary') or (tweet_tokens[myi] == 'clinton'):
            name1 -= 1
        else:
            name1 += 0

    if name1 <= 1:
        name1 = 1
    elif name1 == 0:
        name1 = 0
    else:
        name1 = -1

    tempstring = ''
    JJ1 = 0
    for myi in range(len2):
        if (JJ_list[myi] == D_JJ[0]) or (JJ_list[myi] == D_JJ[1]):
            JJ1 += 1
            tempstring += JJ_list[myi] + ', '
        elif (JJ_list[myi] == R_JJ[0]) or (JJ_list[myi] == R_JJ[1]):
            JJ1 -= 1
            tempstring += JJ_list[myi] + ', '
        else:
            JJ1 += 0

    if len(tempstring) > 0:
        tempstring = tempstring[:-2]
        print('JJs found: ' + tempstring)
    else:
        print('No JJs found associated with candidate names.')

    if JJ1 <= 1:
        JJ1 = 1
    elif JJ1 == 0:
        JJ1 = 0
    else:
        JJ1 = -1

    if (name1 == 1) and (JJ1 == 1):
        flag3 = 1
    elif (name1 == -1) and (JJ1 == -1):
        flag3 = -1
    else:
        flag3 = 0

    return flag3


def NP(lenTweet, tweet_pos_tags):

    NP_list = []
    for myi in range(lenTweet-1):
        if ('JJ' == tweet_pos_tags[myi][1]) and ('NN' == tweet_pos_tags[myi+1][1]):
            temp_NP = tweet_pos_tags[myi][0] + ' ' + tweet_pos_tags[myi+1][0]
            NP_list.append(temp_NP)

    len2 = len(NP_list)

    if len2 == 0:
        print('No JJ_NN NP structure was found.')
        flag4 = 0
    else:
        for myi in range(len2):
            if (NP_list[myi] == D_NP[0]) or (NP_list[myi] == D_NP[1]):
                print('JJ_NN NP structure is:')
                print(NP_list[myi])
                flag4 = 1
                break
            elif (NP_list[myi] == R_NP[0]) or (NP_list[myi] == R_NP[1]):
                print('JJ_NN NP structure is:')
                print(NP_list[myi])
                flag4 = -1
                break
            else:
                print('JJ_NN NP structure is:')
                print(NP_list[myi])
                flag4 = 0

    return flag4


def beneficiary(tweet1):
    len_tweet = len(tweet1)
    beneTemp1 = []

    for i in range(len_tweet-2):
        if (tweet1[i] == 'for'):
            beneTemp1.append(tweet1[i+1])
            beneTemp1.append(tweet1[i+2])

    if (len(beneTemp1) >1 ):
        search_str1 = beneTemp1[0] + ' ' + beneTemp1[1]

        print('The beneficiaries are: ' + search_str1 + '.')

        for ss in wn.synsets(beneTemp1[0]):
            temp_str1 = ss.hypernyms()
            print('The hypernymy of the ' + str(beneTemp1[0]) + ' are:')
            print(temp_str1)
            temp_str11 = ss.hyponyms()
            print('The hyponymy of the ' + str(beneTemp1[0]) + ' are:')
            print(temp_str11)
            search_str1 = search_str1 + ' ' + str(temp_str1) + ' ' + str(temp_str11)

        for ss in wn.synsets(beneTemp1[1]):
            temp_str2 = ss.hypernyms()
            print('The hypernymy of the ' + str(beneTemp1[1]) + ' are:')
            print(temp_str2)
            temp_str21 = ss.hyponyms()
            print('The hyponymy of the ' + str(beneTemp1[1]) + ' are:')
            print(temp_str21)
            search_str1 = search_str1 + ' ' + str(temp_str2) + ' ' + str(temp_str21)


        if (('top 1' in search_str1) or ('white supremacist' in search_str1)):
            flag5 = 1
        elif (('illegal immigrant' in search_str1) or ('muslim immigrant' in search_str1)):
            flag5 = -1
        else:
            flag5 = 0

    else:
        print('The beneficiaries are N/A.')
        print('The hypernymy of the beneficiaries are N/A.')
        print('The hyponymy of the beneficiaries are N/A.')
        flag5 = 0

    return flag5

for i in range(size1):
    print('\n')

    tempTweet1 = testingSetLower[i]
    tempTweet1 = tempTweet1.encode('ascii', 'ignore').decode('ascii')
    print('The tweet is:')
    print(tempTweet1)

    tokens = nltk.word_tokenize(tempTweet1)
    print('The tokens are:')
    print(tokens)

    lmtzr = WordNetLemmatizer()
    len_tokens = len(tokens)
    lemmas = []
    pos_tags = []
    for j in range(len_tokens):
        temp_str1=lmtzr.lemmatize(tokens[j])
        lemmas.append(temp_str1)

    print('The lemmas are:')
    print(lemmas)

    pos_tags=pos_tag(tokens)
    print('The POS tags are:')
    print(pos_tags)

    flag1_output = hashtag(tokens)
    flag2_output = keyword(lemmas)
    flag3_output = JJ(tokens, pos_tags)
    flag4_output = NP(len_tokens, pos_tags)
    flag5_output = beneficiary(tokens)

    feature_hashtag.append(flag1_output)
    feature_keyword.append(flag2_output)
    feature_JJ.append(flag3_output)
    feature_NP.append(flag4_output)
    feature_beneficiary.append(flag5_output)

    temp1 = agent[i]

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

        len_temp2 = len(temp2)
        for j in range(len_temp2):
            temp3 = temp2[j]

            for ss in wn.synsets(temp3):
                temp_str1 = ss.hypernyms()
                print('The hypernymy of ' + str(temp3) + ' are:')
                print(temp_str1)
                temp_str11 = ss.hyponyms()
                print('The hyponymy of ' + str(temp3) + ' are:')
                print(temp_str11)
                search_str1 = search_str1 + ' ' + str(temp_str1) + ' ' + str(temp_str11)

        if ('women' in search_str1) or ('latinos' in search_str1):
            flag6 = 1
            feature_agent.append(flag6)
        elif ('veterans' in search_str1) or ('cops' in search_str1):
            flag6 = -1
            feature_agent.append(flag6)
        else:
            flag6 = 0
            feature_agent.append(flag6)


output1 = open('test_hashtag.txt', 'w')
for i in range(size1):
    temp1 = feature_hashtag[i]
    output1.write(str(temp1) + " ")
output1.close()

output2 = open('test_keyword.txt', 'w')
for i in range(size1):
    temp2 = feature_keyword[i]
    output2.write(str(temp2) + " ")
output2.close()

output3 = open('test_JJ.txt', 'w')
for i in range(size1):
    temp3 = feature_JJ[i]
    output3.write(str(temp3) + " ")
output3.close()

output4 = open('test_NP.txt', 'w')
for i in range(size1):
    temp4 = feature_NP[i]
    output4.write(str(temp4) + " ")
output4.close()

output5 = open('test_BENEFICIARY.txt', 'w')
for i in range(size1):
    temp5 = feature_beneficiary[i]
    output5.write(str(temp5) + " ")
output5.close()

output6 = open('test_AGENT.txt', 'w')
for i in range(size1):
    temp6 = feature_agent[i]
    output6.write(str(temp6) + " ")
output6.close()

print('\n')
