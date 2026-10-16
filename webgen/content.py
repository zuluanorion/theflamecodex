# -*- coding: utf-8 -*-
# Page bodies. url(), S(), hero() are injected as builtins by build.py.
BODY = {'en': {}, 'es': {}}
I = '/assets/img/'

def sigrid(n=33):
    return '<div class="sigils">' + ''.join('<img src="%s" alt="" >' % S(i) for i in range(1, n + 1)) + '</div>'

BK = '/assets/img/books/'
def bk(img, title, tag=''):
    top = f'<img src="{BK}{img}.webp?v=3d" alt="{title}" loading="lazy">' if img else f'<div class="ph" style="aspect-ratio:2/3;max-height:340px">{title}</div>'
    return f'<div class="book">{top}<div class="t">{f"<span class=tag>{tag}</span>" if tag else ""}<h4>{title}</h4></div></div>'

def shelf(lang):
    t = {'en': ('THE LIGHT CODES', 'Codes for the mind, the heart, dreams and energy', 'THE FLAME CODEX', 'The sacred language', 'THE DESCENT', 'The living account', 'HEALING AND MEDITATION', 'Quantum Transformation', 'NOVELS AND STORIES', 'Spiritual fiction', 'FORTHCOMING'),
         'es': ('LOS CÓDIGOS DE LUZ', 'Códigos para la mente, el corazón, los sueños y la energía', 'EL CÓDICE DE LA LLAMA', 'El lenguaje sagrado', 'EL DESCENSO', 'El relato vivo', 'SANACIÓN Y MEDITACIÓN', 'Transformación Cuántica', 'NOVELAS E HISTORIAS', 'Ficción espiritual', 'PRÓXIMAMENTE')}[lang]
    F = t[10]
    g = lambda *b: '<div class="books shelf">' + ''.join(b) + '</div>'
    return f'''<section><div class="wrap">
<p class="eyebrow">{t[0]}</p><h2>{t[1]}</h2>
{g(bk('cl_mente','Códigos de Luz para tu Mente',F), bk('cl_corazon','Códigos de Luz para tu Corazón',F), bk('cl_suenos','Códigos de Luz para tus Sueños',F), bk('cl_energia','Códigos de Luz para tu Energía',F), bk('meditacion_codigos_luz','Meditación de Códigos de Luz',F))}
<p class="eyebrow" style="margin-top:60px">{t[2]}</p><h2>{t[3]}</h2>
{g(bk('codice1','El Códice de la Llama · Vol. I',F), bk('codice2','El Códice de la Llama · Vol. II',F), bk('arte_angelico_1','El Arte Angélico · Vol. I',F), bk('arte_angelico_2','El Arte Angélico · Vol. II',F))}
<p class="eyebrow" style="margin-top:60px">{t[4]}</p><h2>{t[5]}</h2>
{g(bk('yoga_descenso_puerta','Yoga del Descenso · Libro Puerta',F), bk('yoga_descenso_morada','Yoga del Descenso · Libro de la Morada',F), bk('llama_encarnada','La Llama Encarnada',F))}
<p class="eyebrow" style="margin-top:60px">{t[6]}</p><h2>{t[7]}</h2>
{g(bk('transformacion_cuantica','Transformación Cuántica'), bk('transformacion_cuantica_nivel1','Transformación Cuántica · Nivel 1'), bk('puntos_transformacion_cuantica','Puntos de Transformación Cuántica'), bk('meditacion_cuantica','Meditación Cuántica'), bk('el_refugio_del_corazon','El refugio del Corazón'), bk('deshojando_corazon_eternidad','Deshojando el Corazón de la Eternidad'))}
<p class="eyebrow" style="margin-top:60px">{t[8]}</p><h2>{t[9]}</h2>
{g(bk('selarin','Selarín'), bk('dipti_la_invasora_esperada','DIPTI · La invasora esperada'), bk('zendrick_virtudes_khudday','Zendrick y las virtudes del Khudday'), bk('zendrick_ii_cinco_virtudes','Zendrick II y las cinco virtudes'), bk('la_busqueda_del_rey','La búsqueda del rey'))}
</div></section>
'''

def honors(lang, imgs):
    t = {'en': ('RECOGNITION', 'Honored for his work', 'International recognition for integrating Ayurveda, quantum medicine and consciousness in the service of healing.',
                [('Dhanwantari Award', 'AAPNA · Association of Ayurvedic Professionals of North America · 2025'), ('AAPNA 2025', 'Ayurveda and the Mind, Pennsylvania'), ('Leader in Health Sciences', 'Health Sciences Awards · Santander, Spain · 2022'), ('Lifestyle Plus Awards', 'Lifestyle Plus Magazine')],
                [('60,000+', 'hours of meditation'), ('20+ years', 'in India and Thailand'), ('12,000+', 'people initiated into meditation'), ('20+ books', 'published')]),
         'es': ('RECONOCIMIENTOS', 'Reconocido por su trabajo', 'Reconocimiento internacional por integrar la Ayurveda, la medicina cuántica y la consciencia al servicio de la sanación.',
                [('Premio Dhanwantari', 'AAPNA · Asociación de Profesionales Ayurvédicos de Norteamérica · 2025'), ('AAPNA 2025', 'Ayurveda and the Mind, Pensilvania'), ('Líder en Ciencias de la Salud', 'Health Sciences Awards · Santander, España · 2022'), ('Lifestyle Plus Awards', 'Lifestyle Plus Magazine')],
                [('60.000+', 'horas de meditación'), ('20+ años', 'en la India y Tailandia'), ('12.000+', 'personas iniciadas en la meditación'), ('20+ libros', 'publicados')])}[lang]
    figs = ''.join(f'<figure><img src="/assets/img/{im}" alt="{a}" loading="lazy"><figcaption><b>{a}</b><span>{b}</span></figcaption></figure>' for im, (a, b) in zip(imgs, t[3]))
    st = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t[4])
    return f"""<section class="honors"><div class="wrap">
<p class="eyebrow">{t[0]}</p><h2>{t[1]}</h2><p class="sub">{t[2]}</p>
<div class="row">{figs}</div>
<div class="stats">{st}</div>
</div></section>
"""

def trip(lang, eyebrow, title, place, paras, stops):
    st = ''.join(f'<li>{s}</li>' for s in stops)
    return f'''<div class="card" style="padding:34px 32px">
<p class="eyebrow">{eyebrow}</p>
<h3 style="margin-top:4px">{title}</h3>
<p style="font-family:var(--caps);letter-spacing:.08em;font-size:14px;color:var(--gold)">{place}</p>
{''.join(f'<p>{p}</p>' for p in paras)}
<ul class="benefits" style="columns:1">{st}</ul>
</div>'''

