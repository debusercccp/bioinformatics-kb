---
course: "[[Introduction to Computing in Biology]]"
module: "[[Computational Tools and Scripting]]"
source: "bashprog/01 - Introduction to Bash.pdf"
order: 1
tags: [note, cts]
---

> [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 02 - Basic Text Processing in Bash|Basic Text Processing in Bash →]]

# Introduction to Bash

**Goal:** replace manual operations with **reproducible workflows**. Biological data (FASTA, FASTQ, GFF, VCF) are large text files that need to be filtered, reorganised and combined: commands apply the same operation consistently to many files, can be saved, repeated and shared, and run identically on a laptop or on a remote cluster.

## Unix, shells and Bash

- An **operating system** manages hardware, processes, memory, storage and user access. Unix was born at Bell Labs (late 1960s); GNU/Linux and macOS are **Unix-like**; Linux is the *kernel*. Unix-like systems are **multi-user**. Windows can run Linux through **WSL**.
- **GUI vs CLI:** the GUI is intuitive but actions are hard to reproduce; the CLI must be learned but is efficient for repetitive/remote work and leaves an explicit, reusable record.
- **Terminal** = application providing the CLI (text in/out). **Shell** = program that reads and interprets commands. **Bash** (Bourne Again SHell) is one shell; others: Zsh, Dash, Fish, sh.
  `keyboard → terminal (CLI) → shell → operating system`
- **Prompt:** `username@server:~/directory$` — `$` for a regular user, `#` for **root**.

### Anatomy of a command

```bash
mkdir -p -m 750 project/data
#     │  │  │   └─ argument (input)
#     │  │  └─ option argument
#     │  └─ option that requires an argument
#     └─ option without argument
```

General pattern: `command [options] [arguments]`, elements separated by spaces.

- **Built-in commands** are part of Bash, run by the shell itself, often change the shell state: `cd`, `history`, `alias`, `exit`.
- **External commands** are separate programs: `ls`, `mkdir`, `file`, `cp`, `rm`.
- Everything is **case-sensitive**: `sequences.fasta` ≠ `Sequences.fasta`. Avoid spaces in file names (`sample_01_R1.fastq.gz`, `experiment-2026-09-07.tsv`).

## The file system

The file system is a **tree** rooted at `/`.

| Directory | Typical contents |
|---|---|
| `/home` | users' home directories |
| `/root` | administrator's home |
| `/bin`, `/usr/bin` | common programs |
| `/etc` | system-wide configuration |
| `/var` | changing data (logs, caches) |
| `/tmp` | temporary files |
| `/dev` | device interfaces |
| `/proc` | processes and kernel info |

- **Home directory** (`/home/username`, shorthand `~`). Every shell has a **current working directory** (CWD), printed by `pwd`; a new shell starts in the home.
- **Absolute path:** starts with `/`, same meaning from anywhere (`/home/pietro/data/sample.fastq`).
- **Relative path:** does not start with `/`, interpreted from the CWD (`data/sample.fastq`, `../mario/metadata.tsv`, `./run_analysis.sh`).

| Symbol | Meaning |
|---|---|
| `.` | current directory |
| `..` | parent directory |
| `~` | home of the current user |
| `/` | root directory; path separator |
| `-` | previous directory (with `cd`) |

Read paths left to right: `../../results/alignment/sample01.bam` = up, up, into `results`, into `alignment`, file `sample01.bam`. Every component must exist.

> [!warning] Root directory ≠ root user
> `/` is the top of the tree; `root` is the administrator account (home `/root`), which can modify system files and other users' files. A mistake as root can break the system: work as a regular user.

## Working with the file system

