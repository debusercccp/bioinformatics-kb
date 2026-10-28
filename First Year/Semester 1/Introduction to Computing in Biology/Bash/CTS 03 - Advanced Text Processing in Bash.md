---
course: "[[Introduction to Computing in Biology]]"
module: "[[Computational Tools and Scripting]]"
source: "bashprog/03_Advanced_Text_Processing_in_Bash.pdf"
order: 3
tags: [note, cts]
---

> [[CTS 02 - Basic Text Processing in Bash|← Basic Text Processing in Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 04 - Bash Scripting|Bash Scripting →]]

# Advanced Text Processing in Bash

- **Regular expressions** describe the text of interest
- **grep** selects complete lines
- **sed** edits or removes matching text
- **awk** processes fields and performs calculations

Example file: `cat kmers1.tsv kmers2.tsv > kmers.tsv`

```text
1   AAAAAA
15  AACAAG
4   CGGAAA
4   CGGAAA
9   ATGATG
12  GTATAG
3   TTTAAA
```

## Regular expressions

A regex describes a set of strings and matches **text within a line** (part or all of it), not file names.

| Basic | Meaning |
|---|---|
| `.` | any single character |
| `[abc]` / `[^abc]` | one listed / one **not** listed character |
| `^` / `$` | beginning / end of line (positions, not characters) |
| `*` | zero or more copies of the preceding item |

| Extended (`grep -E`) | Meaning |
|---|---|
| `?` | zero or one |
| `+` | one or more |
| `{n}` / `{n,m}` | exactly n / between n and m copies |
| `(A\|B)` | A or B |

A backslash removes the special meaning: `\?` matches `?`, `a\.c` matches `a.c`.

| Regex | Matches lines containing… |
|---|---|
| `a.c` | aac, abc, acc… |
| `a*c` | c, ac, aac… |
| `^abc` / `abc$` / `^abc$` | starting with / ending with / exactly abc |
| `^$` | empty line |
| `[^abc]bc` | dbc, ebc… (not abc/bbc/cbc) |

Examples:

```text
signed integer       ^[+-]?[[:digit:]]+$
decimal number       ^[+-]?[[:digit:]]*\.?[[:digit:]]+$
date 1900–2099       ^(19|20)[[:digit:]]{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][[:digit:]]|3[01])$
integer 0–255        ^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
```

> [!warning] `^[0-255]$` is **not** 0–255: a bracket is one character, so it matches only 0, 1, 2 or 5. The date regex checks the format, not whether the date exists.

### Regex vs glob

| Goal | Glob | Regex |
|---|---|---|
| any sequence | `*` | `.*` |
| one character | `?` | `^.$` |
| one listed char | `[ABC]` | `^[ABC]$` |
| one unlisted char | `[!ABC]` | `^[^ABC]$` |

Bash expands **globs** into file names; programs like grep interpret **regexes**. Always **quote** regexes so Bash doesn't treat them as globs.

## grep

`grep [options] pattern [files]` prints the **lines** matching the pattern, without modifying the input; reads stdin if there's no file. `grep -E` extended regex, `grep -F` fixed strings, `zgrep` on gzip files.

```bash
grep GAT kmers.tsv          # 9   ATGATG
grep 'A.C' kmers.tsv        # 15  AACAAG
grep '[CT]AA' kmers.tsv     # 15 AACAAG ; 3 TTTAAA
grep '^4' kmers.tsv         # the two CGGAAA lines
grep 'C.*A$' kmers.tsv      # contains C and ends with A → the two CGGAAA
grep 'C.*[^A]$' kmers.tsv   # 15 AACAAG  (= grep C kmers.tsv | grep '[^A]$')
```

| Option | Purpose |
|---|---|
| `-i` | ignore case |
| `-v` | select **non**-matching lines |
| `-w` | whole words |
| `-c` | count matching lines (`grep -c GAT kmers.tsv` → 1) |
| `-n` | print line numbers |
| `-m n` | stop after n matches |
| `-E` | extended regex |
| `-e P` | add a pattern (repeatable): `grep -e TAG -e TTT` |
| `-f file` | patterns from a file, one per line (match ≥ 1) |
| `-q` | quiet: no output, only the exit status (used in `if`) |

Logs example — find problems in every log file:

```bash
grep -niE 'err|warn|fail' logs/2024-03/*.log > problems.txt
```

With several files grep prefixes each line with the file name.

## sed — stream editor

`sed [options] 'commands' [file]` transforms text **one line at a time** and writes to stdout; the input file is unchanged (unless `-i`). **Addresses** select the lines: a number, a range `2,4`, `/regex/`, `$` (last line).

### Printing

- By default sed **prints every line** after processing.
- `p` prints explicitly → without `-n` the line appears **twice**.
- `-n` disables automatic printing → selective printing is `sed -n '…p'`.

```bash
sed -n '3p' kmers.tsv       # line 3
sed -n '2,4p' kmers.tsv     # lines 2–4
sed -n '/GAT/p' kmers.tsv   # lines matching GAT
sed -n '$p' kmers.tsv       # last line
```

### Deleting

```bash
sed '3d' kmers.tsv      # all but line 3
sed '2,4d' kmers.tsv    # remove lines 2–4
sed '/CGG/d' kmers.tsv  # remove lines containing CGG
sed '$d' kmers.tsv      # remove last line
```

