# linked list의 코테 적용방법은 크게 2가지
# 1. linked list를 자유자재로 구현(변형이 많다.) => 선형 자료구조를 써야하는 상황 + 중간에 데이터 추가 및 삭제 시 용이
# 2. Tree or Graph 활용 (노드구현에 따라서 tree가 될 수도 있고 Graph가 될 수도 있지만 대부분 Tree > Graph가 더 빈도수가 많다.)

# step 2. 접근 방법. tree 처럼 계층 구조가 아니라, 순서가 있는 선형구조가 필요한 상황. 뒤로 가기도 하고, 앞으로 가기도 하는 상황 doubly linked list
# 으로 생각할 수 있다.

class ListNoded(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNoded(val=homepage)
    
    def visit(self, url):
        self.current.next = ListNoded(val=url, prev=self.current)
        self.current = self.current.next
        return None
    
    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    
    def forward(self, steps):
        while steps > 0 and self.currnet.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("Linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)