def retreats(lang):
    if lang == 'en':
        T = dict(intro1="For more than twenty years I have lived and studied in India and Thailand. Those lands shaped my path: the temples, the masters, the healers, the silence. Now I open those doors to small groups who want to live the journey from the inside.",
                 intro2="These are not tourist trips. They are pilgrimages of the soul: meditation in sacred places, encounters with living traditions, Quantum Transformation along the way, and time to integrate what opens.",
                 up="JUNE 2027", uph="Upcoming journeys", f_e="THAILAND · CHIANG MAI · JUNE 2027", f_t="A spiritual journey through the temples and sacred places of Northern Thailand", f_p="Temples of the Lanna tradition, mountains and waterfalls, meditation with the monks, and the healer Pakkapron, who has channeled the Medicine Buddha for more than thirty years. Places are limited.", f_dl="Download the journey guide",
                 th_e="THAILAND · JUNE 2027", th_t="Holistic retreat in Chiang Mai", th_p="Chiang Mai · Northern Thailand",
                 th=["In the mountains of northern Thailand, among Buddhist temples and forest, we live a holistic retreat of meditation, healing and inner silence.",
                     "One of the heart moments of this journey is our visit to Pakkapron, a very special healer from Chiang Mai who has channeled the Medicine Buddha for more than thirty years, offering healing, Dharma teaching and spiritual guidance. Being in her presence is an experience that stays with you."],
                 th_s=["Meditation in Buddhist temples", "Visit to Pakkapron, who has channeled the Medicine Buddha for more than 30 years", "Quantum Transformation sessions during the journey", "Thai healing traditions, nature and silence"],
                 in_e="INDIA · JUNE 2027", in_t="Pilgrimage to Northern India", in_p="Vrindavan · Mathura · Agra (Taj Mahal) · Jaipur",
                 ind=["A journey through the sacred sites of Northern India, to have a deep spiritual experience and connect with the energy these places have held for thousands of years.",
                      "Along the way we live the activation of the Light Codes: the sacred language of the Flame Codex, received in the places where the soul remembers."],
                 in_s=["Vrindavan and Mathura, the land of Krishna", "The Taj Mahal in Agra", "Jaipur, the pink city", "Temples, meditation and ceremonies in Northern India", "Activation of the Light Codes"],
                 past="WITH THE GROUPS", pasth="Our journeys to Thailand, 2025 and 2026", pastp="In 2025 and 2026 we travelled to Thailand with groups who lived this experience with us: the temples and sacred places of the north, the mountains and waterfalls, the hill-tribe villages, and the healer Pakkapron.",
                 pake="THE HEALER OF CHIANG MAI", pakp="Born in 1946 in the village of Namjum, in the hills of Chiang Mai, Pakkapron discovered her gift when a young girl suffering from seizures arrived at her door. Since then, for more than three decades, she has channeled the energy of the Medicine Buddha to heal, to teach the Dharma and to offer spiritual guidance, freely, to thousands of people from around the world.", pakcap="Dr. Zuluan Orion with Pakkapron in Chiang Mai.", g1="An incorruptible monk of Northern Thailand.", g2="Monks caring for the body of an incorruptible master.", gh="Our groups in Thailand, 2025 and 2026",
                 pdf="Spiritual_Journey_Thailand_EN.pdf", dl="DOWNLOAD THE THAILAND JOURNEY GUIDE (PDF)", dln="PDF · 9 MB",
                 cta="Places are limited. Call for more information and to reserve your place.", call="Call (954) 668-0348", mail="Write to us",
                 fc="The Light Codes that we activate on these journeys are born from the Flame Codex.", fcl="Discover the Flame Codex")
    else:
        T = dict(intro1="Durante más de veinte años he vivido y estudiado en la India y en Tailandia. Esas tierras formaron mi camino: los templos, los maestros, los sanadores, el silencio. Ahora abro esas puertas a grupos pequeños que quieren vivir el viaje desde adentro.",
                 intro2="No son viajes de turismo. Son peregrinaciones del alma: meditación en lugares sagrados, encuentros con tradiciones vivas, Transformación Cuántica en el camino, y tiempo para integrar lo que se abre.",
                 up="JUNIO 2027", uph="Próximos viajes", f_e="TAILANDIA · CHIANG MAI · JUNIO 2027", f_t="Un viaje espiritual por los templos y lugares sagrados del Norte de Tailandia", f_p="Templos de la tradición Lanna, montañas y cascadas, meditación con los monjes, y la sanadora Pakkapron, que canaliza al Buda de la Medicina desde hace más de treinta años. Cupos limitados.", f_dl="Descargar la guía del viaje",
                 th_e="TAILANDIA · JUNIO 2027", th_t="Retiro holístico en Chiang Mai", th_p="Chiang Mai · Norte de Tailandia",
                 th=["En las montañas del norte de Tailandia, entre templos budistas y bosque, vivimos un retiro holístico de meditación, sanación y silencio interior.",
                     "Uno de los momentos del corazón de este viaje es la visita a Pakkapron, una sanadora muy especial de Chiang Mai que canaliza al Buda de la Medicina desde hace más de treinta años, ofreciendo sanación, enseñanza del Dharma y guía espiritual. Estar en su presencia es una experiencia que se queda contigo."],
                 th_s=["Meditación en templos budistas", "Visita a Pakkapron, que canaliza al Buda de la Medicina desde hace más de 30 años", "Sesiones de Transformación Cuántica durante el viaje", "Tradiciones de sanación tailandesas, naturaleza y silencio"],
                 in_e="INDIA · JUNIO 2027", in_t="Peregrinación al Norte de la India", in_p="Vrindavan · Mathura · Agra (Taj Mahal) · Jaipur",
                 ind=["Un recorrido por los lugares sagrados del norte de la India, para tener una vivencia espiritual muy profunda y conectar con la energía que esos lugares han sostenido durante miles de años.",
                      "En el camino vivimos la activación de los Códigos de Luz: el lenguaje sagrado del Códice de la Llama, recibido en los lugares donde el alma recuerda."],
                 in_s=["Vrindavan y Mathura, la tierra de Krishna", "El Taj Mahal en Agra", "Jaipur, la ciudad rosa", "Templos, meditación y ceremonias en el norte de la India", "Activación de los Códigos de Luz"],
                 past="CON LOS GRUPOS", pasth="Nuestros viajes a Tailandia, 2025 y 2026", pastp="En 2025 y 2026 viajamos a Tailandia con grupos que vivieron esta experiencia con nosotros: los templos y lugares sagrados del norte, las montañas y cascadas, las aldeas de las montañas y la sanadora Pakkapron.",
                 pake="LA SANADORA DE CHIANG MAI", pakp="Nacida en 1946 en el pueblo de Namjum, en las montañas de Chiang Mai, Pakkapron descubrió su don cuando una niña que sufría convulsiones llegó a su puerta. Desde entonces, por más de tres décadas, canaliza la energía del Buda de la Medicina para sanar, enseñar el Dharma y ofrecer guía espiritual, sin costo, a miles de personas de todo el mundo.", pakcap="El Dr. Zuluan Orion con Pakkapron en Chiang Mai.", g1="Un monje incorrupto del Norte de Tailandia.", g2="Monjes cuidando el cuerpo de un maestro incorrupto.", gh="Nuestros grupos en Tailandia, 2025 y 2026",
                 pdf="Viaje_Espiritual_por_Tailandia.pdf", dl="DESCARGAR LA GUÍA DEL VIAJE A TAILANDIA (PDF)", dln="PDF · 18 MB",
                 cta="Los cupos son limitados. Llama para más información y para reservar tu lugar.", call="Llamar (954) 668-0348", mail="Escríbenos",
                 fc="Los Códigos de Luz que activamos en estos viajes nacen del Códice de la Llama.", fcl="Conoce el Códice de la Llama")
    return f'''<section class="ba" style="padding:0;text-align:left"><div style="position:relative">
<img src="/assets/img/viajes/grupo_01.jpg" alt="Wat Phra That Doi Suthep, Chiang Mai" style="width:100%;height:min(70vh,620px);object-fit:cover;object-position:center 35%;display:block;opacity:.5">
<div class="wrap" style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;max-width:1120px">
<p class="eyebrow" style="color:var(--gold2)">{T['f_e']}</p>
<h2 style="font-size:clamp(30px,5vw,54px);margin:0 0 12px">{T['f_t']}</h2>
<p style="font-size:clamp(18px,2.2vw,24px);max-width:640px;color:#F1E9FA">{T['f_p']}</p>
<p><a class="btn solid" href="tel:+19546680348">{T['call']}</a> <a class="btn" style="background:rgba(23,19,42,.5)" href="/assets/docs/{T['pdf']}" download>⬇ {T['f_dl']}</a></p>
</div></div></section>
<section><div class="narrow">
<p class="lead">{T['intro1']}</p>
<p>{T['intro2']}</p>
</div></section>
<section class="alt"><div class="wrap">
<p class="eyebrow center">{T['up']}</p><h2 class="center">{T['uph']}</h2>
<div class="grid2 top" style="margin-top:30px">
{trip(lang, T['th_e'], T['th_t'], T['th_p'], T['th'], T['th_s'])}
{trip(lang, T['in_e'], T['in_t'], T['in_p'], T['ind'], T['in_s'])}
</div>
<p class="center" style="margin-top:36px">{T['cta']}</p>
<p class="center"><a class="btn solid" href="tel:+19546680348">{T['call']}</a> <a class="btn" href="mailto:spiritualbalanceinfo@gmail.com">{T['mail']}</a></p>
</div></section>
<section><div class="wrap">
<p class="eyebrow center">{T['past']}</p><h2 class="center">{T['pasth']}</h2>
<p class="center" style="max-width:720px;margin:0 auto 30px">{T['pastp']}</p>
<div class="grid2" style="margin-bottom:40px">
<figure><img class="portrait" src="/assets/img/viajes/th_zuluan_pakkapron.jpg" alt="Dr. Zuluan Orion with Pakkapron" style="max-height:560px;width:auto;margin:0 auto"><figcaption>{T['pakcap']}</figcaption></figure>
<div><p class="eyebrow">{T['pake']}</p><h3 style="margin-top:4px">Pakkapron</h3><p>{T['pakp']}</p></div>
</div>
<div class="gallery tall" style="grid-template-columns:repeat(2,1fr);max-width:900px;margin:0 auto">
<figure><img src="/assets/img/viajes/th_monje_incorrupto.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{T['g1']}</figcaption></figure>
<figure><img src="/assets/img/viajes/th_monjes_vistiendo.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{T['g2']}</figcaption></figure>
</div>
<h3 class="center" style="margin-top:50px">{T['gh']}</h3>
<div class="gallery" style="margin-top:20px"><img src="/assets/img/viajes/grupo_01.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_02.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_03.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_04.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_05.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_06.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_07.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_08.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_10.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_11.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_12.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_13.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_14.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_15.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_16.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_18.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_19.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_20.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_21.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_22.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_23.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_24.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_25.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_26.jpg" alt="" loading="lazy"></div>
<div class="center" style="margin-top:40px"><a class="btn solid" style="font-size:16px;padding:18px 34px" href="/assets/docs/{T['pdf']}" download>⬇ {T['dl']}</a><p class="note" style="margin-top:12px">{T['dln']}</p></div>
</div></section>
<section class="dark"><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:180px;filter:drop-shadow(0 0 18px rgba(200,164,92,.35))">
<div><p>{T['fc']}</p><a class="btn" href="{url(lang,'codex')}">{T['fcl']}</a></div>
</div></section>
'''

