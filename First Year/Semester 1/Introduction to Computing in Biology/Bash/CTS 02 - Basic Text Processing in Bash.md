---
course: "[[Introduction to Computing in Biology]]"
module: "[[Computational Tools and Scripting]]"
source: "bashprog/02_Basic_Text_Processing_in_Bash.pdf"
order: 2
tags: [note, cts]
---

> [[CTS 01 - Introduction to Bash|← Introduction to Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 03 - Advanced Text Processing in Bash|Advanced Text Processing in Bash →]]

# Basic Text Processing in Bash

Small commands that each do one thing, **redirection** to control where data is read and written, and **pipelines** to chain them: together they become reproducible workflows.

**Example files** (`text_demo/`):

```text
kmers1.tsv        kmers2.tsv     samples1.txt   samples2.txt   samples.csv
1   AAAAAA        12  GTATAG     control        control        sample1,control,12
15  AACAAG        3   TTTAAA     sampleA        sampleB        sample2,treated,18
4   CGGAAA                       treated        treated
4   CGGAAA
9   ATGATG
```

The k-mer files are **tab-separated** (count, sequence).

## Basic text tools

| Command | What it does | Example |
|---|---|---|
| `cat f1 f2` | concatenate and print, in the given order | `cat kmers1.tsv kmers2.tsv` |
| `head -n N` | first N lines (default **10**) | `head -n 3 kmers1.tsv` |
| `tail -n N` | last N lines | `tail -n 3 kmers1.tsv` |
| `tail -n +N` | from line N to the end | `tail -n +3 kmers1.tsv` → lines 3–5 |
| `sort` | sort lines (lexicographic by default) | — |
| `uniq` | collapse **consecutive** identical lines | `uniq -d` only duplicated ones |
| `cut -f` | select tab-separated fields | `cut -f 2`, `cut -f 1,3` |
| `cut -d ',' -f` | fields with another one-character delimiter | `cut -d ',' -f 1,3 samples.csv` |
| `cut -c` | character positions | `cut -c 1-6`, `cut -c 1,4,6` |
| `wc` | count `-l` lines, `-w` words, `-c` bytes | `wc -l kmers1.tsv` → `5 kmers1.tsv` |
| `diff` | compare line by line | `diff -u a b`, `diff -q a b` |
| `comm` | compare two **sorted** files in 3 columns | `comm -1 -2 a b` |

### sort

- Default **lexicographic**: compares characters, so `15` comes before `4` (`1 / 15 / 4 / 4 / 9`).
- `-k 1` sort key = field 1; `-n` numeric → `1 / 4 / 4 / 9 / 15`.
- `-r` reverse, `-u` unique (removes duplicates after sorting).
- The input file is **not modified**.

### uniq

Only **adjacent** duplicates are detected → usually `sort | uniq`. `uniq -d` prints one copy of each duplicated line (`4 CGGAAA`).

### wc

`wc -l kmers1.tsv` = 5, `-w` = 10, `-c` = 46 (tabs and newlines count as one byte each). `-l` actually counts **newline characters**: a missing final newline changes the counts. With a file argument the name is printed too; with `wc -l < file` only the number.

### diff and comm

```text
$ diff -u samples1.txt samples2.txt
--- samples1.txt
+++ samples2.txt
@@ -1,3 +1,3 @@
 control
-sampleA        ← only in the first file
+sampleB        ← only in the second file
 treated
```

No output = identical; `-q` only reports whether they differ.

`comm` columns: **1** only in file 1, **2** only in file 2, **3** in both (indentation shows the column). `-1 -2 -3` suppress columns, so `comm -1 -2 a b` = shared lines (`control`, `treated`).

## Streams and redirection

| FD | Stream | Default |
|---|---|---|
| 0 | stdin | keyboard |
| 1 | stdout | terminal |
| 2 | stderr (errors, diagnostics) | terminal |

| Syntax | Effect |
|---|---|
| `cmd > file` | stdout to file — creates it, or **empties** it first (overwrite!) |
| `cmd >> file` | **append** stdout |
| `cmd 2> file` | only stderr to file (`>` = `1>`) |
| `cmd 2>> file` | append stderr |
| `cmd > out 2> err` | separate files |
| `cmd > file 2>&1` | both into the same file (also `&> file`) |
| `cmd < file` | stdin from file |
| `cmd 2> /dev/null` | discard errors |

- `2>&1` sends stderr **to wherever stdout points now**: redirections are processed **left to right**.
- `cat < file` (the shell feeds stdin) vs `cat file` (cat opens the file): same output. Not every command reads stdin (`ls` ignores it).
- Discard errors only when you understand why they occur.

```bash
ls kmers*.tsv missing.txt 2> errors.txt   # stdout on screen, error in the file
ls kmers*.tsv missing.txt 2> /dev/null    # only kmers1.tsv kmers2.tsv
```

## Pipelines and command lists

**Pipe** `|`: stdout of one command → stdin of the next, no intermediate file. **stderr does not go through the pipe.** The last command can still be redirected.

```bash
cat kmers*.tsv | wc -l     # 7
```

| Operator | Next command runs… | Example |
|---|---|---|
| `;` | always | `pwd ; ls` |
| `&&` | only if the previous **succeeded** | `mkdir results && cd results` |
| `\|\|` | only if the previous **failed** | `cd missing \|\| echo "directory not found"` |

### Worked examples

```bash
# sorted list of distinct sequences
cut -f 2 kmers1.tsv | sort -u > sequences.txt

# BED (chrom, start, end; tab-separated): merge several files, keep each region once
cat peaks/*.bed | cut -f 1,2,3 | sort -u > unique_regions.bed
# chromosomes represented
cut -f 1 unique_regions.bed | sort -u > chromosomes.txt
```

Complex tasks = sequences of simple transformations.

## Collegamenti
- [[SATAUMV 09 - Technologies for genomic data generation and data formats]] — FASTQ/SAM/VCF/BED, i formati che si manipolano con questi strumenti

---
> [[CTS 01 - Introduction to Bash|← Introduction to Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 03 - Advanced Text Processing in Bash|Advanced Text Processing in Bash →]]
