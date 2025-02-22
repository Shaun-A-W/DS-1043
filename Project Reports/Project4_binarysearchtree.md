
# Binary Search Trees

### DS-1043 - Project 4

### Shaun W. - 9 Dec. 2024

#

## From the Root

Binary Search Trees (BSTs) are a concept in computer science and mathematics that allow, as the name implies, binary methods for searching and modifying the tree. They work in this way as each node may have up to two children. This means that for every traversal step down the tree towards some goal, around half of the sub-trees are skipped over.

Implementing the BST, I used two classes: Node and Tree. These BSTs contain nodes, which have a few data attributes in their Node class. This includes its own value, its parent node, the value of its right child, and the value of its left child. Additionally, the class was designed to allow for duplicated, so a quantity attribute is present. In the code, these are denoted as the following:

	    self._parent = 
        self._left =        
        self._right = 
        self._value = 
        self._quantity = 

Starting from the top node in a tree, we have the `root` of the tree. This node has no parent. From that point, any inserted nodes will be on the right or left of the `root` node. From any node, its left child will have a value such that `self._left < self._value` and `self._right > self._value`, or in the words of Paul E. Black, "where every node's left subtree has keys less than the node's key, and every right subtree has keys greater than the node's key."[^1]

## Constructing a Tree

When a Tree is created in the program, it takes an iterable list as its input. From this, the first item is initialized as a Node. This will be our `root`. As the program iterates down the list, it adds values according to the <, >, or = values, starting at the root. For each node, it will check the iterated value with `self._value` and determine if it matches, is less than, or is greater than it. Following the principle stated earlier, if the values match, then `self._quantity` will increase by one. Otherwise, if the iterated value is less than `self._value`, the program will check the Node to see if it has a child. If not, the value is inserted as a new Node and the left child of the previous one. If the original Node does have a left child, then the process repeats. In the event that a node's `self._value` is not greater than the iterated value, the lefts are swapped with rights. This process is written like so: 

    def insert(self, value):
        if value < self:
            if self._left is None:
                self._left = Node(value, self)
            else:
                self._left.insert(value)
        elif value > self:
            if self._right is None:
                self._right = Node(value, self)
            else:
                self._right.insert(value)
        elif value == self._value:
            self._quantity = self._quantity + 1

Once this insertion has been completed for every value in the list passed through the Tree initialization, the tree has been constructed and may be traversed, searched, or otherwise modified.

## Traversing the Tree

Several methods were implemented in the Node and Tree classes to provide ways to traverse and use the tree for data management. These include, `Node.insert, Node.traverse, Node.tra_reverse, Node.search, Tree.insert, Tree.insert, Tree.__iter__, Tree.__reversed__, ` and `Tree.__contains__`. While this appears like a lot, they can be broken down easily. The Node methods: insert, traverse, tra_reverse, and search are used by each of the Tree methods respectively. The Tree methods essentially call on `_root.(node method)` for each one. Because of this, I will focus on the Node implementation. The code block previously shown is from the Node.insert method, so further explanation is not necessary. However, for the `traverse`, `tra_reverse` (the reverse of traverse), and `search`, they have more details to be discussed. `Node.traverse` and `Node.tra_reverse` utilize recursion to accomplish opposite ends of the same task: sorting the tree. `Node.traverse` will return a generator that outputs the values on the far left of the tree first, and ends with the values on the far right of the tree. The reverse is true for `Node.tra_reverse`. The following code demonstrates this recursion: 

    def traverse(self):
        if self._left is not None:
            yield from self._left.traverse()
        for _ in range(self._quantity):
            yield self._value
        if self._right is not None:
            yield from self._right.traverse()

For `Node.search`, the Tree is walked along in a similar fashion to insert. This time though, it is looking for matches specifically for the value it receives. If it receives a match, the function returns the Node it matched with. Else, it returns `None`.

## Potential Modification

To improve this Binary Search Tree in the future, it may be wise to implement ways of balancing the tree. Such an example of this is a "height-balanced" tree. In a height-balanced tree, the two sub-trees coming off of the root differ in height by at most one level. This is possible through a variety of methods, such as rotations in an AVL tree. Overall, the variety of self-balancing trees introduces many potential improvements to this code.

## Final Thoughts

Concluding the project, I must say that while the code itself appears simple afterwards, I learned much from the process. This lab and project in particular helped demonstrate the concepts of classes and recursion in Python for which I was not quite comfortable with yet. Now, though, I am much more confident with understanding classes and recursion on top of the opportunity to handle Binary Search Trees. So, while the coding was concise, the learning experience was plentiful.

[^1]:Paul E. Black, "binary search tree", in Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 30 August 2021. Available from: https://www.nist.gov/dads/HTML/binarySearchTree.html. 