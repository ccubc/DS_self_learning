class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for pair in paths:
            d[pair[0]] = pair[1]
        for k in d.keys():
            if d[k] not in d:
                return d[k]