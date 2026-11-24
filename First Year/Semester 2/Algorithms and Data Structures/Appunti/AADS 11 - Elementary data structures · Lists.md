---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 11
tags: [note, aads]
---

> [[AADS 10 - Elementary data structures · Data structures, prototype and implementation + The Dictionary|← Elementary data structures · Data structures, prototype and implementation + The Dictionary]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 12 - Elementary data structures · Stack|Elementary data structures · Stack →]]

# Lists

A **List** stores elements in sequential order (first, second, …, last) and supports at least search, insert, delete.

- **Array implementation:** order given by the indices; static allocation; bounded size but fast access.
- **Linked list implementation** (Newell, Shaw, Simon, IPL language, 1955–56): order given by a chain of pointers; dynamic allocation; unbounded size but slow access.

Memory picture: an array needs a block of *contiguous* free cells (with 5 scattered free cells we cannot allocate an array of size 5), while a linked list can use isolated free cells.

### 6.3.1 Singly linked lists

Each node x has x.key (not necessarily unique) and x.next (pointer to the next node; NIL for the last). It can be traversed only from head to tail.

    class Node:
        def __init__(self, key=None):
            self.key = key
            self.next = None
    class SLList:
        def __init__(self):
            self.head = None

(In Python, self is the reference to the instance: without it we would not access the object’s fields.)

    1: function search(SLList L, Key k) → Node
    2:     tmp = L.head
    3:     while tmp ≠ NIL do
    4:         if tmp.key == k then return tmp
    6:         tmp = tmp.next
    7:     return NIL

Returns the first node with key k. Worst Θ(n), average Θ(n) (n/2 nodes visited on average), best O(1): equivalent to linear search on arrays.

    1: function head_insert(SLList L, Key k)       ▷ O(1)
    2:     tmp = Node(k)
    3:     tmp.next = L.head                       ▷ update (1)
    4:     L.head = tmp                            ▷ update (2)

    1: function tail_insert(SLList L, Key k)       ▷ Θ(n)
    2:     if L.head == NIL then
    3:         L.head = Node(k)
    4:     else
    5:         tmp = L.head
    6:         while tmp.next ≠ NIL do
    7:             tmp = tmp.next
    8:         tmp.next = Node(k)

(Class note: a frequent mistake is the loop condition: we stop on the last node, so the test is tmp.next ≠ NIL, not tmp ≠ NIL.)

    1: function delete(SLList L, Key k)
    2:     tmp = search_prev(L, k)
    3:     if tmp ≠ NIL then
    4:         tmp.next = tmp.next.next            ▷ case 1
    5:     else if L.head ≠ NIL and L.head.key == k then
    6:         L.head = L.head.next                ▷ case 2: head delete

    1: function search_prev(SLList L, Key k) → Node
    2:     prev = NIL
    3:     curr = L.head
    4:     while curr ≠ NIL do
    5:         if curr.key == k then return prev
    7:         prev = curr
    8:         curr = curr.next
    9:     return NIL

To delete we need the node *preceding* the one to remove; search_prev returns NIL both when k is missing and when k is at the head (case 2). We assume a garbage collector frees the removed node. Costs as linear search: Θ(n) worst/average, O(1) best.

**Variants.**

- **Doubly linked list:** each node also has x.prev. Traversable in both directions; no need to search the previous node to delete; same costs.
- **Circular (doubly) linked list:** the last node’s next points to the first, the first’s prev to the last. Head and tail are both reachable in O(1), so tail insert is O(1); scanning is slightly more complex (no NIL to stop on).
- **Head and tail pointers:** a singly or doubly linked list keeping pointers to both ends. Easier than circular lists, same costs.

|                      | search | head insert | tail insert | delete |
|:---------------------|:-------|:------------|:------------|:-------|
| Singly linked        | O(n)   | O(1)        | Θ(n)        | O(n)   |
| Doubly linked        | O(n)   | O(1)        | Θ(n)        | O(n)   |
| Circular             | O(n)   | O(1)        | O(1)        | O(n)   |
| Head + tail pointers | O(n)   | O(1)        | O(1)        | O(n)   |

**Dictionary on a linked list.** search = llsearch; insert = llsearch, then update the data or head-insert; delete = lldelete. All O(n): no improvement over sorted arrays (search dominates), but the structure is unbounded. Keeping the list ordered does not help, because binary search is impossible without random access.

### 6.3.2 Recursive list algorithms (class exercises)

*Beware: every complex exam problem is a re-adaptation of a simpler one.* The recursive scheme on a list is always: base case L == NIL; otherwise handle the current node and recurse on L.next, returning the (possibly new) first node.

    function search(Node L, Key k) → Node
        if L == NIL or L.key == k then
            return L
        else
            return search(L.next, k)

    function count(Node L, Key k) → int
        if L == NIL then return 0
        else if L.key == k then return 1 + count(L.next, k)
        else return count(L.next, k)

    function delete(Node L, Key k) → Node        ▷ delete the first occurrence
        if L == NIL then return NIL
        else if L.key == k then return L.next
        else
            L.next = delete(L.next, k)
            return L

    function deleteall(Node L, Key k) → Node     ▷ delete all occurrences
        if L == NIL then return NIL
        else if L.key == k then return deleteall(L.next, k)
        else
            L.next = deleteall(L.next, k)
            return L

    function deleteeven(Node L) → Node           ▷ delete all even keys
        if L == NIL then return NIL
        else if L.key mod 2 == 0 then return deleteeven(L.next)
        else
            L.next = deleteeven(L.next)
            return L

They are used as L.head = delete(L.head, k). All cost Θ(n).

---
> [[AADS 10 - Elementary data structures · Data structures, prototype and implementation + The Dictionary|← Elementary data structures · Data structures, prototype and implementation + The Dictionary]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 12 - Elementary data structures · Stack|Elementary data structures · Stack →]]
