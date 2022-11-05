// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            
            old=image[sr][sc]
            if old ==color:return image
            n=len(image)
            m=len(image[0])
            index=[(1,0),(0,1),(-1,0),(0,-1)]
            visit=[[False]*m for i in range(n)]

            def valid(i, j):
                if i >= 0 and i < n and j >= 0 and j < m and  not visit[i][j]and  image[i][j]==old: return True
                return False

            def bfs(i, j):
                q = [(i, j)]
                while q:
                    rx,ry=q.pop()
                    visit[rx][ry]=False
                    for u ,v in index :
                        h,k=u+rx,v+ry
                        if valid(h,k)  and  (h,k) not in q:q.append((h,k))
                    image[rx][ry]=color
                return  image


            return bfs(sr,sc)