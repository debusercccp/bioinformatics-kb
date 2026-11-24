---
course: "[[Algorithms and Data Structures]]"
module: "[[Algorithms and Data Structures]]"
source: "MCB/AADS/Algorithms_and_Data_Structures_merged_notes.docx"
order: 16
tags: [note, aads]
---

> [[AADS 15 - Binary search trees|← Binary search trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 17 - Algorithmic techniques|Algorithmic techniques →]]

# Hash tables

*Reference: CLRS Ch. 11.*

## 9.1 Introduction

Many applications need a Dictionary supporting efficiently only search, insert and delete (e.g. compilers store the identifiers of a program). A **Hash Table** is an efficient implementation of a Dictionary that generalizes array indexing. The worst-case cost of the operations is linear, but under reasonable probabilistic assumptions their **average cost is O(1)**. In the short notes: a hash table stores key → value pairs; a **hash function** turns a key (e.g. a string) into an index of an array, and the pair is stored at that index.

Notation (from the personal notes): U = universe of all possible keys; K = set of keys actually used; m = table size (number of slots); n = number of keys stored; α = n/m = **load factor** (average number of elements per slot); L = length of the longest list (with chaining). Division, multiplication and algebraic coding are *hash functions*, not methods to resolve collisions.

## 9.2 Direct-address tables

If U = {0, …, m − 1} with m small (\|K\| ≈ \|U\|), use an array T of size \|U\| and store key k at position k (keys are distinct):

    1: function search(Data T[0, ⋯, m − 1], Key k) → Data
    2:     return T[k]
    4: function insert(Data T[0, ⋯, m − 1], Key k, Data d)
    5:     T[k] = d
    7: function delete(Data T[0, ⋯, m − 1], Key k)
    8:     T[k] = NIL

Time O(1) in all cases, memory Θ(\|U\|): acceptable if \|K\| ≈ \|U\|, unacceptable if \|K\| ≪ \|U\|. Example: identifiers of up to 20 lowercase letters/digits give \|U\| \> 26·36<sup>19</sup> ≈ 10<sup>31</sup>; with 4-byte pointers the table would need more than 10<sup>19</sup> terabytes (the world’s storage capacity in 2025 is below 10<sup>12</sup> TB).

## 9.3 Hash tables

Use an array T\[0..m−1\] with m = Θ(\|K\|) and a **hash function** h : U → \[0, m − 1\]; key k is stored in slot T\[h(k)\] (h(k) is the *hash value* of k). If two distinct keys have the same hash value we have a **collision**. Collisions cannot be avoided (\|U\| \> m), only minimized and resolved.

To implement a hash table we need: (1) a hash function, fast to compute and distributing the keys well on T; (2) a strategy to resolve collisions; (3) an array of size m = Θ(\|K\|). In general m can only be estimated, and the table may have to be resized; the best m depends on the hash function and on the collision strategy.

### 9.3.1 Hash functions

A good hash function satisfies **simple uniform hashing**: every index i = h(k) is generated with probability 1/m. To guarantee it we would need the probability distribution of the keys, which is rarely known (example: if keys are drawn uniformly from \[0, 1), h(k) = ⌊mk⌋ is simple uniform). Working assumptions:

1.  all keys are equally likely to be drawn from U (not always true, e.g. identifiers in a program, but needed for a general study);
2.  hash functions are computable in O(1) (otherwise hashing would dominate the costs);
3.  keys are non-negative integers (any key can be turned into one, e.g. through its binary representation).

*From string to integer:* with codes a = 1, b = 2, …, z = 26 (5 bits each), bin(“beer”) = 00010 00101 00101 10010 = 70834 in base 10.

**Division method:** h(k) = k mod m. Fast (one integer division). Examples: m = 12, k = 100 ⇒ h(k) = 4; m = 10, k = 101 ⇒ 1. Not every m is good: with m = 10, h(k) is just the last digit; with m = 2<sup>p</sup> it depends only on the last p bits. Choose **m prime, far from powers of 2 (and of 10)**.

**Multiplication method:** h(k) = ⌊m(kC − ⌊kC⌋)⌋ with a constant 0 \< C \< 1: multiply k by C, take the fractional part, multiply by m and take the integer part. Examples: m = 12, k = 101, C = 0.8 ⇒ 9; m = 1000, k = 123, C = (√5 − 1)/2 ≈ 0.618 ⇒ 18. The value of m is not critical; C affects uniformity (Knuth suggests (√5 − 1)/2).

