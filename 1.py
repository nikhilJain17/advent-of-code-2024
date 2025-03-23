"""
Problem part 1: 
Given two lists of numbers,
match the least elements with each other,
and keep a running sum of their difference.

Solution:
Create a heap of each list
Keep popping and summing difference
"""
import heapq

heap1, heap2 = [], []
# number in right list --> how many times it appears on the right side
heap2_freq = {}
with open('./1_input.txt') as f:
    for line in f:
        nums = list(map(int, line.split()))
        assert len(nums) == 2
        heapq.heappush(heap1, nums[0])
        heapq.heappush(heap2, nums[1])
        if nums[1] not in heap2_freq:
            heap2_freq[nums[1]] = 0
        heap2_freq[nums[1]] += 1

ans1 = 0
ans2 = 0
while heap1:
    num1 = heapq.heappop(heap1)
    num2 = heapq.heappop(heap2)
    ans1 += max(num1 - num2, num2 - num1)
    freq = 0
    if num1 in heap2_freq.keys():
        freq = heap2_freq[num1]
    ans2 += num1 * freq
print("part 1 answer", ans1)
print("part 2 answer", ans2)

"""
Problem part 2:

Keep the running sum, but multiply it by
how often the number in the first list 
appears in the second list

Solution:

Build the frequency map
Has to be O(n) right?
"""



