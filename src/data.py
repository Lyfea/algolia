import collections

# data maps a string (the query) with the list of date of said query
data = collections.OrderedDict()

def init(file):
    tmp = {}
    fd = open(file, 'r')
    for line in fd.readlines():
        query = line.split('\t')
        text = query[1][:-1]
        if text not in tmp:
            tmp[text] = []
        tmp[text].append(query[0])
    fd.close()
    global data
    data = collections.OrderedDict(sort(tmp))

def sort(dic):
    for key, values in dic.items():
        values.sort()
    #t[1][0] for the first date of the query
    return sorted(dic.items(), key=(lambda t: t[1][0]))


if __name__ == "__main__":
    init("../data/hn_logs.tsv")
    print(len(data))
