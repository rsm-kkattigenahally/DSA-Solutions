# You are given two lists of availability time slots, slt1[][] and slt2[][], for two people. Each slot is represented as [start, end], and it is guaranteed that within each list, no two slots overlap (i.e., for any two intervals, either start1>end2 or start2>end1).
# Given a meeting duration d, return the earliest common time slot of length at least d. If no such slot exists, return an empty array.

# Examples:

# Input: slt1[][] = [[10,50], [60,120], [140,210]], slt2[][] = [[0,15], [60,70]], d = 8
# Output: [60,68]
# Explanation: The only overlap is [60,70] (10 minutes), which is enough for an 8-minute meeting, so answer is [60,68]

# 0...10..11...12....15..50
#     10...11...12....15...

## a[en]< b[st] no overlap or vice versa
## a[st]<=b[en] there is overlap - max(a[st], b[st]), min(a[en], b[en])
## if en-st >=d we return this intervals

def findtime(slt1, slt2, d):
  if slt1==[] or slt2==[]: return []

  i, j = 0,0
  while i<len(slt1) and j<len(slt2):
    a,b = slt1[i], slt2[j]
    interval = [max(a[0], b[0]), min(a[1], b[1])]
    if interval[1]-interval[0]>=d:       # if the end < start then it will be neg so we took care of that
      return[interval[0], interval[0]+d]
    
    if a[1]<b[0]:i+=1
    else: j+=1
  return []

print(findtime([[10,50], [60,120], [140,210]], [[0,15], [60,70]], 8))
print(findtime([[10,50], [60,120], [140,210]],[[0,15], [60,70]], 12))