**Algebraic coding:** h(k) = (k<sub>n</sub>x<sup>n</sup> + k<sub>n−1</sub>x<sup>n−1</sup> + ⋯ + k<sub>1</sub>x + k<sub>0</sub>) mod m, where k<sub>i</sub> are the bits or decimal digits of k and x is a constant. Example: m = 12, k = 234, x = 3 ⇒ (2·3<sup>2</sup> + 3·3 + 4) mod 12 = 31 mod 12 = 7. It uses all digits of k, but naive evaluation needs n sums and about n(n + 1)/2 products, Θ(log<sup>2</sup> k). **Horner’s method** rewrites p(x) = a<sub>0</sub> + x(a<sub>1</sub> + x(a<sub>2</sub> + ⋯ + x(a<sub>n−1</sub> + a<sub>n</sub>x))) with n sums and n products, so the cost drops to Θ(log k), linear in the number of digits; since keys usually have few digits, it is treated as constant.

**The collision problem.** Even with simple uniform hashing collisions are very likely: by the **birthday paradox**, among 23 random people the probability that two share a birthday is above 50%. We review two ways to resolve collisions: chaining and open addressing.

## 9.4 Chaining

All keys with hash value i are stored in a singly linked list; slot T\[i\] points to its head.

    1: function search(SLList T[0, ⋯, m − 1], Key k) → Data
    2:     tmp = llsearch(T[h(k)], k)
    3:     if tmp ≠ NIL then return tmp.data
    4:     else return NIL
    6: function insert(SLList T[0, ⋯, m − 1], Key k, Data d)
    7:     tmp = llsearch(T[h(k)], k)
    8:     if tmp ≠ NIL then tmp.data = d
    9:     else llinsert(T[h(k)], k, d)       ▷ head insert
    11: function delete(SLList T[0, ⋯, m − 1], Key k)
    12:     lldelete(T[h(k)], k)

There are no constraints on m (the hash function may impose some): if m is too big we waste space, if too small the lists become long. With L the length of the longest list, search, insert and delete cost Θ(L) in the worst case and O(1) in the best case; L = O(n), so the worst case depends on n, not on m.

**Average case.** Under simple uniform hashing every slot has on average α = n/m keys.

- *Unsuccessful search:* computing h(k) (cost 1) plus scanning the whole list T\[h(k)\] (α keys on average): Θ(1 + α).
- *Successful search:* computing h(k) plus scanning about half of the list (α/2): Θ(1 + α/2) = Θ(1 + α).

If n = O(m) then α = O(1) and search, insert and delete all cost **O(1) on average**.

## 9.5 Open addressing

All keys are stored in the array itself: each slot contains a key (with its data) or NIL; when a slot is full we look for an alternative position. No extra memory is used (n ≤ m, α ≤ 1). The hash function is extended with the probing step: h : U × \[0, m − 1\] → \[0, m − 1\], and the **probe sequence** h(k, 0), h(k, 1), …, h(k, m − 1) must be a permutation of the indices (each slot inspected at most once; possibly all m).

    1: function search(<Key,Data> T[0, ⋯, m − 1], Key k) → Data
    2:     i = 0
    3:     repeat
    4:         j = h(k, i)                     ▷ hash value at step i
    5:         if T[j].key == k then return T[j].data
    6:         i = i + 1
    7:     until T[j] == NIL or i == T.size
    8:     return NIL

    1: function insert(<Key,Data> T[0, ⋯, m − 1], Key k, Data d)
    2:     i = 0
    3:     repeat
    4:         j = h(k, i)
    5:         if T[j] == NIL or T[j].key == k or T[j] == DELETED then
    6:             T[j].key = k
    7:             T[j].data = d
    8:             return
    9:         i = i + 1
    10:    until i == T.size
    11:    error "overflow"

**Deletion.** We cannot simply write NIL in the slot: search stops at a NIL slot, but the searched key could be further along its probe sequence. We write a special value **DELETED** (slot empty but previously used): search and delete treat DELETED slots as full (they continue probing), insert treats them as empty (it can reuse them).

    1: function delete(<Key,Data> T[0, ⋯, m − 1], Key k)
    2:     i = 0
    3:     repeat
    4:         j = h(k, i)
    5:         if T[j].key == k then
    6:             T[j] = DELETED
    7:             return
    8:         i = i + 1
    9:     until T[j] == NIL or i == T.size

Worst case of search, insert, delete: Θ(m) (the whole table is inspected). The average case depends on the probing strategy.

### 9.5.1 Probing strategies

**Linear inspection:** h(k, i) = (h’(k) + i) mod m, with h’ an auxiliary hash function. Upon collision inspect the next slot; the first index determines the whole sequence h’(k), h’(k) + 1, …, m − 1, 0, …, h’(k) − 1, so there are only m distinct probe sequences. Problem: **primary clustering**, long runs of occupied slots that become longer and longer (an empty slot preceded by i full slots is filled with probability (i + 1)/m).