| Command | Use |
|---|---|
| `pwd` | print CWD |
| `ls [path]` | list contents. `-l` long format, `-a` hidden files, `-h` human-readable sizes (`ls -lah`) |
| `cd [path]` | change directory. `cd` / `cd ~` → home, `cd ..` → parent, `cd -` → previous |
| `mkdir dir...` | create directories; `-p` creates missing parents (`mkdir -p project/data/fasta`) |
| `touch file...` | create empty file; if it exists, only updates the modification time |
| `less file` | view one screen at a time: Space/arrows, `/word` search, `n` next, `q` quit |
| `nano file` | edit (Ctrl+O save, Ctrl+X exit); creates the file if missing |
| `rm file` | remove file; `-r` directory + contents; `-i` ask confirmation |
| `rmdir dir` | remove **empty** directory |
| `cp src dst` | copy; `-i` asks before overwriting |
| `mv src dst` | move, or **rename** if `dst` is a new name; `-i` asks |

- Removal is **permanent**. Unix commands are usually **silent on success**.
- **Hidden files** start with `.` (e.g. `.bashrc`, which configures interactive Bash); shown by `ls -a`, together with `.` and `..`. The dot is only a naming convention.

## Glob patterns

**Globbing is done by the shell, not by the command:** the pattern is expanded into matching file names (sorted alphabetically) *before* the command runs, and the command receives them as separate arguments. Globs match **file names**, not file contents.

Example directory: `notes.txt samp1_R1.fastq samp1_R2.fastq samp2_R1.fastq samp2_R2.fastq samp10_R1.fastq sampA_R1.fastq archive/ .project.conf`

| Glob | Meaning | Example → result |
|---|---|---|
| `*` | any sequence, also empty | `*_R2.fastq` → `samp1_R2.fastq samp2_R2.fastq` |
| `?` | exactly one character | `samp?_R1.fastq` → samp1, samp2, sampA; `samp??_R1.fastq` → samp10 |
| `[abc]` | one listed char | `samp[12]_R1.fastq` → samp1, samp2 |
| `[a-z]` | one char in range | `samp[1-2]_R2.fastq` |
| `[!abc]` | one char **not** listed | `samp[!12]_R1.fastq` → sampA |
| `[[:digit:]]` etc. | named class | `samp[[:digit:]]_R1.fastq` → samp1, samp2 |

Named classes: `[:digit:]`, `[:lower:]`, `[:upper:]`, `[:alpha:]`, `[:alnum:]`, `[:space:]`.

**Brace expansion** *generates* strings, whether or not the files exist:

```bash
echo samp{1,2,A}_R1.fastq   # samp1_R1.fastq samp2_R1.fastq sampA_R1.fastq
echo samp{1..2}_R2.fastq    # samp1_R2.fastq samp2_R2.fastq
echo {A,C,G,T}{A,C,G,T}     # all 16 dinucleotides
ls samp{1..3}_R1.fastq      # error for samp3_R1.fastq: it does not exist
```

Details:
- `cp samp?_R1.fastq archive/` becomes `cp samp1_R1.fastq samp2_R1.fastq sampA_R1.fastq archive/`.
- If **nothing matches**, the pattern is passed **unchanged**.
- A leading `.` must be matched explicitly: `echo *` hides hidden files, `echo .*` shows them.
- **Quoting** disables expansion: `echo "*.fastq"` prints `*.fastq`.
- Test a glob with `echo`/`ls` before using it with `rm` (`rm -r *`!).

## Working efficiently

- **Tab completion:** completes a unique match, double Tab lists alternatives; it also confirms that the path exists.
- **History:** `history`; ↑/↓ arrows; **Ctrl+R** search; `!!` re-runs the previous command.
- **Help:**
  - `man cmd` → full manual for **external** commands (not built-ins). Navigation like `less`.
  - `cmd --help` → short summary (GNU/Linux, not macOS).
  - `help cmd` → documentation for **built-ins** only.

## File types and permissions

- Extensions (`.txt`, `.gz`, `.fasta`) are **optional conventions** on Unix: they do not guarantee the content. `file` inspects the **content** (`ASCII text`, `gzip compressed data`, `Bourne-Again shell script…`).
- Long listing:

```text
-rw-r----- 1 pietro cts 2.4G Sep 7 10:15 sample.fastq
│└┬┘└┬┘└┬┘ │ │      │   │    │            └ name
│ u  g  o  │ owner  group size  last modification
type       hard links
```

