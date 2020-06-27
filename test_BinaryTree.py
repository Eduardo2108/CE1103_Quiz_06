from unittest import TestCase

from BinaryTree import BST


class TestBST(TestCase):
    def test_insert(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
    def test_insertRepeated(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(5)
    def test_delete(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.delete(5)
    def test_onlyRoot(self):
        arbol = BST()
        arbol.add(5)
        arbol.delete(5)
    def test_deleteRoot_onlyLeft(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(1)
        arbol.delete(5)
    def test_deleteRoot_onlyRight(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(50)
        arbol.delete(5)
    def test_deleteRoot_twoChildren(self):
        arbol = BST()
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(5)
        arbol.add(1)

        arbol.delete(10)
    def test_delete_notExist(self):
        arbol = BST()
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.delete(38)
    def test_deleteRootMoreNodes(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.delete(5)
    def test_deleteEmpty(self):
        BST().delete(5)

    def test_deleteNodeNoChildren(self):
        arbol = BST()
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(5)
        arbol.add(1)

        arbol.delete(1)

    def test_deleteNodeLeftChildren(self):
        arbol = BST()
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(5)
        arbol.add(1)
        arbol.delete(5)

    def test_deleteNodeRightChildren(self):
        arbol = BST()
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(80)

        arbol.delete(50)
    def test_max(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        assert arbol.find_max() == 90

    def test_maxEmpty(self):
        arbol = BST()
        arbol.find_max()

    def test_min(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        assert arbol.find_min() == 5

    def test_minEmpty(self):
        arbol = BST()
        arbol.find_min()

    def test_inorder(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.inorder()

    def test_inorderEmpty(self):
        BST().inorder()

    def test_preorder(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.preorder()

    def test_preorderEmpty(self):
        BST().preorder()

    def test_postorder(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        arbol.postorder()

    def test_postorderEmpty(self):
        BST().postorder()

    def test_find(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        assert arbol.find(8) == True

    def test_findUnexist(self):
        arbol = BST()
        arbol.add(5)
        arbol.add(10)
        arbol.add(50)
        arbol.add(20)
        arbol.add(7)
        arbol.add(8)
        arbol.add(90)
        assert arbol.find(666) == False
    def test_findEmpty(self):
        BST().find(60)