**Quadratic inspection:** h(k, i) = (h’(k) + c<sub>1</sub>i + c<sub>2</sub>i<sup>2</sup>) mod m, c<sub>1</sub>, c<sub>2</sub> \> 0 chosen so that the sequence is a permutation. Still m distinct sequences. Problem: **secondary clustering**: two keys with the same initial index have the same probe sequence.

**Double hashing:** h(k, i) = (h<sub>1</sub>(k) + i·h<sub>2</sub>(k)) mod m. It avoids primary and secondary clustering (two keys rarely share both h<sub>1</sub> and h<sub>2</sub>) and gives more than m distinct sequences. Constraints: h<sub>2</sub>(k) must never be 0 and must let the sequence cycle through the whole table (e.g. m prime and 0 \< h<sub>2</sub>(k) \< m).

**Example** (slides): m = 10, h’(k) = h<sub>1</sub>(k) = k mod 10, keys inserted in order 53, 75, 16, 73, 10, 33, 13, 76.

| Slot | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:---|:---|----|----|:---|:---|:---|:---|:---|:---|:---|
| Linear | 10 |  |  | 53 | 73 | 75 | 16 | 33 | 13 | 76 |
| Quadratic (c<sub>1</sub> = 0, c<sub>2</sub> = 1) | 10 | 76 | 13 | 53 | 73 | 75 | 16 | 33 |  |  |
| Double, h<sub>2</sub>(k) = (k mod 9) + 1 | 10 | 76 |  | 53 | 33 | 75 | 16 | 73 | 13 |  |

Linear: 73 collides at 3 and goes to 4; 33 probes 3, 4, 5, 6 and lands in 7; 13 probes 3…7 and lands in 8; 76 probes 6, 7, 8 and lands in 9 (a single long cluster forms). Quadratic: 33 probes 3, 4 (+1), 7 (+4); 13 probes 3, 4, 7, 2 (+9 ≡ 2); 76 probes 6, 7, 0, 5, 2, 1 (with c<sub>2</sub> = 1 and m = 10 the sequence is *not* a permutation of all slots). Double: 73 has h<sub>2</sub> = 2 and probes 3, 5, 7; 33 has h<sub>2</sub> = 7: 3, 0, 7, 4; 13 has h<sub>2</sub> = 5: 3, 8; 76 has h<sub>2</sub> = 5: 6, 1.

### 9.5.2 Average-case analysis of open addressing

Assume simple uniform hashing and that all probe sequences (permutations of \[0, m − 1\]) are equally likely; α = n/m \< 1.

- **Unsuccessful search:** expected number of probes at most 1/(1 − α) for quadratic inspection and double hashing, and (1 + 1/(1 − α)<sup>2</sup>)/2 for linear inspection.
- **Successful search:** at most (1/α) ln(1/(1 − α)) for quadratic/double, and (1 + 1/(1 − α))/2 for linear.

If α is a constant the average cost is O(1). Example: with the table half full (α = 0.5), an unsuccessful search with quadratic inspection makes at most 2 probes on average (2.5 with linear inspection). Linear inspection degrades much faster as α approaches 1.

### 9.5.3 Role of the load factor

Collisions are highly probable (birthday paradox), so the strategy is to keep α small: **α \< 0.75** is considered optimal. When α reaches a threshold the table is extended, which means rebuilding it completely since all hash indices change (expensive, but rare: amortized like the dynamic array).

## 9.6 Dictionary: cost summary

| Implementation | search (worst / avg) | insert (worst / avg) | delete (worst / avg) |
|:---|:---|:---|:---|
| Unsorted array | Θ(n) / Θ(n) | Θ(n) / Θ(n) | Θ(n) / Θ(n) |
| Sorted array | Θ(log n) / O(log n) | Θ(n) / O(n) | Θ(n) / O(n) |
| Linked list | Θ(n) / Θ(n) | Θ(n) / Θ(n) | Θ(n) / Θ(n) |
| BST | Θ(h) / Θ(h̄) | Θ(h) / Θ(h̄) | Θ(h) / Θ(h̄) |
| Balanced tree | O(log n) | O(log n) | O(log n) |
| Hash table, chaining | Θ(n) / O(1) | Θ(n) / O(1) | Θ(n) / O(1) |
| Hash table, open addressing | Θ(m) / O(1) | Θ(m) / O(1) | Θ(m) / O(1) |

(h = tree height, h̄ = average height, n = number of items, m = table size.) Despite the linear worst case, hash tables are very efficient in practice, and dictionaries are typically implemented as hash tables.

