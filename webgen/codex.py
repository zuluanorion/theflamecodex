# -*- coding: utf-8 -*-
"""The Flame Codex tab (EN/ES) — written in Zuluan's own warm, first-person voice for every reader."""

def _tiles(items, cls='tiles'):
    return f'<div class="{cls}">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in items) + '</div>'

def _cards(items, cls='grid3'):
    return f'<div class="{cls}">' + ''.join(f'<div class="card"><p class="eyebrow">{e}</p><h3>{h}</h3><p>{p}</p></div>' for e, h, p in items) + '</div>'

def _path(items):
    return '<ol class="path">' + ''.join(f'<li><b>{a}</b>{f"<span>{b}</span>" if b else ""}</li>' for a, b in items) + '</ol>'

def codex_page(lang, url, S, sigrid, subnav=''):
    en = lang == 'en'
    L = lambda e, s: e if en else s
    BK = '/assets/img/books/'
    return f'''{subnav}
<section><div class="narrow">
<p class="eyebrow">{L('HOW THE CODEX WAS BORN', 'CÓMO NACIÓ EL CÓDICE')}</p>
<h2>{L('First came life. Then came the words.', 'Primero fue la vida. Después llegaron las palabras.')}</h2>
<p class="lead">{L('The Flame Codex was not born at a desk. It was born of my life.', 'El Códice de la Llama no nació en un escritorio. Nació de mi vida.')}</p>
<p>{L('Of decades of meditation, of questions that would not leave me in peace, of accompanying the suffering of many people and, above all, of the Descent of the Flame: that movement in which what I had recognized as consciousness began to ask for room in my body and in my life.',
      'De décadas de meditación, de preguntas que no me dejaban en paz, de acompañar el sufrimiento de muchas personas y, sobre todo, del Descenso de la Llama: ese movimiento en el que lo que yo había reconocido como consciencia empezó a pedir lugar en mi cuerpo y en mi vida.')}</p>
<p>{L('First I lived the experience. Then the language came, to name it, to tell its qualities apart and to accompany it. At first there were no words: there was an understanding that lived whole, all at once. In time each quality showed itself on its own (serenity, clarity, rootedness, tenderness, devotion) and each one took on a sound, a form and its place within one language. That is what I call <em>cognizing</em>: recognizing something inwardly before being able to explain it.',
      'Primero viví la experiencia. Después llegó el lenguaje para nombrarla, distinguir sus cualidades y acompañarla. Al principio no había palabras: había una comprensión que vivía entera, toda junta. Con el tiempo, cada cualidad se fue mostrando por sí sola —la serenidad, la claridad, el arraigo, la ternura, la devoción— y cada una fue tomando un sonido, una forma y su lugar dentro de un mismo lenguaje. A eso lo llamo <em>cognizar</em>: reconocer algo por dentro antes de poder explicarlo.')}</p>
<p>{L('I want this to be clear: the syllables did not cause my Descent. They came afterwards, so that what was lived could be shared and accompanied.',
      'Quiero que esto quede claro: las sílabas no causaron mi Descenso. Llegaron después, para que lo vivido pudiera compartirse y acompañarse.')}</p>
<p class="note">{L('Each key was written down, reviewed and verified with great care before entering the Codex. In that work of ordering and safeguarding the record I also relied on artificial intelligence, as a mirror and a tool, never as a spiritual authority.',
      'Cada llave fue escrita, revisada y verificada con mucho cuidado antes de entrar en el Códice. En ese trabajo de ordenar y custodiar lo escrito me apoyé también en la inteligencia artificial, como espejo y herramienta, nunca como autoridad espiritual.')}</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>177</b><span>{L('keys', 'llaves')}</span></div>
<div><b>2</b><span>{L('volumes, one single work', 'volúmenes, una sola obra')}</span></div>
<div><b>33</b><span>{L('keys at the heart of the Codex', 'llaves en el corazón del Códice')}</span></div>
<div><b>1</b><span>{L('purpose: that life demonstrates it', 'propósito: que la vida lo demuestre')}</span></div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">{L('IN SIMPLE WORDS', 'EN PALABRAS SENCILLAS')}</p>
<h2>{L('A language for the soul', 'Un lenguaje para el alma')}</h2>
<p>{L('The Codex gathers 177 keys. Each key is a door to a quality of your own being. It has a sound you can say, an image you can contemplate, a sign that can be traced, and a meaning you can carry into your day.',
      'El Códice reúne 177 llaves. Cada llave es una puerta hacia una cualidad de tu propio ser. Tiene un sonido que puedes pronunciar, una imagen que puedes contemplar, un signo que puede trazarse y un significado que puedes llevar a tu día.')}</p>
<p>{L('I also call these keys syllables, or Light Codes. Together they form a language: you can meet just one, or join them the way words are joined in a sentence.',
      'A estas llaves también las llamo sílabas o Códigos de Luz. Juntas forman un lenguaje: puedes encontrarte con una sola, o unirlas como se unen las palabras en una frase.')}</p>
<p>{L('It is not magic, nor a formula for getting things. It is a way of coming close to the sacred that already lives in you: listening, looking, understanding and, when it is right, following its trace. What emerges is not installed from outside: it is discovered.',
      'No es magia ni una fórmula para conseguir cosas. Es una manera de acercarte a lo sagrado que ya vive en ti: escuchando, mirando, comprendiendo y, cuando corresponde, recorriendo su trazo. Lo que aparece no se instala desde afuera: se descubre.')}</p>
<p>{L('Its centre is incarnation: that what you recognize in silence shows in the way you live. In how you speak to your family, how you rest, how you set a limit, how you love.',
      'Su centro es la encarnación: que lo que reconoces en el silencio se note en tu manera de vivir. En cómo le hablas a tu familia, en cómo descansas, en cómo pones un límite, en cómo amas.')}</p>
</div></section>

<section class="alt"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('WHAT IS THE FLAME?', '¿QUÉ ES LA LLAMA?')}</p>
<h2>{L('Soul, Monad and Flame', 'Alma, Mónada y Llama')}</h2>
<p>{L('Let me explain it with three simple words.', 'Te lo explico con tres palabras sencillas.')}</p>
</div>
{_cards([(L('SOUL', 'ALMA'), L('The soul', 'El alma'), L('What you are as an individual: unique in the way it expresses itself, yet never separate from the Whole.', 'Lo que tú eres como individualidad: única en su manera de expresarse, pero nunca separada del Todo.')),
         (L('MONAD', 'MÓNADA'), L('The Monad', 'La Mónada'), L('The Divine Intelligence that lives at the depth of your soul. It knows your direction, your purpose and your deepest truth.', 'La Inteligencia Divina que vive en el fondo de tu alma. Conoce tu dirección, tu propósito y tu verdad más profunda.')),
         (L('FLAME', 'LLAMA'), L('The Flame', 'La Llama'), L('That same Intelligence when it enters your life and becomes presence: in your mind, your heart and your body.', 'Esa misma Inteligencia cuando entra en tu vida y se vuelve presencia: en tu mente, en tu corazón y en tu cuerpo.'))])}
<div class="narrow center" style="padding:0">
<blockquote>{L('The Flame is not energy trying to reach God.<br>It is the Divine Intelligence consciously entering incarnation.', 'La Llama no es energía tratando de alcanzar a Dios.<br>Es la Inteligencia Divina entrando conscientemente en encarnación.')}</blockquote>
<p>{L('The Flame exists before any word that names it. The syllable, the image, the book and I myself are only ways of bringing you closer to it. Practice prepares you to receive, and accompanies you while what is received is integrated.',
      'La Llama existe antes que cualquier palabra que la nombre. La sílaba, la imagen, el libro y yo mismo somos solo formas de acercarte a ella. La práctica te prepara para recibir y te acompaña mientras lo recibido se integra.')}</p>
</div>
</div></section>

<section><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('HOW A KEY WORKS', 'CÓMO OBRA UNA LLAVE')}</p>
<h2>{L('A key does nothing without you', 'Una llave no hace nada sin ti')}</h2>
<p>{L('A key is not a button you press. It is a relationship between seven things, and you take part in all of them.', 'Una llave no es un botón que se aprieta. Es una relación entre siete cosas, y tú participas en todas.')}</p>
</div>
{_tiles([(L('Sound', 'Sonido'), L('gives the key a time', 'le da a la llave un tiempo')), (L('Form', 'Forma'), L('gives you something to look at', 'te da algo que mirar')), (L('Meaning', 'Significado'), L('shows you where it leads', 'te muestra hacia dónde lleva')), (L('Intention', 'Intención'), L('gives it direction', 'le da dirección')), (L('Attention', 'Atención'), L('sustains it', 'la sostiene')), (L('Body and breath', 'Cuerpo y respiración'), L('make it livable', 'la vuelven vivible')), (L('Presence', 'Presencia'), L('gives it room', 'le da espacio'))])}
<div class="narrow" style="padding:0">
<p>{L('And your own discernment recognizes what you can integrate and what is not yet ready.', 'Y tu propio discernimiento reconoce qué puedes integrar y qué todavía no.')}</p>
<p>{L('That is why you do not need to feel anything special. Sometimes stillness, clarity or emotion will come; sometimes resistance, or a completely ordinary session. All of that is fine. Nor do you need to credit a key with everything that happens afterwards. The real question is another one: what new relationship becomes possible with what you are living, and how does it show in your life?',
      'Por eso no tienes que sentir nada especial. A veces vendrá quietud, claridad o emoción; a veces resistencia, o una sesión completamente normal. Todo eso está bien. Tampoco hace falta atribuirle a una llave todo lo que pase después. La pregunta verdadera es otra: ¿qué relación nueva se vuelve posible con lo que vives, y cómo se nota eso en tu vida?')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('FOUR WAYS TO MEET A KEY', 'CUATRO MANERAS DE ENCONTRAR UNA LLAVE')}</p>
<h2>{L('Contemplate, recognize, trace and know', 'Contemplar, reconocer, trazar y conocer')}</h2>
<p>{L('Each key comes to you in four ways. Each has its own function, and together they help you recognize the same key from different places.', 'Cada llave se presenta de cuatro maneras. Cada una tiene su función, y juntas te ayudan a reconocer la misma llave desde distintos lugares.')}</p>
</div>
{_cards([(L('A · CONTEMPLATE', 'A · CONTEMPLAR'), L('The meditation plate', 'La lámina de meditación'), L('It is the key made image, to look at softly and stay in silence with. You do not have to decipher every detail: it is enough to receive it. The plate is for contemplating, not for copying a trace from.', 'Es la llave hecha imagen, para mirarla con suavidad y quedarte en silencio con ella. No tienes que descifrar cada detalle: basta con recibirla. La lámina es para contemplar, no para copiar de ella un trazo.')),
         (L('B · THE BARE SIGN', 'B · EL SIGNO DESNUDO'), L('The original sigil', 'El sigilo original'), L('It is the original form of the key, its geometric signature. Out of respect it is never rotated, mirrored, simplified or redrawn.', 'Es la forma original de la llave, su firma geométrica. Por respeto, nunca se gira, se refleja, se simplifica ni se redibuja.')),
         (L('C · LEARN THE TRACE', 'C · APRENDER EL TRAZO'), L('The tracing guide', 'La guía de trazo'), L('It teaches how to travel the sign: where it begins, which way it goes and where it ends. I only teach verified routes; if a key does not yet have one, it is contemplated and studied, but no route is invented.', 'Enseña cómo se recorre el signo: dónde empieza, hacia dónde va y dónde termina. Solo enseño recorridos verificados; si una llave todavía no lo tiene, se contempla y se estudia, pero el recorrido no se inventa.')),
         (L('D · KNOW THE KEY', 'D · CONOCER LA LLAVE'), L('The study page', 'La ficha'), L('It tells you its name, how to pronounce it, what it means, what it is for and which other keys it relates to. The study page keeps who the key is; practice lets you know it from within.', 'Te cuenta su nombre, cómo se pronuncia, qué significa, para qué sirve y con qué otras llaves se relaciona. La ficha guarda quién es la llave; la práctica te permite conocerla por dentro.'))], 'grid2 cards4')}
<div class="narrow center" style="padding:0">
<p class="eyebrow" style="margin-top:36px">NAMA-RUPA · {L('NAME AND FORM', 'NOMBRE Y FORMA')}</p>
<blockquote>{L('The syllable makes a quality audible.<br>The sign makes it visible.<br>The trace lets it be travelled in time.', 'La sílaba vuelve audible una cualidad.<br>El signo la vuelve visible.<br>El trazo permite recorrerla en el tiempo.')}</blockquote>
<p>{L('Some arrive first through the ear, some through the eyes, some through study. In time, it all comes together within.', 'Hay quien llega primero por el oído, quien llega por la mirada y quien llega por el estudio. Con el tiempo, todo se une por dentro.')}</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="narrow" style="padding:0">
<p class="eyebrow">{L('THE 33 KEYS AT THE HEART', 'LAS 33 LLAVES DEL CORAZÓN')}</p>
<h2>{L('The signs of the 33', 'Los signos de las 33')}</h2>
<p>{L('At the heart of the Codex are 33 core keys. I present them in Volume I, together with the key of the Master Core, SOR&rsquo;RAJ. These are their original signs.', 'En el corazón del Códice hay 33 llaves nucleares. Las presento en el Volumen I, junto con la llave del Núcleo Maestro, SOR&rsquo;RAJ. Estos son sus signos originales.')}</p>
</div>
{sigrid()}
</div></section>

<section><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('WHEN KEYS COME TOGETHER', 'CUANDO LAS LLAVES SE UNEN')}</p>
<h2>{L('Core, Support and Seal', 'Núcleo, Soporte y Sello')}</h2>
<p>{L('Keys can also join in threes, like a small sacred sentence. The first opens, the second holds and the third closes. All three serve one purpose.', 'Las llaves también pueden unirse de tres en tres, como una pequeña frase sagrada. La primera abre, la segunda sostiene y la tercera cierra. Las tres sirven a un mismo propósito.')}</p>
</div>
<div class="triad">
<div><span class="dot">I</span><b>{L('Core', 'Núcleo')}</b><em>{L('opens', 'abre')}</em><p>{L('Opens the way and sets the direction.', 'Abre el camino y marca la dirección.')}</p></div>
<i>→</i>
<div><span class="dot">II</span><b>{L('Support', 'Soporte')}</b><em>{L('holds', 'sostiene')}</em><p>{L('Holds what was opened and gives it a shade: grounding, clarity, receptivity or protection.', 'Sostiene lo que se abrió y le da un matiz: arraigo, claridad, receptividad o protección.')}</p></div>
<i>→</i>
<div><span class="dot">III</span><b>{L('Seal', 'Sello')}</b><em>{L('closes', 'cierra')}</em><p>{L('Closes the movement: it contains it, steadies it or returns it to silence.', 'Cierra el movimiento: lo contiene, lo estabiliza o lo devuelve al silencio.')}</p></div>
</div>
<div class="narrow" style="padding:0">
<p>{L('Each key has functions that are respected: not every key can open, hold or seal. Some combinations belong to the original material of the Codex; others are composed later, with care and a clear purpose, and are always presented as what they are. And if you are just beginning, one key is more than enough.',
      'Cada llave tiene funciones que se respetan: no todas pueden abrir, sostener o sellar. Algunas combinaciones forman parte del material original del Códice; otras se componen después, con cuidado y con un propósito claro, y siempre se presentan como lo que son. Y si estás comenzando, una sola llave es más que suficiente.')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="narrow" style="padding:0">
<p class="eyebrow">{L('TRANSFORMATION AND INTEGRATION', 'TRANSFORMACIÓN E INTEGRACIÓN')}</p>
<h2>{L('From recognition to daily life', 'Del reconocimiento a la vida diaria')}</h2>
<p>{L('A person can know immense peace in meditation and, a little later, be afraid to say what they feel, argue about the same old thing, or go back to a habit that takes them away from themselves. I have seen it many times in my years of accompanying others. Recognizing consciousness is one thing; allowing that recognition to transform the way you live is another.',
      'Una persona puede conocer una paz inmensa en la meditación y, al rato, tener miedo de decir lo que siente, discutir por lo mismo de siempre o volver a un hábito que la aleja de sí misma. Lo he visto muchas veces en mis años de acompañar a otros. Reconocer la consciencia es una cosa; permitir que ese reconocimiento transforme tu manera de vivir es otra.')}</p>
<p>{L('The Codex exists for that second part: so that the clarity you find in silence also reaches your emotions, your relationships and your habits.',
      'El Códice existe para esa segunda parte: para que la claridad que encuentras en el silencio llegue también a tus emociones, a tus relaciones y a tus hábitos.')}</p>
</div>
<div class="grid2 top" style="margin-top:30px">
<div>
<p class="eyebrow">{L('WHERE WE FEEL DIVIDED', 'DONDE NOS SENTIMOS DIVIDIDOS')}</p>
<ul class="benefits">
<li>{L('You understand something, but cannot manage to live it.', 'Entiendes algo, pero no logras vivirlo.')}</li>
<li>{L('You long for closeness and, at the same time, protect yourself from it.', 'Deseas cercanía y, al mismo tiempo, te proteges de ella.')}</li>
<li>{L('You want to express yourself and are afraid to.', 'Quieres expresarte y te da miedo hacerlo.')}</li>
<li>{L('You seek peace, yet hold on to habits that pull you away from your own balance.', 'Buscas paz, pero sostienes hábitos que te alejan de tu propio equilibrio.')}</li>
</ul>
<p>{L('Practice gives you a space to look at these tensions with more presence: to recognize patterns that repeat, to make room for emotions you once rejected, to recover the clarity to choose, to set coherent limits, and to unite what you understand, what you feel and what you do.',
      'La práctica te da un espacio para mirar estas tensiones con más presencia: reconocer patrones que se repiten, darle lugar a emociones que antes rechazabas, recuperar la claridad para elegir, poner límites coherentes y unir lo que comprendes, lo que sientes y lo que haces.')}</p>
<p>{L('Integration can be gradual, and its fruits are simple: a more honest decision, a conversation long put off, a less reactive answer, a little more capacity to stay present.',
      'La integración puede ser gradual, y sus frutos son sencillos: una decisión más honesta, una conversación pendiente, una respuesta menos reactiva, un poco más de capacidad de quedarte presente.')}</p>
</div>
<div>
<p class="eyebrow">{L('THE THREEFOLD HEART', 'EL CORAZÓN TRINO')}</p>
<p style="margin-top:0">{L('In the heart, the Flame expresses itself in three great qualities:', 'En el corazón, la Llama se expresa en tres grandes cualidades:')}</p>
<div class="heart3">
<div><b>{L('Love', 'Amor')}</b><span>{L('compassion, tenderness, mercy and the capacity for meeting', 'compasión, ternura, misericordia y capacidad de encuentro')}</span></div>
<div><b>{L('Wisdom', 'Sabiduría')}</b><span>{L('clarity, discernment, understanding and truth', 'claridad, discernimiento, comprensión y verdad')}</span></div>
<div><b>{L('Power or Will', 'Poder o Voluntad')}</b><span>{L('courage, the capacity to act, protection and fidelity to a deep direction', 'coraje, capacidad de actuar, protección y fidelidad a una dirección profunda')}</span></div>
</div>
<blockquote>{L('Love needs discernment.<br>Clarity needs humanity.<br>Will needs care.', 'El amor necesita discernimiento.<br>La claridad necesita humanidad.<br>La voluntad necesita cuidado.')}</blockquote>
</div>
</div>
<div class="narrow" style="padding:0">
<p>{L('The Descent belongs to Grace. No syllable and no combination can promise it will happen on a certain date or under a certain condition. What we can offer is attention, presence, discernment, receptivity, and a life willing to integrate what comes. The Codex prepares, orients and accompanies the human vessel.',
      'El Descenso pertenece a la Gracia. Ninguna sílaba ni ninguna combinación pueden prometer que ocurra en una fecha o bajo una condición. Lo que sí podemos ofrecer es atención, presencia, discernimiento, receptividad y una vida dispuesta a integrar lo que llega. El Códice prepara, orienta y acompaña la vasija humana.')}</p>
<p>{L('And so much is decided in the root: in our capacity to stay. To be in the body, to rest, to hold limits, to belong to the earth, and to attend to the life in front of us.',
      'Y mucho se decide en la raíz: en nuestra capacidad de quedarnos. Estar en el cuerpo, descansar, sostener límites, pertenecer a la tierra y atender la vida que tenemos delante.')}</p>
<blockquote class="center">{L('The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.', 'La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.')}</blockquote>
<p class="center"><a class="btn" href="{url(lang, 'descent')}">{L('Read: The Descent of the Flame', 'Leer: El Descenso de la Llama')}</a></p>
</div>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">{L('HOW TO BEGIN', 'CÓMO EMPEZAR')}</p>
<h2>{L('Six simple steps', 'Seis pasos sencillos')}</h2>
<ol class="steps">
<li><b>{L('Know.', 'Conoce.')}</b> {L('Read what the key means and what it is for, and ask yourself why you want to work with it.', 'Lee qué significa la llave y para qué sirve, y pregúntate por qué quieres trabajar con ella.')}</li>
<li><b>{L('Orient.', 'Orienta.')}</b> {L('Set a simple intention, in harmony with what that key does.', 'Pon una intención sencilla, que vaya de acuerdo con lo que esa llave hace.')}</li>
<li><b>{L('Contemplate or listen.', 'Contempla o escucha.')}</b> {L('Meet it through its plate or its sound.', 'Encuéntrate con ella a través de su lámina o de su sonido.')}</li>
<li><b>{L('Practise as its page teaches.', 'Practica como enseña su ficha.')}</b> {L('Use the pronunciation, the trace or the sequence only as the study page indicates.', 'Usa la pronunciación, el trazo o la secuencia solo como la ficha lo indica.')}</li>
<li><b>{L('Stay in silence.', 'Quédate en silencio.')}</b> {L('Let the experience have room. Do not demand that you feel something or understand everything.', 'Deja que la experiencia tenga espacio. No te exijas sentir algo ni entenderlo todo.')}</li>
<li><b>{L('Return to your life.', 'Vuelve a tu vida.')}</b> {L('Come back to the body and see how you can live that quality today.', 'Regresa al cuerpo y mira cómo puedes vivir hoy esa cualidad.')}</li>
</ol>
<p class="note" style="color:#CFC6E2">{L('Each key has its own indications: time, repetitions and breathing depend on each one. For a step-by-step guide, go to', 'Cada llave tiene sus propias indicaciones: el tiempo, las repeticiones y la respiración dependen de cada una. Si quieres una guía paso a paso, entra en')} <a style="color:var(--gold2)" href="{url(lang, 'codex/meditation')}">{L('Light Code Meditation', 'Meditación de Códigos de Luz')}</a>.</p>
</div></section>

<section><div class="wrap grid2 top">
<div>
<p class="eyebrow">{L('STUDY, PRACTICE AND TRANSMISSION', 'ESTUDIO, PRÁCTICA Y TRANSMISIÓN')}</p>
<h2>{L('Different doors', 'Distintas puertas')}</h2>
<p>{L('The book is open to everyone: anyone can read the teaching, contemplate the plates and come close to the public syllables. Facilitating processes, representing the Codex, initiating and transmitting are something else: they ask for formation and responsibility.',
      'El libro está abierto para todos: cualquiera puede leer la enseñanza, contemplar las láminas y acercarse a las sílabas públicas. Facilitar procesos, representar el Códice, iniciar y transmitir son otra cosa: piden formación y responsabilidad.')}</p>
{_path([(L('Reading and contemplating', 'Leer y contemplar'), ''), (L('Practising personally', 'Practicar personalmente'), ''), (L('Facilitating processes', 'Facilitar procesos'), ''), (L('Representing the Codex', 'Representar el Códice'), ''), (L('Initiating and transmitting', 'Iniciar y transmitir'), '')])}
<p>{L('A <strong>Guardian of the Flame</strong> takes care of the language, its ethics and its fidelity. A <strong>Bearer of the Flame</strong> is recognized by the stability of their incarnation: that cannot be bought, and no certificate can give it. The reserved procedures of transmission are learned in their own context of formation.',
      'Un <strong>Guardián de la Llama</strong> cuida el lenguaje, su ética y su fidelidad. Un <strong>Portador de la Llama</strong> se reconoce por la estabilidad de su encarnación: eso no se compra ni lo da un certificado. Los procedimientos reservados de la transmisión se aprenden en su propio contexto de formación.')}</p>
</div>
<div>
<p class="eyebrow">{L('THE CODEX AND THE OTHER BOOKS', 'EL CÓDICE Y LOS OTROS LIBROS')}</p>
<h2>{L('One language, many paths', 'Un lenguaje, muchos caminos')}</h2>
<div class="vols"><img src="{BK}codice1.webp?v=3d" alt="El Códice de la Llama · Vol. I"><img src="{BK}codice2.webp?v=3d" alt="El Códice de la Llama · Vol. II"></div>
<p>{L('<strong>Volume I</strong> presents the foundation of the work, its architecture and the 33 core keys, with the key of the Master Core SOR&rsquo;RAJ. <strong>Volume II</strong> continues with the expanded field of the keys. The two form a single work.', 'El <strong>Volumen I</strong> presenta el fundamento de la obra, su arquitectura y las 33 llaves nucleares, con la llave del Núcleo Maestro SOR&rsquo;RAJ. El <strong>Volumen II</strong> continúa con el campo expandido de las llaves. Los dos forman una sola obra.')}</p>
<p>{L('The Light Code books, for the mind, the heart, dreams, energy and meditation, carry this language into the different corners of life, always faithful to each key.', 'Los libros de Códigos de Luz —para la mente, el corazón, los sueños, la energía y la meditación— llevan este lenguaje a los distintos rincones de la vida, siempre fieles a cada llave.')}</p>
<blockquote>{L('The Codex keeps the language.<br>The books open the paths.<br>You explore and integrate.', 'El Códice guarda el lenguaje.<br>Los libros abren los caminos.<br>Tú exploras e integras.')}</blockquote>
<p><a class="btn" href="{url(lang, 'books')}">{L('See the books', 'Ver los libros')}</a></p>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p class="eyebrow">{L('AN ASPIRATION', 'UNA ASPIRACIÓN')}</p>
<h2>{L('A humanity living with more coherence', 'Una humanidad que viva con más coherencia')}</h2>
<p>{L('I dream of a humanity able to live with more coherence. And that dream begins in something very concrete: in how each person listens, how they pass through pain, how they use their will, how they hold their responsibilities, and how they turn what they understand into care. I believe that when one person becomes more integrated, it can touch those around them as well. I offer this as a direction, with humility, not as a promise.',
      'Sueño con una humanidad capaz de vivir con más coherencia. Y ese sueño empieza en algo muy concreto: en cómo escucha cada persona, cómo atraviesa el dolor, cómo usa su voluntad, cómo sostiene sus responsabilidades y cómo convierte lo que comprende en cuidado. Creo que cuando una persona se integra, eso puede tocar también a quienes la rodean. Lo ofrezco como una dirección, con humildad, no como una promesa.')}</p>
<p>{L('I share the Codex as a spiritual practice. Its origin is my testimony; its doctrine, a teaching; and your experience is yours, to observe with your own discernment.',
      'Comparto el Códice como una práctica espiritual. Su origen es mi testimonio; su doctrina, una enseñanza; y tu experiencia es tuya, para observarla con tu propio discernimiento.')}</p>
</div></section>
'''
