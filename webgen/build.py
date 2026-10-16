# -*- coding: utf-8 -*-
"""Generate theflamecodex.com: English at /, Spanish at /es/. Output: ../web/public"""
import os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
# Two layouts: the workshop (../web/assets holds the images, ../web/public is rebuilt from scratch)
# and the GitHub repository (webgen/ next to public/, whose images stay in place).
WORKSHOP = os.path.isdir(os.path.join(HERE, '..', 'web', 'assets'))
OUT = os.path.join(HERE, '..', 'web', 'public') if WORKSHOP else os.path.join(HERE, '..', 'public')
IMG_SRC = os.path.join(HERE, '..', 'web', 'assets', 'img')
DOMAIN = 'https://www.theflamecodex.com'

PAGES = ['', 'descent', 'codex', 'retreats', 'books', 'contact']
ALLP = PAGES + ['codex/meditation']
NAV = {
 'en': {'': 'Home', 'descent': 'The Descent', 'codex': 'The Flame Codex', 'retreats': 'Retreats', 'books': 'Books', 'contact': 'Contact'},
 'es': {'': 'Inicio', 'descent': 'El Descenso', 'codex': 'El Códice de la Llama', 'retreats': 'Retiros', 'books': 'Libros', 'contact': 'Contacto'},
}
TITLES = {
 'en': {'': 'The Flame Codex — Dr. Zuluan Orion', 'ground': 'The Ground — Nondual Awakening', 'descent': 'The Descent of the Flame', 'codex': 'The Flame Codex and the Light Codes', 'retreats': 'Retreats and Initiations in the Flame — The Flame Codex', 'books': 'Books of the Flame Codex', 'contact': 'Contact — The Flame Codex', 'codex/meditation': 'Light Code Meditation — The Flame Codex'},
 'es': {'': 'El Códice de la Llama — Dr. Zuluan Orion', 'ground': 'El Fundamento — el despertar no dual', 'descent': 'El Descenso de la Llama', 'codex': 'El Códice de la Llama y los Códigos de Luz', 'retreats': 'Retiros e iniciaciones en la Llama — El Códice de la Llama', 'books': 'Libros del Códice de la Llama', 'contact': 'Contacto — El Códice de la Llama', 'codex/meditation': 'Meditación de Códigos de Luz — El Códice de la Llama'},
}
DESC = {
 'en': 'The Flame Codex — a sacred language of return and incarnation. Light Codes for embodying the Flame, born of a nondual awakening and a living descent of Consciousness into the body. Dr. Zuluan Orion.',
 'es': 'El Códice de la Llama — un lenguaje sagrado de retorno y encarnación. Códigos de Luz para encarnar la Llama, nacidos de un despertar no dual y de un descenso vivo de la Consciencia en el cuerpo. Dr. Zuluan Orion.',
}

def url(lang, page):
    base = '/es/' if lang == 'es' else '/'
    return base + (page + '/' if page else '')

def S(n): return '/assets/img/sigil_%02d.png' % n

def head(lang, page):
    other = 'es' if lang == 'en' else 'en'
    navlinks = ''.join('<a href="%s"%s>%s</a>' % (url(lang, p), ' class="on"' if (p == page or (p and page.startswith(p + '/'))) else '', NAV[lang][p]) for p in PAGES)
    navlinks += '<a class="sb" href="https://drzuluanorion.org%s">Dr. Zuluan Orion ↗</a>' % ('/es/' if lang == 'es' else '/')
    navlinks += '<a class="sb" href="https://www.spiritualbalanceinfo.com%s">%s</a>' % ('/es/' if lang == 'es' else '/', 'Sesiones ↗' if lang == 'es' else 'Sessions ↗')
    navlinks += '<a class="lang" href="%s" hreflang="%s">%s</a>' % (url(other, page), other, 'Español' if lang == 'en' else 'English')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLES[lang][page]}</title>
