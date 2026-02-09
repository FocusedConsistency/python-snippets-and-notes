# Using heapq is faster than sort when k >> n, 
# where k - number of selections
import heapq

scores = [42, 17, 89, 3, 76, 54, 31, 98, 23, 67]
top3 = sorted(scores, reverse=True)[:3] # [98, 89, 76]
top3 = heapq.nlargest(3, scores) # [98, 89, 76]
