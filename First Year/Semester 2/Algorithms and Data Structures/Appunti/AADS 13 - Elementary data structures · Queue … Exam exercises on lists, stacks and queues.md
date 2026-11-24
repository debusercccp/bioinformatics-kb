---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 13
tags: [note, aads]
---

> [[AADS 12 - Elementary data structures · Stack|← Elementary data structures · Stack]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 14 - Trees and binary trees|Trees and binary trees →]]

# Queue

A **Queue** supports enqueue (add at the rear) and dequeue (remove from the front): **FIFO**, like a line of people. Elements in the middle are not accessible. Applications: process scheduling, breadth-first search.

Implementations: circular linked list or linked list with head and tail pointers (enqueue at the tail, dequeue at the head; unbounded, pointer overhead), or a **circular array** (no overhead, bounded size). In all cases O(1).

**Circular array.** The buffer buf of size n, the index head of the front, tail of the first free slot, and size. Indices wrap around modulo n:

    class CircularQueue:
        def __init__(self, n):
            self.buf = [None]*n
            self.head = 0
            self.tail = 0
            self.size = 0
        def enqueue(self, x):
            if self.isfull(): raise RuntimeError("Full queue")
            self.buf[self.tail] = x
            self.tail = (self.tail + 1) % len(self.buf)
            self.size = self.size + 1
        def dequeue(self):
            if self.isempty(): raise RuntimeError("Empty queue")
            x = self.buf[self.head]
            self.head = (self.head + 1) % len(self.buf)
            self.size = self.size - 1
            return x

## 6.6 Built-in structures in Python

**list** is a dynamic array: access by index O(1), append and pop() at the end amortized O(1), insert(0, x), pop(0) and del q\[i\] O(n) (they shift the elements), x in L O(n), sort O(n log n). Using a list as a queue (append + pop(0)) gives O(n) dequeues.

**deque** (collections.deque), double-ended queue: append, appendleft, pop, popleft all O(1); access to the middle O(n). It is the efficient way to implement a queue in Python (there is no built-in queue class in the core language; experiments in class show the dequeue on a list becomes much slower than on a deque as n grows).

## 6.7 Exam exercises on lists, stacks and queues

**Exam 13 February 2026, Ex. 2: doubling a singly linked list.** Duplicate every element, placing the copy next to the original (\[4, 5, 2\] → \[4, 4, 5, 5, 2, 2\]).

    1: function doubling(Node L) → Node
    2:     if L == NIL then
    3:         return NIL
    4:     else
    5:         node = Node(L.key)            ▷ new node with the same key
    6:         node.next = L                 ▷ link it before the original
    7:         L.next = doubling(L.next)     ▷ process the rest of the list
    8:         return node                   ▷ new first node

Each node is processed once with constant work: Θ(n).

**Exam 29 June 2023, Ex. 2: list complement (solved in class).** Remove from L<sub>1</sub> all integers appearing in L<sub>2</sub>, recursively, without modifying L<sub>2</sub> (L<sub>1</sub> = \[2, 1, 3, 1, 4\], L<sub>2</sub> = \[5, 3, 1, 3\] ⇒ L<sub>1</sub> = \[2, 4\]). Three cases: one list is empty (return L<sub>1</sub>); L<sub>1</sub>.key is in L<sub>2</sub> (drop the node: return the recursive call on L<sub>1</sub>.next); otherwise set L<sub>1</sub>.next to the recursive call and return L<sub>1</sub>.

     1: function listComplement(Node L1, List L2) → Node
     2:     if L1 == NIL or L2.head == NIL then
     3:         return L1
     4:     else if search(L2.head, L1.key) ≠ NIL then
     5:         return listComplement(L1.next, L2)
     6:     else
     7:         L1.next = listComplement(L1.next, L2)
     8:         return L1
    10: function search(Node L, int key) → Node
    11:     while L ≠ NIL and L.key ≠ key do L = L.next
    12:     return L

Used as L<sub>1</sub>.head = listComplement(L<sub>1</sub>.head, L<sub>2</sub>). With m = \|L<sub>1</sub>\|, n = \|L<sub>2</sub>\|: worst case Θ(mn) (no element of L<sub>1</sub> in L<sub>2</sub>), best case Θ(m) (L<sub>1</sub> contains a single repeated value found at the head of L<sub>2</sub>). In class we also wrote a version for *sorted* lists, which advances on L<sub>1</sub> or on L<sub>2</sub> at each step (merge-like): if L<sub>1</sub>.key == L<sub>2</sub>.key remove L<sub>1</sub>; if L<sub>1</sub>.key \< L<sub>2</sub>.key keep L<sub>1</sub> and advance on L<sub>1</sub>; if L<sub>1</sub>.key \> L<sub>2</sub>.key advance on L<sub>2</sub>. It stops when one list is empty, with cost O(m + n).

**Exam 28 June 2024, Ex. 2: palindrome on a doubly linked list.** Find the tail, then compare characters moving the head forward and the tail backward.

     1: function ispalindrome(List L) → bool
     2:     if L == NIL or L.head == NIL then
     3:         return true                     ▷ the empty string is a palindrome
     4:     else
     5:         head = tail = L.head
     6:         while tail.next ≠ NIL do tail = tail.next
     8:         return ispalindromeaux(head, tail)
    10: function ispalindromeaux(Node head, Node tail) → bool
    11:     if head.char ≠ tail.char then return false
    13:     else if head == tail or head.next == tail then return true
    15:     else return ispalindromeaux(head.next, tail.prev)

The auxiliary function is Θ(n) in the worst case (a palindrome) and O(1) in the best case (first and last characters differ); ispalindrome is always Θ(n) because it must reach the tail first.

**Exam 14 February 2025, Ex. 3: stack and queue execution.** Sequence TTG\*A\*\*\*A\*AC\*\*AC, where a letter is a push/enqueue and \* a pop/dequeue.

- Stack: push T, T, G; pop → G; push A; pop → A, T, T; push A; pop → A; push A, C; pop → C, A; push A, C. Popped sequence **GATTACA**; at the end the stack contains A C, with C on top.
- Queue: enqueue T, T, G; dequeue → T; enqueue A; dequeue → T, G, A; enqueue A; dequeue → A; enqueue A, C; dequeue → A, C; enqueue A, C. Dequeued sequence **TTGAAAC**; at the end the queue contains A C, with A at the front.

### 6.7.1 Past exam exercises on this topic

3)  Ex. 2 2022/07/21 F; (C) Ex. 2 2022/11/30 F; (C) Ex. 2 2023/02/06; (C) Ex. 2 2023/06/29; (E) Ex. 3 2023/07/24 F; (C) Ex. 2 2023/10/27; (A) Ex. 3 2023/10/27 (requires binary trees); (C) Ex. 2 2024/02/12; (C) Ex. 2 2024/06/28; (C) Ex. 2 2024/07/26; (E) Ex. 3 2025/02/14; (C) Ex. 2 2026/02/13.

---
> [[AADS 12 - Elementary data structures · Stack|← Elementary data structures · Stack]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 14 - Trees and binary trees|Trees and binary trees →]]
