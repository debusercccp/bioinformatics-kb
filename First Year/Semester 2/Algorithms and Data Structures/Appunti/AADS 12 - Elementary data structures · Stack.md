---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 12
tags: [note, aads]
---

> [[AADS 11 - Elementary data structures · Lists|← Elementary data structures · Lists]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 13 - Elementary data structures · Queue … Exam exercises on lists, stacks and queues|Elementary data structures · Queue … Exam exercises on lists, stacks and queues →]]

# Stack

A **Stack** supports push (add an element) and pop (remove the most recently added element): **LIFO**, like a pile of dishes. Applications: activation records of function calls, stack-oriented languages (PostScript, BibTeX), undo/redo in editors, syntax parsing (balanced parentheses).

A stack is a special list. **With a singly linked list:** push = head insert, pop = remove the head; unbounded, small memory overhead for the pointers (a doubly or circular list would add overhead without benefit). **With an array:** push writes in the first free position, pop removes the last element; no overhead, bounded size. In both cases push and pop are O(1).

    1: function push(Stack S, Data x)
    2:     if S.top == S.length then error "overflow"
    4:     else
    5:         S.top = S.top + 1
    6:         S.stack[S.top] = x

    1: function pop(Stack S) → Data
    2:     if S.top == 0 then error "underflow"
    4:     else
    5:         e = S.stack[S.top]
    6:         S.top = S.top − 1
    7:         return e

### 6.4.1 Dynamic array

Resizing an array means allocating a new one and copying everything. Strategy: **double** the size when the array is full; **halve** it when occupancy drops to 1/4.

     1: function push(Stack S, Int x)
     2:     if S.top == S.length then
     3:         n = S.length
     4:         let T[1 ⋯ 2n] be a new array
     5:         for i = 1, ⋯, n do T[i] = S.stack[i]
     7:         S.stack = T
     8:         S.length = 2n
     9:     S.top = S.top + 1
    10:     S.stack[S.top] = x

     1: function pop(Stack S) → Int
     2:     if S.top == 0 then error "underflow"
     4:     else
     5:         e = S.stack[S.top]
     6:         S.top = S.top − 1
     7:         if S.top ≤ ⌊S.length/4⌋ then
     8:             n = S.length
     9:             let T[1 ⋯ ⌈n/2⌉] be a new array
    10:             for i = 1, ⋯, ⌊n/4⌋ do T[i] = S.stack[i]
    12:             S.stack = T
    13:             S.length = ⌈n/2⌉
    14:         return e

Push and pop cost Θ(n) in the worst case (the copy) and O(1) in the best case.

**Amortized analysis of push.** Using the O(n) worst case, n pushes would cost O(n<sup>2</sup>), but this bound is not tight: the array is expanded rarely. Starting from size 1, the i-th push costs c<sub>i</sub> = i if i − 1 is an exact power of 2 (copy), 1 otherwise. Aggregate method:

Σ<sub>i=1..n</sub> c<sub>i</sub> ≤ n + Σ<sub>j=0..log n</sub> 2<sup>j</sup> = n + (2<sup>log n + 1</sup> − 1) ≤ n + 2n = 3n − 1 = O(n),

so the amortized cost of push is O(1). For pop on a full stack and for any mixed sequence of n push/pop on an initially empty dynamic array the actual cost is O(n) (proved with the accounting method, e.g. 2 € per operation: 1 € for the operation, 1 € deposited), so both are O(1) amortized. This holds for this expansion/contraction policy (double when full, halve at 1/4).

**Python.** A stack is simply a list: push = list.append(x), pop = list.pop() (both amortized O(1)); isempty() is len(self.stack) == 0, top is self.stack\[−1\].

---
> [[AADS 11 - Elementary data structures · Lists|← Elementary data structures · Lists]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 13 - Elementary data structures · Queue … Exam exercises on lists, stacks and queues|Elementary data structures · Queue … Exam exercises on lists, stacks and queues →]]
