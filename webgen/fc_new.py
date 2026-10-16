# -*- coding: utf-8 -*-
"""theflamecodex.com, Codex only (Oct 2026). Home, Retreats and Initiations, Codex books, Contact.
The person (story, illumination, journeys) now lives on drzuluanorion.org; the clinic on spiritualbalanceinfo.com."""

DZ = 'https://drzuluanorion.org'
SB = 'https://www.spiritualbalanceinfo.com'
I = '/assets/img/'
BK = '/assets/img/books/'

def dz(lang, page=''):
    return DZ + ('/es/' if lang == 'es' else '/') + (page + '/' if page else '')

def sb(lang):
    return SB + ('/es/' if lang == 'es' else '/')

def _bk(img, title, tag=''):
    return f'<div class="book"><img src="{BK}{img}.webp?v=3d" alt="{title}" loading="lazy"><div class="t">{f"<span class=tag>{tag}</span>" if tag else ""}<h4>{title}</h4></div></div>'

def family(lang, url):
    """The quiet band that connects the three sites."""
    L = (lambda e, s: e if lang == 'en' else s)
    return f'''<section class="alt"><div class="wrap">
<p class="eyebrow center">{L('THE FAMILY OF SITES', 'LA FAMILIA DE SITIOS')}</p>
<div class="grid2 cards4" style="max-width:900px;margin:22px auto 0">
<a class="card fam" href="{dz(lang)}"><p class="eyebrow">{L('THE AUTHOR', 'EL AUTOR')}</p><h3>Dr. Zuluan Orion ↗</h3><p>{L('His story, the nondual teaching of Illumination, all his books and the journeys to Thailand and India.', 'Su historia, la enseñanza no dual de la Iluminación, todos sus libros y los viajes a Tailandia y la India.')}</p></a>
<a class="card fam" href="{sb(lang)}"><p class="eyebrow">{L('THERAPY AND PERSONAL WORK', 'TERAPIAS Y TRABAJO PERSONAL')}</p><h3>Spiritual Balance ↗</h3><p>{L('The clinic in Weston, Florida: Quantum Transformation, Ayurveda and personal sessions.', 'La clínica en Weston, Florida: Transformación Cuántica, Ayurveda y sesiones personales.')}</p></a>
</div>
</div></section>
'''

