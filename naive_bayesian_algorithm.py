input1 = open('feature1_hashtag.txt', 'r')
set1 = input1.readlines()
feature1 = set1[0].split()

input2 = open('feature2_keyword.txt', 'r')
set2 = input2.readlines()
feature2 = set2[0].split()

input3 = open('feature3_JJ.txt', 'r')
set3 = input3.readlines()
feature3 = set3[0].split()

input4 = open('feature4_NP.txt', 'r')
set4 = input4.readlines()
feature4 = set4[0].split()

input5 = open('feature5_BENEFICIARY.txt', 'r')
set5 = input5.readlines()
feature5 = set5[0].split()

input6 = open('feature6_AGENT.txt', 'r')
set6 = input6.readlines()
feature6 = set6[0].split()

input7 = open('classification_training_set.txt', 'r')
set7 = input7.readlines()
output = set7[0].split()

size1 = len(output)

hillary = []
trump = []
neutral = []

for i in range(size1):
    if (output[i] == '1'):
        hillary.append(i)
    elif (output[i] == '-1'):
        trump.append(i)
    elif (output[i] == '0'):
        neutral.append(i)

h_size = len(hillary)
h = h_size/float(size1)

d_size = len(trump)
d = d_size/float(size1)

n_size = len(neutral)
n = n_size/float(size1)

def conditionalP(index, feature):
    f_h = 0
    f_d = 0
    f_n = 0

    len1 = len(index)

    for i in range(len1):
        index1 = index[i]
        if (feature[index1] == '1'):
            f_h = f_h + 1
        elif (feature[index1] == '-1'):
            f_d = f_d + 1
        elif (feature[index1] == '0'):
            f_n = f_n + 1

    f_h = f_h/float(len1)
    f_d = f_d/float(len1)
    f_n = f_n/float(len1)

    return {'output1':f_h, 'output2':f_d, 'output3':f_n}

readout1 = conditionalP(hillary, feature1)
h_f1_h = readout1['output1']
h_f1_d = readout1['output2']
h_f1_n = readout1['output3']

readout2 = conditionalP(hillary, feature2)
h_f2_h = readout2['output1']
h_f2_d = readout2['output2']
h_f2_n = readout2['output3']

readout3 = conditionalP(hillary, feature3)
h_f3_h = readout3['output1']
h_f3_d = readout3['output2']
h_f3_n = readout3['output3']

readout4 = conditionalP(hillary, feature4)
h_f4_h = readout4['output1']
h_f4_d = readout4['output2']
h_f4_n = readout4['output3']

readout5 = conditionalP(hillary, feature5)
h_f5_h = readout5['output1']
h_f5_d = readout5['output2']
h_f5_n = readout5['output3']

readout6 = conditionalP(hillary, feature6)
h_f6_h = readout6['output1']
h_f6_d = readout6['output2']
h_f6_n = readout6['output3']

readout7 = conditionalP(trump, feature1)
d_f1_h = readout7['output1']
d_f1_d = readout7['output2']
d_f1_n = readout7['output3']

readout8 = conditionalP(trump, feature2)
d_f2_h = readout8['output1']
d_f2_d = readout8['output2']
d_f2_n = readout8['output3']

readout9 = conditionalP(trump, feature3)
d_f3_h = readout9['output1']
d_f3_d = readout9['output2']
d_f3_n = readout9['output3']

readout10 = conditionalP(trump, feature4)
d_f4_h = readout10['output1']
d_f4_d = readout10['output2']
d_f4_n = readout10['output3']

readout11 = conditionalP(trump, feature5)
d_f5_h = readout11['output1']
d_f5_d = readout11['output2']
d_f5_n = readout11['output3']

readout12 = conditionalP(trump, feature6)
d_f6_h = readout12['output1']
d_f6_d = readout12['output2']
d_f6_n = readout12['output3']

readout13 = conditionalP(neutral, feature1)
n_f1_h = readout13['output1']
n_f1_d = readout13['output2']
n_f1_n = readout13['output3']

readout14 = conditionalP(neutral, feature2)
n_f2_h = readout14['output1']
n_f2_d = readout14['output2']
n_f2_n = readout14['output3']

readout15 = conditionalP(neutral, feature3)
n_f3_h = readout15['output1']
n_f3_d = readout15['output2']
n_f3_n = readout15['output3']

readout16 = conditionalP(neutral, feature4)
n_f4_h = readout16['output1']
n_f4_d = readout16['output2']
n_f4_n = readout16['output3']

readout17 = conditionalP(neutral, feature5)
n_f5_h = readout17['output1']
n_f5_d = readout17['output2']
n_f5_n = readout17['output3']

readout18 = conditionalP(neutral, feature6)
n_f6_h = readout18['output1']
n_f6_d = readout18['output2']
n_f6_n = readout18['output3']

