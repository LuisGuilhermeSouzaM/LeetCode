class Solution(object):
    def groupAnagrams(self, strs):

        new_list = []
        empty_dict ={}

        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in empty_dict:
                empty_dict[sorted_item] = [item]
            else:
                empty_dict[sorted_item].append(item)
        # return empty_dict 
        for k,v in empty_dict.items():
            new_list.append(v)
        return new_list