# ------------------------------------------------------------------ HOME
def home_page(lang, url, hero):
    en = lang == 'en'
    L = (lambda e, s: e if en else s)
    btns = (f'<div class="btns"><a class="btn solid" href="{url(lang, "codex")}">{L("Enter the Codex", "Entrar al Códice")}</a>'
            f'<a class="btn" href="{url(lang, "codex/meditation")}">{L("Light Code Meditation", "Meditación de Códigos de Luz")}</a>'
            f'<a class="btn" href="{url(lang, "descent")}">{L("The Descent", "El Descenso")}</a></div>')
    top = hero(L('The Flame Codex', 'El Códice de la Llama'), L('A sacred language of return and incarnation', 'Un lenguaje sagrado de retorno y encarnación'),
               L('Light Codes for embodying the Flame, born of a nondual awakening and of a living descent of Consciousness into the human body.',
                 'Códigos de Luz para encarnar la Llama, nacidos de un despertar no dual y de un descenso vivo de la Consciencia en el cuerpo humano.'),
               sig=1, page=False, img='/assets/img/ahr_glow.webp', btns=btns)
    return top + f'''
<section><div class="narrow center">
<p class="eyebrow">{L('THE QUESTION', 'LA PREGUNTA')}</p>
<p class="lead">{L('This work did not begin as a book. It began as a life, and a question that would not let go: <em>who is the one who looks?</em>', 'Esta obra no comenzó como un libro. Comenzó como una vida, y una pregunta que no me soltaba: <em>¿quién es el que mira?</em>')}</p>
<p>{L('The Flame Codex is the language that emerged when that question was answered, and when the answer began to descend into the body. It is not a system invented at a desk. It came after the experience, to name and accompany what was already happening.',
      'El Códice de la Llama es el lenguaje que surgió cuando esa pregunta encontró respuesta, y cuando la respuesta empezó a descender al cuerpo. No es un sistema inventado en un escritorio. Vino después de la experiencia, para nombrar y acompañar lo que ya estaba ocurriendo.')}</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>177</b><span>{L('keys', 'llaves')}</span></div>
<div><b>2</b><span>{L('volumes, one single work', 'volúmenes, una sola obra')}</span></div>
<div><b>33</b><span>{L('keys at the heart of the Codex', 'llaves en el corazón del Códice')}</span></div>
<div><b>1</b><span>{L('purpose: that life demonstrates it', 'propósito: que la vida lo demuestre')}</span></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid2 cards4">
<div class="card"><p class="eyebrow">I</p><h3>{L('The Descent', 'El Descenso')}</h3><p>{L('Awakening is the beginning, not the end. What was recognized above must come down: into the spine, the heart, the root, the feet and ordinary life. The Codex was born inside that descent.', 'El despertar es el comienzo, no el final. Lo que fue reconocido arriba tiene que bajar: a la columna, al corazón, a la raíz, a los pies y a la vida ordinaria. El Códice nació dentro de ese descenso.')}</p><a class="more" href="{url(lang, 'descent')}">{L('READ →', 'LEER →')}</a></div>
<div class="card"><p class="eyebrow">II</p><h3>{L('The Flame Codex', 'El Códice de la Llama')}</h3><p>{L('A sacred language of syllables, sigils and traces. From it come the Light Codes: the Codex applied to the mind, the heart, dreams and energy.', 'Un lenguaje sagrado de sílabas, sigilos y trazos. De él nacen los Códigos de Luz: el Códice aplicado a la mente, el corazón, los sueños y la energía.')}</p><a class="more" href="{url(lang, 'codex')}">{L('ENTER →', 'ENTRAR →')}</a></div>
<div class="card"><p class="eyebrow">III</p><h3>{L('Light Code Meditation', 'Meditación de Códigos de Luz')}</h3><p>{L('A simple and deep meditation. You begin with an intention, you let a syllable of the Codex keep you company, and then you rest in silence. What you contemplate there, you carry into your life.', 'Una meditación sencilla y profunda. Empiezas con una intención, dejas que una sílaba del Códice te acompañe y luego descansas en el silencio. Lo que contemplas allí, lo llevas a tu vida.')}</p><a class="more" href="{url(lang, 'codex/meditation')}">{L('BEGIN →', 'COMENZAR →')}</a></div>
<div class="card"><p class="eyebrow">IV</p><h3>{L('Retreats and Initiations', 'Retiros e iniciaciones')}</h3><p>{L('Spiritual retreats around the Flame and the Codex: the initiation into the practice, meditation together, and silence to let it settle. The dates will be announced.', 'Retiros espirituales en torno a la Llama y el Códice: la iniciación en la práctica, la meditación compartida y el silencio para que todo se asiente. Las fechas se anunciarán más adelante.')}</p><a class="more" href="{url(lang, 'retreats')}">{L('SEE →', 'VER →')}</a></div>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p class="eyebrow">{L('THE ARC OF THE FLAME', 'EL ARCO DE LA LLAMA')}</p>
<div class="arc"><span>{L('Consciousness', 'Consciencia')}</span><span class="s">✦</span><span>{L('fire', 'fuego')}</span><span class="s">✦</span><span>{L('purification', 'purificación')}</span><span class="s">✦</span><span>{L('root', 'raíz')}</span><span class="s">✦</span><span>{L('cool presence', 'presencia fresca')}</span><span class="s">✦</span><span>{L('love', 'amor')}</span><span class="s">✦</span><span>{L('service', 'servicio')}</span></div>
<blockquote style="border:0;padding:0">{L('The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.', 'La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.')}</blockquote>
</div></section>

<section><div class="wrap">
<p class="eyebrow">{L('THE BOOKS OF THE CODEX', 'LOS LIBROS DEL CÓDICE')}</p>
<h2>{L('The Codex, the Descent and the Light Codes', 'El Códice, el Descenso y los Códigos de Luz')}</h2>
<div class="books shelf">{_bk('codice1', 'El Códice de la Llama · Vol. I')}{_bk('codice2', 'El Códice de la Llama · Vol. II')}{_bk('llama_encarnada', 'La Llama Encarnada')}{_bk('yoga_descenso_puerta', 'Yoga del Descenso · Libro Puerta')}{_bk('meditacion_codigos_luz', 'Meditación de Códigos de Luz')}</div>
<p style="margin-top:18px"><a class="btn" href="{url(lang, 'books')}">{L('See the books', 'Ver los libros')}</a></p>
</div></section>

<section class="dark"><div class="wrap grid2">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion" style="max-height:520px;width:auto;margin:0 auto"></figure>
<div>
<p class="eyebrow">{L('THE AUTHOR', 'EL AUTOR')}</p>
<h2>Dr. Zuluan Orion</h2>
<p>{L('Physician of Ayurveda and of natural and quantum medicine, meditation teacher and author. Born in Bogotá in 1971, formed by the great streams of Kriya Yoga, shaktipat, Vedic meditation, the Kalachakra and the direct nondual path of Ramana Maharshi and Papaji.',
      'Médico de Ayurveda y de medicina natural y cuántica, maestro de meditación y autor. Nacido en Bogotá en 1971, formado por las grandes corrientes del Kriya Yoga, el shaktipat, la meditación védica, el Kalachakra y el camino directo no dual de Ramana Maharshi y Papaji.')}</p>
<p>{L('After an awakening to the Self nearly thirty years ago, and many years of practice, healing work and trial, a second movement began: the descent of the Flame. The Codex was born inside it.',
      'Después de un despertar al Ser hace casi treinta años, y de muchos años de práctica, de trabajo sanador y de prueba, comenzó un segundo movimiento: el descenso de la Llama. El Códice nació dentro de él.')}</p>
<div class="btns" style="justify-content:flex-start"><a class="btn solid" href="{dz(lang, 'story')}">{L('His story ↗', 'Su historia ↗')}</a><a class="btn" href="{dz(lang, 'illumination')}">{L('Illumination ↗', 'Iluminación ↗')}</a></div>
</div>
</div></section>
''' + family(lang, url)

