# Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis based on a given set of training data samples. Read the training data from a .CSV file.
import csv
num_attributes = 6
a = []
print("\n The Given Training Data Set \n")
with open('enjoysport.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        a.append(i)
        print(i)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = a[0][j]

print("\n Find S: Finding a Maximally Specific Hypothesis\n")

for i in range(0, len(a)):
    if a[i][num_attributes] == 'yes':
        for j in range(0, num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]
    print(" For Training instance No:{0} the hypothesis is ".format(
        i), hypothesis)

print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
