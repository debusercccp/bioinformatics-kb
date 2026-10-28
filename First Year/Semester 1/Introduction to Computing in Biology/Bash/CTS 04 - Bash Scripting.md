---
course: "[[Introduction to Computing in Biology]]"
module: "[[Computational Tools and Scripting]]"
source: "bashprog/04_Bash_Scripting.pdf"
order: 4
tags: [note, cts]
---

> [[CTS 03 - Advanced Text Processing in Bash|← Advanced Text Processing in Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]]

# Bash Scripting

A **Bash script** is a text file of Bash commands, run in order. Variables and arguments make it reusable, conditions let it choose, loops repeat. A script = a reusable command-line procedure.

## Creating and executing a script

```bash
#!/bin/bash

# Search for a pattern in a file
grep "$1" "$2"
```

- `#!/bin/bash` (**shebang**) selects Bash as the interpreter; `#` lines are comments; `.sh` is only a convention.
- Run it:
  - `bash search.sh GAT kmers.tsv`, or
  - `chmod u+x search.sh` then `./search.sh GAT kmers.tsv` (uses the shebang interpreter; `./` because `.` is not in `PATH`).

## Arguments and variables

`./search.sh GAT kmers.tsv`

| Variable | Meaning | Value |
|---|---|---|
| `$0` | script name (as invoked) | `./search.sh` |
| `$1`, `$2`… | positional arguments | `GAT`, `kmers.tsv` |
| `$#` | number of arguments | `2` |
| `$@` | all arguments | `GAT kmers.tsv` |
| `$?` | exit status of the last command | `0` = success |

```bash
pattern=$1          # name=value, NO spaces around =
input=$2
grep "$pattern" "$input"
```

**Quote** variable expansions (`"$input"`) unless you want word splitting: it protects names with spaces and empty values.

**Command substitution** — `$(...)` runs a command and uses its stdout (trailing newlines removed):

```bash
records=$(wc -l < kmers.tsv)       # < → only the number, no file name
echo "The file contains $records records"   # The file contains 7 records
```

## Exit status and if

Every command returns an **exit status**: `0` = success, non-zero = failure. Bash conditions use the **exit status**, not the printed output.

```bash
ls kmers.tsv > /dev/null;  echo $?   # 0
ls missing.tsv > /dev/null; echo $?  # 1 (error message still on stderr)
```

```bash
if grep -q GAT kmers.tsv     # -q: no output, only the status
then
    echo "Pattern found"
else
    echo "Pattern not found"
fi
```

### Tests with `[`

`[` is a command: **spaces** around `[`, the expression and `]` are mandatory.

| Test | True if |
|---|---|
| `[ "$a" = "$b" ]` | strings equal |
| `[ "$a" -ne "$b" ]` | numbers different (also `-eq -lt -le -gt -ge`) |
| `[ -e "$f" ]` | path exists |
| `[ -f "$f" ]` | regular file |
| `[ -r "$f" ]` | readable |
| `[ -d "$p" ]` | directory |
| `[ ! … ]` | negation |

Strings use `=`/`!=`, numbers use `-eq`, `-ne`, `-gt`…

### Validating input

```bash
if [ $# -ne 2 ]
then
    echo "Usage: $0 PATTERN FILE"
    exit 1
fi

if [ ! -e "$2" ]
then
    echo "Error: $2 does not exist or it is not readable"
    exit 1
fi

grep "$1" "$2"
```

`exit 1` stops the script with a non-zero status; the **usage** message shows how to call it.

## for loops

```bash
for file in *.log
do
    echo "Checking $file"
    grep -iE 'error|warning|failed' "$file"
done
```

The glob is expanded **before** the loop starts; `file` takes one name at a time; the body between `do` and `done` runs for each.

## Complete example — filter_kmers.sh

Takes a k-mer table and a minimum count, checks its inputs, saves the records ≥ threshold and reports how many were saved.

```bash
#!/bin/bash

# Check the number of arguments
if [ $# -ne 2 ]
then
    echo "Usage: $0 FILE MIN_COUNT"
    exit 1
fi

file=$1
count=$2
output=filtered_kmers.tsv

# Check the input file
if [ ! -r "$file" ]
then
    echo "Error: cannot read $file"
    exit 1
fi

# Select records and save them
awk -v n=$count '$1 >= n {print $0}' "$file" > $output

# Count and report the selected records
echo Saved $(cat $output | wc -l) records in $output
```

```text
$ chmod +x filter_kmers.sh
$ ./filter_kmers.sh kmers.tsv 10
Saved 2 records in filtered_kmers.tsv
$ cat filtered_kmers.tsv
15  AACAAG
12  GTATAG
```

> [!tip] Exam pattern
> The sample exams (`bashprog/2026_10_16A/B/C.pdf`) ask you to read a script like this one and give the values of `$0 $1 $2 $#` and of the variables, what it prints on the terminal and what it writes to the output file. Remember: `awk '{print $1, $2}'` writes **space**-separated columns (default OFS), even when the input is tab-separated.

---
> [[CTS 03 - Advanced Text Processing in Bash|← Advanced Text Processing in Bash]] · [[Computational Tools and Scripting|↑ Computational Tools and Scripting]]
