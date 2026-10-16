# -*- coding: utf-8 -*-
"""Illumination — the nondual teaching, a tab inside the Flame Codex section (EN/ES). Text by Zuluan."""

def illumination_page(lang, url, subnav):
    en = lang == 'en'
    L = lambda e, s: e if en else s
    I = '/assets/img/'
    return f'''{subnav}
<section><div class="narrow center">
<p class="eyebrow">{L('ILLUMINATION · THE NONDUAL TEACHING', 'ILUMINACIÓN · LA ENSEÑANZA NO DUAL')}</p>
<p class="lead">{L('The teaching I share in <em>Illumination</em> is born of a very intimate question:', 'La enseñanza que comparto en <em>Iluminación</em> nace de una pregunta muy íntima:')}</p>
<blockquote style="font-size:1.35em">{L('Who am I, beyond everything<br>I have learned to think about myself?', '¿Quién soy, más allá de todo<br>lo que he aprendido a pensar sobre mí?')}</blockquote>
</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img class="portrait" src="{I}portrait_front.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">{L('SELF-KNOWLEDGE', 'AUTOCONOCIMIENTO')}</p>
<h2>{L('The presence that observes', 'La presencia que observa')}</h2>
<p>{L('Self-knowledge begins when we stop to look and recognize that our thoughts, emotions and stories change, while there is a conscious presence that can observe them.', 'El autoconocimiento comienza cuando nos detenemos a mirar y reconocemos que nuestros pensamientos, emociones e historias cambian, mientras hay una presencia consciente que puede observarlos.')}</p>
<p>{L('I invite you to become familiar with that presence, to discover it in your own experience. That recognition can begin right here, in the middle of your life, with your questions, your difficulties and your humanity.', 'Te invito a familiarizarte con esa presencia, a descubrirla en tu propia experiencia. Ese reconocimiento puede comenzar aquí mismo, en medio de tu vida, con tus preguntas, tus dificultades y tu humanidad.')}</p>
</div>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">{L('NONDUALITY', 'NO DUALIDAD')}</p>
<h2>{L('One same reality', 'Una misma realidad')}</h2>
<p>{L('As that relationship deepens, nonduality begins to take on a living meaning: the consciousness you recognize in yourself and the life you meet in others share in one same reality.', 'Al profundizar en esa relación, la no dualidad comienza a cobrar un sentido vivo: la consciencia que reconoces en ti y la vida que encuentras en los demás participan de una misma realidad.')}</p>
<p>{L('For me, this discovery opened a deeply loving relationship with God, with the Self, with what sustains us from within. That intimacy also becomes devotion, gratitude and a more sensitive way of being in the world.', 'Para mí, este descubrimiento abrió una relación profundamente amorosa con Dios, con el Ser, con aquello que nos sostiene desde dentro. Esa intimidad también se vuelve devoción, gratitud y una manera más sensible de estar en el mundo.')}</p>
<blockquote>{L('Awakening goes on maturing in how we live,<br>in how we pass through pain, listen to another person,<br>and allow love to find expression in everyday life.', 'El despertar continúa madurando en cómo vivimos,<br>en cómo atravesamos el dolor, escuchamos a otra persona<br>y permitimos que el amor encuentre expresión en lo cotidiano.')}</blockquote>
</div></section>

<section><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('MEETING IN TRUTH AND SILENCE', 'ENCUENTRO EN VERDAD Y SILENCIO')}</p>
<h2>Satsang &amp; Darshan</h2>
</div>
<div class="grid2 cards4">
<div class="card"><p class="eyebrow">SATSANG</p><h3>{L('Exploring together', 'Explorar juntos')}</h3><p>{L('The meeting in which we explore together the truth of what we are.', 'El encuentro para explorar juntos la verdad de lo que somos.')}</p></div>
<div class="card"><p class="eyebrow">DARSHAN</p><h3>{L('Presence and silence', 'Presencia y silencio')}</h3><p>{L('A contemplative meeting where presence and silence have their place.', 'El encuentro contemplativo donde la presencia y el silencio tienen su lugar.')}</p></div>
</div>
<div class="narrow" style="padding:0">
<p>{L('That is why I value them so much. The company of someone who has recognized their own nature can help us discover, more simply, what we are still seeking. On my own path, sharing with beings who had awakened was a blessing: sometimes a question, a glance or a moment of silence allowed something to become evident.', 'Por eso valoro tanto el satsang y el darshan. La compañía de alguien que ha reconocido su propia naturaleza puede ayudarnos a descubrir con más sencillez aquello que todavía buscamos. En mi camino, compartir con seres que habían despertado fue una bendición: a veces una pregunta, una mirada o un momento de silencio permitió que algo se hiciera evidente.')}</p>
<p>{L('Such accompaniment has value when it returns us to our own experience and strengthens our inner freedom.', 'Ese acompañamiento tiene valor cuando nos devuelve a nuestra propia experiencia y fortalece nuestra libertad interior.')}</p>
<p class="center" style="font-style:italic;color:var(--violet);font-size:1.15em">{L('Recognition has its own time; Grace cannot be forced.', 'El reconocimiento tiene su tiempo; la Gracia no puede forzarse.')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap grid2">
<div>
<p class="eyebrow">{L('MY SERVICE', 'MI SERVICIO')}</p>
<h2>{L('A close and human meeting', 'Un encuentro cercano y humano')}</h2>
<p>{L('From what I have lived, I am here to serve in that function: to offer a space where we can meet with honesty, ask questions, share silence and look together.', 'Desde lo que he vivido, estoy aquí para servir en esa función: ofrecer un espacio donde podamos encontrarnos con honestidad, hacer preguntas, compartir silencio y mirar juntos.')}</p>
<p>{L('I too have known the search, the confusion and the pain; that is why it matters to me that this meeting be close and human. What I share goes on maturing in my own life.', 'Yo también he conocido la búsqueda, la confusión y el dolor; por eso me importa que este encuentro sea cercano y humano. Lo que comparto sigue madurando en mi propia vida.')}</p>
<p>{L('If my presence and my experience can help you recognize more clearly what you are, and live from there with more love and freedom, that is the meaning of my service.', 'Si mi presencia y mi experiencia pueden ayudarte a reconocer con mayor claridad lo que eres, y a vivir desde allí con más amor y libertad, ese es el sentido de mi servicio.')}</p>
<div class="btns" style="justify-content:flex-start"><a class="btn solid" href="{url(lang, 'contact')}">{L('Write to me about satsang', 'Escríbeme sobre el satsang')}</a><a class="btn" href="{url(lang, 'ground')}">{L('Read: The Ground', 'Leer: El Fundamento')}</a></div>
</div>
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion"></figure>
</div></section>
'''
