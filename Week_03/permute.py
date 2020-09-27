class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        trace = []
        res = []
        def help(input_list, input_trace):
            if len(input_trace) == len(input_list):
                res.append(input_trace[:])
                return
            for num in input_list:
                if num in input_trace:
                    continue
                input_trace.append(num)
                help(input_list, input_trace)
                input_trace.pop()
        help(nums, trace)
        return res
            