# =================================================================== ENGLISH
E = BODY['en']

E[''] = hero('The Flame Codex', 'A sacred language of return and incarnation',
  'Light Codes for embodying the Flame — born of a nondual awakening and of a living descent of Consciousness into the human body.',
  sig=1, page=False, img='/assets/img/ahr_glow.webp',
  btns='<div class="sbcta"><p class="q">Looking for therapy or personal work?</p><a class="btn gold" href="https://www.spiritualbalanceinfo.com/">Visit Spiritual Balance &middot; Therapy &amp; personal sessions &#8599;</a><p class="a">If you are seeking the spiritual teaching, stay here and walk through the Codex.</p></div><div class="btns"><a class="btn solid" href="%s">The Descent</a><a class="btn" href="%s">Where this comes from</a></div>' % (url('en', 'descent'), url('en', 'about'))) + honors('en', ['award_aapna_ceremony.jpg', 'award_aapna_temple.jpg', 'award_siisdet.jpg', 'award_lifestyle.jpg']) + f'''
<section><div class="narrow center">
<p class="eyebrow">THE QUESTION</p>
<p class="lead">This work did not begin as a book. It began as a life — and a question that would not let go: <em>who is the one who looks?</em></p>
<p>The Flame Codex is the language that emerged when that question was answered, and when the answer began to descend into the body. It is not a system invented at a desk. It came after the experience, to name and accompany what was already happening.</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60,000+</b><span>hours of meditation</span></div>
<div><b>20+ years</b><span>living and studying in India and Thailand</span></div>
<div><b>~30 years</b><span>since the awakening to the Self</span></div>
<div><b>12,000+</b><span>people initiated into meditation</span></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid3">
<div class="card"><p class="eyebrow">I</p><h3>The Ground</h3><p>Everything rests on one recognition: Consciousness is not something we have. It is what we are. The nondual awakening is the foundation of all that follows.</p><a class="more" href="{url('en','ground')}">READ →</a></div>
<div class="card"><p class="eyebrow">II</p><h3>The Descent</h3><p>Awakening is the beginning, not the end. What was recognized above must come down — into the spine, the heart, the root, the feet, and ordinary life.</p><a class="more" href="{url('en','descent')}">READ →</a></div>
<div class="card"><p class="eyebrow">III</p><h3>The Flame Codex</h3><p>A sacred language of syllables, sigils and traces. From it come the Light Codes: the Codex applied to the mind, the heart, dreams and energy.</p><a class="more" href="{url('en','codex')}">READ →</a></div>
</div>
</div></section>

<section><div class="wrap grid2">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">THE AUTHOR</p>
<h2>Dr. Zuluan Orion</h2>
<p>Physician of Ayurveda and of natural and quantum medicine, meditation teacher and author. Born in Bogotá in 1971, formed by the great streams of Kriya Yoga, shaktipat, Vedic meditation, the Kalachakra and the direct nondual path of Ramana Maharshi and Papaji.</p>
<p>After an awakening to the Self nearly thirty years ago, and many years of practice, healing work and trial, a second movement began: the descent of the Flame. The Codex was born inside it.</p>
<p><a class="btn" href="{url('en','about')}">His story</a></p>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p class="eyebrow">THE ARC OF THE FLAME</p>
<div class="arc"><span>Consciousness</span><span class="s">✦</span><span>fire</span><span class="s">✦</span><span>purification</span><span class="s">✦</span><span>root</span><span class="s">✦</span><span>cool presence</span><span class="s">✦</span><span>love</span><span class="s">✦</span><span>service</span></div>
<blockquote style="border:0;padding:0">The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.</blockquote>
</div></section>

<section><div class="wrap grid2">
<figure><img class="portrait" src="/assets/img/books/transformacion_cuantica.webp" alt="Transformación Cuántica" style="max-height:420px;width:auto;margin:0 auto;border:0;box-shadow:none"></figure>
<div>
<p class="eyebrow">SPIRITUAL BALANCE · WESTON, FLORIDA</p>
<h2>Quantum Transformation, in person</h2>
<p>The Light Codes live inside the healing work I do in my clinic. Quantum Transformation is the system I created to guide the soul to purify itself, unblock its energy and reconnect with the Spirit, supported by Ayurveda, Panchakarma, Rasayana, bioresonance and biofeedback.</p>
<p><a class="btn solid" href="https://www.spiritualbalanceinfo.com/">Visit Spiritual Balance ↗</a></p>
</div>
</div></section>
<section class="dark"><div class="narrow center">
<p class="eyebrow">JOURNEYS &amp; RETREATS · JUNE 2027</p>
<h2>Living the Light Codes in the sacred lands</h2>
<p>Travel with me to Chiang Mai, Thailand, for a holistic retreat, and on a pilgrimage to Vrindavan, Mathura, the Taj Mahal and Jaipur in Northern India, where we live the activation of the Light Codes.</p>
<a class="btn solid" href="/journeys/">See the journeys</a>
</div></section>
'''

E['ground'] = hero('The Ground', 'The nondual awakening of Consciousness', sig=3) + f'''
<section><div class="narrow">
<p class="lead">Before any code, any sigil or any practice, there is one recognition. Everything else on this site rests on it.</p>
<p>For years I lived as if the mind were the centre of my life. The mind searched, argued, suffered, desired, feared, interpreted, defended and named. And then attention turned toward the one who was aware of the mind.</p>
<p>Something loosened. The mind was seen as movement. The witness was seen as stillness. The personal self was seen as a wave within a greater ocean. The wave had never been separate from the ocean; it had only been fascinated by its own form.</p>
<blockquote>What is this life? What is suffering?<br>Who is the one who suffers? Who is the one who looks?<br>And what remains when the one who looks is finally seen?</blockquote>
<h3>Not a belief</h3>
<p>This recognition is not a doctrine to accept or a philosophy to defend. It is direct. It is what the great nondual teachers — Ramana Maharshi, Papaji — point to with a single question: turn inward and discover who or what you truly are. Not as belief. Not as spiritual clothing. As recognition.</p>
<p>When it happened for me it was simple, almost comic. I laughed: <em>«It can't be that easy.»</em> In the days that followed the personality was seen for what it is: an event within Consciousness. That recognition has not reversed in nearly thirty years.</p>
<h3>Why it comes first</h3>
<p>The Flame Codex is built on this ground for one reason: the source of liberation is not the facilitator, not the code and not the method. The source is Consciousness itself. A wound does not heal because someone hands the person something. It frees itself because the person's own Consciousness recognizes what was false and returns to what was always true.</p>
<p>I describe my own realization as the recognition of the nonlocal essence of Consciousness through a finite form. Not the descent of a god, not the ascent of a superhuman. A finite human life in which the Infinite recognizes itself.</p>
<hr class="rule">
<p class="center">But recognition is not the whole movement. Knowing you are the ocean is not the same as every drop of the body being saturated by it.</p>
<p class="center"><a class="btn" href="{url('en','descent')}">Continue: The Descent</a></p>
</div></section>
'''

