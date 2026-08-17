class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = defaultdict(list)
        emailtoname = {}
        allemails = set()
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                emailtoname[account[i]] = name
                allemails.add(account[i])
                if i < len(account)-1:
                    adjList[account[i]].append(account[i+1])
                    adjList[account[i+1]].append(account[i])
        allemails = list(allemails)
        seen = set()
        emaillists = []
        for email in allemails:
            if email not in seen:
                q = deque()
                curr = []
                q.append(email)
                while q:
                    for _ in range(len(q)):
                        current = q.popleft()
                        if current not in seen:
                            curr.append(current)
                            seen.add(current)
                            for e in adjList[current]:
                                if e not in seen:
                                    q.append(e)
                emaillists.append(curr)
        res = []
        for lis in emaillists:
            curr = []
            curr.append(emailtoname[lis[0]])
            curr += sorted(lis)
            res.append(curr)
        return res
        

        
        