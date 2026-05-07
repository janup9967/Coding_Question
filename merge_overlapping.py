
'''
Merge Overlapping Intervals 
Given a collection of intervals, merge all overlapping intervals.
Input 
4
1 3 
2 6 
8 10 
15 18

Output
1 6
8 10
15 18

Explanations
Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''
def merge_overlapping(intervals):
    
    if not intervals:
        return []
    
    intervals.sort()
    merged = []
    start, end = intervals[0]
    for i in range(1,len(intervals)):
        current_start,current_end = intervals[i]
        if current_start <= end:
            end = max(end,current_end)
        else:
            merged.append([start, end])
            start,end = current_start,current_end
    merged.append([start,end])
    return merged
        
    

n = int(input().strip()) # Number of Intervals 
intervals = []
for i in range(n):
    start , end = map(int,input().split())  # Start & End of each intervals
    intervals.append([start,end])
result = merge_overlapping(intervals)
for interval in result:
    print(*interval)    