E['descent'] = hero('The Descent of the Flame', 'The Yoga of the Descent', sig=6) + f'''
<section><div class="narrow">
<p class="lead">For many years I thought awakening meant recognizing the truth of Consciousness — and it does. But a person can see the sky and still carry unpurified earth. The truth had been seen. The vessel still had to be transformed.</p>
<p>Then, after many years of the witness, of practice and of service, another movement began. Not the original awakening. Not a new philosophy. <strong>Descent.</strong></p>

<h3>Fusion</h3>
<p>A living Presence began to move within the body with force, precision and intelligence — as if Consciousness itself were entering incarnation more fully than before. It came first as fusion: wisdom, love, strength, devotion, silence, fire and human tenderness, which had lived separately in the psyche and the subtle body, began to braid into one movement. The path was no longer upward, inward or beyond. It turned downward, through, and here.</p>

<h3>The current comes down</h3>
<p>Then the descent proper. The current came down through the body as if realization were no longer willing to stay above the human instrument. It pressed down into the vessel. It entered the spine, the heart, the root, the limbs, the feet and the subtle field. It asked the body to take part.</p>

<h3>Fire</h3>
<p>Then came the heat. Heat as purification. Heat as pressure. Heat as inner fire. Real, physical, yogic heat rising through the spine, the legs, the back, the head — the friction between a new Presence and a body that did not yet know how to receive it. The fire exposed. The fire clarified. The fire consumed residues of fear, of identity, of resistance and contraction.</p>

<h3>Cool fire</h3>
<p>But the fire did not stay hot, and this was one of the most important recognitions of the whole path. Over time the heat began to cool. The fire did not disappear: it changed nature. What had been pressure became presence. What had moved as intensity began to move as cool fire.</p>
<blockquote>Cool fire is not coldness. It is not numbness. It is the same current of fire once it has stopped fighting and begun to hold. Fire without agitation. Power without violence. Bliss without escape.</blockquote>

<h3>The root</h3>
<p>The root became the anchor. A cool, steady presence at the base of the body, day and night — there in worry, in sadness, in doubt, and stronger in calm and in service. A realization that does not reach the root cannot live fully in the world. The root teaches realization to stay. The root teaches the soul to inhabit the body. The root teaches the fire to become human.</p>

<h3>The heart with two faces</h3>
<p>From the root the cool fire spread through the feet and the spine and opened the heart from the front and from the back: in front, tenderness, intimacy and compassion; behind, strength, depth and the capacity to hold without collapsing. Love stopped being only something felt toward someone. It became the atmosphere of presence. The crown stayed luminous, but stopped being the destination. The crown had to serve the heart; the heart, the root; the root, life.</p>
<blockquote>The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.</blockquote>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">THE ARC OF THE FLAME</p>
<h2>Not an escape from the human condition</h2>
<p>This is the movement I call the Arc of the Flame: Consciousness becomes fire, fire becomes purification, purification becomes rootedness, rootedness becomes cool presence, presence becomes love, and love becomes service.</p>
<p>The old spiritual imagination often looked upward — toward heaven, transcendence, special states, the mountaintop. The descent asks a harder and more beautiful question:</p>
<blockquote>Can the Infinite live through the ordinary?<br>Can the crown bow to the heart? Can the heart bow to the root?<br>Can realization become tenderness? Can fire become care?</blockquote>
<p>The divine descent is not a movement away from humanity. It is a movement into humanity: the sacred becoming ordinary without becoming less sacred; the body becoming a temple, not because it is perfect, but because it is inhabited.</p>
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">The year of the Incarnate Flame</h3>
<p>From 29 March 2025 to 26 January 2026 I lived, day by day, the year that became <em>La Llama Encarnada · The Incarnate Flame</em>. The process itself is set down in <em>Yoga del Descenso</em>, in three volumes: <em>Libro Puerta</em>, <em>Libro de la Morada</em> and <em>El Códice en el Cuerpo</em>.</p>
<h3>The Codex came after</h3>
<p>One precision protects everything else: the syllables did not cause the descent. The language emerged while the process was already happening and asked for a form able to name, distinguish and accompany what was being lived. That is why the Flame comes before the code. The Codex can prepare, orient and integrate the vessel; it does not manufacture Grace.</p>
<p class="center"><a class="btn" href="{url('en','codex')}">Continue: The Flame Codex</a></p>
</div></section>
'''

E['codex'] = hero('The Flame Codex', 'and its child, the Light Codes', sig=10) + f'''
<section><div class="narrow">
<p class="lead">The Flame Codex is a language of return. It is not a collection of random words, not a book of spells, not an attempt to command forces, and not a substitute for practice, medicine, therapy, prayer or moral responsibility.</p>
<p>Each code is a vessel. Each vessel gathers attention. Each movement of attention is held within presence. Each presence lets the soul meet a cage. And each cage, when it is truly seen, begins to lose its power. What emerges is not installed: it is discovered.</p>
<h3>How a code works</h3>
<p>A code does not act apart from the Consciousness that enters into relationship with it. The syllable offers sound; the sign offers form; the colour orients; intention gives direction; attention gathers; the body receives; presence gives life. As these meet, the code can become an inner key — a condensed form of meaning the person learns to recognize and to inhabit.</p>
<p>That is why the Codex must be approached with reverence. A word spoken without presence is only sound. A code used without humility is only technique. But held within Consciousness, love, humility and discernment, it becomes a door.</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="narrow" style="padding:0">
<p class="eyebrow">THE 33 CORE SYLLABLES</p>
<h2>Traced by hand, in one continuous line</h2>
<p>The Codex holds 177 keys. At its heart are 33 core syllables, each with its own sigil, its trace, its meditation plate and its poem. These are the traces of the 33 — drawn so that they can be followed by hand, without lifting the pen.</p>
</div>
{sigrid()}
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">The Light Codes</h3>
<p>The Light Codes are the child of the Flame Codex: the Codex applied to a human life. The syllables exist before any information arises; they give coherence to what manifests and realign it with the true intention of the Origin — which is one's own Consciousness.</p>
<p>Their purpose is to align the whole psyche toward one's own divinity, so that the Divine can descend into form and the Flame can be anchored in this world, flowering as love, presence and revealed intuition. They are applied, book by book, to the mind, the heart, dreams and energy, and to meditation.</p>
<h3>What the Codex is for</h3>
<blockquote>The stilling of what is agitated.<br>The seeing of what binds.<br>The softening of what contracted.<br>The release of what was never true.<br>The return of the soul to its own light.<br>The embodiment of that light in ordinary human life.</blockquote>
<h3>What it is not</h3>
<p>The facilitator is not the source. The code is not the source. The method is not the source. The work belongs to the soul, and the body has its own domain: this work can ease fear, shame, grief and despair, but it does not claim to treat illness, and it never replaces medical care. We open cages. We do not cut lifelines.</p>
<p class="center"><a class="btn" href="{url('en','books')}">The books</a></p>
</div></section>
'''