def MAP(features):
    h1 = h
    d1 = d
    n1 = n
    if (features[0] == '1'):
        h1 = h1*h_f1_h
        d1 = d1*d_f1_h
        n1 = n1*n_f1_h
    elif (features[0] == '-1'):
        h1 = h1*h_f1_d
        d1 = d1*d_f1_d
        n1 = n1*n_f1_d
    elif (features[0] == '0'):
        h1 = h1*h_f1_n
        d1 = d1*d_f1_n
        n1 = n1*n_f1_n

    if (features[1] == '1'):
        h1 = h1*h_f2_h
        d1 = d1*d_f2_h
        n1 = n1*n_f2_h
    elif (features[1] == '-1'):
        h1 = h1*h_f2_d
        d1 = d1*d_f2_d
        n1 = n1*n_f2_d
    elif (features[1] == '0'):
        h1 = h1*h_f2_n
        d1 = d1*d_f2_n
        n1 = n1*n_f2_n

    if (features[2] == '1'):
        h1 = h1*h_f3_h
        d1 = d1*d_f3_h
        n1 = n1*n_f3_h
    elif (features[2] == '-1'):
        h1 = h1*h_f3_d
        d1 = d1*d_f3_d
        n1 = n1*n_f3_d
    elif (features[2] == '0'):
        h1 = h1*h_f3_n
        d1 = d1*d_f3_n
        n1 = n1*n_f3_n

    if (features[3] == '1'):
        h1 = h1*h_f4_h
        d1 = d1*d_f4_h
        n1 = n1*n_f4_h
    elif (features[3] == '-1'):
        h1 = h1*h_f4_d
        d1 = d1*d_f4_d
        n1 = n1*n_f4_d
    elif (features[3] == '0'):
        h1 = h1*h_f4_n
        d1 = d1*d_f4_n
        n1 = n1*n_f4_n

    if (features[4] == '1'):
        h1 = h1*h_f5_h
        d1 = d1*d_f5_h
        n1 = n1*n_f5_h
    elif (features[4] == '-1'):
        h1 = h1*h_f5_d
        d1 = d1*d_f5_d
        n1 = n1*n_f5_d
    elif (features[4] == '0'):
        h1 = h1*h_f5_n
        d1 = d1*d_f5_n
        n1 = n1*n_f5_n

    if (features[5] == '1'):
        h1 = h1*h_f6_h
        d1 = d1*d_f6_h
        n1 = n1*n_f6_h
    elif (features[5] == '-1'):
        h1 = h1*h_f6_d
        d1 = d1*d_f6_d
        n1 = n1*n_f6_d
    elif (features[5] == '0'):
        h1 = h1*h_f6_n
        d1 = d1*d_f6_n
        n1 = n1*n_f6_n

    max1 = max(h1, d1, n1)

    if (max1 == h1):
        flag1 = '1'
    elif (max1 == d1):
        flag1 = '-1'
    elif (max1 == n1):
        flag1 = '0'

    return flag1

input11 = open('test_hashtag.txt', 'r')
set11 = input11.readlines()
feature11 = set11[0].split()

input12 = open('test_keyword.txt', 'r')
set12 = input12.readlines()
feature12 = set12[0].split()

input13 = open('test_JJ.txt', 'r')
set13 = input13.readlines()
feature13 = set13[0].split()

input14 = open('test_NP.txt', 'r')
set14 = input14.readlines()
feature14 = set14[0].split()

input15 = open('test_BENEFICIARY.txt', 'r')
set15 = input15.readlines()
feature15 = set15[0].split()

input16 = open('test_AGENT.txt', 'r')
set16 = input16.readlines()
feature16 = set16[0].split()

lenTest = len(feature11)

analysis_value = []

for i in range(lenTest):
    temp_features = []
    temp_features.append(feature11[i])
    temp_features.append(feature12[i])
    temp_features.append(feature13[i])
    temp_features.append(feature14[i])
    temp_features.append(feature15[i])
    temp_features.append(feature16[i])

    outputTest = MAP(temp_features)

    analysis_value.append(outputTest)

input_expected = open('classification_testing_set.txt', 'r')
expectedSet = input_expected.readlines()

expected_value = expectedSet[0].split()

mistake_count = 0
for i in range(len(expected_value)):
    if (analysis_value[i] != expected_value[i]):
        mistake_count = mistake_count + 1

error_rate = float(mistake_count)/size1

#print(len(expected_value))
#print(len(analysis_value))

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

for i in range(len(expected_value)):
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

print("The error rate for the testing set using the naive Bayesian algorithm is: "
      + str(mistake_count) + " mistakes / " + str(size1) + " total tweets = " + str(round(error_rate*100, 2)) + '%.')
