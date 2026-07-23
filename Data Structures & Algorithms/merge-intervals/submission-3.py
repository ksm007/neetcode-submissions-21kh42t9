class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for beg, end in intervals[1:]:
            if output[-1][1] >= beg:
                if output[-1][1] < end:
                    output[-1][1] = end
            else:
                output.append([beg,end])
        
        return output
