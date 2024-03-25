# Test 1
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        canMax = []
        for i in range(len(candies)):
            # print(i)
            canMax.append(True if candies[i] + extraCandies >= max_candy else False)

        return canMax

# Test 2
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        indices = list(range(len(heights)))
        indices.sort(key=lambda i: -heights[i])
        sorted_names = [names[i] for i in indices]
        return sorted_names

# Test 3
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        cnt = Counter()
        for v, w in chain(items1, items2):
            cnt[v] += w
        return sorted(cnt.items())