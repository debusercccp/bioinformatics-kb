"""Rewrite the '## Collegamenti' cross-course links at the bottom of the Appunti notes."""
import re, glob, os
V=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files={}
for p in glob.glob(V+'/**/Appunti/**/*.md',recursive=True):
    n=os.path.basename(p)[:-3]; files[n.split(' - ')[0]]=(p,n)
def L(code): return f'[[{files[code][1]}]]'
REL = {
 'AML 03': [('MBD 01','norma e distanza'),('MBD 02','prodotto scalare')],
 'AML 05': [('MBD 19','gradiente e ottimizzazione multivariata'),('MBD 16','gradient descent in una variabile')],
 'AML 06': [('MBD 15','punti estremi, derivata nulla'),('MBD 19','Hessiana e natura dei punti critici')],
 'AML 07': [('MBD 19','gradiente di funzioni di più variabili'),('MBD 06','matrice inversa (soluzione in forma chiusa)')],
 'AML 08': [('MBD 05','prodotto righe per colonne: notazione matriciale delle feature'),('MBD 06','matrice inversa / trasposta')],
 'AML 11': [('MBD 03','iperpiani come classificatori lineari')],
 'AML 12': [('MBD 03','iperpiani e decision boundary lineare')],
 'AML 43': [('MBD 10','autovalori e autovettori'),('MBD 11','diagonalizzazione'),('SATAUMV 13','PCA per la struttura di popolazione')],
 'MBD 03': [('AML 12','decision boundary nella regressione logistica')],
 'MBD 10': [('AML 43','PCA nel corso di ML'),('SATAUMV 13','PCA in genetica di popolazione')],
 'MBD 16': [('AML 05','gradient descent in ML')],
 'MBD 19': [('AML 05','gradient descent')],
 'MBD 20': [('SATAUMV 03','Hardy-Weinberg: probabilità applicata alle popolazioni')],
 'SATAUMV 03': [('MBD 20','richiami di probabilità')],
 'SATAUMV 13': [('AML 43','PCA nel corso di ML'),('MBD 10','autovalori e autovettori')],
 'SATAUMV 09': [('BFB 03','banche dati e formati di sequenza'),('BFB 04','allineamento di sequenze / read mapping')],
 'BFB 03': [('SATAUMV 09','FASTQ/SAM/VCF e tecnologie di sequenziamento')],
 'BFB 04': [('SATAUMV 09','read mapping e variant calling')],
}
# hand-written notes outside Appunti/: re-point links whose Appunti note was renumbered
# (same title, different NN after a re-import)
by_title={}
for code,(p,n) in files.items():
    by_title[(code.split()[0], n.split(' - ',1)[-1])]=n
for p in glob.glob(V+'/**/*.md',recursive=True):
    if '/Appunti/' in p.replace(os.sep,'/'): continue
    t=open(p,encoding='utf-8').read()
    def fix(m):
        key,title=m.group(1),m.group(3)
        full=f'{key} {m.group(2)} - {title}'
        if full.split(' - ')[0] in files and files[full.split(' - ')[0]][1]==full: return m.group(0)
        new=by_title.get((key,title))
        return '[['+new if new else m.group(0)
    t2=re.sub(r'\[\[([A-Z]+) (\d+) - ([^\]|#]+)', fix, t)
    if t2!=t: open(p,'w',encoding='utf-8',newline='\n').write(t2)

for p,_ in files.values():
    t=open(p,encoding='utf-8').read()
    t2=re.sub(r'\n## Collegamenti\n.*?(?=\n---\n)', '', t, flags=re.S)
    if t2!=t: open(p,'w',encoding='utf-8',newline='\n').write(t2)
for code,items in REL.items():
    if code not in files: print('skip',code); continue
    items=[(c,w) for c,w in items if c in files]
    p,_=files[code]; t=open(p,encoding='utf-8').read()
    t=re.sub(r'\n## Collegamenti\n.*?(?=\n---\n)', '', t, flags=re.S)
    block='\n## Collegamenti\n'+''.join(f'- {L(c)} — {w}\n' for c,w in items)
    i=t.rindex('\n---\n')
    t=t[:i]+block+t[i:]
    open(p,'w',encoding='utf-8',newline='\n').write(t)
print('ok')