#!/usr/bin/env python3
"""Split the pandoc-converted MCB docx notes into atomic, linked Obsidian notes.

Run through update.sh, which converts the docx first. `build.py --list` prints KEY<TAB>source.
"""
import os, re, shutil, subprocess, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SCR = Path(os.environ.get('IMPORT_WORK', Path.home() / '.cache' / 'bioinformatics-import'))
CONV = SCR / 'conv'
# `src` paths below are relative to the folder that contains MCB/ (ROOT).
# Order: MCB_ROOT env var > OS-specific path > folder next to the vault.
WIN_ROOT = Path(r'C:\Users\Rocco\Documents\Universita')   # C:\Users\Rocco\Documents\Universita\MCB
LINUX_ROOTS = [VAULT.parent, Path.home() / 'Documents' / 'Universita']


def find_root():
    if os.environ.get('MCB_ROOT'):
        return Path(os.environ['MCB_ROOT'])
    if os.name == 'nt' or sys.platform in ('win32', 'cygwin', 'msys'):
        return WIN_ROOT
    for r in LINUX_ROOTS:
        if (r / 'MCB').is_dir():
            return r
    sys.exit(f'MCB/ not found in {", ".join(map(str, LINUX_ROOTS))}: set MCB_ROOT')


ROOT = find_root()


def write(path, text):
    """UTF-8 with LF line endings on every OS (no CRLF diffs from Windows)."""
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def tool(*names):
    """First executable found in PATH or in the usual Windows install folders."""
    for n in names:
        if shutil.which(n):
            return shutil.which(n)
    pf = [Path(os.environ.get(v, '')) for v in ('ProgramFiles', 'ProgramFiles(x86)', 'LOCALAPPDATA') if os.environ.get(v)]
    for base in pf:
        for n in names:
            for hit in sorted(base.glob(f'*/{n}.exe')) + sorted(base.glob(f'*/program/{n}.exe')) + sorted(base.glob(f'Programs/*/{n}.exe')):
                return str(hit)
    sys.exit(f'Not found: {" / ".join(names)} (install it or add it to PATH)')
S1 = VAULT / 'First Year' / 'Semester 1'
ATT = VAULT / '_attachments'

FGIG = 'Functional Genetics and Integrative Genomics'
SOURCES = {
    'SATAUMV': dict(
        course='Statistical Approaches to Assess Human Molecular Variability',
        module_note='Statistical Approaches to Assess Human Molecular Variability',
        dir=S1 / 'Statistical Approaches to Assess Human Molecular Variability',
        src='MCB/SATAUMV/Statistical_approaches.docx', label='Statistical Approaches'),
    'FG': dict(
        course=FGIG, module_note='Functional Genetics', dir=S1 / FGIG,
        src='MCB/FGIG/FG/FunctionalGen_common.docx', label='Functional Genetics', sub='Functional Genetics'),
    'IG': dict(
        course=FGIG, module_note='Integrative Genomics', dir=S1 / FGIG,
        src='MCB/FGIG/IG/IntegrativeGen_RS.docx', label='Integrative Genomics', sub='Integrative Genomics'),
    'AML': dict(
        course='Applied Machine Learning', module_note='Applied Machine Learning (AML-Basic)',
        dir=S1 / 'Applied Machine Learning', src='MCB/AML/MLFULL.docx',
        label='AML-Basic', sub='AML-Basic'),
    'MBD': dict(
        course='Introduction to Computing in Biology',
        module_note='Introduction to Modeling of Biological Data',
        dir=S1 / 'Introduction to Computing in Biology', src='MCB/MBD/ModelingBioData.docx',
        label='Modeling of Biological Data'),
    'BFB': dict(
        course='Bioinformatics for Biology', module_note='Bioinformatics for Biology',
        dir=S1 / 'Bioinformatics for Biology', src='MCB/BFB/Bioinformatics_For_Biology.docx',
        label='Bioinformatics for Biology'),
}

# hand fixes re-applied after every rebuild: (note name prefix, old text, new text)
FIXES = [
    ('FG 12 -', '![[FG-image32.png|303]]**How the flanking gene', '![[FG-image32.png|303]]\n\n**How the flanking gene'),
]

BIG = 300      # lines: a chapter longer than this is split at its H2s
MIN = 40       # lines: smaller H2 chunks are merged forward


ACR = re.compile(r'\b(nns?|mlp|svm|dt|lle|pca|rnns?|cnns?|gans?|nlp|vaes?|ae|ann|mlops|gd|ml|ai|roc|auc|dna|rna)\b', re.I)
ACR_FIX = {'nn': 'NN', 'nns': 'NNs', 'rnns': 'RNNs', 'cnns': 'CNNs', 'gans': 'GANs', 'vaes': 'VAEs', 'mlops': 'MLOps'}


