import re


path1 = "F:/200nodes/col.txt"
path3 = "F:/200nodes/sorted-10000_demo.log"
path4 = "F:/200nodes/sorted-10000_log_key_pattern.log"

# s = "081111 023119 19 INFO dfs.FSDataset: Deleting block blk_-9213208660385013681 file /mnt/hadoop/dfs/data/current/subdir35/blk_-9213208660385013681"
# regex = re.compile('Deleting block (.*) file (.*)')
# res=regex.search(s)
# if res:
#     print(res)

index_list = []
log_content_list = []
with open(path1, 'r') as f:
    for line in f:
        line = line.strip()
        il = re.search('(\d+)(\.)(.*)', line).group(1)
        index_list.append(il)
        pl = str(re.search('(\d+)(\.)(.*)', line).group(3))
        log_content_list.append(pl)
print(index_list)
print(log_content_list)
pattern_list = list(zip(index_list, log_content_list))

label_list = []
with open(path3, 'r') as f:
    for line in f:
        label = 0
        for p in pattern_list:
            regex = re.compile(p[1])
            res=regex.search(line)
            # match 从开头开始
            # res=regex.match(line)
            if res:
                label = p[0]
                break
        if label == 0:
            #label = random.randint(1, 29)  # 1<= n <=29
            label = 30  # 1<= n <=29
        label_list.append(label)


outf = open(path4, 'w')
for i in label_list:
    # print(type(i)) # str
    outf.write(str(i) + "\n")
outf.close()
