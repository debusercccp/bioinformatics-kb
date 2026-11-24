---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 14
tags: [note, aads]
---

> [[AADS 13 - Elementary data structures · Queue … Exam exercises on lists, stacks and queues|← Elementary data structures · Queue … Exam exercises on lists, stacks and queues]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 15 - Binary search trees|Binary search trees →]]

# Trees and binary trees

*Reference: CLRS Ch. 10.4 and Appendix B.5.*

## 7.1 Definitions

A **Tree** is a non-linear data structure representing a hierarchy: a set of nodes (vertices) and a set of edges (links) such that there is exactly one way (path) to go from a node to another. The nodes directly reachable from a node are its **children**. A tree is **ordered** if the children of each node are ordered (first child, second child, …), **rooted** if one node is designated as the root.

A **Binary Tree** is an ordered tree in which each node has at most two children, a left and/or a right one (a node may have a right child and no left child, and conversely).

- **Depth** of a node: length (number of edges) of the path from the root to the node.
- **Level**: the set of nodes at the same depth.
- **Height** of a tree: its maximum depth.
- **Degree** of a node: number of its children. A **leaf** has degree 0.
- A binary tree is **full** if each node is either a leaf or has degree 2.
- A binary tree is **complete** if it is full and all leaves are at the same depth. A complete binary tree of height h has 2<sup>h+1</sup> − 1 nodes and 2<sup>h</sup> leaves.

**Fundamental property.** Every non-empty tree with n nodes has exactly n − 1 edges (proof by induction). It can be used to prove that a structure is *not* a tree; the converse does not hold in general (n − 1 edges do not guarantee a tree).

## 7.2 Traversal algorithms

Tree traversal (tree search) visits all the nodes. **Depth-First Search (DFS)** goes as deep as possible before visiting the other nodes of the same level; it has three variants. **Breadth-First Search (BFS)** visits level by level. Assuming visit(T) is O(1), all traversals cost Θ(n) in every case.

    1: function preorder(Node T)         1: function postorder(Node T)
    2:     if T ≠ NIL then               2:     if T ≠ NIL then
    3:         visit(T)                  3:         postorder(T.left)
    4:         preorder(T.left)          4:         postorder(T.right)
    5:         preorder(T.right)         5:         visit(T)

    1: function inorder(Node T)
    2:     if T ≠ NIL then
    3:         inorder(T.left)
    4:         visit(T)
    5:         inorder(T.right)

Pre-order visits the node first, post-order last (class note: *similar to pre-order, but the visit — e.g. the printing — is the last thing*), in-order in the middle.

     1: function BFS(Tree T)
     2:     Q = Queue()
     3:     if T.root ≠ NIL then
     4:         enqueue(Q, T.root)
     5:     while Q.size ≠ 0 do
     6:         x = dequeue(Q)
     7:         visit(x)
     8:         if x.left ≠ NIL then enqueue(Q, x.left)
    10:         if x.right ≠ NIL then enqueue(Q, x.right)

The queue simulates the level-by-level order. To know the depth of each node we can enqueue the pair (node, depth), with the children at depth + 1.

The traversals generalize to non-binary trees (visit all the children in order); only in-order needs an extra convention (e.g. visit the first k children, then the root, then the rest).

**Example: counting the nodes.**

    1: function countnodes(Node T) → int
    2:     if T == NIL then
    3:         return 0
    4:     else
    5:         return 1 + countnodes(T.left) + countnodes(T.right)

It is a post-order traversal (to evaluate a node we must evaluate its children first) and costs Θ(n).

**Rebuilding a tree from its traversals.** The root is the first key of the pre-order and the last of the post-order. In pre-order the key after the root is its left child (or the right child if there is no left one); in post-order the key before the root is its right child (or the left one if there is no right child). If they are different, they are the left and the right child; if they are the same key the node has a single child and pre- and post-order alone cannot tell on which side (this is the typical ambiguity). Then split the sequences into the two subtrees and repeat.

## 7.3 Implementation

**Binary tree with pointers:** each node has key, data, left, right and (optionally) parent.

    class Node:
        def __init__(self, key=None):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