- Classes: **u** (owner), **g** (group), **o** (others). Permissions **r**, **w**, **x**.
- `-rw-r-----`: regular file; owner reads+writes; group only reads; others nothing.

| | Regular file (`-`) | Directory (`d`) |
|---|---|---|
| `r` | read contents | list entries |
| `w` | modify contents | add/remove entries |
| `x` | execute | enter/traverse |

Entering and listing a directory needs `r+x`; creating/removing entries needs `w+x`. Root bypasses permissions.

File types (first character): `-` regular, `d` directory, `l` symbolic link, `c` character device, `b` block device, `p` named pipe, `s` socket.

**Symbolic links:** `ln -s TARGET LINKNAME` — a file containing a path.

```bash
ln -s /ref/hg38.fa gen.fa
# lrwxrwxrwx 1 pietro cts 12 Sep 8 11:29 gen.fa -> /ref/hg38.fa
```

The link is 12 bytes (length of the path); its own permissions are ignored (target permissions apply; deleting the link depends on the directory); it **breaks** if the target is moved or deleted.

**chmod:** `chmod WHO OPERATION PERMISSION file`, WHO ∈ `u g o`, OPERATION ∈ `+ -`, PERMISSION ∈ `r w x`.

```bash
chmod u+x analysis.sh     # -rw-r--r-- → -rwxr--r--
chmod go-rwx private.txt  # remove everything from group and others
```

Only the owner or root can change permissions.

## The Bash environment

Environment variables: named values used by the shell and the programs it starts; `$` replaces the name with its value.

| Variable | Content |
|---|---|
| `USER` | user name |
| `HOME` | home directory |
| `SHELL` | default shell |
| `PATH` | directories searched for commands, separated by `:` |

- Bash searches `PATH` **left to right** and uses the **first** match. `.` is normally **not** in `PATH`, so a local script needs `./analysis.sh`.
- `export VARIABLE=value` sets a variable for the current session; `export PATH=$PATH:.` appends the CWD. For permanent changes, edit `~/.bashrc`.
- `which cmd` locates an **external** executable; `type cmd` says how **Bash** interprets the name (builtin, alias, file). `echo` is both a builtin and `/bin/echo`: Bash runs the builtin, so `which` doesn't necessarily show what Bash executes.
- **Aliases:** `alias ll='ls -lhF --color=auto'`; `alias` lists them, `unalias ll` removes one, `type ll` shows the replacement. Permanent → `~/.bashrc`.

## Compression and remote access

```bash
gzip reads.fastq            # → reads.fastq.gz (replaces the original; files only, not dirs)
gunzip reads.fastq.gz       # restore
tar -czf project.tar.gz project/   # c create, z gzip, f archive name
tar -tzf project.tar.gz            # t list
tar -xzf project.tar.gz            # x extract
zless reads.fastq.gz        # read without decompressing
wget "https://server.example/data/reads.fastq.gz"     # download into CWD
wget -O reads.gz "https://server.example/data/file.gz" # choose output name
ssh alice@cluster.example.org        # remote encrypted shell; `exit` to close
scp results.tsv alice@cluster.example.org:~/project/   # local → remote
scp alice@cluster.example.org:~/project/results.tsv .  # remote → local; -r for dirs
```

Remote path form: `user@machine:path`. Quote URLs (special characters).

## Command reference

| Built-in | Meaning |
|---|---|
| `cd`, `pwd` | change / print working directory |
| `echo` | print text or variable values |
| `export` | define an environment variable |
| `history`, `help`, `type` | history, built-in help, how Bash reads a name |
| `alias`, `unalias`, `exit` | aliases, terminate the shell |

External: `ls mkdir touch nano cp mv rm rmdir ln chmod less file man which gzip gunzip tar zless wget ssh scp`.

---
> [[Computational Tools and Scripting|↑ Computational Tools and Scripting]] · [[CTS 02 - Basic Text Processing in Bash|Basic Text Processing in Bash →]]
