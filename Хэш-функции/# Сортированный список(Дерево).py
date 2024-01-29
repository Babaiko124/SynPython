# Сортированный список (Дерево)

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def sorted_list_to_BST(self, nums):
        def build_BST(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = Node(nums[mid])
            node.left = build_BST(left, mid - 1)
            node.right = build_BST(mid + 1, right)
            return node

        self.root = build_BST(0, len(nums) - 1)
    
    def find(self, value):
        if self.root.value is None:
            return False
        
        if self.root.value == value:
            return True
        
        node = self.find_node(self.root, value)
        if node is None:
            return False
        
        return True
    
    def find_node(self, cn, value):
        if cn is None:
            return None
        
        if cn.value == value:
            return cn
        
        if cn.value > value:
            res = self.find_node(cn.left, value)
            return res
        else:
            res = self.find_node(cn.right, value)
            return res
    
bst = BinarySearchTree()
nums = [1,2,3,4,5,6,7,8,9,10]
bst.sorted_list_to_BST(nums)

print(bst.find(1), bst.find(2), bst.find(3), bst.find(4), bst.find(5), bst.find(6), bst.find(7), bst.find(8), bst.find(9), bst.find(10), bst.find(11))

a = 10