def titlecase(s):
    letters = [c for c in s if c.isalpha()]
    if letters and sum(c.isupper() for c in letters) / len(letters) >= 0.7:
        small = {'vs', 'of', 'and', 'to', 'the', 'in', 'for', 'a', 'on', 'using'}
        s = ' '.join(w if (i and w in small) else w.capitalize() for i, w in enumerate(s.lower().split()))
    s = ACR.sub(lambda m: ACR_FIX.get(m.group(1).lower(), m.group(1).upper()), s)
    return s.replace('Tensorflow', 'TensorFlow').replace('Keras Interface for a Shallow NN', 'Keras Interface for a Shallow NN')


def clean_title(raw):
    t = re.sub(r'\$`.*?`\$', lambda m: re.sub(r'\\\w+|[{}\\]', '', m.group(0)).strip('$`') , raw)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('*', '').replace('\\', '').strip()
    t = re.sub(r'^\d+(\.\d+)*\.?\s+', '', t)          # leading numbering
    t = titlecase(t)
    t = t.replace(' — ', ' – ')
    t = re.sub(r'[:]', ' –', t)
    t = re.sub(r'[/\\?*"<>|#^\[\]]', '', t)
    t = re.sub(r'\s+', ' ', t).strip(' .')
    return t[:110].rstrip()


def parse_sections(text, key):
    """Return list of (level, title_raw, body_lines) with level in {1,2,>=3 kept in body}."""
    lines = text.split('\n')
    out, cur = [], None
    in_code = False
    late = False       # AML: after 13.5 the course topics are H3/H4 headings
    for ln in lines:
        if ln.startswith('```'):
            in_code = not in_code
        m = None if in_code else re.match(r'^(#{1,6}) (.*)$', ln)
        if m:
            lvl, title = len(m.group(1)), m.group(2).strip()
            if key == 'AML':   # inconsistent heading levels: derive from numbering
                if re.match(r'^\d+\. ', title):
                    lvl = 1
                elif re.match(r'^\d+\.\d+ ', title):
                    lvl = 2
            np = False
            if key == 'AML' and re.match(r'^13\.5 ', title):
                late = True
            elif key == 'AML' and late and lvl in (3, 4):   # H4 or H3 depending on pandoc version
                lvl, np = 2, True
            if lvl <= 2:
                cur = [lvl, title, [], np]
                out.append(cur)
                continue
        if cur is None:
            cur = [0, '', [], False]
            out.append(cur)
        cur[2].append(ln)
    return out


def short_prefix(h1):
    full = clean_title(h1)
    t = re.split(r'[:(]| – ', full)[0].strip()
    if len(t) <= 45:
        return t if re.match(r'^(Module|Appendix)', full) is None else (full if len(full) <= 45 else re.match(r'^(Module \d+|Appendix [A-Z])', full).group(1))
    m = re.match(r'^(Module \d+|Appendix [A-Z])', full)
    return m.group(1) if m else ''


def group_chunks(secs):
    """Split into chapters at H1; chapters > BIG lines get split at H2 (small H2s merged).
    Returns a list of (sections, prefix)."""
    chapters = []
    for s in secs:
        if s[0] <= 1 or not chapters:
            chapters.append([s])
        else:
            chapters[-1].append(s)
    chunks = []
    for ch in chapters:
        total = sum(len(s[2]) + 1 for s in ch)
        if total <= BIG or len(ch) == 1:
            chunks.append((ch, ''))
            continue
        head, rest = ch[0], ch[1:]
        pre = short_prefix(head[1])
        local = []                       # [sections, has_head]
        cur = [head] if len(head[2]) > 3 else []   # intro text under the H1 joins the first chunk
        size = sum(len(s[2]) for s in cur)
        for s in rest:
            if not s[1]:                 # empty heading: fold into the running chunk
                cur.append(s); size += len(s[2]); continue
            if cur and size >= MIN and cur[0] is not head:
                local.append(cur); cur, size = [], 0
            elif cur and size >= MIN and cur[0] is head and size >= MIN:
                local.append(cur); cur, size = [], 0
            cur.append(s); size += len(s[2]) + 1
        if cur:
            if local and size < MIN:
                local[-1].extend(cur)
            else:
                local.append(cur)
        for c in local:
            chunks.append((c, '' if (c[0] is head or c[0][3]) else pre))
    return chunks