### Substitution

`s/regexp/replacement/flags`

```bash
echo AAAAAA | sed 's/AAA/ACG/'     # ACGAAA  (first match only)
echo AAAAAA | sed 's/AAA/ACG/g'    # ACGACG  (g = every non-overlapping match)
sed -n '/CGG/s/AAA/TTT/p' kmers.tsv  # only lines with CGG; p prints changed lines → 4 CGGTTT ×2
```

- **In-place:** `sed -i 's/AAA/ACG/g' file` (GNU/Linux) or `sed -i '' …` (macOS). Silent; test without `-i` first.
- **Multiple commands:** `sed -e '1d' -e 's/GAT/XXX/g' kmers.tsv` — applied in order.

### Complementing a sequence

Chained substitutions **fail** because each one acts on the result of the previous one:

```text
echo ACTG | sed -e 's/A/T/g' -e 's/T/A/g' -e 's/C/G/g' -e 's/G/C/g'
ACTG → TCTG → ACAG → AGAG → ACAC     (wanted TGAC)
```

Solutions:
1. **Placeholder** absent from the sequence: `s/A/X/g; s/T/A/g; s/X/T/g`, then the same for C/G.
2. **Transliteration** `y`: `echo ACTG | sed 'y/ACGT/TGCA/'` → `TGAC` (sets of equal length, single operation).

Both give the **complement**, not the reverse complement.

## awk

A language for structured text (named after **A**ho, **W**einberger, **K**ernighan). It reads one **record** at a time (default: one line), splits it into **fields** (default: whitespace), and applies **pattern { action }** rules.

`awk 'pattern { action }' [file]`

- missing pattern → every record; missing action → `print` the whole record.
- `$0` whole record, `$1`, `$2`… fields. `print` adds a newline; `print a, b` separates with **OFS** (default a space).

```bash
awk '/GAT/ { print }' kmers.tsv
awk '{ print $2 }' kmers.tsv
awk 'BEGIN {print "Begin"} { print $2 } END {print "End"}' kmers.tsv
```

**BEGIN** runs once before the input (settings, headers), **END** once after the last record (summaries).

### Separators and built-in variables

```bash
awk -F '\t' '{ print $2,$1 }' kmers.tsv                          # AAAAAA 1 …
awk 'BEGIN { FS="\t"; OFS=" --> " } { print $2, $1 }' kmers.tsv  # AAAAAA --> 1 …
```

| Variable | Meaning |
|---|---|
| `NR` | records read so far (across all files) |
| `FNR` | record number in the current file |
| `NF` | number of fields in the current record |
| `FILENAME` | current input file |
| `FS` / `OFS` | input / output field separator |

`awk '{ print NR, NF, $0 }' kmers.tsv` → `1 2 1   AAAAAA` …

### Variables, conditions, operators

```bash
awk '{total += $1} END {print total}' kmers.tsv    # 48 — uninitialised vars = 0
awk '$1 >= 10 { print $2 }' kmers.tsv               # AACAAG, GTATAG
awk '{if ($1 >= 10) {print $2, "high"} else {print $2, "low"}}' kmers.tsv
awk -v limit=10 '$1 >= limit { print $2 }' kmers.tsv  # -v passes a shell value
grep 'A$' kmers.tsv | awk '{total+=$1} END{print total}'   # 12
```

| Category | Operators |
|---|---|
| arithmetic | `+ - * / % ^` |
| assignment | `= += -= *= /= %=` |
| increment | `++ --` |
| comparison | `== != < <= > >=` |
| logical | `&& \|\| !` |
| regex match | `~ !~` |
| conditional | `cond ? a : b` |
| array membership | `key in array` |
| concatenation | `a b` |

`=` assigns, `==` compares. A pattern–action rule has no `else`: use `if/else` to choose between two actions. `-f script.awk` reads a longer program from a file.

### Associative arrays

An array indexed by **keys** (strings): `seq_count["CGGAAA"]`. A new element starts at 0.

```bash
awk '{seq_count[$2]++} END {print "CGGAAA:", seq_count["CGGAAA"]}' kmers.tsv   # CGGAAA: 2
```

**Duplicated names** (gene name in column 2):

```bash
cut -f 2 genes.tsv | sort | uniq -d                        # sort-based
awk -F '\t' '{if (++count[$2] == 2) print $2}' genes.tsv   # single pass
```

`++count[$2] == 2` prints each duplicated name **exactly once**, at its second occurrence. AWK **trades memory for speed**: no sort on huge files (compare with `time`).

## Quick reference

| Tool | Purpose | Example |
|---|---|---|
| `grep` | select matching lines | `grep GAT file` |
| `grep -E` | extended regex | `grep -E 'A\|G' file` |
| `sed` | select or transform lines | `sed 's/A/T/g' file` |
| `awk` | process records and fields | `awk '{print $2}' file` |

Build complex transformations **incrementally**: start from a small file, check each selection before transforming, combine tools only once each works on its own.

---
> [[CTS 02 - Basic Text Processing in Bash|← Basic Text Processing in Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 04 - Bash Scripting|Bash Scripting →]]
