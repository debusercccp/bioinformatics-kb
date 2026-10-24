"""Rewrite the '## Collegamenti' cross-course links at the bottom of the Appunti notes."""
import re, glob, os
V=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files={}
for p in glob.glob(V+'/**/Appunti/**/*.md',recursive=True):
    n=os.path.basename(p)[:-3]; files[n.split(' - ')[0]]=(p,n)
def L(code): return f'[[{files[code][1]}]]'
REL = {
 'AML 03': [('MBD 19','regressione lineare, lato matematico'),('MBD 04','norma e distanza')],
 'AML 05': [('MBD 14','gradiente e ottimizzazione multivariata')],
 'AML 06': [('MBD 14','estremi, Hessiana, condizioni di ottimo')],
 'AML 07': [('MBD 14','gradiente di funzioni di più variabili'),('MBD 09','soluzione in forma chiusa di Ax=b / minimi quadrati')],
 'AML 08': [('MBD 06','notazione matriciale delle feature'),('MBD 09','minimi quadrati')],
 'AML 09': [('MBD 19','regressione polinomiale e overfitting')],
 'AML 11': [('MBD 05','iperpiani come classificatori lineari')],
 'AML 12': [('MBD 05','iperpiani e decision boundary lineare')],
 'AML 13': [('MBD 18','massima verosimiglianza')],
 'AML 17': [('MBD 19','regolarizzazione (ridge/lasso)')],
 'AML 43': [('MBD 20','PCA: formulazione e algoritmo'),('MBD 11','autovalori e autovettori')],
 'AML 45': [('MBD 20','PCA come riduzione lineare di dimensionalità')],
 'MBD 05': [('AML 12','decision boundary nella regressione logistica')],
 'MBD 14': [('AML 05','gradient descent')],
 'MBD 18': [('AML 13','cost function logistica = log-verosimiglianza')],
 'MBD 19': [('AML 03','regressione in ML'),('AML 17','regolarizzazione')],
 'MBD 20': [('AML 43','PCA nel corso di ML'),('AML 45','autoencoder come PCA non lineare')],
 'MBD 15': [('SATAUMV 03','Hardy-Weinberg: probabilità applicata alle popolazioni')],
 'SATAUMV 03': [('MBD 15','richiami di probabilità')],
 'SATAUMV 11': [('MBD 20','PCA per la struttura di popolazione')],
 'SATAUMV 09': [('BFB 03','banche dati e formati di sequenza'),('BFB 04','allineamento di sequenze / read mapping')],
 'BFB 03': [('SATAUMV 09','FASTQ/SAM/VCF e tecnologie di sequenziamento')],
 'BFB 04': [('SATAUMV 09','read mapping e variant calling')],
}
for p,_ in files.values():
    t=open(p).read()
    t2=re.sub(r'\n## Collegamenti\n.*?(?=\n---\n)', '', t, flags=re.S)
    if t2!=t: open(p,'w').write(t2)
for code,items in REL.items():
    if code not in files: print('skip',code); continue
    items=[(c,w) for c,w in items if c in files]
    p,_=files[code]; t=open(p).read()
    t=re.sub(r'\n## Collegamenti\n.*?(?=\n---\n)', '', t, flags=re.S)
    block='\n## Collegamenti\n'+''.join(f'- {L(c)} — {w}\n' for c,w in items)
    i=t.rindex('\n---\n')
    t=t[:i]+block+t[i:]
    open(p,'w').write(t)
print('ok')