import logging
import functools
import time

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Node():
    def __init__(self, data=None):
        self._data = data
        self._left, self._right = None, None

    def __str__(self):
        return 'Node:<data:%s>, <left:%s>, <right:%s>' % (
            str(self._data), str(self._left), str(self._right))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value


# todo 不理解
def check_null(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        if self.__bool__():
            return func(self, *args, **kw)
        else:
            if func.__name__ in ['_insert', '_insert2']:
                self._root = Node(args[0])
            else:
                print('The tree is empty')

    return wrapper


class BinarySearchTree():
    """
    如果非空，那么左子树的所有节点都小于根节点，右子树的所有节点都大于根节点，数为二叉搜索树。
    左右子树都为二叉搜索树。
    """

    def __init__(self):
        self._root = None

    def __str__(self):
        """ yield 迭代器 """
        tree2list = [x.data for x in self._generate_node()]
        return 'the BinarySearchTree is %s' % tree2list

    def __bool__(self):
        if self._root is not None:
            return True
        else:
            return False

    @staticmethod
    def _redirect(pre_node, is_left, target):
        """将target节点赋值成 pre_node的is_left/right子节点
        :param is_left: 将target赋成父节点 pre_node 的 left 还是 right 子节点
        """
        if is_left:
            pre_node.left = target
        else:
            pre_node.right = target

    def _generate_node(self):
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            yield node
            queue.extend([x for x in (node.left, node.right) if x != None])
            # (node.left, node.right) is tuple

    @check_null
    def _metal_find(self, value, node, alert=True):
        """
        内部接口: 实现了基本的查找功能,并且实现了跟踪父节点和判断是否为左右子节点的功能
        思   路: 比较简单
        :return: 找到的node, 该节点的父节点_pre_node, 该节点是_pre_node的左还是右节点bool(is_left)"""
        # if you want the pre_node and is_left get the specific value, let the node=root
        is_left, _pre_node = None, None
        while node and value != node.data:
            # _pre_node 作用跟踪父节点
            _pre_node = node
            if value < node.data:
                node = node.left
                # is_left 作用跟踪是否为左子节点
                is_left = True
            elif value > node.data:
                node = node.right
                is_left = False
        # while 循环完没找到,则node is None
        # while 循环完找到的话,则node is not None 跳过if,return 找到的node
        if alert and node is None:  # alert and (node is None)
            print('There is no node<%s>' % value)
        return node, _pre_node, is_left

    def find(self, value):
        """暴露给外面的接口，按值查找，返回节点"""
        # *_ 除第一个外的其他返回值
        result, *_ = self._metal_find(value, self._root)
        return result

    @check_null
    def _insert(self, value, node):
        """
        递归插入方法
        :return:  插入的节点node
        """
        # _insert函数最终结果是
        # 1 找到value==node.data的节点即已有这个节点,执行print(),再返回这个节点
        # 2 node is None,然后将此节点新建出来,执行node = Node(value)
        if node is None:
            node = Node(value)
        else:
            if value < node.data:
                # _insert()返回待插入的节点
                # 当前节点的左子节点 指向待插入的节点
                node.left = self._insert(value, node.left)
            elif value > node.data:
                # _insert()返回待插入的节点
                # 当前节点的右子节点 指向待插入的节点
                node.right = self._insert(value, node.right)
            else:
                print('have the same value')

        # 注意这种写法
        return node

    @check_null
    def _insert2(self, value):
        """
        非递归插入方法
        先_metal_find()循环找value, 找到value说明已存在,没找到_redirect()赋值
        """
        result, pre_node, is_left = self._metal_find(value, self._root, False)
        # 先找,没找到通过self._redirect() 赋值
        if result is None:
            self._redirect(pre_node, is_left, Node(value))
        # 找到说明已经存在
        else:
            print('already have the value')

    # 默认走循环的实现, 递归的程序栈很容易爆掉，并且test_insert()测试了下循环比递归快很多
    def insert(self, value, isrecursion=False):
        if isrecursion:
            self._insert(value, self._root)
        else:
            self._insert2(value)

    @check_null
    def _find_extremum(self, node, by='max'):
        """
        找 max min 节点
        :return node:
        """
        if by == 'max':
            while node.right:
                node = node.right
        elif by == 'min':
            while node.left:
                node = node.left
        return node

    def findmax(self):
        return self._find_extremum(self._root)

    def findmin(self):
        return self._find_extremum(self._root, by='min')

    @check_null
    def _delete(self, value, node):
        """ recursion delete
        step1: 通过value 与 node.data比较来找到要删除的节点
        step2: 要删除的节点又有三种situations
                 situation1: 要删除的节点  是叶节点,没有子节点。
                 situation2: 要删除的节点  只有一个子节点。
                 situation3: 要删除的节点  有两个子节点。
        :return: 删除完value以后的新的node
        """
        if not node:
            print('can\'t find')
        else:

            # If the key to be deleted is smaller than the root's
            # key then it lies in left subtree
            if value < node.data:
                node.left = self._delete(value, node.left)

            # If the kye to be delete is greater than the root's key
            # then it lies in right subtree
            elif value > node.data:
                node.right = self._delete(value, node.right)

            # If key is same as root's key, then this is the node
            # to be deleted
            else:

                # Node with two children: Get the inorder successor 中序继承者

                # 最后node.left = self._delete(tmp.data, node.left)其实转化成了
                # 后边 Node with only one child or no child 的情形
                ### 可以找左子树的最大值或者右子树的最小值作为successor
                ### 而左子树的最大值或者右子树的最小值必然只有一个或零个节点
                ### 所以转化成了前边 Node with only one child or no child 的情形
                if node.left and node.right:
                    # find the largest in the left subtree as successor
                    tmp = self._find_extremum(node.left)
                    # Copy the inorder successor's content to this node
                    node.data = tmp.data
                    # Delete the inorder successor
                    node.left = self._delete(tmp.data, node.left)

                # Node with only one child or no child
                else:
                    if node.left is None:
                        node = node.right
                    else:
                        node = node.left
        return node

    @check_null
    def _delete2(self, value, node):
        """非递归删除
        首先: 找到要删除的节点result
        再次: 找到并删除result的successor，再将successor的data赋给要删除的节点result
        讨论复杂的2个节点的情况:
        1 找到value所在的节点result，该节点有两个子节点
        2 找到result的左子节点的max记为tmp，tmp只有0或1个节点
        3 从result中删除tmp，tmp只有0或1个节点，
        4 ...
        """
        # 首先: 找到要删除的节点result
        result, pre_node, is_left = self._metal_find(value, node)
        if result is None:
            return
        # 有2个节点的情况
        if result.left and result.right:
            # 再次: 找到result的successor
            tmp = self._find_extremum(result.left)
            # 再次: 删除result的successor 这步会走后边else里 "# 有1个或者没有" 的情形
            self._delete2(tmp.data, result)
            # 再将successor的data赋给要删除的节点result
            result.data = tmp.data
        # 有1个或者没有
        else:
            if result.left is None:
                result = result.right
            else:
                # 将 result.left 赋给 result
                result = result.left
            # 将 result 赋成 pre_node 的 is_left节点
            self._redirect(pre_node, is_left, result) # 对节点pre_node的子节点进行赋值

    def delete(self, value, isrecursion=False):
        if isrecursion:
            return self._delete(value, self._root)
        else:
            return self._delete2(value, self._root)


def test_insert(value):
    def _test(value, control=False):
        tree = BinarySearchTree()
        start = time.time()
        for i in range(value):
            tree.insert(i, isrecursion=control)
        end = time.time()
        print('the isrecursion control=%s, the time is: %s' % (control, end - start))

    _test(value)
    _test(value, control=True)


def main():
    # test_insert(100)
    tree = BinarySearchTree()
    nums = [7, 2, 9, 1, 4, 8, 10]
    for i in nums:
        tree.insert(i)
    print(tree)
    print(tree.find(4))
    tree.insert(3)
    print(tree)
    tree.delete(2)
    print(tree)


if __name__ == '__main__':
    main()