E['about'] = hero('Dr. Zuluan Orion', 'Where this teaching comes from', sig=2) + f'''
<section><div class="wrap grid2 top">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">IN SHORT</p>
<p class="lead">More than sixty thousand hours of meditation. More than two decades living and studying in India and Thailand. Initiation in Kriya Yoga, shaktipat, Vedic meditation and the Kalachakra. An awakening to the Self — <em>I Am That</em> — that has not reversed in nearly thirty years.</p>
<p>And then, much later, the descent: Consciousness entering the body as fire, then as cool fire, settling in the root. The Flame Codex and its Light Codes were born inside that descent. They did not cause it. They came after it, to name and accompany what was already happening.</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60,000+</b><span>hours of meditation</span></div>
<div><b>20+ years</b><span>in India and Thailand</span></div>
<div><b>12,000+</b><span>people initiated into meditation</span></div>
<div><b>20+ years</b><span>in Ayurvedic, natural and quantum medicine</span></div>
</div>
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">A life of practice</h3>
<p>This work did not begin as a book. It began as a life. I grew up in Bogotá in a hard home, and the void it left in my heart became the beginning of a spiritual path: I needed to find something, though I did not know what. For most of my life the central question was not academic. It was a wound and a fire.</p>
<p>I have sat in meditation for more than sixty thousand hours. I have lived and studied for more than twenty years in India and Thailand: yoga, meditation and Ayurvedic medicine in India, the Atharva Veda in New Delhi, the Kumbh Mela in Varanasi; Buddhism and healing in Thailand, with the monk Kruba Wom, beside the healer Me Pat, and in a long friendship with the monk Kruba Tuang. I have initiated more than twelve thousand people into meditation, and I have spent more than twenty years in healing rooms, seeing the same pattern again and again: what feels like reality itself turns out to be a cage — and beneath the cage something alive remains.</p>

<h3>The masters and the streams</h3>
<ul class="lineage">
<li><b>Ramana Maharshi and Papaji</b> — the direct nondual path: turn inward and discover what you truly are. Not as belief. As recognition.</li>
<li><b>Kriya Yoga</b> — through Lahiri Mahasaya, Sri Yukteswar, Paramahansa Yogananda and Paramahamsa Hariharananda, who initiated me and with whom I meditated for more than a year in his house in Kendall, Florida. <em>«Meditate, meditate, meditate and become aware of God.»</em></li>
<li><b>Vedic meditation</b> — through Bob Fickes, a teacher who became a brother and a friend.</li>
<li><b>Shaktipat</b> — through the living stream of Shri Dhyanyogi Madhusudandas: awakening as transmission, current and inner fire.</li>
<li><b>Kalachakra</b> — the empowerment of His Holiness the Dalai Lama.</li>
<li><b>Embodied awakening</b> — Saniel Bonder, Phil Servedio and Nick Arjuna Ardagh, in whose presence I awakened.</li>
<li><b>Sunburst</b> — Norman Paulsen, through the Sun Meditation, who refined my Kriya practice.</li>
</ul>
<p class="note">I name these streams with gratitude, not as a claim of endorsement. None of these teachers or traditions is responsible for the Flame Codex. They prepared the vessel. Life tested the vessel. The Flame emerged through the life that held them all.</p>

<h3>The awakening</h3>
<p>It opened in stages. On a night of meditation on the central stone of the Great Pyramid the kundalini rose along my spine, and a blue pearl in my chest kept asking <em>«Who am I?»</em> — and something within answered, every time, <em>«You are.»</em> Eight months later, in the most ordinary moment: <em>the mind has no being of its own.</em></p>
<p>Then I saw that my tireless search had built a new identity — the seeker — and I gave it up. I put away the books, took down the altars, went to work as an engineer and let everything rest. On my birthday, in a simple exercise at Arjuna's seminar, my heart opened into <em>I Am That</em>, and I laughed: <em>«It can't be that easy.»</em> One with everything, without separation. In the following days the personality was seen for what it is: an event within Consciousness.</p>
<p>That recognition was direct, complete and irreversible. It is the ground under everything on this site. But it was not the end. It was the beginning of incarnation.</p>

<h3>The vessel must be transformed</h3>
<p>The vessel was transformed through life: years in Asia, years of practice and healing work, and years of real trial — seasons that were neither peaceful nor luminous. Those years taught me that discernment is not optional, that spiritual power without humility is dangerous, and that the deepest service is not to make people believe in you, but to return them to their own light.</p>

<h3>The descent of the Flame</h3>
<p>Then, after many years of the witness, practice and service, the descent began: fusion, then real heat, then cool fire settling in the root, opening the heart front and back. This is what I call the Yoga of the Descent. <a href="{url('en','descent')}">Read the full account →</a></p>

<h3>What I do not claim</h3>
<p>I am not special. I am not chosen. I am a finite form through which the Divine is coming to know itself. The Codex is not for making anyone a master of the Flame; it is for returning each person to the light they never lost.</p>
<blockquote>The root is the throne. The heart is the love. The crown is the knowing.</blockquote>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid2 top">
<div>
<p class="eyebrow">MEDICINE</p>
<h2>Credentials</h2>
<table class="cred">
<tr><td>MD in Ayurveda (Vaidya Shiromani / Vachaspati)</td><td>India</td></tr>
<tr><td>Bachelor of Ayurvedic Medicine and Science (B.A.M.S.)</td><td>India</td></tr>
<tr><td>Ph.D. in Natural Medicine — World Organization of Natural Medicine</td><td>2014</td></tr>
<tr><td>Ph.D. in Quantum Medicine</td><td>2014</td></tr>
<tr><td>Doctorate in Humanitarian Services — World Organization of Natural Medicine</td><td>2013</td></tr>
<tr><td>Academic Council member — AAPNA, Association of Ayurvedic Professionals of North America</td><td></td></tr>
<tr><td>Member — NAMA, National Ayurvedic Medical Association</td><td></td></tr>
</table>
<p style="margin-top:20px">Private clinic in Weston, Florida, for two decades, integrating Ayurvedic, natural and quantum medicine, with patients from many countries.</p>
</div>
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion in prayer"></figure>
</div>
<h2 style="margin-top:60px">Recognition</h2>
<div class="awards">
<figure><img src="{I}award_aapna_ceremony.jpg" alt="AAPNA Dhanwantari Award ceremony" ><figcaption>Dhanwantari Award, AAPNA, 2025 — for integrating Ayurveda with contemporary science.</figcaption></figure>
<figure><img src="{I}award_aapna_temple.jpg" alt="With the AAPNA award before the temple" ><figcaption>AAPNA, 2025.</figcaption></figure>
<figure><img src="{I}award_siisdet.jpg" alt="Health Sciences Awards 2022" ><figcaption>Leader in Research and Health Sciences for the Benefit of Mankind, Health Sciences Awards, Santander, Spain, 2022.</figcaption></figure>
<figure><img src="{I}award_lifestyle.jpg" alt="Lifestyle Plus Magazine Awards" ><figcaption>Lifestyle Plus Magazine Awards.</figcaption></figure>
</div>
<h2 style="margin-top:60px">With Ayurvedic physicians</h2>
<p>Ayurveda is a living tradition, and I share it with Ayurvedic physicians from India.</p>
<figure style="max-width:720px;margin:26px 0"><img class="portrait" src="/assets/img/kerala_dr_reddy_kumar.jpg" alt="Studying Ayurvedic medicine with Dr. Reddy Kumar" loading="lazy"><figcaption>Studying Ayurvedic medicine beside Dr. Reddy Kumar, University of Kerala, India.</figcaption></figure>
<div class="gallery tall" style="grid-template-columns:repeat(3,1fr);max-width:1000px">
<figure><img src="/assets/img/with_dr_shekhar_annambhotla.jpg" alt="With Dr. Shekhar Annambhotla" loading="lazy"><figcaption>With Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_suresh_swarnapuri.jpg" alt="With Dr. Suresh Swarnapuri" loading="lazy"><figcaption>With Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_shan_lakshmanan.jpg" alt="With Dr. Shan Lakshmanan, Ph.D" loading="lazy"><figcaption>With Dr. Shan Lakshmanan, Ph.D.</figcaption></figure>
</div>
</div></section>
'''

def book(img, title, line, tag=''):
    top = f'<img src="{I}{img}" alt="{title}" >' if img else f'<div class="ph">{title}</div>'
    return f'<div class="book">{top}<div class="t">{f"<span class=tag>{tag}</span>" if tag else ""}<h4>{title}</h4><p>{line}</p></div></div>'

E['books'] = hero('Books', 'By Dr. Zuluan Orion', sig=12) + shelf('en')

E['contact'] = hero('Contact', 'Write to me', sig=18) + f'''
<section><div class="narrow center">
<p class="lead">For questions about the books, the Flame Codex, meditation or consultations:</p>
<p><a class="btn solid" href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a></p>
<hr class="rule">
<p><a href="https://www.instagram.com/drzuluanorion/">Instagram</a> · <a href="https://www.facebook.com/zuluanorion/">Facebook</a> · <a href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube</a></p>
<p>Sessions and clinic in Weston, Florida: <a href="https://www.spiritualbalanceinfo.com/">Spiritual Balance</a></p>
<p>Journeys and retreats to Thailand and India: <a href="/journeys/">Journeys</a></p>
<p>Clinic and medical practice: <a href="https://drzuluanorion.com/">drzuluanorion.com</a></p>
</div></section>
'''

# =================================================================== ESPAÑOL
X = BODY['es']

X[''] = hero('El Códice de la Llama', 'Un lenguaje sagrado de retorno y encarnación',
  'Códigos de Luz para encarnar la Llama — nacidos de un despertar no dual y de un descenso vivo de la Consciencia en el cuerpo humano.',
  sig=1, page=False, img='/assets/img/ahr_glow.webp',
  btns='<div class="sbcta"><p class="q">¿Buscas terapia o trabajo personal?</p><a class="btn gold" href="https://www.spiritualbalanceinfo.com/es/">Visita Spiritual Balance &middot; Terapias y trabajo personal &#8599;</a><p class="a">Si buscas la enseñanza espiritual, quédate aquí y recorre el Códice.</p></div><div class="btns"><a class="btn solid" href="%s">El Descenso</a><a class="btn" href="%s">De dónde viene esto</a></div>' % (url('es', 'descent'), url('es', 'about'))) + honors('es', ['award_aapna_ceremony.jpg', 'award_aapna_temple.jpg', 'award_siisdet.jpg', 'award_lifestyle.jpg']) + f'''
<section><div class="narrow center">
<p class="eyebrow">LA PREGUNTA</p>
<p class="lead">Esta obra no comenzó como un libro. Comenzó como una vida — y una pregunta que no me soltaba: <em>¿quién es el que mira?</em></p>
<p>El Códice de la Llama es el lenguaje que surgió cuando esa pregunta encontró respuesta, y cuando la respuesta empezó a descender al cuerpo. No es un sistema inventado en un escritorio. Vino después de la experiencia, para nombrar y acompañar lo que ya estaba ocurriendo.</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60.000+</b><span>horas de meditación</span></div>
<div><b>20+ años</b><span>viviendo y estudiando en la India y Tailandia</span></div>
<div><b>~30 años</b><span>desde el despertar al Ser</span></div>
<div><b>12.000+</b><span>personas iniciadas en meditación</span></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid3">
<div class="card"><p class="eyebrow">I</p><h3>El Fundamento</h3><p>Todo descansa en un solo reconocimiento: la Consciencia no es algo que tenemos. Es lo que somos. El despertar no dual es la base de todo lo que sigue.</p><a class="more" href="{url('es','ground')}">LEER →</a></div>
<div class="card"><p class="eyebrow">II</p><h3>El Descenso</h3><p>El despertar es el comienzo, no el final. Lo que fue reconocido arriba tiene que bajar — a la columna, al corazón, a la raíz, a los pies y a la vida ordinaria.</p><a class="more" href="{url('es','descent')}">LEER →</a></div>
<div class="card"><p class="eyebrow">III</p><h3>El Códice de la Llama</h3><p>Un lenguaje sagrado de sílabas, sigilos y trazos. De él nacen los Códigos de Luz: el Códice aplicado a la mente, el corazón, los sueños y la energía.</p><a class="more" href="{url('es','codex')}">LEER →</a></div>
</div>
</div></section>

<section><div class="wrap grid2">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">EL AUTOR</p>
<h2>Dr. Zuluan Orion</h2>
<p>Médico de Ayurveda y de medicina natural y cuántica, maestro de meditación y autor. Nacido en Bogotá en 1971, formado por las grandes corrientes del Kriya Yoga, el shaktipat, la meditación védica, el Kalachakra y el camino directo no dual de Ramana Maharshi y Papaji.</p>
<p>Después de un despertar al Ser hace casi treinta años, y de muchos años de práctica, de trabajo sanador y de prueba, comenzó un segundo movimiento: el descenso de la Llama. El Códice nació dentro de él.</p>
<p><a class="btn" href="{url('es','about')}">Su historia</a></p>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p class="eyebrow">EL ARCO DE LA LLAMA</p>
<div class="arc"><span>Consciencia</span><span class="s">✦</span><span>fuego</span><span class="s">✦</span><span>purificación</span><span class="s">✦</span><span>raíz</span><span class="s">✦</span><span>presencia fresca</span><span class="s">✦</span><span>amor</span><span class="s">✦</span><span>servicio</span></div>
<blockquote style="border:0;padding:0">La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.</blockquote>
</div></section>

<section><div class="wrap grid2">
<figure><img class="portrait" src="/assets/img/books/transformacion_cuantica.webp" alt="Transformación Cuántica" style="max-height:420px;width:auto;margin:0 auto;border:0;box-shadow:none"></figure>
<div>
<p class="eyebrow">SPIRITUAL BALANCE · WESTON, FLORIDA</p>
<h2>La Transformación Cuántica, en persona</h2>
<p>Los Códigos de Luz viven dentro del trabajo de sanación que hago en mi clínica. La Transformación Cuántica es el sistema que creé para guiar al alma a depurarse, desbloquear su energía y reconectar con el Espíritu, con el apoyo de la Ayurveda, el Panchakarma, el Rasayana, la biorresonancia y el biofeedback.</p>
<p><a class="btn solid" href="https://www.spiritualbalanceinfo.com/es/">Visita Spiritual Balance ↗</a></p>
</div>
</div></section>
<section class="dark"><div class="narrow center">
<p class="eyebrow">VIAJES Y RETIROS · JUNIO 2027</p>
<h2>Vivir los Códigos de Luz en las tierras sagradas</h2>
<p>Viaja conmigo a Chiang Mai, Tailandia, para un retiro holístico, y en peregrinación a Vrindavan, Mathura, el Taj Mahal y Jaipur en el norte de la India, donde vivimos la activación de los Códigos de Luz.</p>
<a class="btn solid" href="/es/journeys/">Ver los viajes</a>
</div></section>
'''

