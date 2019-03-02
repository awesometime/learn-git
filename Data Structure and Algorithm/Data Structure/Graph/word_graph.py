from pythonds.graphs import Graph


def buildGraph():
    d = {}
    g = Graph()
    word_list = ["fool", "pool", "poll", "pole", "pale", "page", "sage"]
    # create buckets of words that differ by one letter
    for word in word_list:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    print(d)
    print(len(d))
    s = 0
    for i in d.values():
        s += len(i)
    print(s)
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


buildGraph()
# d={'_ool': ['fool', 'pool'], 'f_ol': ['fool'], 'fo_l': ['fool'], 'foo_': ['fool'],
# 'p_ol': ['pool'], 'po_l': ['pool', 'poll'], 'poo_': ['pool'],
# '_oll': ['poll'], 'p_ll': ['poll'], 'pol_': ['poll', 'pole'],
# '_ole': ['pole'], 'p_le': ['pole', 'pale'], 'po_e': ['pole'],
# '_ale': ['pale'], 'pa_e': ['pale', 'page'], 'pal_': ['pale'],
# '_age': ['page', 'sage'], 'p_ge': ['page'], 'pag_': ['page'],
# 's_ge': ['sage'], 'sa_e': ['sage'], 'sag_': ['sage']}
