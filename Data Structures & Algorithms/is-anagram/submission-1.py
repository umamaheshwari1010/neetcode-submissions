class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs={}
        ct={}
        if len(s)!=len(t):
            return False
        for a in s:
            cs[a]=1 + cs.get(a,0)
        for a in t:
            ct[a]=1 + ct.get(a,0)

        if cs==ct:
            return True
        else:
            return False