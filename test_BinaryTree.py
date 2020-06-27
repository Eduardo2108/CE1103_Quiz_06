from unittest import TestCase

from BinaryTree import BST


class TestBST(TestCase):
    def test_insert(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
    def test_insertRepeated(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(5)
    def test_delete(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.remove(5)
    def test_onlyRoot(self):
        arbol = BST()
        arbol.insert(5)
        arbol.remove(5)
    def test_deleteRoot_onlyLeft(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(1)
        arbol.remove(5)
    def test_deleteRoot_onlyRight(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(50)
        arbol.remove(5)
    def test_deleteRoot_twoChildren(self):
        arbol = BST()

        arbol.insert(50)
        arbol.insert(5)
        arbol.insert(1)

        arbol.remove(50)
    def test_delete_notExist(self):
        arbol = BST()
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.remove(38)
    def test_deleteRootMoreNodes(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.remove(5)
    def test_deleteEmpty(self):
        BST().remove(5)
    def test_max(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        assert arbol.findMax() == 90

    def test_maxEmpty(self):
        arbol = BST()
        arbol.findMax()

    def test_min(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        assert arbol.findMin() == 5

    def test_minEmpty(self):
        arbol = BST()
        arbol.findMin()

    def test_inorder(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.inorder()

    def test_inorderEmpty(self):
        BST().inorder()

    def test_preorder(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.preorder()

    def test_preorderEmpty(self):
        BST().preorder()

    def test_postorder(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        arbol.postorder()

    def test_postorderEmpty(self):
        BST().postorder()

    def test_find(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        assert arbol.find(8) == True

    def test_findUnexist(self):
        arbol = BST()
        arbol.insert(5)
        arbol.insert(10)
        arbol.insert(50)
        arbol.insert(20)
        arbol.insert(7)
        arbol.insert(8)
        arbol.insert(90)
        assert arbol.find(666) == False
    def test_findEmpty(self):
        BST().find(60)
