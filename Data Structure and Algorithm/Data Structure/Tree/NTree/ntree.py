# import config

event_list = [{'logid': 3, 'ibv': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:05:39.018', 'processguid': '{4AA00B44-2C2F-5C83-0000-00102F730A00}',
               'parentprocessguid': None},
              {'logid': 4, 'ibv': [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:21.320', 'processguid': '{4AA00B44-768D-5C87-0000-0010EA1EE400}',
               'parentprocessguid': '{4AA00B44-2C2F-5C83-0000-00102F730A00}', 'updateid': [5, 7, 8],
               'updatetime': ['2019-03-10 06:14:03.459', '2019-03-12 09:06:44.143', '2019-03-12 09:06:44.143']},
              {'logid': 6, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:44.143', 'processguid': '{4AA00B44-76A4-5C87-0000-00109ED1E400}',
               'parentprocessguid': '{4AA00B44-768D-5C87-0000-0010EA1EE400}'},
              {'logid': 9, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:45.094', 'processguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}',
               'parentprocessguid': '{4AA00B44-768D-5C87-0000-0010EA1EE400}'},
              {'logid': 10, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               'utctime': '2019-03-12 09:06:46.015', 'processguid': '{4AA00B44-76A6-5C87-0000-00104B38E500}',
               'parentprocessguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}'},
              {'logid': 11, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:46.218', 'processguid': '{4AA00B44-76A6-5C87-0000-0010D540E500}',
               'parentprocessguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}'},
              {'logid': 12, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               'utctime': '2019-03-12 09:06:46.467', 'processguid': '{4AA00B44-76A6-5C87-0000-0010E74AE500}',
               'parentprocessguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}'},
              {'logid': 13, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:46.592', 'processguid': '{4AA00B44-76A6-5C87-0000-00103452E500}',
               'parentprocessguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}'},
              {'logid': 14, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:06:47.840', 'processguid': '{4AA00B44-76A7-5C87-0000-0010CA96E500}',
               'parentprocessguid': '{4AA00B44-76A5-5C87-0000-001071F8E400}'},
              {'logid': 15, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:07:09.665', 'processguid': '{4AA00B44-76BD-5C87-0000-001040A5E800}',
               'parentprocessguid': '{4AA00B44-768D-5C87-0000-0010EA1EE400}'},
              {'logid': 16, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               'utctime': '2019-03-12 09:07:09.758', 'processguid': '{4AA00B44-76BD-5C87-0000-00106CACE800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-001040A5E800}'},
              {'logid': 161, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               'utctime': '2019-03-12 09:07:09.758', 'processguid': '{4AA00B44-76BD-5C87-0000-00116CACE800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-00106CACE800}'},
              {'logid': 162, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               'utctime': '2019-03-12 09:07:09.758', 'processguid': '{4AA00B44-76BD-5C87-0000-00136CACE800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-00106CACE800}'},
              {'logid': 1611, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               'utctime': '2019-03-12 09:07:09.758', 'processguid': '{4AA00B44-76BD-5C87-0000-02156CACE800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-00116CACE800}'},
              {'logid': 17, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:07:09.821', 'processguid': '{4AA00B44-76BD-5C87-0000-00108EB0E800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-001040A5E800}'},
              {'logid': 18, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               'utctime': '2019-03-12 09:07:09.930', 'processguid': '{4AA00B44-76BD-5C87-0000-00101DB6E800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-001040A5E800}'},
              {'logid': 19, 'ibv': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 09:07:10.008', 'processguid': '{4AA00B44-76BE-5C87-0000-001074BBE800}',
               'parentprocessguid': '{4AA00B44-76BD-5C87-0000-001040A5E800}'},
              {'logid': 21, 'ibv': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 10:51:42.841', 'processguid': '{4AA00B44-2B9D-5C83-0000-00106AB10000}',
               'parentprocessguid': None, 'updateid': [21],
               'updatetime': ['2019-03-12 10:51:51.093']},
              {'logid': 20, 'ibv': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'utctime': '2019-03-12 10:51:42.841', 'processguid': '{4AA00B44-8F3E-5C87-0000-0010DD3D2301}',
               'parentprocessguid': '{4AA00B44-2B9D-5C83-0000-00106AB10000}', 'updateid': [21],
               'updatetime': ['2019-03-12 10:51:51.093']}]


# 创建树结点类

# event_list = []
class NAryTreeNode():
    def __init__(self, e):  # (e,children=[])不对
        self.id = e['logid']
        self.data = e  # dict
        self.children = []  # list

    # 添加一个孩子节点
    def add_children(self, node):
        self.children.append(node)


class ProcessTree():
    def __init__(self, event):
        self.event = event
        self.behavior_size = 25

    def preorder_tree(self, root):
        """
        前序遍历树
        :param root:
        :return:
        """
        # 递归终止条件：该节点是否有子节点（及根节点）
        if not root:
            return []
        res = []
        res.append(root)
        # 递归每一级所做的事：遍历该子树
        for child in root.children:
            res.extend(self.preorder_tree(child))
        # 递归返回值：返回该父节点的所有子节点
        return res

    def build_tree(self):
        """
        构建进程树
        :return:
        """
        count = 64
        root_nodes_list = []
        for e in self.event:
            # 若日志为空，则返回
            if not e:
                return
            # 若日志的parentprocessguid为None，则为父节点，加入树中，继续循环
            if e['parentprocessguid'] is None:
                root = NAryTreeNode(e)
                root_nodes_list.append(root)
                continue
            # 若日志记录e的parentprocessguid与树的所有节点的processguid都不相等，
            # 则构建一条日志，使其processguid=e['parentprocessguid']
            node_guid = []
            for root in root_nodes_list:
                # 获取树的所有节点（包含根节点）
                all_nodes = self.preorder_tree(root)
                for node in all_nodes:
                    node_guid.append(node.data['processguid'])
            if e['parentprocessguid'] not in node_guid:
                count += 1
                data_event = {'logid': chr(count), 'ibv': [0] * self.behavior_size,
                              'utctime': '1970-01-01 00:00:00.000',
                              'processguid': e['parentprocessguid'], 'parentprocessguid': None}
                root = NAryTreeNode(data_event)
                root_nodes_list.append(root)
            # 遍历每颗树
            for root in root_nodes_list:
                # 获取包含树的根节点的所有子节点
                all_nodes = self.preorder_tree(root)
                for node_index in range(len(all_nodes)):
                    if e['parentprocessguid'] == all_nodes[node_index].data['processguid']:
                        child_node = NAryTreeNode(e)
                        all_nodes[node_index].add_children(child_node)
        return root_nodes_list

    def preorder_show_tree(self, root, depth, rst):
        """
        层次显示树状结构
        :param root:
        :param depth:
        :return:
        """
        if not root.children:
            return ''
        depth += 1
        for child_index in range(len(root.children)):
            if child_index == len(root.children) - 1:
                cur_str = [('\n' + '|   ' * (depth - 1) + '+-- ' + str(root.children[child_index].id))]
            else:
                cur_str = [('\n' + '|   ' * (depth - 1) + '|-- ' + str(root.children[child_index].id))]
            rst += cur_str
            self.preorder_show_tree(root.children[child_index], depth, rst)
            # 不要 rst += cur_str
            # self.preorder_show_tree(root.children[child_index], depth, rst+cur_str)
            # rst值并没有改变

    def print_tree(self, outpath):
        """
        打印树
        :return:
        """
        with open(outpath, 'w', encoding='utf-8') as f:
            for tree in self.build_tree():
                f.write('Show tree, current tree.root.id is ' + str(tree.id))
                f.write('\n' + str(tree.id))
                tree_graph = []
                self.preorder_show_tree(tree, 0, tree_graph)
                for s in tree_graph:
                    f.write(str(s))
                f.write('\n\n')


    def generate_obv(self, root):
        """
        后序遍历多叉树，并生成OBV
        :param root:
        :return:
        """
        root.data.setdefault('obv', root.data['ibv'])
        if not root:
            return []
        # 1.递归终止条件是什么：该节点没有子节点，则将该节点的数据返回
        if not root.children:
            return [root.data]
        result = []
        # 3.每一层递归干什么：1.遍历每一个子节点，并生成其obv,父节点的obv=各子节点obv的和
        for child in root.children:
            result += self.generate_obv(child)
            child.data.setdefault('obv', root.data['ibv'])
            root.data['obv'] = list(map(lambda x, y: x + y, root.data['obv'], child.data['obv']))
        result += [root.data]
        # 2.返回值是什么：返回该节点的所有子节点的数据（包括该节点）
        return result[::-1]

    def each_tree_obv(self):
        """
        给每颗树生成OBV
        :return:
        """
        root_nodes_list = self.build_tree()
        event_tree_list = []
        for root in root_nodes_list:
            event_tree_list.extend(self.generate_obv(root))
        return event_tree_list


if __name__ == '__main__':
    pro = ProcessTree(event_list)
    pro.build_tree()
    outpath = 'D:\data analysis\wuyifan18DeepLog\DeepLog-master\Tree_graph'
    pro.print_tree(outpath)
    event_tree_list = pro.each_tree_obv()

    # file = open(r'H:\sysfile\desktop\python_stu\SysmonLog\data\obvlist', 'w', encoding='utf-8')
    # file.write(str(event_tree_list));
    # file.close()


###    
Show tree, current tree.root.id is 3
3
+-- 4
|   |-- 6
|   |-- 9
|   |   |-- 10
|   |   |-- 11
|   |   |-- 12
|   |   |-- 13
|   |   +-- 14
|   +-- 15
|   |   |-- 16
|   |   |   |-- 161
|   |   |   |   +-- 1611
|   |   |   +-- 162
|   |   |-- 17
|   |   |-- 18
|   |   +-- 19

Show tree, current tree.root.id is 21
21
+-- 20