X['ground'] = hero('El Fundamento', 'El despertar no dual de la Consciencia', sig=3) + f'''
<section><div class="narrow">
<p class="lead">Antes de cualquier código, de cualquier sigilo o de cualquier práctica, hay un reconocimiento. Todo lo demás en este sitio descansa sobre él.</p>
<p>Durante años viví como si la mente fuera el centro de mi vida. La mente buscaba, discutía, sufría, deseaba, temía, interpretaba, defendía, nombraba. Y entonces la atención se volvió hacia aquel que era consciente de la mente.</p>
<p>Algo se aflojó. La mente fue vista como movimiento. El testigo fue visto como quietud. El yo personal fue visto como una ola dentro de un océano mayor. La ola nunca había estado separada del océano; solo había estado fascinada con su propia forma.</p>
<blockquote>¿Qué es esta vida? ¿Qué es el sufrimiento?<br>¿Quién es el que sufre? ¿Quién es el que mira?<br>¿Y qué permanece cuando aquel que mira es por fin visto?</blockquote>
<h3>No es una creencia</h3>
<p>Este reconocimiento no es una doctrina que aceptar ni una filosofía que defender. Es directo. Es aquello a lo que apuntan los grandes maestros no duales — Ramana Maharshi, Papaji — con una sola pregunta: vuelve hacia adentro y descubre quién o qué eres en verdad. No como creencia. No como vestidura espiritual. Como reconocimiento.</p>
<p>Cuando me ocurrió fue sencillo, casi cómico. Me reí: <em>«No puede ser tan fácil.»</em> En los días que siguieron la personalidad fue vista como lo que es: un acontecimiento dentro de la Consciencia. Ese reconocimiento no se ha revertido en casi treinta años.</p>
<h3>Por qué va primero</h3>
<p>El Códice de la Llama se construye sobre este fundamento por una razón: la fuente de la liberación no es el facilitador, no es el código y no es el método. La fuente es la Consciencia misma. La herida no sana porque alguien le entregue algo a la persona. Se libera porque la propia Consciencia de la persona reconoce lo que era falso y regresa a lo que siempre fue verdadero.</p>
<p>Describo mi propia realización como el reconocimiento de la esencia no local de la Consciencia a través de una forma finita. No el descenso de un dios, ni el ascenso de un superhombre. Una vida humana finita en la que el Infinito se reconoce a sí mismo.</p>
<hr class="rule">
<p class="center">Pero el reconocimiento no es el movimiento entero. Saber que eres el océano no es lo mismo que cada gota del cuerpo quede saturada de él.</p>
<p class="center"><a class="btn" href="{url('es','descent')}">Continúa: El Descenso</a></p>
</div></section>
'''

X['descent'] = hero('El Descenso de la Llama', 'La Yoga del Descenso', sig=6) + f'''
<section><div class="narrow">
<p class="lead">Durante muchos años pensé que despertar significaba reconocer la verdad de la Consciencia — y lo significa. Pero un ser humano puede ver el cielo y aún cargar tierra sin purificar. La verdad había sido vista. La vasija todavía tenía que ser transformada.</p>
<p>Entonces, después de muchos años de testigo, de práctica y de servicio, comenzó otro movimiento. No fue el despertar original. No fue una nueva filosofía. Fue <strong>descenso</strong>.</p>

<h3>Fusión</h3>
<p>Una presencia viva comenzó a moverse dentro del cuerpo con fuerza, precisión e inteligencia — como si la Consciencia misma estuviera entrando en la encarnación más plenamente que antes. Al principio llegó como fusión: sabiduría, amor, fuerza, devoción, silencio, fuego y ternura humana, que habían vivido separados en la psique y en el cuerpo sutil, comenzaron a trenzarse en un solo movimiento. El camino ya no era hacia arriba, hacia adentro o más allá. Se volvió hacia abajo, a través y aquí.</p>

<h3>La corriente baja</h3>
<p>Luego vino el descenso propiamente dicho. La corriente bajó por el cuerpo como si la realización ya no estuviera dispuesta a permanecer por encima del instrumento humano. Presionó hacia abajo, dentro de la vasija. Entró en la columna, el corazón, la raíz, las extremidades, los pies y el campo sutil. Le pidió al cuerpo que participara.</p>

<h3>El fuego</h3>
<p>Luego vino el calor. Calor como purificación. Calor como presión. Calor como fuego interior. Un calor real, físico, yóguico, subiendo por la columna, las piernas, la espalda, la cabeza — la fricción entre una Presencia nueva y un cuerpo que todavía no sabía recibirla. El fuego expuso. El fuego clarificó. El fuego consumió residuos de miedo, de identidad, de resistencia y de contracción.</p>

<h3>El fuego frío</h3>
<p>Pero el fuego no permaneció caliente, y este fue uno de los reconocimientos más importantes de todo el camino. Con el tiempo, el calor empezó a enfriarse. El fuego no desapareció: cambió de naturaleza. Lo que antes era presión se volvió presencia. Lo que se movía como intensidad comenzó a moverse como fuego frío.</p>
<blockquote>El fuego frío no es frialdad. No es entumecimiento. Es la misma corriente del fuego una vez que ha dejado de combatir y ha empezado a sostener. Fuego sin agitación. Poder sin violencia. Dicha sin escape.</blockquote>

<h3>La raíz</h3>
<p>La raíz se volvió el ancla. Una presencia fresca y estable en la base del cuerpo, de día y de noche — presente en la preocupación, en la tristeza, en la duda, y más fuerte en la calma y en el servicio. Una realización que no llega a la raíz no puede vivir plenamente en el mundo. La raíz le enseña a la realización a permanecer. La raíz le enseña al alma a habitar el cuerpo. La raíz le enseña al fuego a volverse humano.</p>

<h3>El corazón de dos rostros</h3>
<p>Desde la raíz, el fuego frío se extendió por los pies y la columna y abrió el corazón desde el frente y desde la espalda: al frente, ternura, intimidad y compasión; detrás, fuerza, profundidad y capacidad de sostener sin colapsar. El amor dejó de ser solo algo sentido hacia alguien. Se volvió la atmósfera misma de la presencia. La corona permaneció luminosa, pero dejó de ser el destino. La corona tenía que servir al corazón; el corazón, a la raíz; la raíz, a la vida.</p>
<blockquote>La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.</blockquote>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">EL ARCO DE LA LLAMA</p>
<h2>No es un escape de la condición humana</h2>
<p>Este es el movimiento que llamo el Arco de la Llama: la Consciencia se vuelve fuego, el fuego se vuelve purificación, la purificación se vuelve arraigo, el arraigo se vuelve presencia fresca, la presencia se vuelve amor y el amor se vuelve servicio.</p>
<p>La antigua imaginación espiritual miraba a menudo hacia arriba — hacia el cielo, la trascendencia, los estados especiales, la cima de la montaña. El descenso hace una pregunta más difícil y más hermosa:</p>
<blockquote>¿Puede el Infinito vivir a través de lo ordinario?<br>¿Puede la corona inclinarse ante el corazón? ¿Puede el corazón inclinarse ante la raíz?<br>¿Puede la realización volverse ternura? ¿Puede el fuego volverse cuidado?</blockquote>
<p>El descenso divino no es un movimiento que aleja de la humanidad: es un movimiento que entra en la humanidad. Es lo sagrado volviéndose ordinario sin volverse menos sagrado; el cuerpo volviéndose templo, no porque sea perfecto, sino porque está habitado.</p>
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">El año de la Llama Encarnada</h3>
<p>Del 29 de marzo de 2025 al 26 de enero de 2026 viví, día a día, el año que se convirtió en <em>La Llama Encarnada</em>. El proceso mismo está escrito en <em>Yoga del Descenso</em>, en tres volúmenes: <em>Libro Puerta</em>, <em>Libro de la Morada</em> y <em>El Códice en el Cuerpo</em>.</p>
<h3>El Códice vino después</h3>
<p>Una precisión protege todo lo demás: las sílabas no causaron el Descenso. El lenguaje emergió cuando el proceso ya estaba ocurriendo y pidió una forma capaz de nombrar, diferenciar y acompañar lo que se estaba viviendo. Por eso la Llama precede al código. El Códice puede preparar, orientar e integrar la vasija; no fabrica la Gracia.</p>
<p class="center"><a class="btn" href="{url('es','codex')}">Continúa: El Códice de la Llama</a></p>
</div></section>
'''

