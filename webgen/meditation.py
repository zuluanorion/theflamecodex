# -*- coding: utf-8 -*-
"""Light Code Meditation (MCL) — a tab inside the Flame Codex section (EN/ES), in Zuluan's own warm voice."""

def subnav(lang, url, on):
    en = lang == 'en'
    items = [('codex', 'The Codex · Transformation and Integration' if en else 'El Códice · Transformación e Integración'),
             ('codex/meditation', 'Light Code Meditation' if en else 'Meditación de Códigos de Luz')]
    return '<nav class="subnav"><div class="wrap">' + ''.join(
        f'<a href="{url(lang, p)}"{" class=on" if p == on else ""}>{t}</a>' for p, t in items) + '</div></nav>'

def meditation_page(lang, url):
    en = lang == 'en'
    L = lambda e, s: e if en else s
    BK = '/assets/img/books/'
    path = lambda items: '<ol class="path">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in items) + '</ol>'
    syl = [('AHR', 'ÁR', L('Opening, presence and anchoring', 'Apertura, presencia y anclaje')),
           ('LO’EN', 'LÓ-EN', L('Serene presence before emotion', 'Presencia serena ante la emoción')),
           ('ZEN’LUM', 'SEN-LUM', L('Stillness and neutrality', 'Quietud y neutralidad')),
           ('SHA’EL', 'SHA-ÉL', L('Discernment', 'Discernimiento')),
           ('LOH’VEN', 'LÓ-ven', L('Acceptance and union', 'Aceptación y unión')),
           ('JAH’VEN', 'YÁ-VEN', L('Devotion', 'Devoción')),
           ('ROH’KAH', 'RO-KÁ', L('Stability and support', 'Estabilidad y apoyo'))]
    faq = [(L('If many thoughts come', 'Si llegan muchos pensamientos'), L('Notice that you are thinking, and come back kindly to the support you chose.', 'Date cuenta de que estás pensando y vuelve con amabilidad al apoyo que elegiste.')),
           (L('If you cannot see the plate inwardly', 'Si no logras ver la lámina por dentro'), L('Carry on with the syllable, the intention, or simply the presence of your body.', 'Sigue con la sílaba, con la intención o simplemente con la presencia de tu cuerpo.')),
           (L('If you feel nothing special', 'Si no sientes nada especial'), L('Write the session down as it was. It is not a failure, and there is no need to imagine invisible effects you cannot observe.', 'Anota la sesión tal como fue. No es un fracaso, y no hace falta imaginar efectos invisibles que no puedes observar.')),
           (L('If images or messages appear', 'Si aparecen imágenes o mensajes'), L('You can write them down as inner experiences. They are not orders you have to obey.', 'Puedes anotarlos como experiencias interiores. No son órdenes que tengas que obedecer.')),
           (L('If an emotion comes up', 'Si surge una emoción'), L('Give it room, as much as you can hold, without pushing it into a catharsis.', 'Dale espacio, hasta donde puedas sostenerla, sin empujarla hacia una catarsis.')),
           (L('If it becomes too much', 'Si se vuelve demasiado'), L('Open your eyes, look around you and stop. Ask for accompaniment if you need it.', 'Abre los ojos, mira a tu alrededor y detente. Pide acompañamiento si lo necesitas.'))]
    return f'''{subnav(lang, url, 'codex/meditation')}
<section><div class="wrap grid2">
<figure class="ahr"><img src="/assets/img/ahr_glow.webp" alt="AHR"><figcaption>AHR · ÁR</figcaption></figure>
<div>
<p class="eyebrow">{L('LIGHT CODE MEDITATION', 'MEDITACIÓN DE CÓDIGOS DE LUZ')}</p>
<h2>{L('A simple and deep meditation', 'Una meditación sencilla y profunda')}</h2>
<p class="lead">{L('Meditation has been at the centre of my life, and I have had the privilege of initiating thousands of people into it. I used to teach it with the bija mantras, the seed sounds of the tradition of India. Today I share it with the syllables of the Flame Codex.',
                   'La meditación ha estado en el centro de mi vida, y he tenido el privilegio de iniciar a miles de personas en ella. Antes la enseñaba con los bija mantras, los sonidos semilla de la tradición de la India. Hoy la comparto con las sílabas del Códice de la Llama.')}</p>
<p>{L('Each syllable is chosen for what it is and what it does, not because it sounds like another. It is a door to a quality that already lives in you: serenity, clarity, rootedness, devotion.',
      'Cada sílaba se elige por lo que es y por lo que hace, no porque suene parecido a otra. Es una puerta hacia una cualidad que ya vive en ti: la serenidad, la claridad, el arraigo, la devoción.')}</p>
<p>{L('The practice is simple. You begin with an intention. You look at the plate, if you have it. You let the syllable keep you company. And then you rest in silence. What you contemplate there, you carry afterwards into your life.',
      'La práctica es sencilla. Empiezas con una intención. Miras la lámina, si la tienes. Dejas que la sílaba te acompañe. Y luego descansas en el silencio. Lo que contemplas allí, lo llevas después a tu vida.')}</p>
<blockquote>{L('The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.', 'La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.')}</blockquote>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('WHAT YOU NEED', 'LO QUE NECESITAS')}</p>
<h2>{L('Nothing special', 'Nada especial')}</h2>
<p>{L('A quiet place, a few minutes and a sincere intention. That is enough to begin. The practice brings together six simple things:', 'Un lugar tranquilo, unos minutos y una intención sincera. Con eso basta para comenzar. La práctica reúne seis cosas sencillas:')}</p>
</div>
<div class="tiles six">
<div><b>{L('Intention', 'Intención')}</b><span>{L('what you wish to contemplate', 'lo que deseas contemplar')}</span></div>
<div><b>{L('Syllable', 'Sílaba')}</b><span>{L('one key of the Codex', 'una llave del Códice')}</span></div>
<div><b>{L('Plate', 'Lámina')}</b><span>{L('its image, if you use it', 'su imagen, si la usas')}</span></div>
<div><b>{L('Body and breath', 'Cuerpo y respiración')}</b><span>{L('your support', 'tu apoyo')}</span></div>
<div><b>{L('Silence', 'Silencio')}</b><span>{L('where you rest', 'donde descansas')}</span></div>
<div><b>{L('Your life', 'Tu vida')}</b><span>{L('where it all comes together', 'donde todo se integra')}</span></div>
</div>
<div class="narrow center" style="padding:0">
<blockquote>{L('The syllable opens a door. Contemplation makes its quality familiar.<br>Silence gives it room. And your daily life makes it real.', 'La sílaba abre una puerta. La contemplación te hace familiar su cualidad.<br>El silencio le da espacio. Y tu vida diaria la vuelve real.')}</blockquote>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">{L('WHY MEDITATE THIS WAY?', '¿PARA QUÉ MEDITAR ASÍ?')}</p>
<h2>{L('To relate differently to what you live', 'Para relacionarte de otra manera con lo que vives')}</h2>
<p>{L('To learn to look at your thoughts, emotions and sensations without believing you are each one of them. And so that qualities like these can find a place in your life:', 'Para aprender a mirar tus pensamientos, tus emociones y tus sensaciones sin creer que eres cada uno de ellos. Y para que cualidades como estas encuentren lugar en tu vida:')}</p>
<p class="qualities">{' · '.join(L('Presence,Clarity,Serenity,Discernment,Devotion,Rootedness,Receptivity,Will,Integration', 'Presencia,Claridad,Serenidad,Discernimiento,Devoción,Arraigo,Receptividad,Voluntad,Integración').split(','))}</p>
<p>{L('Its meaning becomes concrete in small things: listening with more attention, answering with more clarity, holding a limit, acting with more coherence.', 'Su sentido se vuelve concreto en cosas pequeñas: escuchar con más atención, responder con más claridad, sostener un límite, actuar con más coherencia.')}</p>
<p>{L('In the language of the Codex we say this practice prepares the human vessel so that the Flame, the Divine Intelligence entering incarnation, can express itself. But the Descent belongs to Grace: no technique and no syllable can guarantee it. When the practice speaks of <em>making room for the descent</em>, I mean a willingness: allowing what you contemplate to find body and expression. It does not mean that each session produces a new Descent.',
      'En el lenguaje del Códice decimos que esta práctica prepara la vasija humana para que la Llama, la Inteligencia Divina entrando en la encarnación, pueda expresarse. Pero el Descenso pertenece a la Gracia: ninguna técnica ni ninguna sílaba pueden garantizarlo. Cuando en la práctica hablo de <em>dar lugar al descenso</em>, hablo de una disposición: permitir que lo que contemplas encuentre cuerpo y expresión. No significa que cada sesión produzca un nuevo Descenso.')}</p>
</div></section>

<section class="alt"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('YOUR SUPPORTS', 'TUS APOYOS')}</p>
<h2>{L('Intention, syllable, gaze and the Observer', 'Intención, sílaba, mirada y Observador')}</h2>
</div>
<div class="grid2 cards4">
<div class="card"><p class="eyebrow">{L('THE INTENTION', 'LA INTENCIÓN')}</p><h3>{L('What do you wish to contemplate?', '¿Qué quieres contemplar?')}</h3>
<p>{L('Before you begin, recognize it and say it simply, in harmony with what the syllable you chose does:', 'Antes de empezar, reconócelo y dilo con sencillez, de acuerdo con lo que hace la sílaba que elegiste:')}</p>
<p class="examples">{L('&ldquo;I want to be present.&rdquo;<br>&ldquo;I want to accompany this emotion with serenity.&rdquo;<br>&ldquo;I want to see my next step clearly.&rdquo;<br>&ldquo;I want a more intimate relationship with the sacred.&rdquo;', '&ldquo;Quiero estar presente.&rdquo;<br>&ldquo;Quiero acompañar esta emoción con serenidad.&rdquo;<br>&ldquo;Quiero reconocer con claridad mi siguiente paso.&rdquo;<br>&ldquo;Quiero cultivar una relación más íntima con lo sagrado.&rdquo;')}</p>
<p>{L('Once recognized, you do not need to repeat it: let it rest in the silence too. Intention gives you a direction; it does not oblige you to get a result.', 'Una vez reconocida, no necesitas repetirla: déjala también en el silencio. La intención te da una dirección; no te obliga a conseguir un resultado.')}</p></div>
<div class="card"><p class="eyebrow">{L('THE SYLLABLE', 'LA SÍLABA')}</p><h3>{L('A sound that keeps you company', 'Un sonido que te acompaña')}</h3>
<p>{L('You can say it softly or remember it inwardly, as its study page indicates. Pronounce it with care and without strain. You do not have to hold it with force the whole session: when it grows faint, let it rest in silence. If you get lost in your thoughts, remember it gently and rest again. There is no required number of repetitions.',
      'Puedes pronunciarla suavemente o recordarla por dentro, como indique su ficha. Pronúnciala con cuidado y sin tensión. No tienes que sostenerla con fuerza toda la sesión: cuando se vuelva tenue, déjala descansar en el silencio. Si te pierdes en tus pensamientos, la recuerdas con suavidad y vuelves a descansar. No hay un número obligatorio de repeticiones.')}</p></div>
<div class="card"><p class="eyebrow">{L('THE PLATE', 'LA LÁMINA')}</p><h3>{L('An image for the gaze', 'Una imagen para la mirada')}</h3>
<p>{L('Look at it softly, without straining your eyes or analysing every detail. You can contemplate it before closing your eyes or during part of the session. If the image disappears when you close them, that is fine: carry on with the intention, the syllable, or simply being present. And if you have no plate, sound and presence are enough.',
      'Mírala con suavidad, sin forzar los ojos ni analizar cada detalle. Puedes contemplarla antes de cerrar los ojos o durante parte de la sesión. Si al cerrarlos la imagen desaparece, no pasa nada: sigues con la intención, con la sílaba o simplemente presente. Y si no tienes lámina, el sonido y la presencia son suficientes.')}</p>
<p class="note">{L('The plate is for contemplating, not for taking a trace from. When a practice includes tracing, the key&rsquo;s original sign and its verified route are used.', 'La lámina es para contemplar, no para sacar de ella un trazo. Cuando una práctica incluye trazar, se usa el signo original de la llave y su recorrido verificado.')}</p></div>
<div class="card"><p class="eyebrow">{L('THE OBSERVER', 'EL OBSERVADOR')}</p><h3>{L('The awareness that notices', 'La consciencia que se da cuenta')}</h3>
<p>{L('I call the Observer that awareness in you that notices what appears: thoughts, emotions, sensations, memories, images, sounds, silences. Observing is not policing every thought: it is noticing, and kindly coming back when you get distracted. And you do not have to feel separate from your body or your emotions: presence includes them too.',
      'Llamo Observador a esa consciencia en ti que se da cuenta de lo que aparece: pensamientos, emociones, sensaciones, recuerdos, imágenes, sonidos, silencios. Observar no es vigilar cada pensamiento: es darte cuenta y volver con amabilidad cuando te distraes. Y no tienes que sentirte separado de tu cuerpo ni de tus emociones: la presencia también los incluye.')}</p></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('A SESSION, STEP BY STEP', 'UNA SESIÓN, PASO A PASO')}</p>
<h2>{L('The six scenes', 'Las seis escenas')}</h2>
<p>{L('This is what a session looks like, in six simple moments that accompany the five stages of the method.', 'Así se ve una sesión, en seis momentos sencillos que acompañan las cinco etapas del método.')}</p>
</div>
<div class="scenes">
<div><i>1</i><b>{L('The meeting', 'El encuentro')}</b><span>{L('Arrive, feel your body and get to know the key.', 'Llegar, sentir el cuerpo y conocer la llave.')}</span></div>
<div><i>2</i><b>{L('Contemplation', 'La contemplación')}</b><span>{L('Look at the plate softly.', 'Mirar la lámina con suavidad.')}</span></div>
<div><i>3</i><b>{L('The sound', 'El sonido')}</b><span>{L('Say or remember the syllable as indicated.', 'Pronunciar o recordar la sílaba según su indicación.')}</span></div>
<div><i>4</i><b>{L('Turning inward', 'La interiorización')}</b><span>{L('Let attention rest and the sound grow subtle.', 'Dejar que la atención repose y el sonido se vuelva sutil.')}</span></div>
<div><i>5</i><b>{L('Silence', 'El silencio')}</b><span>{L('Rest, without demanding that thoughts disappear.', 'Descansar sin exigir que desaparezcan los pensamientos.')}</span></div>
<div><i>6</i><b>{L('Integration', 'La integración')}</b><span>{L('Come back, and carry one quality into your life.', 'Regresar y llevar una cualidad a la vida.')}</span></div>
</div>
</div></section>

<section><div class="wrap grid2 top">
<div>
<p class="eyebrow">{L('THE METHOD', 'EL MÉTODO')}</p>
<h2>{L('Five stages', 'Cinco etapas')}</h2>
{path([(L('Recognize the quality', 'Reconoce la cualidad'), L('Be clear about your intention and the syllable you chose. Notice how you arrive, how your body is. You can begin even if thoughts or emotions are present.', 'Ten clara tu intención y la sílaba que elegiste. Mira cómo llegas, cómo está tu cuerpo. Puedes empezar aunque haya pensamientos o emociones.')),
       (L('Open the inner relationship', 'Abre la relación interior'), L('Let attention gather. Sound, breath and presence grow simpler. If you get distracted, come back gently.', 'Deja que la atención se recoja. El sonido, la respiración y la presencia se van volviendo más sencillos. Si te distraes, vuelve con suavidad.')),
       (L('Make room for the descent', 'Da lugar al descenso'), L('Let the quality you contemplate touch your human, bodily experience: from the mind to the heart, to vitality, to the root and to the body. You do not have to visualize or feel something in each place.', 'Permite que la cualidad que contemplas toque tu experiencia humana y corporal: de la mente al corazón, a la vitalidad, a la raíz y al cuerpo. No tienes que visualizar ni sentir algo en cada lugar.')),
       (L('Observe and allow', 'Observa y permite'), L('Give room to what appears. The syllable may grow faint: rest without chasing it. If an emotion arises, recognize it without forcing it to grow. If something becomes too much, open your eyes, look around you and stop the practice.', 'Dale espacio a lo que aparece. La sílaba puede volverse tenue: descansa sin perseguirla. Si surge una emoción, reconócela sin forzarla a crecer. Si algo se vuelve demasiado, abre los ojos, mira a tu alrededor y detén la práctica.')),
       (L('Return and integrate', 'Regresa e integra'), L('Feel your hands, your feet, your breath and the sounds of the place again. Move gently and open your eyes at your own pace. Integration continues when what you contemplated becomes a gesture in your day.', 'Siente otra vez tus manos, tus pies, tu respiración y los sonidos del lugar. Muévete con suavidad y abre los ojos a tu ritmo. La integración continúa cuando lo que contemplaste se vuelve un gesto en tu día.'))])}
</div>
<div>
<p class="eyebrow">{L('BEFORE YOU BEGIN', 'ANTES DE EMPEZAR')}</p>
<h2>{L('Begin from where you are', 'Comienza desde donde estás')}</h2>
<p>{L('Find a corner where you can be quiet for a few minutes. If you use a plate, place it at a comfortable distance; if it is on a screen, lower the brightness so it does not tire your eyes. Sit on a chair or a stable support, back upright but not rigid, hands resting, feet or seat as your support. No posture should hurt. Recognize your breath as it comes and soften your face and shoulders. Preparing is simply recognizing how you are and allowing yourself to begin from there.',
      'Busca un rincón donde puedas estar unos minutos con tranquilidad. Si usas una lámina, ponla a una distancia cómoda; si está en una pantalla, baja el brillo para no cansar la vista. Siéntate en una silla o en un apoyo estable, con la espalda derecha pero sin rigidez, las manos en reposo y los pies o el asiento como apoyo. Ninguna postura tiene que doler. Reconoce tu respiración tal como llega y suaviza la cara y los hombros. Prepararte es simplemente reconocer cómo estás y permitirte empezar desde ahí.')}</p>
<h3>{L('How long?', '¿Cuánto tiempo?')}</h3>
<p>{L('Begin small and regularly. Five or ten minutes is a good start; fifteen or twenty if you feel comfortable. These times do not measure your depth and are not a requirement. Give yourself a moment to arrive and a minute or two to return. A fairly fixed time and place help. Constancy grows by coming back, not by competing.',
      'Empieza con poco y con regularidad. Cinco o diez minutos son un buen comienzo; quince o veinte, si te sientes cómodo. Estos tiempos no miden tu profundidad ni son un requisito. Date un momento para llegar y uno o dos minutos para regresar. Un horario y un lugar más o menos fijos ayudan. La constancia se cultiva volviendo, no compitiendo.')}</p>
<h3>{L('Silence', 'El silencio')}</h3>
<p>{L('Silence is the heart of this meditation. The syllable orients and then leaves room; it does not have to be held by force for the session to have meaning. There can be thoughts and sounds and, even so, rest. When you notice you have gone off after a mental story, return once to the sound or the body, and rest again. That is how attention learns to come back without fighting itself.',
      'El silencio es el corazón de esta meditación. La sílaba orienta y después deja espacio; no hace falta sostenerla a la fuerza para que la sesión tenga sentido. Puede haber pensamientos y sonidos y, aun así, descanso. Cuando notes que te fuiste detrás de una historia mental, vuelve una vez al sonido o al cuerpo, y descansa de nuevo. Así la atención aprende a regresar sin pelear consigo misma.')}</p>
</div>
</div></section>

<section class="dark"><div class="wrap grid2">
<figure class="ahr"><img src="/assets/img/ahr_glow.webp" alt="AHR"></figure>
<div>
<p class="eyebrow">{L('THE FIRST SYLLABLE', 'LA SÍLABA INICIAL')}</p>
<h2>AHR · <span style="color:var(--gold2)">ÁR</span></h2>
<p><em>{L('Opening and anchoring of the primordial Flame.', 'Apertura y anclaje de la Llama primordial.')}</em> {L('In the Codex it relates to the centres of the root, the heart and the crown. In the book I use it to teach you how to prepare the body, contemplate, bring in the sound and rest. To begin:', 'En el Códice se relaciona con los centros de la raíz, del corazón y de la corona. En el libro la uso para enseñarte a preparar el cuerpo, contemplar, introducir el sonido y descansar. Para comenzar:')}</p>
<ul class="benefits" style="columns:1">
<li>{L('Remember ÁR inwardly during a soft inhalation.', 'Recuerda interiormente ÁR durante una inhalación suave.')}</li>
<li>{L('Let any pause be natural.', 'Permite que cualquier pausa sea natural.')}</li>
<li>{L('As you exhale, let your attention go along the spine down to where your body rests.', 'Al exhalar, acompaña con la atención el eje de la columna hacia el apoyo del cuerpo.')}</li>
<li>{L('Do not force your throat or hold your breath.', 'No fuerces la garganta ni retengas el aire.')}</li>
<li>{L('Then leave room for silence.', 'Después deja espacio para el silencio.')}</li>
</ul>
<p class="note" style="color:#CFC6E2">{L('This guidance belongs to AHR; each syllable has its own.', 'Esta indicación es propia de AHR; cada sílaba tiene la suya.')}</p>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">{L('A GUIDED MOMENT WITH AHR', 'UN MOMENTO GUIADO CON AHR')}</p>
<h2>{L('Meditate with me', 'Medita conmigo')}</h2>
<div class="script">
<p>{L('Sit comfortably.<br>Let your weight find its support.<br>Feel your hands, your feet and the seat.', 'Siéntate con comodidad.<br>Permite que el peso encuentre su apoyo.<br>Siente las manos, los pies y el asiento.')}</p>
<p>{L('Recognize one breath.<br>Let the next one come.', 'Reconoce una respiración.<br>Deja que llegue la siguiente.')}</p>
<p>{L('Remember the intention of opening and presence.', 'Recuerda la intención de apertura y presencia.')}</p>
<p>{L('If you have the plate, look at it softly.<br>Receive the image as a whole.<br>You may close your eyes when it feels comfortable.', 'Si tienes la lámina, mírala suavemente.<br>Recibe el conjunto de la imagen.<br>Puedes cerrar los ojos cuando te resulte cómodo.')}</p>
<p>{L('Remember ÁR inwardly during a soft inhalation.<br>As you exhale, let your attention go<br>along the spine down to where your body rests.', 'Recuerda interiormente ÁR durante una inhalación suave.<br>Al exhalar, permite que la atención acompañe<br>el eje de la columna hacia el apoyo del cuerpo.')}</p>
<p>{L('Now leave room.<br>You do not need to hold the sound.<br>Stay with what appears.', 'Deja ahora espacio.<br>No necesitas sostener el sonido.<br>Permanece con lo que aparece.')}</p>
<p>{L('If you notice you are following a thought, come back kindly.<br>You may remember ÁR softly and let it rest again.', 'Si adviertes que estás siguiendo un pensamiento, vuelve con amabilidad.<br>Puedes recordar suavemente ÁR y dejarlo descansar otra vez.')}</p>
<p>{L('Remain a few moments in silence.', 'Permanece unos momentos en silencio.')}</p>
<p>{L('When it is time to finish, feel your hands and feet.<br>Listen to the sounds of the place.<br>Move your body gently. Open your eyes at your own pace.', 'Cuando sea tiempo de terminar, reconoce las manos y los pies.<br>Escucha los sonidos del lugar.<br>Mueve el cuerpo suavemente. Abre los ojos a tu ritmo.')}</p>
<p>{L('Before you go on, recognize one simple gesture of presence you can carry into your day.', 'Antes de continuar, reconoce un gesto sencillo de presencia que puedas llevar a tu día.')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('CHOOSING THE SYLLABLE', 'CÓMO ELEGIR LA SÍLABA')}</p>
<h2>{L('Where do I begin?', '¿Por cuál empiezo?')}</h2>
<p>{L('Begin with your life, not with the list. Ask yourself: <em>What needs attention right now? Do I need clarity, serenity, direction, receptivity, rootedness, or a more conscious way of relating to what I feel?</em> Then look at the study page of that syllable and talk it over with whoever accompanies you. The first practice uses AHR, to learn the way.',
      'Empieza por tu vida, no por la lista. Pregúntate: <em>¿qué necesita atención en este momento? ¿Necesito claridad, serenidad, dirección, receptividad, arraigo, o una forma más consciente de relacionarme con lo que siento?</em> Después se consulta la ficha de esa sílaba y lo conversas con quien te acompaña. La práctica inicial usa AHR para aprender el recorrido.')}</p>
<p>{L('The book gathers the 33 syllables at the heart of the Codex, but their order is not a calendar and you do not have to go through them all. These are some of the ones I present in the guide; they are chosen according to your intention, not recited all together:',
      'El libro reúne las 33 sílabas del corazón del Códice, pero su orden no es un calendario ni tienes que recorrerlas todas. Estas son algunas de las que presento en la guía; se eligen según la intención, no se recitan todas juntas:')}</p>
</div>
<div class="syl">{''.join(f'<div><b>{a}</b><em>{p}</em><span>{q}</span></div>' for a, p, q in syl)}</div>
<p class="note center">{L('Each one keeps the indications of its own study page. A Support syllable can be contemplated on its own without becoming a Core within a triad.', 'Cada una conserva las indicaciones de su propia ficha. Una sílaba de Soporte puede contemplarse sola sin convertirse por eso en Núcleo dentro de una tríada.')}</p>
</div></section>

<section><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('FROM ONE SYLLABLE TO A TRIAD', 'DE UNA SÍLABA A UNA TRÍADA')}</p>
<h2>{L('Your first triad: settling into deep stillness', 'Tu primera tríada: asentarte en una quietud profunda')}</h2>
<p>{L('Once a simple practice feels familiar, you can get to know the combinations. The first one I teach, for settling into deep stillness, is:', 'Cuando una práctica sencilla ya te es familiar, puedes conocer las combinaciones. La primera que enseño, para asentarte en una quietud profunda, es:')}</p>
</div>
<div class="triad">
<div><span class="dot">I</span><b>AHR</b><em>{L('Core', 'Núcleo')} · ÁR</em><p>{L('Opens and orients: opening and anchoring.', 'Abre y orienta: apertura y anclaje.')}</p></div>
<i>→</i>
<div><span class="dot">II</span><b>DRO’VAL</b><em>{L('Support', 'Soporte')} · DRO-VAL</em><p>{L('Holds: foundation, rooting and consolation.', 'Sostiene: fundamento, enraizamiento y consuelo.')}</p></div>
<i>→</i>
<div><span class="dot">III</span><b>ZEN’LUM</b><em>{L('Seal', 'Sello')} · SEN-LUM</em><p>{L('Closes: stillness and completion.', 'Cierra: quietud y cierre.')}</p></div>
</div>
<div class="narrow" style="padding:0">
<p>{L('In the guide you become familiar with its sound in that order, with comfortable pauses, and then you rest. There is no required number of repetitions. This is different from the full ritual with traces: when the traced invocation is performed, the verified signs of the three keys are used, with their own instructions. Triads are studied with accompaniment, respecting the role of each key.',
      'En la guía te familiarizas con su sonido en ese orden, con pausas cómodas, y después descansas. No hay un número obligatorio de repeticiones. Esto es distinto del ritual completo con trazos: cuando se hace la invocación trazada, se usan los signos verificados de las tres llaves, con sus propias instrucciones. Las tríadas se estudian con acompañamiento y respetando el papel de cada llave.')}</p>
</div>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">{L('WHAT MAY HAPPEN', 'LO QUE PUEDE PASAR')}</p>
<h2>{L('Every session is different', 'Cada sesión es distinta')}</h2>
<p>{L('There may be stillness, distraction, emotion, sensations in the body, or a session that feels completely ordinary. No phenomenon proves you went deeper.', 'Puede haber quietud, distracción, emoción, sensaciones en el cuerpo, o una sesión que se sienta completamente normal. Ningún fenómeno demuestra que fuiste más profundo.')}</p>
<div class="faq">{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)}</div>
</div></section>

<section><div class="wrap grid2 top">
<div>
<p class="eyebrow">{L('AFTER MEDITATING', 'DESPUÉS DE MEDITAR')}</p>
<h2>{L('Meditation continues in your day', 'La meditación continúa en tu día')}</h2>
<p>{L('When you finish, you can ask yourself: <em>What did I observe? What meaning do I give it? What simple gesture could express today the quality I contemplated?</em> For example:', 'Al terminar, puedes preguntarte: <em>¿Qué observé? ¿Qué significado le doy? ¿Qué gesto sencillo puede expresar hoy la cualidad que contemplé?</em> Por ejemplo:')}</p>
<div class="heart3">
<div><b>{L('Clarity', 'Claridad')}</b><span>{L('say something honestly', 'decir algo con honestidad')}</span></div>
<div><b>{L('Serenity', 'Serenidad')}</b><span>{L('listen without hurrying to answer', 'escuchar sin apresurarte a responder')}</span></div>
<div><b>{L('Rootedness', 'Arraigo')}</b><span>{L('take care of one concrete task', 'atender una tarea concreta')}</span></div>
<div><b>{L('Devotion', 'Devoción')}</b><span>{L('offer a gesture of gratitude or care', 'ofrecer un gesto de gratitud o de cuidado')}</span></div>
<div><b>{L('Discernment', 'Discernimiento')}</b><span>{L('recognize a decision that needs more information, or a clear limit', 'reconocer una decisión que necesita más información, o un límite claro')}</span></div>
</div>
<p>{L('Let it be something possible and concrete. You do not need to repeat the syllable all day: the quality can stay alive after the sound has ended.', 'Que sea algo posible y concreto. No necesitas repetir la sílaba todo el día: la cualidad puede seguir viva cuando el sonido ya terminó.')}</p>
</div>
<div>
<p class="eyebrow">{L('A SMALL JOURNAL', 'UN PEQUEÑO DIARIO')}</p>
<h2>{L('What you observe, and what you interpret', 'Lo que observas y lo que interpretas')}</h2>
<table class="cred log"><tr><td>{L('Date', 'Fecha')}</td><td></td></tr><tr><td>{L('Approximate duration', 'Duración aproximada')}</td><td></td></tr><tr><td>{L('Syllable or triad', 'Sílaba o tríada')}</td><td></td></tr><tr><td>{L('Intention', 'Intención')}</td><td></td></tr><tr><td>{L('What I observed', 'Lo que observé')}</td><td></td></tr><tr><td>{L('How I interpret it', 'Cómo lo interpreto')}</td><td></td></tr><tr><td>{L('Gesture of integration', 'Gesto de integración')}</td><td></td></tr></table>
<p>{L('It helps to tell what you observe from what you interpret. &ldquo;I felt warmth in my chest&rdquo; is a sensation; &ldquo;I think it has to do with an emotion&rdquo; is an interpretation. That way you recognize changes without crediting everything to the practice.', 'Ayuda distinguir lo que observas de lo que interpretas. &laquo;Sentí calor en el pecho&raquo; es una sensación; &laquo;creo que tiene que ver con una emoción&raquo; es una interpretación. Así reconoces los cambios sin atribuirle todo a la práctica.')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img src="{BK}meditacion_codigos_luz.webp?v=3d" alt="Meditación de Códigos de Luz" style="max-height:440px;width:auto;margin:0 auto"></figure>
<div>
<p class="eyebrow">{L('ACTIVATION AND ACCOMPANIMENT', 'ACTIVACIÓN Y ACOMPAÑAMIENTO')}</p>
<h2>{L('When you want to go deeper', 'Cuando quieras ir más hondo')}</h2>
<p>{L('The basic meditation and the observation I teach in the book are open to everyone. When you wish to practise formally with a code, the path begins with its activation, received from a Guardian or Bearer of the Flame authorized to transmit it. Looking at the image or learning the sound does not replace it, and activation is not measured by how intensely you feel something.',
      'La meditación básica y la observación que enseño en el libro están abiertas para todos. Cuando desees practicar formalmente con un código, el camino comienza con su activación, que se recibe de un Guardián o Portador de la Llama autorizado para transmitirla. Mirar la imagen o aprender el sonido no la sustituye, y la activación no se mide por lo intenso que sientas algo.')}</p>
<p>{L('Accompaniment helps you know which syllable to begin with, its intention, how to pronounce it, its particular indications, how to continue, and what to do with the questions or difficulties that come up. Meanwhile, you can study the material and continue with your basic meditation.',
      'El acompañamiento te ayuda a saber con qué sílaba empezar, cuál es su intención, cómo se pronuncia, qué indicaciones tiene, cómo seguir y qué hacer con las dudas o dificultades que aparezcan. Mientras tanto, puedes estudiar el material y seguir con tu meditación básica.')}</p>
<div class="btns" style="justify-content:flex-start"><a class="btn solid" href="{url(lang, 'contact')}">{L('Ask about activation', 'Pregunta por la activación')}</a><a class="btn" href="https://www.spiritualbalanceinfo.com{'/es/' if not en else '/'}">{L('Sessions in Weston ↗', 'Sesiones en Weston ↗')}</a></div>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<p>{L('I share this meditation as a contemplative and spiritual practice. When I speak of light, frequency, the causal body or descent, I am speaking the language of the spirit, and I always leave room for your experience to be your own.', 'Comparto esta meditación como una práctica contemplativa y espiritual. Cuando hablo de luz, de frecuencia, de cuerpo causal o de descenso, hablo el lenguaje del espíritu, y dejo siempre espacio para que tu experiencia sea tuya.')}</p>
<blockquote style="border:0;padding:0">{L('The crown receives. The heart translates.<br>The root incarnates. Life demonstrates.', 'La corona recibe. El corazón traduce.<br>La raíz encarna. La vida demuestra.')}</blockquote>
<p><a class="btn" href="{url(lang, 'codex')}">{L('← Back to the Codex', '← Volver al Códice')}</a></p>
</div></section>
'''