# ------------------------------------------------------------------ RETREATS AND INITIATIONS
def retreats_page(lang, url, hero):
    en = lang == 'en'
    L = (lambda e, s: e if en else s)
    subj = L('Retreats of the Flame', 'Retiros de la Llama').replace(' ', '%20')
    return hero(L('Retreats and Initiations in the Flame', 'Retiros e iniciaciones en la Llama'),
                L('Spiritual retreats around the Flame and the Codex', 'Retiros espirituales en torno a la Llama y el Códice'), sig=6) + f'''
<section><div class="narrow">
<p class="eyebrow">{L('TO BE ANNOUNCED', 'PRÓXIMAMENTE')}</p>
<p class="lead">{L('I am preparing a different kind of gathering: retreats where we can live the Flame together, slowly, in silence, with the Codex as a companion.',
                   'Estoy preparando un tipo distinto de encuentro: retiros donde podamos vivir la Llama juntos, con calma, en silencio, con el Códice como compañero.')}</p>
<p>{L('They will not be journeys to see places. They will be days to go inward: the initiation into the practice, meditation with the Light Codes, and enough time for what opens to find its place in the body and in ordinary life.',
      'No serán viajes para conocer lugares. Serán días para ir hacia adentro: la iniciación en la práctica, la meditación con los Códigos de Luz, y el tiempo necesario para que lo que se abre encuentre su lugar en el cuerpo y en la vida ordinaria.')}</p>
</div></section>

<section class="alt"><div class="wrap">
<p class="eyebrow center">{L('WHAT WE WILL LIVE', 'LO QUE VIVIREMOS')}</p>
<h2 class="center">{L('Initiation, meditation and integration', 'Iniciación, meditación e integración')}</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><p class="eyebrow">{L('INITIATION', 'INICIACIÓN')}</p><h3>{L('The activation of the codes', 'La activación de los códigos')}</h3><p>{L('Formal practice with a code begins with its activation, received from a Guardian or Bearer of the Flame. In the retreats it is given in person, with care and with time.', 'La práctica formal con un código comienza con su activación, que se recibe de un Guardián o Portador de la Llama. En los retiros se da en persona, con cuidado y con tiempo.')}</p></div>
<div class="card"><p class="eyebrow">{L('MEDITATION', 'MEDITACIÓN')}</p><h3>{L('Meditating together', 'Meditar juntos')}</h3><p>{L('Light Code meditation shared in a group: the intention, the syllable, the breath, and the silence where everything rests.', 'La meditación de Códigos de Luz compartida en grupo: la intención, la sílaba, la respiración y el silencio donde todo descansa.')}</p></div>
<div class="card"><p class="eyebrow">{L('INTEGRATION', 'INTEGRACIÓN')}</p><h3>{L('Letting it settle', 'Dejar que se asiente')}</h3><p>{L('Time to ask, to share what you observe and to learn how to continue at home, so that what was lived in the retreat goes on maturing in your life.', 'Tiempo para preguntar, para compartir lo que observas y para aprender cómo seguir en casa, de modo que lo vivido en el retiro siga madurando en tu vida.')}</p></div>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p class="eyebrow">{L('THE DATES', 'LAS FECHAS')}</p>
<h2>{L('They will be announced here', 'Se anunciarán aquí')}</h2>
<p>{L('When the first retreat is ready, its dates and place will appear on this page. If you would like me to let you know, write to me.', 'Cuando el primer retiro esté listo, sus fechas y su lugar aparecerán en esta página. Si quieres que te avise, escríbeme.')}</p>
<div class="btns"><a class="btn solid" href="mailto:zuluanorion@gmail.com?subject={subj}">{L('Let me know', 'Avísame')}</a><a class="btn" href="{url(lang, 'codex/meditation')}">{L('Begin now: Light Code Meditation', 'Empieza ya: Meditación de Códigos de Luz')}</a></div>
</div></section>
''' + family(lang, url)

