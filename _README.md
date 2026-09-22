---
tags: [meta]
---

# ℹ️ How this vault works

Study vault for the **Bioinformatics** master's degree (UniBo). It mirrors the official study plan and holds one note per course, with lecture/exam notes inside.

- **Dashboard / study plan:** [[_Dashboard]] — checklist of every course + Dataview views (CFU totals, still-to-choose, etc.).
- **New course note:** start from `Templates/Corso.md`.

## Folder structure
```
Bioinformatics/
├── _Dashboard.md     → study plan + Dataview views
├── _README.md        → this file: conventions
├── Templates/        → note templates
└── <Year>/<Semester>/<Course>/<Course>.md
```
Naming: one folder per course, the note is named **exactly like the course**; grouping notes (`<Year>.md`, `<Year> - <Semester>.md`) share the folder's name.

## Note types (tags)
| Tag            | What it is                          | Front-matter      |
|----------------|-------------------------------------|-------------------|
| `#course`      | A single course                     | schema below ⇩    |
| `#semester`    | Semester grouping node              | `aliases`, `tags` |
| `#first-year` / `#second-year` | Year grouping node  | `tags`            |
| `#dashboard`   | The study-plan dashboard            | —                 |
| `#meta`        | Notes about the vault (this README) | free              |

> [!important] The [[_Dashboard]] Dataview views list **only** `#course` notes (`FROM #course`). Grouping nodes never pollute the tables because they don't carry that tag.

## Front-matter schema of a `#course`
| Field      | Allowed values                          | Meaning                                   |
|------------|-----------------------------------------|-------------------------------------------|
| `tags`     | `[course]`                              | note type — required for the dashboard    |
| `code`     | integer (e.g. `29526`)                  | official UniBo course code                |
| `area`     | grouping label (must match a Dashboard group, e.g. `Mandatory`, `Bioinformatics`, `Opzionale 1`, `Electives`) | which study-plan group the course belongs to |
| `year`     | `1` · `2`                               | academic year                             |
| `period`   | `1` · `2`                               | semester within the year                  |
| `required` | `true` · `false`                        | 🔴 mandatory vs 🟡 to-be-chosen           |
| `type`     | `B` · `E` · `F` (UniBo activity type)   | B = course · E = final exam · F = internship |
| `ssd`      | code (e.g. `INFO-01/A`)                 | scientific-disciplinary sector            |
| `cfu`      | integer                                 | credits                                   |

## How to add a course
1. **Create the folder + note** as `<Year>/<Semester>/<Course>/<Course>.md`. The note is named **exactly** like the course.
2. **Insert the template:** `Ctrl+P` → *Templates: Insert template* → **Corso** (or copy an existing course note).
3. **Fill the front-matter** per the schema above. Official `code` / `ssd` / `cfu` / `type` values come from the [UniBo study plan](https://corsi.unibo.it/2cycle/MolecularComputationalBiology/course-structure-diagram/piano/2026/6254/D33/000/2026).
4. **Update the summary line** (the `>` blockquote under the title), e.g. `> C8703 · Period 1 · Type B · BIOS-08/A · 6 CFU · Opzionale 1`.
5. Done — thanks to `tags: [course]` it shows up **automatically** in every [[_Dashboard]] Dataview view. Tick its checkbox in the study plan when completed.

## Linking notes
Two kinds of links do two different jobs:

- **Automatic — via tags.** The [[_Dashboard]] views use `FROM #course`, so any note with `tags: [course]` is collected on its own. You never link a course to the dashboard by hand. ⚠️ Grouping nodes (`<Year>.md`, `<Year> - <Semester>.md`) must **not** carry `#course` (they use `#semester` / `#first-year` / `#second-year`) or they pollute the tables.
- **Manual — via wikilinks.** For navigating between related notes. Type `[[` for autocomplete:

| Syntax                            | Result                       |
|-----------------------------------|------------------------------|
| `[[Quantitative Biology]]`        | link to the note             |
| `[[Quantitative Biology\|QB]]`    | link with a display alias    |
| `[[Quantitative Biology#Exam]]`   | link to a heading            |
| `[[Quantitative Biology#^blockid]]` | link to a specific block   |

  Use them to connect related/prerequisite courses and to link grouping nodes to their courses. The **Backlinks** pane shows every note pointing here, so links are bidirectional for free.

## Special cases
- **Integrated courses (I.C.)** — e.g. *Introduction to Computing in Biology*, *Programming for Bioinformatics*: each **module** is its own `#course` note (with its own `code`/`cfu`); set `area: … (I.C.)`.
- **Electives / group choices** — create a `#course` note only for the course you actually chose, with `required: false` (it lands in the "🟡 Still to choose" view).
- **Thesis & Internship** — special activities: `type: E` (thesis) / `type: F` (internship), **no `ssd`**, and composite/multiple codes, so leave `code` empty. That's correct.
