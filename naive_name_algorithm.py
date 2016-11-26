input1=open('tweet_testing_set.txt','r')
testingSet=input1.readlines()

#print(testingSet)

size1=len(testingSet)

testingSetLower=[]

for i in range(size1):
    tempTweet=testingSet[i].lower()
    testingSetLower.append(tempTweet)

D_name=['hillary','clinton']
R_name=['donald','trump']

def naive_name(tweet1):
    len1=len(tweet1)
    for i in range(len1):
        if ((tweet1[i]==D_name[0]) or (tweet1[i]==D_name[1])):
            flag1=1
            break
        elif ((tweet1[i]==R_name[0]) or (tweet1[i]==R_name[1])):
            flag1=-1
            break
        else:
            flag1=0

    return flag1

analysis_value=[]
for i in range(size1):
    tweetList=testingSetLower[i].split()
    flag_output=naive_name(tweetList)
    analysis_value.append(str(flag_output))

input2=open('classification_testing_set.txt','r')
expectedSet=input2.readlines()

expected_value=expectedSet[0].split()

mistake_count=0
for i in range(size1):
    if (analysis_value[i]!=expected_value[i]):
        mistake_count=mistake_count+1

error_rate=float(mistake_count)/size1

print("The error rate for the testing set using the naive algorithm is: "+str(error_rate)+'.')