## 9.7 Python dict and set

Python’s **dict** and **set** are hash tables. dict: d\[k\], d\[k\] = v, del d\[k\], k in d all O(1) on average (O(n) worst case); iteration O(n). set: add, remove, x in s O(1) average; union s\|t O(len(s) + len(t)); intersection s&t O(min(len(s), len(t))) on average, because Python iterates on the smaller set and looks up in the larger. Experiments in class (n = 10 000 and more): searching keys in a list is O(n) per search, in a dict/set O(1), so the gap grows linearly with n.

## 9.8 Exam exercises on hash tables

**Photo exercise (Ex. 3, 5 points).** m = 7, initially empty, open addressing with linear inspection h(k, i) = (h’(k) + i) mod m, h’(k) = k mod m. Show the table after: (a) insert 21, (b) insert 14, (c) insert 20, (d) insert 13, (e) delete 21, (f) insert 27.

<figure>
![[AADS-rId153.jpg|448]]
<figcaption aria-hidden="true"><p>The exercise as photographed</p></figcaption>
</figure>

- 1)  21 mod 7 = 0: slot 0 free ⇒ T\[0\] = 21.
- 2)  14 mod 7 = 0: slot 0 full; i = 1 ⇒ slot 1 ⇒ T\[1\] = 14.
- 3)  20 mod 7 = 6 ⇒ T\[6\] = 20.
- 4)  13 mod 7 = 6: slot 6 full; i = 1 ⇒ (6 + 1) mod 7 = 0 full; i = 2 ⇒ 1 full; i = 3 ⇒ 2 free ⇒ T\[2\] = 13.
- 5)  delete 21: probe slot 0, found ⇒ T\[0\] = DELETED (not NIL, otherwise a later search for 14 or 13 would stop at slot 0 and fail).
- 6)  27 mod 7 = 6: slot 6 full; i = 1 ⇒ slot 0 is DELETED, which insert treats as empty ⇒ T\[0\] = 27.

| Slot      | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
|:----------|:----|:----|:----|-----|-----|-----|:----|
| after (d) | 21  | 14  | 13  |     |     |     | 20  |
| after (e) | DEL | 14  | 13  |     |     |     | 20  |
| after (f) | 27  | 14  | 13  |     |     |     | 20  |

(Remainders written on the sheet: 21/7 → 3 remainder 0, 14/7 → 2 remainder 0, 20/7 → 2 remainder 6, 13/7 → 1 remainder 6, 27/7 → 3 remainder 6.)

**Exam 24 July 2023, Ex. 4.** m = 6, h’(k) = k mod 6; insert 17, 5, 7, 6, delete 7, insert 11.

1)  Linear inspection: 17 → 5; 5 → 5 full → 0; 7 → 1; 6 → 0 full, 1 full → 2; delete 7 ⇒ T\[1\] = DELETED; 11 → 5 full, 0 full, 1 DELETED ⇒ T\[1\] = 11. Final table: T\[0\] = 5, T\[1\] = 11, T\[2\] = 6, T\[5\] = 17, the rest empty.

2)  Chaining (head insertion): T\[5\]: 17, then 5 → 17; T\[1\]: 7; T\[0\]: 6; delete 7 empties T\[1\]; 11 goes to T\[5\]: 11 → 5 → 17. Final: T\[0\] = \[6\], T\[5\] = \[11, 5, 17\], all other lists empty.

**Exam 15 November 2024, Ex. 1 (analysis with a hash table).** mystery1 inserts n pairs (i, mystery2(i)) into a hash table with chaining; mystery2(n) = mystery2(n/2) + n<sup>2</sup> costs Θ(log n). The calls cost Σ Θ(log i) = Θ(n log n). Average case: each insert O(1) ⇒ Θ(n), total Θ(n log n). Worst case: all keys collide in the same list; the k-th insert scans k items, Σ Θ(k) = Θ(n<sup>2</sup>), total Θ(n<sup>2</sup>).

**Exam 13 February 2026, Ex. 3 (repsort)** uses a hash table to count repetitions; see the sorting chapter.

### 9.8.1 Past exam exercises on this topic

5)  Ex. 3 2022/11/30 F; (E) Ex. 3 2023/02/06; (E) Ex. 4 2023/07/24 F; (E) Ex. 4 2024/02/12; (E) Ex. 4 2024/07/26; (A) Ex. 1 2024/11/15; (C) Ex. 2 2025/02/14.

---
> [[AADS 15 - Binary search trees|← Binary search trees]] · [[Algorithms and Data Structures|↑ Algorithms and Data Structures]] · [[AADS 17 - Algorithmic techniques|Algorithmic techniques →]]
