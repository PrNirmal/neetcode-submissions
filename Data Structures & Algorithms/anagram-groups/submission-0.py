class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_dict={}
        for i in strs:
            text="".join(sorted(i))
            if check_dict.get(text,0)==0:
                check_dict[text]=[i]
            else:
                check_dict[text].append(i)
        return list(check_dict.values())