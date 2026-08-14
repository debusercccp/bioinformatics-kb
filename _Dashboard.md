---
tags: [dashboard]
aa: 2026-2027
---

# Bioinformatics — Study Plan

> [!note] Vault conventions, front-matter schema & how-to → [[_README]]
> Guide: [[_README#How to add a course]] · [[_README#Linking notes]] · [[_README#Special cases]]

> [!info] Legend
> 🔴 **Obbligatorio** — mandatory, no choice (`required: true`)
> 
> 🟡 **A scelta / facoltativo** — you choose within a group or freely (`required: false`)

## [[First Year]]

### Semester 1
🔴 **Mandatory**
- [[Functional Genetics and Integrative Genomics]] *(6 CFU totali)*
	- Moduli: Functional Genetics (Modulo 1) + Integrative Genomics (Modulo 2)

- [[Introduction to Computing in Biology]] *(I.C.)* · 6 CFU
	- Moduli: Computational Tools and Scripting (3 CFU) + Introduction to Modeling of Biological Data (3 CFU)

- [ ] Statistical Approaches to Assess Human Molecular Variability · 6 CFU

🟡 **Gruppo Bioinformatics (9 CFU — pick 1)**
- [[Applied Machine Learning]] *(9 CFU totali)*
	- Moduli: AML-Basic (Modulo 1) + AML-Advanced (Modulo 2)

- [[Programming for Bioinformatics]] *(I.C.)* · 9 CFU
	- Moduli: Applications to Bioinformatics Problems (3 CFU) + Python Programming (6 CFU)


🟡 **Opzionale 1 (6 CFU — pick 1)**
- [ ] Bioinformatics for Biology · 6 CFU
- [[Molecular Structural Biology]] *(6 CFU totali)*
	- Moduli: Molecular Structural Biology — Modulo 1 + Modulo 2

- [ ] Quantitative Biology · 6 CFU

### Semester 2
🔴 **Mandatory**
- [ ] Advanced Cell Imaging and Spectroscopy Analysis · 6 CFU
- [ ] Algorithms and Data Structures · 6 CFU
- [ ] Computational System Biology · 6 CFU
- [ ] Laboratory of Bioinformatics and Computational Biology · 9 CFU

## [[Second Year]]

### Semester 1
🔴 **Mandatory**
- [ ] Advanced Laboratory of Bioinformatics and Computational Biology · 6 CFU

🟡 **Opzionale 2 (6 CFU — pick 1)**
- [ ] **Microbial Sensing, Signalling and Interactions** · 6 CFU

🟡 **Electives — free choice (12 CFU)**
- Electives — add one note per chosen course

### Semester 2
- [ ] 🔴 Internship · Type F · 6 CFU
- [ ] 🔴 Final Examination (Thesis) · Type E · 27 CFU

### Not scheduled in 2026/27
- Labour Market Integration Skills (3 CFU) — Italian Culture / Teamwork in Interdisciplinary Experimental Design — *n/a 2026/27*

---
*Totals: Year 1 = 60 CFU · Year 2 = 60 CFU · Degree = 120 CFU. Verified against the official UniBo study-plan page (a.y. 2026-27).*

## 📊 Views (Dataview)

### 🟡 Still to choose (a scelta)
```dataview
TABLE WITHOUT ID file.link AS Course, area AS Group, cfu AS CFU, year AS Year, period AS Sem
FROM #course and -#hub
WHERE required = false
SORT year ASC, area ASC, cfu DESC
```

### 🔴 Mandatory courses
```dataview
TABLE WITHOUT ID file.link AS Course, cfu AS CFU, year AS Year, period AS Sem
FROM #course and -#hub
WHERE required = true
SORT year ASC, period ASC
```

### CFU by group
```dataview
TABLE sum(rows.cfu) AS CFU, length(rows) AS Courses
FROM #course and -#hub
GROUP BY area
SORT key ASC
```

### CFU per year
```dataview
TABLE sum(rows.cfu) AS "Total CFU"
FROM #course and -#hub
GROUP BY year
SORT key ASC
```

### All courses
```dataview
TABLE WITHOUT ID file.link AS Course, code AS Code, choice(required, "🔴", "🟡") AS Req, area AS Group, cfu AS CFU, period AS Sem, ssd AS SSD
FROM #course and -#hub
SORT year ASC, period ASC, area ASC
```
