/* Health is an editorial layer. It references, and never rewrites, source triads. */
(function(root){'use strict';
 const normalize=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
 function search(data,query='',category=''){
  const q=normalize(query);
  return data.entries.filter(e=>!category||e.category===category).map(entry=>{
   const terms=[entry.title,...entry.aliases].map(normalize);
   let score=q?0:1;
   for(const term of terms){
    if(q===term)score=Math.max(score,100);
    else if(q&&(' '+q+' ').includes(' '+term+' '))score=Math.max(score,70+term.length/100);
    else if(q.length>=3&&(' '+term).includes(' '+q))score=Math.max(score,40);
   }
   return {entry,score};
  }).filter(h=>h.score>0).sort((a,b)=>b.score-a.score||a.entry.title.localeCompare(b.entry.title,'es')).map(h=>h.entry);
 }
 function create(data,engine,ui){
  const {esc,codeCard,reference}=ui;
  const entries=new Map(data.entries.map(e=>[e.id,e]));
  const intents=new Map(data.intents.map(e=>[e.id,e]));
  const state={query:'',category:'',page:1};
  const route=(e,i)=>'#salud='+e.id+(i?':'+i.id:'');
  const card=e=>`<a class="topic health-topic" href="${route(e)}"><span class="tag">${esc(e.category)}</span><h3>${esc(e.title)}</h3><p>${esc(e.reflectionHeading)}</p><small>Abrir la reflexión y elegir una intención ↗</small></a>`;
  function searchSection(query){
   if(!String(query||'').trim())return '';
   const matches=search(data,query);
   if(!matches.length)return '';
   return `<section class="health-search-section" aria-label="Entradas del diccionario de salud"><div class="section-head"><p class="eyebrow">DICCIONARIO DE ESCUCHA INTERIOR</p><h2>Salud · entradas relacionadas</h2><p>Abre el tema y elige qué experiencia interior deseas acompañar.</p></div><div class="topic-grid">${matches.slice(0,6).map(card).join('')}</div><a class="text-link" href="#salud">Ver las ${data.entries.length} entradas del diccionario →</a></section>`;
  }
  function results(){
   const hits=search(data,state.query,state.category),pages=Math.max(1,Math.ceil(hits.length/24));state.page=Math.min(state.page,pages);const visible=hits.slice((state.page-1)*24,state.page*24);
   return `<p class="catalog-summary" role="status">${hits.length} ${hits.length===1?'entrada':'entradas'}${state.query?' '+(hits.length===1?'relacionada':'relacionadas')+' con «'+esc(state.query)+'»':''}</p>${hits.length?`<div class="topic-grid">${visible.map(card).join('')}</div>${pages>1?`<div class="health-pager"><button class="btn secondary small" data-health-page="${state.page-1}" ${state.page===1?'disabled':''}>← Anterior</button><span>${state.page} / ${pages}</span><button class="btn secondary small" data-health-page="${state.page+1}" ${state.page===pages?'disabled':''}>Siguiente →</button></div>`:''}`:`<div class="empty"><h2>Esta entrada todavía está por desarrollar.</h2><p>El diccionario comienza con ${data.entries.length} temas. Puedes probar otro nombre o explorar una intención en los libros.</p><div class="actions"><button class="btn secondary" data-health-clear>Ver todas las entradas</button><a class="btn" href="#guia">Explorar una intención</a></div></div>`}`;
  }
  function index(){
   const categories=[...new Set(data.entries.map(e=>e.category))].sort((a,b)=>a.localeCompare(b,'es'));
   return `<section class="wrap"><a class="crumb" href="#inicio">← Inicio</a><div class="health-heading"><div><p class="eyebrow">CÓDIGOS DE LUZ PARA TU SALUD</p><h1>Un espacio para <br>escucharte.</h1><p class="lead">${esc(data.meta.opening)}</p><p>Busca una condición, abre sus preguntas y elige la intención que deseas acompañar con los Códigos de Luz.</p><p class="micro">Primera colección · ${data.entries.length} entradas · propuesta editorial para revisión del autor.</p></div><aside class="health-invitation"><span aria-hidden="true">✦</span><p>¿Qué pide<br>atención en mí<br>hoy?</p><small>LA LLAMA EN TU EXPERIENCIA</small></aside></div><p class="health-framework">${esc(data.meta.framework)}</p><form id="health-search-form" class="health-filters"><div><label class="field-label" for="health-query">Nombre de la condición o término relacionado</label><div class="search-row"><input id="health-query" type="search" maxlength="120" value="${esc(state.query)}" placeholder="Migraña, insomnio, artritis…"><button class="btn" type="submit">Buscar →</button></div></div><div><label class="field-label" for="health-category">Área</label><select id="health-category"><option value="">Todas las áreas</option>${categories.map(c=>`<option value="${esc(c)}" ${state.category===c?'selected':''}>${esc(c)}</option>`).join('')}</select></div></form><div id="health-results">${results()}</div><div class="health-editorial"><h2>Una lectura personal</h2><p>Cada ficha reúne una definición general, preguntas originales y una invitación a la contemplación. El significado que encuentres pertenece a tu experiencia. La intención que elijas abre una tríada documentada en los libros.</p><a class="text-link" href="#fuentes">Consultar fuentes y alcance →</a></div></section>`;
  }
  function chosen(entry,intent){
   const f=engine.formulas.get(intent.formulaId),context=engine.entries.get(f.entryId);
   return `<section class="health-selection" aria-labelledby="health-intention-title"><p class="eyebrow">TU INTENCIÓN ELEGIDA</p><h2 id="health-intention-title">${esc(intent.title)}</h2><p>${esc(intent.description)}</p><p class="formula-line">${f.names.map(esc).join(' → ')}</p><div class="health-source-reason"><p><b>Por qué se presenta esta tríada</b></p><p>${esc(intent.sourceRationale)} Aparece aquí por la intención que acabas de elegir.</p><p class="source-mini">${esc(reference(context,f.page))} · ${esc(f.label)}.</p></div><div class="code-grid">${f.codes.map(codeCard).join('')}</div><section class="practice"><div><p class="eyebrow">LA LLAMA EN TU VIDA</p><h2>Recibir.<br>Escuchar.<br>Dar un paso.</h2><p class="micro">Invitación contemplativa de esta ficha.</p></div><div><ol><li><b>Llega a tu momento.</b> Elige una posición cómoda y deja la respiración a su ritmo natural.</li><li><b>Contempla la secuencia.</b> Mira las tres láminas y sus sigilos en el orden mostrado. Puedes recibir sus nombres en silencio y seguir la práctica del libro cuando quieras profundizar.</li><li><b>Recibe tu experiencia.</b> Elige una de las preguntas anteriores. Da espacio a lo que aparezca; también puedes quedarte sencillamente en silencio.</li><li><b>Llévalo a tu vida.</b> Escribe una necesidad, una pregunta o un gesto que quieras compartir. Decide un paso pequeño y posible para hoy.</li></ol></div></section><div class="actions"><a class="btn secondary" href="#tema=${context.id}">Leer la práctica en el libro →</a><button class="btn secondary" data-action="print">Imprimir / guardar PDF</button><button class="btn" data-health-save="${entry.id}:${intent.id}">Guardar reflexión</button></div><p class="micro">La reflexión pertenece a la nueva propuesta de Salud. La fórmula y las imágenes conservan su procedencia en los libros.</p></section>`;
  }
  function detail(entry,intentId){
   const intent=intents.get(intentId);const suggested=(entry.suggestedIntents||['claridad','compasion','apoyo']).map(id=>intents.get(id)).filter(Boolean);const more=data.intents.filter(i=>!suggested.some(s=>s.id===i.id));const intentLink=i=>{const f=engine.formulas.get(i.formulaId);return `<a class="health-intent ${intent?.id===i.id?'selected':''}" href="${route(entry,i)}" ${intent?.id===i.id?'aria-current="true"':''}><strong>${esc(i.title)}</strong><span>${esc(i.description)}</span><span class="health-theme-codes">${f.names.map(esc).join(' → ')}</span>${intent?.id===i.id?'<small>Intención elegida ✓</small>':''}</a>`;};
   return `<section class="wrap health-detail"><a class="crumb" href="#salud">← Diccionario de escucha interior</a><div class="page-top"><p class="eyebrow">SALUD · ${esc(entry.category)}</p><h1>${esc(entry.title)}</h1><p>${esc(entry.reflectionHeading)}</p></div><div class="health-context"><section><p class="eyebrow">PARA SITUAR LA PALABRA</p><p>${esc(entry.definition)}</p><a class="source-mini" href="${esc(entry.source.url)}" target="_blank" rel="noopener noreferrer">${esc(entry.source.organization)} · ${esc(entry.source.title)} ↗</a></section><section><p class="eyebrow">LA LLAMA EN TU EXPERIENCIA</p><p>${esc(entry.reflection)}</p></section></div><div class="health-reflection"><div><p class="eyebrow">PREGUNTAS PARA ESCUCHARTE</p><h2>Acércate a lo que<br>estás viviendo.</h2><p>Elige una pregunta. Dale el tiempo y el significado que tenga para ti.</p></div><ol>${entry.questions.map(q=>`<li>${esc(q)}</li>`).join('')}</ol></div><blockquote class="health-phrase">«${esc(entry.phrase)}»<span>UNA FRASE PARA CONTEMPLAR · PUEDES HACERLA TUYA</span></blockquote><section class="health-intents" aria-labelledby="choose-intent"><p class="eyebrow">TEMAS QUE PUEDES EXPLORAR</p><h2 id="choose-intent">¿Qué reconoces en tu experiencia?</h2><p>Estos son posibles puntos de partida. Elige el tema que tenga sentido para ti o explora otras intenciones.</p><div class="health-intent-grid">${suggested.map(intentLink).join('')}</div><details class="health-more" ${intent&&more.some(i=>i.id===intent.id)?'open':''}><summary>Explorar otras ${more.length} intenciones</summary><div class="health-intent-grid">${more.map(intentLink).join('')}</div></details></section>${intent?chosen(entry,intent):'<div class="health-prompt">Elige una intención para ver su tríada, sus tres láminas y sus sigilos 2D.</div>'}<p class="source-mini">Reflexión original · propuesta editorial para Zuluan Orion. Definición general consultada el ${esc(entry.source.verifiedDate)}.</p></section>`;
  }
  function render(id){
   if(!id)return index();
   const [entryId,intentId]=String(id).split(':');
   const entry=entries.get(entryId);
   if(!entry)return `<section class="wrap"><div class="empty"><h1>Esta entrada todavía está por desarrollar.</h1><a class="btn" href="#salud">Abrir el diccionario</a></div></section>`;
   return detail(entry,intentId);
  }
  function textFor(entryId,intentId){
   const e=entries.get(entryId),i=intents.get(intentId);if(!e||!i)return '';
   const f=engine.formulas.get(i.formulaId),context=engine.entries.get(f.entryId);
   return ['CÓDIGOS DE LUZ PARA TU SALUD · DICCIONARIO DE ESCUCHA INTERIOR','Propuesta editorial para revisión de Zuluan Orion','',e.title,e.definition,e.source.organization,e.source.url,'','LA LLAMA EN TU EXPERIENCIA',e.reflection,'','PREGUNTAS',...e.questions,'',e.phrase,'','INTENCIÓN ELEGIDA',i.title,i.description,f.names.join(' → '),i.sourceRationale,'',reference(context,f.page),'',...f.codes.map((id,n)=>['Núcleo','Sostén','Sello'][n]+': '+engine.codes.get(id).name),'','Escribe una necesidad, una pregunta o un gesto que quieras compartir. Decide un paso pequeño y posible para hoy.'].join('\n');
  }
  function update(){
   const input=document.querySelector('#health-query'),category=document.querySelector('#health-category'),box=document.querySelector('#health-results');
   if(!input||!category||!box)return;
   state.query=input.value.trim();state.category=category.value;state.page=1;box.innerHTML=results();
  }
  if(typeof document!=='undefined'){
   document.addEventListener('submit',event=>{if(event.target.id==='health-search-form'){event.preventDefault();update();}});
   document.addEventListener('input',event=>{if(event.target.id==='health-query')update();});
   document.addEventListener('change',event=>{if(event.target.id==='health-category')update();});
   document.addEventListener('click',event=>{
    const page=event.target.closest('[data-health-page]');if(page){state.page=Number(page.dataset.healthPage);document.querySelector('#health-results').innerHTML=results();document.querySelector('#health-results').scrollIntoView({block:'start'});return;}
    const clear=event.target.closest('[data-health-clear]');if(clear){state.query='';state.category='';document.querySelector('#health-query').value='';document.querySelector('#health-category').value='';update();return;}
    const save=event.target.closest('[data-health-save]');if(save){const [e,i]=save.dataset.healthSave.split(':');const txt=textFor(e,i);if(!txt)return;const url=URL.createObjectURL(new Blob([txt],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='Reflexion_'+e+'_'+i+'.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1500);}
   });
  }
  return {render,searchSection,textFor,search:q=>search(data,q),count:data.entries.length};
 }
 const api={search,create,normalize};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 else root.HealthDictionary=api;
})(typeof window!=='undefined'?window:globalThis);
