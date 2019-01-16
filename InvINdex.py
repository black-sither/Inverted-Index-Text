from collections import defaultdict, OrderedDict
from pprint import pprint

docs = OrderedDict()

with open('ML.txt', 'r') as fle:
    docs['ML'] = fle.read().replace("\n", "")
with open('mobile.txt', 'r') as fle:
    docs['mobile'] = fle.read().replace("\n", "")
with open('telephone.txt', 'r') as fle:
    docs['telephone'] = fle.read().replace("\n", "")

keywords = defaultdict(lambda: [0, set(), defaultdict(lambda:0)])

for document_id, key in enumerate(docs.iterkeys()):
    text = docs[key]
    text = text.replace(',', ' ').replace(')', ' ').replace(
        '(', ' ').replace('[', ' ').replace(']', ' ').replace('.', '').replace(':', '').replace(';', '').replace('\"', '')
    text2 = text.split(' ')
    for i in text2:
        keywords[i][0] += 1
        keywords[i][1].add(key)
        keywords[i][2][document_id] += 1
keylist = sorted(keywords)

# for viewing the generated keylist
# for key in keylist:
#     print "keyword:%s count:%d documents:" % (
#         key, keywords[key][0])
#     print(keywords[key][1])
#     print("count in individual documents:")
#     for k, v in keywords[key][2].iteritems():
#         print "doc_id: %d count: %d" % (k, v)

# searching relevant documents
to_search = "Google mobile"
to_search = to_search.split(' ')
threshold = 2
search_results = set()
for i in to_search:
    if i in keylist:
        for j in keywords[i][1]:
            if keywords[i][2][docs.keys().index(j)] > threshold:
                search_results.add(j)
if search_results:
    print("The following documents are of relevance to us")
    for i in search_results:
        print(i)
else:
    print("no relevant search results found")
