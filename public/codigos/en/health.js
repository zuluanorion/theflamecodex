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
  }).filter(h=>h.score>0).sort((a,b)=>b.score-a.score||a.entry.title.localeCompare(b.entry.title,'en')).map(h=>h.entry);
 }
 function create(data,engine,ui){
  const {esc,codeCard,reference}=ui;
  const entries=new Map(data.entries.map(e=>[e.id,e]));
  const intents=new Map(data.intents.map(e=>[e.id,e]));
  const state={query:'',category:'',page:1};
  const route=(e,i)=>'#salud='+e.id+(i?':'+i.id:'');
  const card=e=>`<a class="topic health-topic" href="${route(e)}"><span class="tag">${esc(e.category)}</span><h3>${esc(e.title)}</h3><p>${esc(e.reflectionHeading)}</p><small>Open the reflection and choose an intention ↗</small></a>`;
  function searchSection(query){
   if(!String(query||'').trim())return '';
   const matches=search(data,query);
   if(!matches.length)return '';
   return `<section class="health-search-section" aria-label="Health dictionary entries"><div class="section-head"><p class="eyebrow">INNER LISTENING DICTIONARY</p><h2>Health · related entries</h2><p>Open the topic and choose the inner experience you would like to accompany.</p></div><div class="topic-grid">${matches.slice(0,6).map(card).join('')}</div><a class="text-link" href="#salud">View all ${data.entries.length} dictionary entries →</a></section>`;
  }
  function results(){
   const hits=search(data,state.query,state.category),pages=Math.max(1,Math.ceil(hits.length/24));state.page=Math.min(state.page,pages);const visible=hits.slice((state.page-1)*24,state.page*24);
   return `<p class="catalog-summary" role="status">${hits.length} ${hits.length===1?'entry':'entries'}${state.query?' '+(hits.length===1?'related':'related')+' to “'+esc(state.query)+'”':''}</p>${hits.length?`<div class="topic-grid">${visible.map(card).join('')}</div>${pages>1?`<div class="health-pager"><button class="btn secondary small" data-health-page="${state.page-1}" ${state.page===1?'disabled':''}>← Previous</button><span>${state.page} / ${pages}</span><button class="btn secondary small" data-health-page="${state.page+1}" ${state.page===pages?'disabled':''}>Next →</button></div>`:''}`:`<div class="empty"><h2>This entry is still to be developed.</h2><p>The dictionary begins with ${data.entries.length} topics. Try another name or explore an intention in the books.</p><div class="actions"><button class="btn secondary" data-health-clear>View all entries</button><a class="btn" href="#guia">Explore an intention</a></div></div>`}`;
  }
  function index(){
   const categories=[...new Set(data.entries.map(e=>e.category))].sort((a,b)=>a.localeCompare(b,'en'));
   return `<section class="wrap"><a class="crumb" href="#inicio">← Home</a><div class="health-heading"><div><p class="eyebrow">CODES OF LIGHT FOR YOUR HEALTH</p><h1>A space to <br>listen within.</h1><p class="lead">${esc(data.meta.opening)}</p><p>Find a condition, explore its questions, and choose the intention you would like to accompany with the Codes of Light.</p><p class="micro">Initial collection · ${data.entries.length} entries · editorial proposal for the author’s review.</p></div><aside class="health-invitation"><span aria-hidden="true">✦</span><p>What in me<br>needs attention<br>today?</p><small>THE FLAME IN YOUR EXPERIENCE</small></aside></div><p class="health-framework">${esc(data.meta.framework)}</p><form id="health-search-form" class="health-filters"><div><label class="field-label" for="health-query">Condition name or related term</label><div class="search-row"><input id="health-query" type="search" maxlength="120" value="${esc(state.query)}" placeholder="Migraine, insomnia, arthritis…"><button class="btn" type="submit">Search →</button></div></div><div><label class="field-label" for="health-category">Area</label><select id="health-category"><option value="">All areas</option>${categories.map(c=>`<option value="${esc(c)}" ${state.category===c?'selected':''}>${esc(c)}</option>`).join('')}</select></div></form><div id="health-results">${results()}</div><div class="health-editorial"><h2>A personal reading</h2><p>Each entry brings together a general definition, original questions, and an invitation to contemplation. The meaning you find belongs to your experience. Your chosen intention opens a triad documented in the books.</p><a class="text-link" href="#fuentes">View sources and scope →</a></div></section>`;
  }
  function chosen(entry,intent){
   const f=engine.formulas.get(intent.formulaId),context=engine.entries.get(f.entryId);
   return `<section class="health-selection" aria-labelledby="health-intention-title"><p class="eyebrow">YOUR CHOSEN INTENTION</p><h2 id="health-intention-title">${esc(intent.title)}</h2><p>${esc(intent.description)}</p><p class="formula-line">${f.names.map(esc).join(' → ')}</p><div class="health-source-reason"><p><b>Why this triad is shown</b></p><p>${esc(intent.sourceRationale)} It appears here because of the intention you just chose.</p><p class="source-mini">${esc(reference(context,f.page))} · ${esc(f.label)}.</p></div><div class="code-grid">${f.codes.map(codeCard).join('')}</div><section class="practice"><div><p class="eyebrow">THE FLAME IN YOUR LIFE</p><h2>Receive.<br>Listen.<br>Take a step.</h2><p class="micro">A contemplative invitation from this entry.</p></div><div><ol><li><b>Arrive in your moment.</b> Choose a comfortable position and let your breath follow its natural rhythm.</li><li><b>Contemplate the sequence.</b> View the three plates and their sigils in the order shown. You may receive their names in silence and follow the practice in the book when you wish to go deeper.</li><li><b>Receive your experience.</b> Choose one of the questions above. Give room to whatever arises; you may also simply remain in silence.</li><li><b>Bring it into your life.</b> Write a need, a question, or a gesture you want to share. Choose a small, achievable step for today.</li></ol></div></section><div class="actions"><a class="btn secondary" href="#tema=${context.id}">Read the practice in the book →</a><button class="btn secondary" data-action="print">Print / save PDF</button><button class="btn" data-health-save="${entry.id}:${intent.id}">Save reflection</button></div><p class="micro">The reflection belongs to the new Health proposal. The formula and images retain their provenance in the books.</p></section>`;
  }
  function detail(entry,intentId){
   const intent=intents.get(intentId);const suggested=(entry.suggestedIntents||['claridad','compasion','apoyo']).map(id=>intents.get(id)).filter(Boolean);const more=data.intents.filter(i=>!suggested.some(s=>s.id===i.id));const intentLink=i=>{const f=engine.formulas.get(i.formulaId);return `<a class="health-intent ${intent?.id===i.id?'selected':''}" href="${route(entry,i)}" ${intent?.id===i.id?'aria-current="true"':''}><strong>${esc(i.title)}</strong><span>${esc(i.description)}</span><span class="health-theme-codes">${f.names.map(esc).join(' → ')}</span>${intent?.id===i.id?'<small>Chosen intention ✓</small>':''}</a>`;};
   return `<section class="wrap health-detail"><a class="crumb" href="#salud">← Inner listening dictionary</a><div class="page-top"><p class="eyebrow">HEALTH · ${esc(entry.category)}</p><h1>${esc(entry.title)}</h1><p>${esc(entry.reflectionHeading)}</p></div><div class="health-context"><section><p class="eyebrow">UNDERSTANDING THE TERM</p><p>${esc(entry.definition)}</p><a class="source-mini" href="${esc(entry.source.url)}" target="_blank" rel="noopener noreferrer">${esc(entry.source.organization)} · ${esc(entry.source.title)} ↗</a></section><section><p class="eyebrow">THE FLAME IN YOUR EXPERIENCE</p><p>${esc(entry.reflection)}</p></section></div><div class="health-reflection"><div><p class="eyebrow">QUESTIONS FOR INNER LISTENING</p><h2>Come closer to<br>your experience.</h2><p>Choose a question. Give it the time and meaning it holds for you.</p></div><ol>${entry.questions.map(q=>`<li>${esc(q)}</li>`).join('')}</ol></div><blockquote class="health-phrase">“${esc(entry.phrase)}”<span>A PHRASE TO CONTEMPLATE · MAKE IT YOUR OWN</span></blockquote><section class="health-intents" aria-labelledby="choose-intent"><p class="eyebrow">THEMES YOU CAN EXPLORE</p><h2 id="choose-intent">What do you recognize in your experience?</h2><p>These are possible starting points. Choose the theme that makes sense to you or explore other intentions.</p><div class="health-intent-grid">${suggested.map(intentLink).join('')}</div><details class="health-more" ${intent&&more.some(i=>i.id===intent.id)?'open':''}><summary>Explore ${more.length} other intentions</summary><div class="health-intent-grid">${more.map(intentLink).join('')}</div></details></section>${intent?chosen(entry,intent):'<div class="health-prompt">Choose an intention to see its triad, three plates, and 2D sigils.</div>'}<p class="source-mini">Original reflection · editorial proposal for Zuluan Orion. General definition consulted on ${esc(entry.source.verifiedDate)}.</p></section>`;
  }
  function render(id){
   if(!id)return index();
   const [entryId,intentId]=String(id).split(':');
   const entry=entries.get(entryId);
   if(!entry)return `<section class="wrap"><div class="empty"><h1>This entry is still to be developed.</h1><a class="btn" href="#salud">Open the dictionary</a></div></section>`;
   return detail(entry,intentId);
  }
  function textFor(entryId,intentId){
   const e=entries.get(entryId),i=intents.get(intentId);if(!e||!i)return '';
   const f=engine.formulas.get(i.formulaId),context=engine.entries.get(f.entryId);
   return ['CODES OF LIGHT FOR YOUR HEALTH · INNER LISTENING DICTIONARY','Editorial proposal for Zuluan Orion’s review','',e.title,e.definition,e.source.organization,e.source.url,'','THE FLAME IN YOUR EXPERIENCE',e.reflection,'','QUESTIONS',...e.questions,'',e.phrase,'','CHOSEN INTENTION',i.title,i.description,f.names.join(' → '),i.sourceRationale,'',reference(context,f.page),'',...f.codes.map((id,n)=>['Core','Sustaining','Sealing'][n]+': '+engine.codes.get(id).name),'','Write a need, a question, or a gesture you want to share. Choose a small, achievable step for today.'].join('\n');
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
    const save=event.target.closest('[data-health-save]');if(save){const [e,i]=save.dataset.healthSave.split(':');const txt=textFor(e,i);if(!txt)return;const url=URL.createObjectURL(new Blob([txt],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='Reflection_'+e+'_'+i+'.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1500);}
   });
  }
  return {render,searchSection,textFor,search:q=>search(data,q),count:data.entries.length};
 }
 const api={search,create,normalize};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 else root.HealthDictionary=api;
})(typeof window!=='undefined'?window:globalThis);