**Non-binary trees.** Version 1: each node has an array of k pointers to the children (k fixed; wastes space if many nodes have fewer than k children). Version 2 (left-child right-sibling): each node has a pointer to its first child and one to its next sibling, so the children of a node form a singly linked list. Version 2 is like a binary tree in which “left” means first child and “right” means next sibling; the pseudocode of DFS and BFS is adapted by scanning the list of children.

## 7.4 Exam exercises on trees

**Exam 24 June 2022, Ex. 2: is a binary tree full?** T is full iff it is empty, or it is a single node, or both subtrees are non-empty full trees.

    1: function fullbintree(Node T) → bool
    2:     if T == NIL then return true                         ▷ empty tree
    4:     else if T.left == NIL and T.right == NIL then return true    ▷ leaf
    6:     else if T.left == NIL or T.right == NIL then return false    ▷ one child
    8:     else return fullbintree(T.left) and fullbintree(T.right)

Worst case Θ(n) (T full, all nodes checked); best case O(1) (the root has only one child).

**Exam 16 December 2024, Ex. 2: mirror tree** (T must stay unchanged).

     1: function mirrortree(Node T) → Node
     2:     if T == NIL then return NIL
     4:     else
     5:         tmp = Node(T.key)
     6:         tmp.left = mirrortree(T.right)
     7:         if tmp.left ≠ NIL then tmp.left.parent = tmp
     9:         tmp.right = mirrortree(T.left)
    10:         if tmp.right ≠ NIL then tmp.right.parent = tmp
    12:         return tmp

Called as T’.root = mirrortree(T.root). Each node is copied once at constant cost: Θ(n).

**Exam 12 February 2024, Ex. 3: tree from pre-order 7 3 6 1 2 2 4 5 4 6 and post-order 1 2 6 2 3 4 6 5 4 7.** The root is 7; the key after it in pre-order is 3, the key before it in post-order is 4: being different, 3 is the left and 4 the right child. Left subtree: pre 3 6 1 2 2, post 1 2 6 2 3 ⇒ 3 has children 6 (left) and 2 (right), 6 has children 1 and 2. Right subtree: pre 4 5 4 6, post 4 6 5 4 ⇒ 4 has the single child 5, which has children 4 and 6. The only ambiguity is whether 5 is the left or the right child of 4. (Class tip: *the root is the first value of the pre-order and the last of the post-order.*)

**Exam 1 July 2026, Ex. 3: BST from pre-order 1 5 4 3 2 4 7 6 8 and post-order 2 4 3 4 6 8 7 5 1.** Root 1; in a BST, 5 \> 1 so 5 is the right child and 1 has no left child (confirmed by the post-order). For 5: post-order gives 7 (\> 5) as right child, pre-order gives 4 (\< 5) as left child. Keys smaller than 5 (4, 3, 2, 4) go left, larger (7, 6, 8) go right. Left: pre 4 3 2 4, post 2 4 3 4 ⇒ 4 has the single child 3 on the left (3 \< 4), 3 has children 2 and 4. Right: pre 7 6 8, post 6 8 7 ⇒ 7 with children 6 and 8. Here the BST property removes all ambiguity: the solution is unique.

            1
             \
              5
            /   \
           4     7
          /     / \
         3     6   8
        / \
       2   4

### 7.4.1 Past exam exercises on this topic

3)  Ex. 2 2022/06/24 F; (A) Ex. 3 2022/07/21 F; (C) Ex. 2 2022/10/28; (E) Ex. 3 2022/10/28; (C) Ex. 2 2023/01/16; (E) Ex. 3 2023/01/16; (C) Ex. 2 2023/07/24 F; (A) Ex. 3 2023/10/27; (C) Ex. 2 2023/12/01; (C) Ex. 2 2024/01/15; (A) Ex. 3 2024/02/12; (C) Ex. 2 2024/04/24; (A) Ex. 3 2024/04/24; (E) Ex. 3 2024/07/26; (C) Ex. 2 2024/12/16; (E) Ex. 3 2026/07/01.

---
> [[AADS 13 - Elementary data structures · Queue … Exam exercises on lists, stacks and queues|← Elementary data structures · Queue … Exam exercises on lists, stacks and queues]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 15 - Binary search trees|Binary search trees →]]
