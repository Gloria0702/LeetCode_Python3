class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem  # 存入数据
        self.next = None  # 初始设置下一节点为空

# 下面创建单链表，并实现其应有的功能


class LinkList(object):
    """单链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):  # 判断链表是否为空
        return self.__head == None

    def length(self):  # 求链表长度
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历整个列表
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("\n")

    def add(self, item):  # 头插法添加结点
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):  # 尾插法添加结点
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):  # 往指定结点（第pos个&序号为pos-1）后添加结点
        if pos <= 0:
                # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(item)
        elif pos >= self.length():
            # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:  # 常规情况
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，per指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):  # 删除链表中特定值节点
        cur = self.__head
        per = None
        while cur != None:
            if cur.elem == item:
                # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    per.next = cur.next
                break
            else:
                per = cur
                cur = cur.next

    def search(self, item):  # 查找特定值节点是否存在
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    # 当.py文件单独运行时，此代码块会被运行
    # 当.py以模块形式被导入，此代码块不运行

    ll = LinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(3)
    ll.add(999)
    ll.insert(-3, 110)
    ll.insert(99, 111)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    ll.remove(111)
    ll.travel()
    print(ll.search(110))