X['codex'] = hero('El Códice de la Llama', 'y su hijo, los Códigos de Luz', sig=10) + f'''
<section><div class="narrow">
<p class="lead">El Códice de la Llama es un lenguaje de retorno. No es una colección de palabras al azar, no es un libro de hechizos, no es un intento de mandar sobre las fuerzas, y no es un sustituto de la práctica, la medicina, la terapia, la oración o la responsabilidad moral.</p>
<p>Cada código es una vasija. Cada vasija reúne la atención. Cada movimiento de atención se sostiene dentro de la presencia. Cada presencia le permite al alma encontrar una jaula. Y cada jaula, cuando es vista de verdad, empieza a perder su poder. Lo que emerge no se instala: se descubre.</p>
<h3>Cómo actúa un código</h3>
<p>Un código no actúa separado de la Consciencia que entra en relación con él. La sílaba ofrece sonido; el signo ofrece forma; el color orienta; la intención da dirección; la atención reúne; el cuerpo recibe; la presencia vivifica. A medida que estos elementos se encuentran, el código puede convertirse en una llave interior: una forma condensada de significado que la persona aprende a reconocer y a habitar.</p>
<p>Por eso el Códice debe abordarse con reverencia. Una palabra pronunciada sin presencia es solo sonido. Un código usado sin humildad es solo técnica. Pero sostenido dentro de la Consciencia, el amor, la humildad y el discernimiento, se vuelve una puerta.</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="narrow" style="padding:0">
<p class="eyebrow">LAS 33 SÍLABAS NUCLEARES</p>
<h2>Trazadas a mano, en una sola línea</h2>
<p>El Códice reúne 177 llaves. En su corazón están las 33 sílabas nucleares, cada una con su sigilo, su trazo, su lámina de meditación y su poema. Estos son los trazos de las 33 — dibujados para poder seguirse a mano, sin levantar la pluma.</p>
</div>
{sigrid()}
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">Los Códigos de Luz</h3>
<p>Los Códigos de Luz son hijos del Códice de la Llama: el Códice aplicado a una vida humana. Las sílabas existen antes de que surja cualquier información; dan coherencia a lo que se manifiesta y lo realinean con la verdadera intención del Origen — que es la propia Consciencia.</p>
<p>Su propósito es alinear toda la psique hacia la propia divinidad, para que lo Divino pueda descender a la forma y la Llama pueda anclarse en este mundo, floreciendo como amor, presencia e intuición revelada. Se aplican, libro por libro, a la mente, al corazón, a los sueños, a la energía y a la meditación.</p>
<h3>Para qué existe el Códice</h3>
<blockquote>La quietud de lo que se agita.<br>La visión de lo que ata.<br>El suavizamiento de lo que se contrajo.<br>La liberación de lo que nunca fue verdadero.<br>El retorno del alma a su propia luz.<br>La encarnación de esa luz en la vida humana ordinaria.</blockquote>
<h3>Lo que no es</h3>
<p>El facilitador no es la fuente. El código no es la fuente. El método no es la fuente. El trabajo pertenece al alma, y el cuerpo tiene su propio dominio: este trabajo puede aliviar el miedo, la vergüenza, el duelo y la desesperación, pero no pretende tratar enfermedades y nunca reemplaza la atención médica. Abrimos jaulas. No cortamos líneas de vida.</p>
<p class="center"><a class="btn" href="{url('es','books')}">Los libros</a></p>
</div></section>
'''