def postprocess(body, key, media_map):
    # math: $`x`$ -> $x$ ; fenced math -> $$ blocks
    body = re.sub(r'\$`(.+?)`\$', lambda m: '$' + m.group(1).strip() + '$', body, flags=re.S)
    body = re.sub(r'^([ \t]*)``` ?math\n(.*?)\n\1```[ \t]*$',
                  lambda m: f'{m.group(1)}$$\n{m.group(2)}\n{m.group(1)}$$', body, flags=re.S | re.M)

    def fix_math(m):
        x = re.sub(r'(?<![\\\w])dimker', r'\\dim\\ker', m.group(0))
        return re.sub(r'(?<![\\\w])(rank|argmin|argmax)(?=[\s(_{])', r'\\operatorname{\1}', x)
    body = re.sub(r'\$\$.*?\$\$|\$[^$\n]+\$', fix_math, body, flags=re.S)

    # images
    def img(m):
        tag = m.group(0)
        if 'src="_attachments/' in tag:
            return tag
        src = re.search(r'src="([^"]+)"', tag).group(1)
        name = Path(src).name
        name = media_map.get(name, name)
        w = re.search(r'width:([\d.]+)in', tag)
        px = min(int(float(w.group(1)) * 96), 700) if w else None
        return f'![[{key}-{name}|{px}]]' if px else f'![[{key}-{name}]]'

    def tag_in_table(m):
        return re.sub(r'<img [^>]*src="([^"]+)"[^>]*/?>',
                      lambda i: f'<img src="_attachments/{key}-{media_map.get(Path(i.group(1)).name, Path(i.group(1)).name)}" width="300">',
                      m.group(0))
    body = re.sub(r'<table.*?</table>', tag_in_table, body, flags=re.S)
    body = re.sub(r'<img [^>]*/?>', img, body)
    # nbsp / stray empty headings
    body = body.replace('\u00a0', ' ')
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip() + '\n'


def convert_media(key):
    mdir = CONV / key / 'media' / 'media'
    media_map = {}
    if not mdir.exists():
        return media_map
    for old in ATT.glob(f'{key}-*'):     # drop images from the previous import
        old.unlink()
    dest = ATT / key
    dest.mkdir(parents=True, exist_ok=True)
    for f in sorted(mdir.iterdir()):
        if f.suffix.lower() == '.emf':
            tmp = SCR / 'emf' / key
            tmp.mkdir(parents=True, exist_ok=True)
            subprocess.run([tool('soffice'), '--headless', '--convert-to', 'png', '--outdir', str(tmp), str(f)],
                           capture_output=True, timeout=180)
            png = tmp / (f.stem + '.png')
            if png.exists():
                subprocess.run([tool('magick', 'convert') if os.name != 'nt' else tool('magick'), str(png), '-trim', '+repage', '-define', 'png:exclude-chunks=date,time', str(dest / f'{key}-{f.stem}.png')], check=True)
                media_map[f.name] = f.stem + '.png'
            continue
        shutil.copy2(f, dest / f'{key}-{f.name}')
    # flat layout: _attachments/KEY-name  (wikilinks resolve by file name)
    for f in list(dest.iterdir()):
        shutil.move(str(f), str(ATT / f.name))
    dest.rmdir()
    return media_map


def build(key):
    cfg = SOURCES[key]
    text = (CONV / key / f'{key}.md').read_text(encoding='utf-8')
    media_map = convert_media(key)
    secs = parse_sections(text, key)

    # drop preamble (cover / TOC)
    secs = [x for x in secs if x[0] != 0 and x[1] != 'Table of Contents']

    chunks = group_chunks(secs)
    out_dir = cfg['dir'] / 'Appunti' / (cfg.get('sub') or '')
    out_dir = out_dir if cfg.get('sub') else cfg['dir'] / 'Appunti'
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    notes = []
    for i, (ch, pre) in enumerate(chunks, 1):
        heads = [clean_title(x[1]) for x in ch if x[1]]
        title = heads[0] if heads else f'Part {i}'
        if len(heads) > 1 and ch[0][0] == 2:
            title = f'{heads[0]} … {heads[-1]}' if len(heads) > 2 else f'{heads[0]} + {heads[1]}'
        if pre and pre.lower() not in title.lower() and cfg['module_note'].lower() not in pre.lower():
            title = f'{pre} · {title}'
        notes.append(dict(n=i, title=title, name=f'{key} {i:02d} - {title}', chunk=ch))
    for idx, nt in enumerate(notes):
        parts = []
        for j, s in enumerate(nt['chunk']):
            lvl, raw, body = s[:3]
            if j == 0:
                parts.append(f'# {clean_heading(raw)}\n')
            elif raw:
                parts.append(f'## {raw}\n')
            parts.append('\n'.join(body))
        body = postprocess('\n'.join(parts), key, media_map)
        prev_l = f'[[{notes[idx-1]["name"]}|← {notes[idx-1]["title"]}]]' if idx else ''
        next_l = f'[[{notes[idx+1]["name"]}|{notes[idx+1]["title"]} →]]' if idx + 1 < len(notes) else ''
        nav = ' · '.join(x for x in [prev_l, f'[[{cfg["module_note"]}|↑ {cfg["label"]}]]', next_l] if x)
        fm = (f'---\ncourse: "[[{cfg["course"]}]]"\nmodule: "[[{cfg["module_note"]}]]"\nsource: "{cfg["src"]}"\n'
              f'order: {nt["n"]}\ntags: [note, {key.lower()}]\n---\n\n')
        nt['path'] = out_dir / f'{nt["name"]}.md'
        text = fm + f'> {nav}\n\n' + body + f'\n---\n> {nav}\n'
        for prefix, old, new in FIXES:
            if nt['name'].startswith(prefix) and old in text:
                text = text.replace(old, new)
        write(nt['path'], text)
    return cfg, notes, out_dir


