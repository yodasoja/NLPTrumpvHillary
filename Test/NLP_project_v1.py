import nltk
from nltk import word_tokenize,pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

input1=open('tweet_training_set.txt','r')
trainingSet=input1.readlines()

#print(trainingSet)

size1=len(trainingSet)

trainingSetLower=[]

for i in range(size1):
    tempTweet=trainingSet[i].lower()
    trainingSetLower.append(tempTweet)

#print(trainingSetLower)

D_hashtag=['strongertogether','voteforhillary','imwithher']
R_hashtag=['draintheswamp','makeamericagreatagain']
feature_hashtag=[]

D_keyword=['grope','kkk']
R_keyword=['benghazi','foundation']
feature_keyword=[]

D_JJ=['disgusting','racist']
R_JJ=['dishonest','corrupt']
feature_JJ=[]

def hashtag(tweet1):
    len1=len(tweet1)
    for i in range(len1-1):
        temp1=tweet1[i]
        temp2=tweet1[i+1]

        if ((temp1=='#') and ((temp2==D_hashtag[0]) or (temp2==D_hashtag[1]) or (temp2==D_hashtag[2]))):
            flag1=1
            break
        elif ((temp1=='#') and ((temp2==R_hashtag[0]) or (temp2==R_hashtag[1]))):
            flag1=-1
            break
        else:
            flag1=0

    return flag1

def keyword(tweet1):
    len1=len(tweet1)
    for i in range(len1):
        temp1=tweet1[i]

        if ((temp1==D_keyword[0]) or (temp1==D_keyword[1])):
            flag2=1
            break
        elif ((temp1==R_keyword[0]) or (temp1==R_keyword[1])):
            flag2=-1
            break
    else:
        flag2=0

    return flag2

def JJ(tweet1,tweet2):
    len1=len(tweet1)
    JJ_list=[]
    for i in range(len1):
        if (tweet2[i][1]=='JJ'):
            JJ_list.append(tweet2[i][0])

    len2=len(JJ_list)
    for i in range(len1):
        if ((tweet1[i]=='donald') or (tweet1[i]=='trump')):
            name1=1
            break
        elif ((tweet1[i]=='hillary') or (tweet1[i]=='clinton')):
            name1=-1
            break
        else:
            name1=0

    JJ1=0
    for i in range(len2):
        if ((JJ_list[i]==D_JJ[0]) or (JJ_list[i]==D_JJ[1])):
            JJ1=1
            break
        elif ((JJ_list[i]==R_JJ[0]) or (JJ_list[i]==R_JJ[1])):
            JJ1=-1
            break
        else:
            JJ1=0

    #print(JJ_list)

    if ((name1==1) and (JJ1==1)):
        flag3=1
    elif ((name1==-1) and (JJ1==-1)):
        flag3=-1
    else:
        flag3=0

    return flag3


for i in range(size1):
    tempTweet1=trainingSetLower[i]
    tokens=nltk.word_tokenize(tempTweet1)
    print(tokens)

    lmtzr=WordNetLemmatizer()
    len_tokens=len(tokens)
    lemmas=[]
    pos_tags=[]
    for j in range(len_tokens):
        temp_str1=lmtzr.lemmatize(tokens[j])
        lemmas.append(temp_str1)

    print(lemmas)

    pos_tags=pos_tag(tokens)
    print(pos_tags)


    flag1_output=hashtag(tokens)
    flag2_output=keyword(lemmas)
    flag3_output=JJ(tokens, pos_tags)
    feature_hashtag.append(flag1_output)
    feature_keyword.append(flag2_output)
    feature_JJ.append(flag3_output)


#print(feature_hashtag)
#print(feature_keyword)
#print(feature_JJ)

output1=open('feature1_hashtag.txt','w')
for i in range(size1):
    temp1=feature_hashtag[i]
    output1.write(str(temp1)+" ")
output1.close()

output2=open('feature2_keyword.txt','w')
for i in range(size1):
    temp2=feature_keyword[i]
    output2.write(str(temp2)+" ")
output2.close()

output3=open('feature3_JJ.txt','w')
for i in range(size1):
    temp3=feature_JJ[i]
    output3.write(str(temp3)+" ")
output3.close()