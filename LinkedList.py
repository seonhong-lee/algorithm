class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            self.tail.next = new_node
            self.tail = self.tail.next
            # 이렇게 하면 O(1)로 append를 만들 수 있음. 이전에는 O(N)이었음.
            # LinkedList는 단골 주제는 아니다. 하지만, 트리나 그래프 구현할 때 LinkedList를 모르면 할 수 없기 때문에 잘 이해를 해야한다.

    # def insert 중간에 들어가는 것은 for문을 통해서 접근을 핟 다음, temp_주소 값을 설정해서 이어주는 형식으로 진행
    # def remove 는 삭제하려는 곳의 전의 주소 값을 삭제하려는 곳의 다음 주소값으로 연결한다. 아무것도 참조하지 않은 객체는 garbage collector가 삭제함


    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