<meta name="description" content="{DESC[lang]}">
<link rel="canonical" href="{DOMAIN}{url(lang, page)}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{url('en', page)}">
<link rel="alternate" hreflang="es" href="{DOMAIN}{url('es', page)}">
<meta property="og:title" content="{TITLES[lang][page]}">
<meta property="og:description" content="{DESC[lang]}">
<meta property="og:image" content="{DOMAIN}/assets/img/portrait_side.jpg">
<link rel="icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{url(lang, '')}">THE FLAME CODEX</a>
<button class="menu-btn" onclick="document.querySelector('nav.main').classList.toggle('open')">{'MENU' if lang == 'en' else 'MENÚ'}</button>
<nav class="main">{navlinks}</nav>
</div></header>
<main>
'''

def foot(lang):
    t = {'en': ('A sacred language of return and incarnation.', 'The family of sites', 'Dr. Zuluan Orion — the author, his story and his teaching', 'Spiritual Balance — therapy and personal work, Weston, Florida'),
         'es': ('Un lenguaje sagrado de retorno y encarnación.', 'La familia de sitios', 'Dr. Zuluan Orion — el autor, su historia y su enseñanza', 'Spiritual Balance — terapias y trabajo personal, Weston, Florida')}[lang]
    pre = '/es/' if lang == 'es' else '/'
    return f'''</main>
<footer class="site"><div class="wrap">
<a class="brand" href="{url(lang, '')}">THE FLAME CODEX</a>
<p>{t[0]}</p>
<p>{t[1]}: <a href="https://drzuluanorion.org{pre}">{t[2]}</a> · <a href="https://www.spiritualbalanceinfo.com{pre}">{t[3]}</a></p>
<p>© 2026 Dr. Zuluan Orion · <a href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a> · <a href="https://drzuluanorion.org{pre}">drzuluanorion.org</a></p>
</div></footer>
</body>
</html>
'''

def hero(title, sub, lede='', sig=1, page=True, btns='', img=None):
    return f'''<section class="hero{' page' if page else ''}"><div class="wrap">
<img class="sig{' glow' if img else ''}" src="{img or S(sig)}" alt="{'AHR' if img else ''}">
<h1>{title}</h1>
<p class="sub">{sub}</p>
{f'<p class="lede">{lede}</p>' if lede else ''}
{btns}
</div></section>
'''

# ------------------------------------------------------------------ content
import builtins; builtins.url = url; builtins.S = S; builtins.hero = hero
from content import BODY

def build():
    if WORKSHOP:
        if os.path.exists(OUT): shutil.rmtree(OUT)
        os.makedirs(os.path.join(OUT, 'assets', 'img'))
        for f in os.listdir(IMG_SRC):
            p = os.path.join(IMG_SRC, f)
            if os.path.isdir(p): shutil.copytree(p, os.path.join(OUT, 'assets', 'img', f))
            else: shutil.copy(p, os.path.join(OUT, 'assets', 'img', f))
    else:
        os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    # (the Thailand journey guides now live on drzuluanorion.org and spiritualbalanceinfo.com)
    shutil.copy(os.path.join(HERE, 'style.css'), os.path.join(OUT, 'assets', 'style.css'))
    for lang in ('en', 'es'):
        for page in ALLP:
            d = os.path.join(OUT, 'es' if lang == 'es' else '', page)
            os.makedirs(d, exist_ok=True)
            html = head(lang, page) + BODY[lang][page] + foot(lang)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(html)
    # pages that moved to drzuluanorion.org: a gentle redirect (old files may still be in the repo)
    from fc_new import MOVED, moved_stub
    for lang in ('en', 'es'):
        for old in MOVED:
            d = os.path.join(OUT, 'es' if lang == 'es' else '', old)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(moved_stub(lang, old))
    # 404
    open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(head('en', '') + hero('Not found', 'This page does not exist. <a href="/" style="color:#E9D5A6">Return home</a> · <a href="/es/" style="color:#E9D5A6">Volver al inicio</a>') + foot('en'))
    # sitemap + robots
    sm = ''.join('<url><loc>%s%s</loc></url>' % (DOMAIN, url(l, p)) for l in ('en', 'es') for p in ALLP)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % DOMAIN)
    print('built', OUT)

if __name__ == '__main__':
    build()
