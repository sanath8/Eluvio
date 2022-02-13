from collections import defaultdict
from reader import Reader
from writer import Writer
from dynamic_programming import SubstringMatch

fp = Reader()
files = [fp.readFile(i) for i in range(1, 11)]
lcs = SubstringMatch()
hashMap = defaultdict(dict)
curMax = 0
# compare the files pairwise to get the strand with maximum length between them
# and make use of hash map to identify and store the strand with maximum length across all files
for f1 in range(len(files)):
    for f2 in range(f1+1, len(files)):
        maxLen, fInd, sInd = lcs.longestCommonSubstring(files[f1], files[f2])
        if(maxLen >= curMax):
            curMax = maxLen
            hashMap[files[f1][fInd: fInd + maxLen]].update({f1: fInd, f2: sInd})
# get the strand which has maximum length among all possible combinations
maxMatched = max(hashMap.keys(), key = lambda item: len(item))
fileDetails = [(fName, off) for fName, off in hashMap[maxMatched].items()]
fileNames = [f[0] + 1 for f in fileDetails]
offsets = [f[1] for f in fileDetails]
# write the results into /src/results.txt and display in console as well
writeData = {
    'length': len(maxMatched),
    'files': fileNames,
    'offsets': offsets
}
wfp = Writer()
wfp.writeToFile("results.txt", writeData)


