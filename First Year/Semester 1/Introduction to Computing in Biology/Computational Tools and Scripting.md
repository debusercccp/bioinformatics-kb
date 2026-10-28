---
code: D0523
area: Mandatory (I.C.)
year: 1
required: true
period: 1
type: B
ssd: INFO-01/A
cfu: 3
tags: [course]
---

# Computational Tools and Scripting

> D0523 · Period 1 · Type B · INFO-01/A · 3 CFU · Mandatory (I.C.)

> [!info] Modulo di [[Introduction to Computing in Biology]]

## Lectures

Docente: Pietro Di Lena.

- Breve introduzione a Linux
- Uso della shell Bash
- Strumenti da riga di comando per la manipolazione di file
- Bash scripting
- Introduzione al linguaggio di scripting AWK

## Notes

Bibliografia: review e risorse online fornite durante le lezioni e su Virtuale (nessun libro di testo fisso).

Fonte: [pagina insegnamento UniBo A.A. 2026/27](https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2026/566207)

## Appunti

Fonte: slide del corso in `bashprog/` — 4 note collegate in ordine (cartella `Bash/`).

1. [[CTS 01 - Introduction to Bash|Introduction to Bash]] — shell, file system, path, glob, permessi, ambiente, compressione e accesso remoto
2. [[CTS 02 - Basic Text Processing in Bash|Basic Text Processing in Bash]] — cat/head/tail/sort/uniq/cut/wc/diff/comm, redirezione, pipe, `;` `&&` `||`
3. [[CTS 03 - Advanced Text Processing in Bash|Advanced Text Processing in Bash]] — regex, grep, sed, awk
4. [[CTS 04 - Bash Scripting|Bash Scripting]] — argomenti, variabili, `$(...)`, exit status, `if`/`[ ]`, `for`

## Exam

**Scritto (pratico).** Risoluzione di due problemi di scripting Bash in 60 minuti. Uso di IA vietato in sede d'esame.

Esami di prova (16/10/2026, versioni A/B/C, con soluzioni): `bashprog/2026_10_16A.pdf`, `…B.pdf`, `…C.pdf`. Struttura: 4 esercizi su un file TSV — path/glob/permessi (7 pt), output esatto di pipeline `cut`/`sort`/`uniq`/`head`/`tail` (7 pt), output di `grep -E`/`sed`/`awk` (9 pt), lettura di uno script con argomenti, `if` e `awk` (9 pt). Allenatore interattivo: `python3 bashprog/esercizi.py`.
