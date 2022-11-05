// https://leetcode.com/problems/implement-trie-prefix-tree

class Trienode:
    def __init__(self):
        self.childern={}
        self.end=False
class Trie:

    def __init__(self):
        self.root=Trienode()

    def insert(self, word: str) -> None:
        cur =self.root
        for c in word:
            if c not in cur.childern:
                cur.childern[c]=Trienode()
            cur=cur.childern[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur =self.root
        for c in word:
            if c not in cur.childern:return False
            cur=cur.childern[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
            cur=self.root
            for c in prefix:
                if c not in cur.childern:return False
                cur=cur.childern[c]
            return True
 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)