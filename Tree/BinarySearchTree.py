from BinaryTree import treenode as Node

class BST:
    def __init__(self):
        self.root=None
    def search(self,k):
        return self._search(self.root,k)
    #n은 루트, k는 찾는값
    def _search(self,n,k):
    #비어있거나, 정답 노드일때
        if n==None or n.get_key()==k:
    #찾았는지 리턴
            return n!=None
        elif n.get_key()>k:
            #if the root node is bigger than the value, search the left side.
            return self._search(n.get_left(),k)
        #작으면 오른쪽 탐색
        else:
            return self._search(n.get_right(),k)
        
    def insert(self,key):
        self.root=self._insert(self.root,self)
    def _insert(self,n,key):
        #없으면 노드만 넣어서
        if n==None:
            return Node(key)
        elif n.get_key()>key:
            n.set_left(self._insert,key)
        else:
            n.set_right(self._insert,key)

    def delete(self,key):
        self.root=self._delete(self.get_left(),key)
    def _delete(self,n,key):
        if n==None:
            if n.get_key()>key:
                n.set_left(self._delte(n.get_left(),key))
            elif n.get_key()<key:
                n.set_right(self._delete(n.get_right(),key))
            else:
                if n.get_left()==None and n.get_right()==None:
                    return None
                if n.get_left()==None or n.get_right()==None:
                    if n.get_left()==None:
                        return n.get_right()
                    else:
                        return n.get_left()
                target=n
                n=self._find_min(target.get_right())
                n.set_right(self._delete_min(target.get_right()))
                n.set_left(target.get_left())
            return n