X['about'] = hero('Dr. Zuluan Orion', 'De dónde viene esta enseñanza', sig=2) + f'''
<section><div class="wrap grid2 top">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">EN POCAS PALABRAS</p>
<p class="lead">Más de sesenta mil horas de meditación. Más de dos décadas viviendo y estudiando en la India y Tailandia. Iniciación en Kriya Yoga, shaktipat, meditación védica y Kalachakra. Un despertar al Ser — <em>Yo Soy Eso</em> — que no se ha revertido en casi treinta años.</p>
<p>Y después, mucho más tarde, el descenso: la Consciencia entrando en el cuerpo como fuego, luego como fuego frío, asentándose en la raíz. El Códice de la Llama y sus Códigos de Luz nacieron dentro de ese descenso. No lo causaron. Vinieron después, para nombrar y acompañar lo que ya estaba ocurriendo.</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60.000+</b><span>horas de meditación</span></div>
<div><b>20+ años</b><span>en la India y Tailandia</span></div>
<div><b>12.000+</b><span>personas iniciadas en meditación</span></div>
<div><b>20+ años</b><span>en medicina ayurvédica, natural y cuántica</span></div>
</div>
</div></section>

<section><div class="narrow">
<h3 style="margin-top:0">Una vida de práctica</h3>
<p>Esta obra no comenzó como un libro. Comenzó como una vida. Crecí en Bogotá en un hogar difícil, y el vacío que dejó en mi corazón se convirtió en el comienzo de un camino espiritual: necesitaba encontrar algo, aunque no sabía qué. Durante la mayor parte de mi vida la pregunta central no fue académica. Fue una herida y un fuego.</p>
<p>He meditado más de sesenta mil horas. He vivido y estudiado más de veinte años en la India y Tailandia: yoga, meditación y medicina ayurvédica en la India, el Atharva Veda en Nueva Delhi, la Kumbh Mela en Varanasi; budismo y sanación en Tailandia, con el monje Kruba Wom, junto a la sanadora Me Pat, y en una larga amistad con el monje Kruba Tuang. He iniciado en meditación a más de doce mil personas, y llevo más de veinte años en salas de sanación, viendo el mismo patrón una y otra vez: lo que se siente como la realidad misma resulta ser una jaula — y debajo de la jaula, algo vivo permanece.</p>

<h3>Los maestros y las corrientes</h3>
<ul class="lineage">
<li><b>Ramana Maharshi y Papaji</b> — el camino directo no dual: vuelve hacia adentro y descubre lo que eres en verdad. No como creencia. Como reconocimiento.</li>
<li><b>Kriya Yoga</b> — a través de Lahiri Mahasaya, Sri Yukteswar, Paramahansa Yogananda y Paramahamsa Hariharananda, quien me inició y con quien medité durante más de un año en su casa de Kendall, Florida. <em>«Medita, medita, medita y toma consciencia de Dios.»</em></li>
<li><b>Meditación védica</b> — a través de Bob Fickes, un maestro que llegó a ser hermano y amigo.</li>
<li><b>Shaktipat</b> — a través de la corriente viva de Shri Dhyanyogi Madhusudandas: el despertar como transmisión, corriente y fuego interior.</li>
<li><b>Kalachakra</b> — la iniciación de Su Santidad el Dalai Lama.</li>
<li><b>Despertar encarnado</b> — Saniel Bonder, Phil Servedio y Nick Arjuna Ardagh, en cuya presencia desperté.</li>
<li><b>Sunburst</b> — Norman Paulsen, a través de la Meditación del Sol, quien refinó mi práctica de Kriya.</li>
</ul>
<p class="note">Nombro estas corrientes con gratitud, no como una afirmación de respaldo. Ninguno de estos maestros ni de estas tradiciones es responsable del Códice de la Llama. Prepararon la vasija. La vida puso a prueba la vasija. La Llama emergió a través de la vida que las sostuvo a todas.</p>

<h3>El despertar</h3>
<p>Se abrió por etapas. Una noche de meditación sobre la piedra central de la Gran Pirámide, la kundalini subió por mi columna, y una perla azul en mi pecho preguntaba una y otra vez <em>«¿Quién soy yo?»</em> — y algo dentro respondía, cada vez, <em>«Tú eres.»</em> Ocho meses después, en el momento más ordinario: <em>la mente no tiene ser propio.</em></p>
<p>Entonces vi que mi búsqueda incansable había construido una nueva identidad — el buscador — y la dejé. Guardé los libros, desmonté los altares, me fui a trabajar como ingeniero y dejé que todo descansara. El día de mi cumpleaños, en un ejercicio sencillo en el seminario de Arjuna, mi corazón se abrió al <em>Yo Soy Eso</em>, y me reí: <em>«No puede ser tan fácil.»</em> Uno con todo, sin separación. En los días siguientes la personalidad fue vista como lo que es: un acontecimiento dentro de la Consciencia.</p>
<p>Ese reconocimiento fue directo, completo e irreversible. Es el fundamento de todo lo que hay en este sitio. Pero no fue el final. Fue el comienzo de la encarnación.</p>

<h3>La vasija debe transformarse</h3>
<p>La vasija se transformó a través de la vida: años en Asia, años de práctica y de trabajo sanador, y años de prueba real — temporadas que no fueron pacíficas ni luminosas. Esos años me enseñaron que el discernimiento no es opcional, que el poder espiritual sin humildad es peligroso, y que el servicio más hondo no consiste en lograr que las personas crean en ti, sino en devolverlas a su propia luz.</p>

<h3>El descenso de la Llama</h3>
<p>Luego, después de muchos años de testigo, práctica y servicio, comenzó el descenso: fusión, luego calor real, luego el fuego frío asentándose en la raíz y abriendo el corazón por delante y por detrás. Esto es lo que llamo la Yoga del Descenso. <a href="{url('es','descent')}">Lee el relato completo →</a></p>

<h3>Lo que no afirmo</h3>
<p>No soy especial. No soy elegido. Soy una forma finita a través de la cual lo Divino se está conociendo. El Códice no existe para convertir a nadie en dueño de la Llama; existe para devolver a cada persona a la luz que nunca perdió.</p>
<blockquote>La raíz es el trono. El corazón es el amor. La corona es el saber.</blockquote>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid2 top">
<div>
<p class="eyebrow">MEDICINA</p>
<h2>Formación</h2>
<table class="cred">
<tr><td>MD en Ayurveda (Vaidya Shiromani / Vachaspati)</td><td>India</td></tr>
<tr><td>Licenciatura en Medicina y Ciencia Ayurvédica (B.A.M.S.)</td><td>India</td></tr>
<tr><td>Ph.D. en Medicina Natural — World Organization of Natural Medicine</td><td>2014</td></tr>
<tr><td>Ph.D. en Medicina Cuántica</td><td>2014</td></tr>
<tr><td>Doctorado en Servicios Humanitarios — World Organization of Natural Medicine</td><td>2013</td></tr>
<tr><td>Miembro del Consejo Académico — AAPNA, Association of Ayurvedic Professionals of North America</td><td></td></tr>
<tr><td>Miembro — NAMA, National Ayurvedic Medical Association</td><td></td></tr>
</table>
<p style="margin-top:20px">Consulta privada en Weston, Florida, desde hace dos décadas, integrando medicina ayurvédica, natural y cuántica, con pacientes de muchos países.</p>
</div>
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion en oración"></figure>
</div>
<h2 style="margin-top:60px">Reconocimientos</h2>
<div class="awards">
<figure><img src="{I}award_aapna_ceremony.jpg" alt="Ceremonia del Premio Dhanwantari de AAPNA" ><figcaption>Premio Dhanwantari, AAPNA, 2025 — por integrar el Ayurveda con la ciencia contemporánea.</figcaption></figure>
<figure><img src="{I}award_aapna_temple.jpg" alt="Con el premio de AAPNA frente al templo" ><figcaption>AAPNA, 2025.</figcaption></figure>
<figure><img src="{I}award_siisdet.jpg" alt="Health Sciences Awards 2022" ><figcaption>Líder en Investigación y Ciencias de la Salud en Beneficio de la Humanidad, Premios Ciencias de la Salud, Santander, España, 2022.</figcaption></figure>
<figure><img src="{I}award_lifestyle.jpg" alt="Lifestyle Plus Magazine Awards" ><figcaption>Lifestyle Plus Magazine Awards.</figcaption></figure>
</div>
<h2 style="margin-top:60px">Con médicos ayurvédicos</h2>
<p>La Ayurveda es una tradición viva, y la comparto con médicos ayurvédicos de la India.</p>
<figure style="max-width:720px;margin:26px 0"><img class="portrait" src="/assets/img/kerala_dr_reddy_kumar.jpg" alt="Estudiando medicina ayurvédica con el Dr. Reddy Kumar" loading="lazy"><figcaption>Estudiando medicina ayurvédica al lado del Dr. Reddy Kumar, Universidad de Kerala, India.</figcaption></figure>
<div class="gallery tall" style="grid-template-columns:repeat(3,1fr);max-width:1000px">
<figure><img src="/assets/img/with_dr_shekhar_annambhotla.jpg" alt="Con el Dr. Shekhar Annambhotla" loading="lazy"><figcaption>Con el Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_suresh_swarnapuri.jpg" alt="Con el Dr. Suresh Swarnapuri" loading="lazy"><figcaption>Con el Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_shan_lakshmanan.jpg" alt="Con el Dr. Shan Lakshmanan, Ph.D" loading="lazy"><figcaption>Con el Dr. Shan Lakshmanan, Ph.D.</figcaption></figure>
</div>
</div></section>
'''

X['books'] = hero('Libros', 'Del Dr. Zuluan Orion', sig=12) + shelf('es')

X['contact'] = hero('Contacto', 'Escríbeme', sig=18) + f'''
<section><div class="narrow center">
<p class="lead">Para preguntas sobre los libros, el Códice de la Llama, la meditación o las consultas:</p>
<p><a class="btn solid" href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a></p>
<hr class="rule">
<p><a href="https://www.instagram.com/drzuluanorion/">Instagram</a> · <a href="https://www.facebook.com/zuluanorion/">Facebook</a> · <a href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube</a></p>
<p>Sesiones y clínica en Weston, Florida: <a href="https://www.spiritualbalanceinfo.com/es/">Spiritual Balance</a></p>
<p>Viajes y retiros a Tailandia y la India: <a href="/es/journeys/">Viajes</a></p>
<p>Consulta y práctica médica: <a href="https://drzuluanorion.com/">drzuluanorion.com</a></p>
</div></section>
'''

E['journeys'] = hero('Holistic Journeys', 'Thailand and India with Dr. Zuluan Orion', sig=10) + retreats('en')
X['journeys'] = hero('Viajes Holísticos', 'Tailandia e India con el Dr. Zuluan Orion', sig=10) + retreats('es')


# ---- The Flame Codex page, rebuilt from the base document (Oct 2026)
from codex import codex_page
from meditation import meditation_page, subnav
E['codex'] = hero('The Flame Codex', 'A sacred language of return and incarnation', sig=10) + codex_page('en', url, S, sigrid, subnav('en', url, 'codex'))
X['codex'] = hero('El Códice de la Llama', 'Un lenguaje sagrado de retorno y encarnación', sig=10) + codex_page('es', url, S, sigrid, subnav('es', url, 'codex'))
E['codex/meditation'] = hero('Light Code Meditation', 'A meeting of sound, contemplation and presence', sig=1) + meditation_page('en', url)
X['codex/meditation'] = hero('Meditación de Códigos de Luz', 'Un encuentro entre sonido, contemplación y presencia', sig=1) + meditation_page('es', url)

from illumination import illumination_page
E['codex/illumination'] = hero('Illumination', 'The nondual teaching', sig=3) + illumination_page('en', url, subnav('en', url, 'codex/illumination'))
X['codex/illumination'] = hero('Iluminación', 'La enseñanza no dual', sig=3) + illumination_page('es', url, subnav('es', url, 'codex/illumination'))

# ---- The Descent page, rebuilt around Zuluan's text «El Descenso de la Llama» (Oct 2026)
from descent import descent_page
E['descent'] = hero('The Descent of the Flame', 'From the realization of consciousness to incarnation', sig=6) + descent_page('en', url)
X['descent'] = hero('El Descenso de la Llama', 'De la realización de la consciencia a la encarnación', sig=6) + descent_page('es', url)


# ---- Codex only (Oct 2026): the person lives on drzuluanorion.org, the clinic on spiritualbalanceinfo.com
from fc_new import home_page, retreats_page, books_page, contact_page
for _lang, _B in (('en', E), ('es', X)):
    _B[''] = home_page(_lang, url, hero)
    _B['retreats'] = retreats_page(_lang, url, hero)
    _B['books'] = books_page(_lang, url, hero)
    _B['contact'] = contact_page(_lang, url, hero)
