from scipy import stats
import scipy


def replace(string):
    string.replace('\n', '')


file = open('/Users/shelan/Downloads/training.txt')
lineno = 0
headers = []
elements = []
for line in file:
    if lineno == 0:
        headers = line.split()
    else:
        elements.append(line.split('\t'))
    lineno += 1

sorted_data = []
for i in range(len(headers)):
    sorted_data.append([])

for data_set in elements:
    for i in range(len(data_set)):
        sorted_data[i].append(data_set[i])

cleaned = [float(elem.replace('\n','')) for elem in sorted_data[68]]

file = open("output",'+w')

for set in data_set:
    file.write()


# for i in range(68):
#     try:
#         print i, scipy.stats.pearsonr([float(elem) for elem in sorted_data[i]], cleaned)
#     except:
#         print 'errr in ', i







