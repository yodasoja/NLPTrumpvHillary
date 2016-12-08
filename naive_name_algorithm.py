input1 = open('tweet_testing_set.txt', 'r')
testingSet=input1.readlines()
#print(testingSet)

size1 = len(testingSet)

testingSetLower = []

for i in range(size1):
    tempTweet = testingSet[i].lower()
    testingSetLower.append(tempTweet)

D_name = ['hillary', 'clinton']
R_name = ['donald', 'trump']

def naive_name(tweet1):
    len1 = len(tweet1)
    flag1 = 0
    for i in range(len1):
        if (tweet1[i] == D_name[0]) or (tweet1[i] == D_name[1]):
            flag1 += 1
            break
        elif (tweet1[i] == R_name[0]) or (tweet1[i] == R_name[1]):
            flag1 -= 1
            break
        else:
            flag1 += 0
            break

    if flag1 >= 1:
        flag1 = 1
    elif flag1 <= -1:
        flag1 = -1
    else:
        flag1 = 0

    return flag1

analysis_value = []
for i in range(size1):
    tweetList = testingSetLower[i].split()
    flag_output = naive_name(tweetList)
    analysis_value.append(str(flag_output))

input2 = open('classification_testing_set.txt', 'r')
expectedSet = input2.readlines()

expected_value = expectedSet[0].split()

mistake_count = 0
for i in range(size1):
    if (analysis_value[i] != expected_value[i]):
        mistake_count = mistake_count+1

error_rate = float(mistake_count)/size1

false_positive_hillary = []
false_negative_hillary = []
false_positive_trump = []
false_negative_trump = []
false_positive_neutral = []
false_negative_neutral = []
count_positive_hillary = 0
count_negative_hillary = 0
count_positive_trump = 0
count_negative_trump = 0
count_positive_neutral = 0
count_negative_neutral = 0

for i in range(size1):
    if ((expected_value[i] != '1') and (analysis_value[i] == '1')):
        false_positive_hillary.append(str(i))
        count_positive_hillary = count_positive_hillary + 1
    elif ((expected_value[i] == '1') and (analysis_value[i] != '1')):
        false_negative_hillary.append(str(i))
        count_negative_hillary = count_negative_hillary + 1
    elif ((expected_value[i] != '-1') and (analysis_value[i] == '-1')):
        false_positive_trump.append(str(i))
        count_positive_trump = count_positive_trump + 1
    elif ((expected_value[i] == '-1') and (analysis_value[i] != '-1')):
        false_negative_trump.append(str(i))
        count_negative_trump = count_negative_trump + 1
    elif ((expected_value[i] != '0') and (analysis_value[i] == '0')):
        false_positive_neutral.append(str(i))
        count_positive_neutral = count_positive_neutral + 1
    elif ((expected_value[i] == '0') and (analysis_value[i] != '0')):
        false_negative_neutral.append(str(i))
        count_negative_neutral = count_negative_neutral + 1

print('There are ' + str(count_positive_hillary) + ' tweets are mistakenly classified as pro-Hillary.')
print('The indices for those mistakenly classified tweets are: ' + str(false_positive_hillary))
print('There are ' + str(count_negative_hillary) + ' tweets are mistakenly not classified as pro-Hillary.')
print('The indices for those mistakenly classified tweets are: ' + str(false_negative_hillary))

print('There are ' + str(count_positive_trump) + ' tweets are mistakenly classified as pro-Trump.')
print('The indices for those mistakenly classified tweets are: ' + str(false_positive_trump))
print('There are ' + str(count_negative_trump) + ' tweets are mistakenly not classified as pro-Trump.')
print('The indices for those mistakenly classified tweets are: ' + str(false_negative_trump))

print('There are ' + str(count_positive_neutral) + ' tweets are mistakenly classified as neutral.')
print('The indices for those mistakenly classified tweets are: ' + str(false_positive_neutral))
print('There are ' + str(count_negative_neutral) + ' tweets are mistakenly not classified as neutral.')
print('The indices for those mistakenly classified tweets are: ' + str(false_negative_neutral))


print("The error rate for the testing set using the naive algorithm is: " + str(mistake_count) + " mistakes / " +
      str(size1) + " total tweets = " + str(round(error_rate*100, 2)) + '%.')

