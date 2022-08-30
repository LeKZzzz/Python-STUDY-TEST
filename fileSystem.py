# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/8/30


class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.partent = None

    def __repr__(self):
        return self.name


class FileSystem:
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.partent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.partent
        else:
            for child in self.now.children:
                if name == child.name:
                    self.now = child
                    return
            raise ValueError('invalid dir')


tree = FileSystem()
tree.mkdir('bin/')
tree.mkdir('src/')
tree.mkdir('lib/')
tree.cd('lib')
tree.mkdir('test.py')
print(tree.ls())
