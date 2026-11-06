#!/usr/bin/env python3
"""Assemble the Kirina book: shell.html + parts/*.html -> ../tiira/index.html"""
import glob, os, re, sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'tiira', 'index.html')
VOID = {'br', 'hr', 'img', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'col', 'path', 'line', 'rect',
        'circle', 'ellipse', 'polygon', 'polyline', 'stop', 'use'}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack = []; self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID: self.stack.append((tag, self.getpos()))
    def handle_startendtag(self, tag, attrs): pass
    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.stack and self.stack[-1][0] == tag: self.stack.pop(); return
        if any(t == tag for t, _ in self.stack):
            while self.stack and self.stack[-1][0] != tag:
                t, pos = self.stack.pop(); self.errors.append(f'unclosed <{t}> opened at line {pos[0]}')
            self.stack.pop()
        else:
            self.errors.append(f'stray </{tag}> at line {self.getpos()[0]}')

def main():
    parts = sorted(glob.glob(os.path.join(HERE, 'parts', '*.html')))
    body, total, ok = [], 0, True
    for f in parts:
        src = open(f, encoding='utf-8').read()
        n = len(re.findall(r'<section class="page', src))
        c = Checker(); c.feed(src); c.close()
        errs = c.errors + [f'unclosed <{t}> opened at line {p[0]}' for t, p in c.stack]
        missing = [m.start() for m in re.finditer(r'<section class="page[^>]*>', src)
                   if 'data-title=' not in m.group(0) or 'data-part=' not in m.group(0)]
        status = 'OK' if not errs and not missing else 'CHECK'
        if status != 'OK': ok = False
        print(f'{os.path.basename(f):28s} {n:3d} pages  {status}')
        for e in errs[:8]: print('   ', e)
        if missing: print(f'    {len(missing)} section(s) missing data-title/data-part')
        total += n; body.append(f'<!-- ===== {os.path.basename(f)} ===== -->\n' + src.strip())
    shell = open(os.path.join(HERE, 'shell.html'), encoding='utf-8').read()
    html = shell.replace('<!--PAGES-->', '\n'.join(body))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(html)
    words = len(re.sub(r'<[^>]+>', ' ', '\n'.join(body)).split())
    print(f'\nTOTAL: {total} pages, ~{words:,} words -> {os.path.normpath(OUT)}')
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
