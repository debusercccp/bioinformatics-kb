---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 15
tags: [note, aads]
---

> [[AADS 14 - Trees and binary trees|← Trees and binary trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 16 - Hash tables|Hash tables →]]

# Binary search trees

*Reference: CLRS Ch. 12.*

## 8.1 Definition

The idea (around 1960) is to bring binary search to a linked structure. A **Binary Search Tree (BST)** is a rooted binary tree in which each node v has a sortable key v.key and data v.data, with the **sorting property**: all keys in the left subtree of v are ≤ v.key and all keys in the right subtree are ≥ v.key (variants put equal keys consistently on one side). The property allows binary search on the tree: an **in-order visit returns the keys in sorted order**. All basic operations cost O(h), where h is the height of the tree.

Operations: search(T, k), insert(T, k, d), delete(T, k); auxiliary: max(T), min(T), predecessor(T) and successor(T) (the node preceding/following T in the in-order visit).

## 8.2 Search, insert, min, max

     1: function search(BST T, Key k) → Node
     2:     tmp = T.root
     3:     while tmp ≠ NIL do
     4:         if k == tmp.key then return tmp
     6:         else if k < tmp.key then tmp = tmp.left
     8:         else tmp = tmp.right
    10:     return NIL

Best case O(1) (k at the root), worst case Θ(h): the search follows a single root-to-leaf path. (Example: searching 8 or 12 in the class tree, going left or right at each node.)

     1: function insert(BST T, Key k, Data d)
     2:     N = Node(k, d), P = NIL, S = T.root
     3:     while S ≠ NIL do                 ▷ search the position
     4:         P = S
     5:         if k < S.key then S = S.left
     7:         else S = S.right
     9:     N.parent = P
    10:     if P == NIL then T.root = N      ▷ the tree was empty
    12:     else if k < P.key then P.left = N
    14:     else P.right = N

The new node is always a leaf. Θ(h) in the worst case. (The implementation is not strict: inserting an existing key adds a duplicate on the right; a variant updates the data instead.)

    1: function min(Node T) → Node       1: function max(Node T) → Node
    2:     while T.left ≠ NIL do         2:     while T.right ≠ NIL do
    3:         T = T.left                3:         T = T.right
    4:     return T                      4:     return T

The minimum is the leftmost node, the maximum the rightmost: Θ(h) worst case.

## 8.3 Predecessor

     1: function predecessor(Node T) → Node
     2:     if T == NIL then return NIL
     4:     else if T.left ≠ NIL then          ▷ case 1
     5:         return max(T.left)
     6:     else                               ▷ case 2
     7:         P = T.parent
     8:         while P ≠ NIL and T == P.left do
     9:             T = P
    10:             P = P.parent
    11:         return P

Case 1: if T has a left subtree, the predecessor is the maximum of that subtree. Case 2: otherwise, go up until we arrive from a right child; that ancestor is the predecessor (NIL if T is the minimum). Worst case Θ(h), best case O(1). The successor is symmetric (min of the right subtree, or go up until we arrive from a left child).

## 8.4 Delete

Three cases for the node v to delete:

1.  v is a **leaf**: remove it.
2.  v has **one child**: link the child directly to v’s parent.
3.  v has **two children**: replace v’s key and data with those of its predecessor u (the maximum of the left subtree, which has no right child), then delete u, which falls in case 1 or 2.

<!-- -->

     1: function delete(BST T, Key k)
     2:     v = search(T, k)
     3:     if v ≠ NIL then
     4:         if v.left ≠ NIL and v.right ≠ NIL then   ▷ case 3
     5:             u = predecessor(v)
     6:             v.key = u.key
     7:             v.data = u.data
     8:             deletenode(T, u)
     9:         else                                     ▷ cases 1 and 2
    10:             deletenode(T, v)

     1: function deletenode(BST T, Node v)               ▷ v has at most one child
     2:     p = v.parent
     3:     if v.right == NIL then c = v.left
     5:     else c = v.right
     7:     if p == NIL then T.root = c                  ▷ v is the root
     9:     else if p.left == v then p.left = c          ▷ v is a left child
    11:     else p.right = c                             ▷ v is a right child
    13:     if c ≠ NIL then c.parent = p

Cost: search Θ(h), predecessor Θ(h), deletenode O(1) ⇒ worst case Θ(h), best case O(1). The pseudocode is not complex per se, but many pointers must be updated (class note). Example from class: removing 80, which has two children: its predecessor (max of its left subtree) takes its place.

## 8.5 Height and costs

All operations cost O(h) in the worst case, so the average cost depends on the average height.

- **Maximum height:** h = n − 1 = Θ(n), when the BST degenerates into a list (e.g. keys inserted in sorted order). A BST of height h has at least h + 1 nodes.
- **Minimum height:** h = Θ(log n), when the tree is complete/balanced. A BST of height h has at most 2<sup>h+1</sup> − 1 nodes, so n ≤ 2<sup>h+1</sup> − 1 ⇒ h ≥ log<sub>2</sub>(n + 1) − 1.
- On average, the height of a BST built by inserting n keys in random order is O(log n).

**Balanced trees.** Self-balancing search trees (AVL, red-black trees, B-trees, 2-3 trees, …) keep h = Θ(log n): search, insert and delete perform re-balancing when needed without increasing their O(h) cost, so all operations become O(log n).

**Dictionary: cost summary (worst / average).**

| Implementation | search              | insert          | delete          |
|:---------------|:--------------------|:----------------|:----------------|
| Unsorted array | Θ(n) / Θ(n)         | Θ(n) / Θ(n)     | Θ(n) / Θ(n)     |
| Sorted array   | Θ(log n) / O(log n) | Θ(n) / O(n)     | Θ(n) / O(n)     |
| Linked list    | Θ(n) / Θ(n)         | Θ(n) / Θ(n)     | Θ(n) / Θ(n)     |
| BST            | Θ(n) / O(log n)     | Θ(n) / O(log n) | Θ(n) / O(log n) |
| Balanced BST   | O(log n)            | O(log n)        | O(log n)        |

The big benefit of BSTs comes when the tree is well balanced.

---
> [[AADS 14 - Trees and binary trees|← Trees and binary trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 16 - Hash tables|Hash tables →]]