def extras(cfg):
    """Hand-written notes in <course>/Approfondimenti/<sub>/ (never touched by the import).
    Front-matter `companion_of: ["title fragment", ...]` links them from the matching Appunti notes."""
    d = cfg['dir'] / 'Approfondimenti' / (cfg.get('sub') or '')
    out = []
    for f in sorted(d.glob('*.md')) if d.is_dir() else []:
        t = f.read_text(encoding='utf-8')
        fm = re.match(r'^---\n(.*?)\n---\n', t, re.S)
        comp = []
        if fm:
            m = re.search(r'^companion_of:\n((?:[ \t]+- .*\n?)+)', fm.group(1) + '\n', re.M)
            if m:
                comp = [x.strip().strip('"\'') for x in re.findall(r'- (.*)', m.group(1))]
        name = f.stem
        out.append(dict(name=name, title=name.split(' - ', 1)[-1], comp=comp))
    return out


def link_extras(notes, ex):
    """Add an 'Approfondimento' line under the top nav bar of the Appunti notes named in companion_of."""
    for nt in notes:
        hits = [e for e in ex if any(c.lower() in nt['title'].lower() for c in e['comp'])]
        if not hits:
            continue
        t = nt['path'].read_text(encoding='utf-8')
        line = '*Approfondimento: ' + ' · '.join(f'[[{e["name"]}|{e["title"]}]]' for e in hits) + '*'
        i = t.index('\n\n', t.index('\n> ')) + 2      # right after the first nav blockquote
        write(nt['path'], t[:i] + line + '\n\n' + t[i:])


def clean_heading(raw):
    t = re.sub(r'<[^>]+>', '', raw).replace('*', '').strip()
    t = re.sub(r'\$`(.+?)`\$', lambda m: '$' + m.group(1) + '$', t)
    if t.upper() == t and re.search('[A-Z]', t):
        t = titlecase(t)
    return re.sub(r'^\d+(\.\d+)*\.?\s+', '', t) or t


def add_moc(cfg, notes, key):
    """Insert an '## Appunti' index into the module note, before '## Exam' (or append)."""
    f = cfg['dir'] / f'{cfg["module_note"]}.md'
    t = f.read_text(encoding='utf-8')
    t = re.sub(r'\n## Appunti \(MCB\)\n.*?(?=\n## |\Z)', '', t, flags=re.S)
    block = f'\n## Appunti (MCB)\n\nFonte: `{cfg["src"]}` — {len(notes)} note collegate in ordine.\n\n'
    block += '\n'.join(f'{n["n"]}. [[{n["name"]}|{n["title"]}]]' for n in notes) + '\n'
    ex = extras(cfg)
    if ex:
        block += '\nApprofondimenti (note scritte a mano in `Approfondimenti/`, non generate dal docx):\n\n'
        block += '\n'.join(f'- [[{e["name"]}|{e["title"]}]]' for e in ex) + '\n'
    if '\n## Exam' in t:
        t = t.replace('\n## Exam', block + '\n## Exam', 1)
    else:
        t = t.rstrip('\n') + '\n' + block
    write(f, t)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:] == ['--list']:
        for k, cfg in SOURCES.items():
            print(f'{k}\t{(ROOT / cfg["src"]).as_posix()}')   # forward slashes: fine for bash on Windows too
        sys.exit()
    keys = sys.argv[1:] or list(SOURCES)
    for k in keys:
        cfg, notes, d = build(k)
        link_extras(notes, extras(cfg))
        add_moc(cfg, notes, k)
        print(f'{k}: {len(notes)} notes -> {d.relative_to(VAULT)}')
        for n in notes:
            print('   ', n['name'], f'({sum(len(s[2]) for s in n["chunk"])} l)')