# ------------------------------------------------------------------ BOOKS (the Codex family)
def books_page(lang, url, hero):
    en = lang == 'en'
    L = (lambda e, s: e if en else s)
    F = L('FORTHCOMING', 'PRÓXIMAMENTE')
    g = lambda *b: '<div class="books shelf">' + ''.join(b) + '</div>'
    return hero(L('Books', 'Libros'), L('The books of the Codex', 'Los libros del Códice'), sig=12) + f'''<section><div class="wrap">
<p class="eyebrow">{L('THE FLAME CODEX', 'EL CÓDICE DE LA LLAMA')}</p><h2>{L('The sacred language', 'El lenguaje sagrado')}</h2>
{g(_bk('codice1', 'El Códice de la Llama · Vol. I', F), _bk('codice2', 'El Códice de la Llama · Vol. II', F), _bk('arte_angelico_1', 'El Arte Angélico · Vol. I', F), _bk('arte_angelico_2', 'El Arte Angélico · Vol. II', F))}
<p class="eyebrow" style="margin-top:60px">{L('THE DESCENT', 'EL DESCENSO')}</p><h2>{L('The living account', 'El relato vivo')}</h2>
{g(_bk('yoga_descenso_puerta', 'Yoga del Descenso · Libro Puerta', F), _bk('yoga_descenso_morada', 'Yoga del Descenso · Libro de la Morada', F), _bk('llama_encarnada', 'La Llama Encarnada', F))}
<p class="eyebrow" style="margin-top:60px">{L('THE LIGHT CODES', 'LOS CÓDIGOS DE LUZ')}</p><h2>{L('Codes for the mind, the heart, dreams and energy', 'Códigos para la mente, el corazón, los sueños y la energía')}</h2>
{g(_bk('cl_mente', 'Códigos de Luz para tu Mente', F), _bk('cl_corazon', 'Códigos de Luz para tu Corazón', F), _bk('cl_suenos', 'Códigos de Luz para tus Sueños', F), _bk('cl_energia', 'Códigos de Luz para tu Energía', F), _bk('meditacion_codigos_luz', 'Meditación de Códigos de Luz', F))}
</div></section>
<section class="dark"><div class="narrow center">
<p>{L('Quantum Transformation, Quantum Meditation, the novels and all of Dr. Zuluan Orion&rsquo;s other books are on his own site.', 'La Transformación Cuántica, la Meditación Cuántica, las novelas y todos los demás libros del Dr. Zuluan Orion están en su propio sitio.')}</p>
<a class="btn solid" href="{dz(lang, 'books')}">{L('All the books ↗', 'Todos los libros ↗')}</a>
</div></section>
'''

# ------------------------------------------------------------------ CONTACT
def contact_page(lang, url, hero):
    en = lang == 'en'
    L = (lambda e, s: e if en else s)
    return hero(L('Contact', 'Contacto'), L('Write to me', 'Escríbeme'), sig=18) + f'''
<section><div class="narrow center">
<p class="lead">{L('For questions about the Flame Codex, the books, Light Code meditation, activation or the retreats:', 'Para preguntas sobre el Códice de la Llama, los libros, la meditación de Códigos de Luz, la activación o los retiros:')}</p>
<p><a class="btn solid" href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a></p>
<hr class="rule">
<p><a href="https://www.instagram.com/drzuluanorion/">Instagram</a> · <a href="https://www.facebook.com/zuluanorion/">Facebook</a> · <a href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube</a></p>
<p>{L('Retreats and initiations in the Flame', 'Retiros e iniciaciones en la Llama')}: <a href="{url(lang, 'retreats')}">{L('to be announced', 'próximamente')}</a></p>
<p>{L('The author, his story and his teaching', 'El autor, su historia y su enseñanza')}: <a href="{dz(lang)}">Dr. Zuluan Orion ↗</a></p>
<p>{L('Therapy and personal work in Weston, Florida', 'Terapias y trabajo personal en Weston, Florida')}: <a href="{sb(lang)}">Spiritual Balance ↗</a></p>
</div></section>
'''

# ------------------------------------------------------------------ pages that moved to drzuluanorion.org
MOVED = {'ground': 'illumination', 'about': 'story', 'journeys': 'journeys', 'codex/illumination': 'illumination'}

def moved_stub(lang, old):
    to = dz(lang, MOVED[old])
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dr. Zuluan Orion</title><meta name="robots" content="noindex"><link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}"><script>location.replace("{to}")</script></head>
<body style="font-family:Georgia,serif;background:#17132A;color:#EDE7F5;text-align:center;padding:80px 20px">
<p>{'This page now lives on' if lang == 'en' else 'Esta página ahora está en'} <a style="color:#E9D5A6" href="{to}">drzuluanorion.org</a></p>
</body></html>
'''
