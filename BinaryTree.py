from Node import Node

#hola mundo
class BST(object):
    def __init__(self):
        self.root = None

    # False si ya estaba
    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:

            self.root = Node(d)
            return True

    # return True if d is found in tree, false otherwise
    def find(self, d):
        if self.root is not None:
            return self.root.find(d)
        else:
            return False
    # return True if node successfully removed, False if not removed
    def remove(self, d):
        # Case 1: Empty Tree?
        if self.root is None:
            return False

        # Case 2: Deleting root node
        if self.root.data == d:
            # Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root = None
                return True
            # Case 2.2: Root node has left child
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
            # Case 2.3: Root node has right child
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
            # Case 2.4: Root node has two children
            else:
                move_node = self.root.right
                move_node_parent = None
                while move_node.left:
                    move_node_parent = move_node
                    move_node = move_node.left
                self.root.data = move_node.data
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = None
                else:
                    move_node_parent.right = None
                return True
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != d:
            parent = node
            if d < node.data:
                node = node.left
            elif d > node.data:
                node = node.right
        # Case 3: Node not found
        if node is None or node.data != d:
            return False
        # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if d < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 5: Node has left child only
        elif node.left and node.right is None:
            if d < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 6: Node has right child only
        elif node.left is None and node.right:
            if d < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 7: Node has left and right child
        else:
            move_node_parent = node
            move_node = node.right
            while move_node.left:
                move_node_parent = move_node
                move_node = move_node.left
            node.data = move_node.data
            if move_node.right:
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = move_node.right
                else:
                    move_node_parent.right = move_node.right
            else:
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = None
                else:
                    move_node_parent.right = None
            return True

    # return list of data elements resulting from preorder tree traversal
    def preorder(self):
        if self.root:
            return self.root.preorder([])
        else:
            return []

    # return list of postorder elements
    def postorder(self):
        if self.root:
            return self.root.postorder([])
        else:
            return []

    # return list of inorder elements
    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []

    def findMin(self):
        temp = self.root
        if self.root is None:
            print("Null value")
            return None

        while temp.left is not None:
            temp = temp.left
        print("The min value is: " + str(temp.data))
        return temp.data

    def findMax(self):
        temp = self.root
        if self.root is None:
            print("Null value")
            return None

        while temp.right is not None:
            temp = temp.right
        print("The max value: " + str(temp.data))
        return temp.data
