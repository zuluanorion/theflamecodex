(function(root){
  'use strict';
  const normalize=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[’‘ʼ']/g,'').replace(/[^a-z0-9]+/g,' ').trim();
  const stop=new Set(('que como para con una uno unas unos del los las por quiero necesito siento tengo estoy esta esto este algo mucho poco poder hacer tener mis sus hay mas sin desde donde cuando puedo puede sobre entre hacia tambien porque muy ser sea soy son esto eso esa mi el la un de a y o en me se le al lo es no si sone sonar sueno suenos tuve soñado sonado persona estaba').split(' '));
  const tokens=s=>[...new Set(normalize(s).split(' ').filter(w=>w.length>2&&!stop.has(w)))];
  const stem=w=>w.length>6?w.replace(/(?:mente|ciones|cion|ando|iendo|ados|adas|idad|es|os|as)$/,''):w.length>4?w.replace(/s$/,''):w;
  const groups=[['duda','dudas','indecision','decision','decidir','claridad'],['trabajo','laboral','empleo','profesion'],['miedo','temor','inseguridad'],['calma','tranquilidad','serenidad','paz'],['enfado','ira','rabia','enojo'],['tristeza','triste','pena','desanimo','duelo','desamor','decepcion','afliccion'],['perdida','duelo','despedida'],['agotamiento','cansancio','descanso'],['limites','limite','proteger','proteccion'],['pareja','relacion','vinculo'],['ruptura','rompimiento','separacion','divorcio','desamor'],['arana','telarana'],['dinero','economia','abundancia'],['cambio','transicion','transformacion'],['soledad','solo','sola'],['culpa','culpable'],['confianza','confiar'],['perdon','perdonar'],['autoestima','valor','dignidad']];
  const keywordLabels=['Araña','Noche','Agua','Casa','Puerta','Escalera','Vuelo','Serpiente','Miedo','Tristeza','Rompimiento','Relación','Duelo','Soledad','Confianza','Límites','Culpa','Perdón','Calma','Cansancio','Trabajo','Dinero','Familia','Cambio','Claridad','Integración','Protección','Silencio','Voluntad','Aura','Enraizamiento','Activar','Depurar'];
  function create(data){
    const codes=new Map(data.codes.map(c=>[c.id,c])),entries=new Map(data.entries.map(e=>[e.id,e])),formulas=new Map(data.formulas.map(f=>[f.id,f]));
    const words=text=>new Set(normalize(text).split(' ').map(stem));
    const documents=data.entries.map(e=>{const title=normalize(e.title),category=normalize(e.category),body=normalize([e.intro,e.pattern,e.integration,e.when,e.archetype,e.practice,e.mode,(e.keywords||[]).join(' ')].join(' ')),labels=normalize(e.formulas.map(id=>{const f=formulas.get(id);return f.label+' '+f.names.join(' ')}).join(' '));return {e,title,category,body,labels,titleWords:words(title),categoryWords:words(category),bodyWords:words(body),labelWords:words(labels),allWords:words([title,category,body,labels].join(' '))};});
    const contains=(text,w)=>text instanceof Set?text.has(stem(w)):words(text).has(stem(w));
    function queryTerms(q){const direct=tokens(q);let terms=direct.map(w=>({w,weight:1}));for(const g of groups)if(g.some(w=>direct.some(d=>stem(w)===stem(d))))for(const w of g)if(!direct.includes(w))terms.push({w,weight:.5});return {direct,terms};}
    function search({query='',domain='all',category='',requiredTerms=[]}={}){
      const {direct,terms}=queryTerms([query,...requiredTerms].join(' ')),phrase=normalize(query);const out=[];const concepts=direct.map(w=>groups.find(g=>g.some(x=>stem(x)===stem(w)))||[w]);
      const required=requiredTerms.map(t=>queryTerms(t).terms);
      for(const doc of documents){const e=doc.e;if(domain!=='all'&&e.domain!==domain||category&&e.category!==category)continue;if(!required.every(group=>group.some(({w})=>contains(doc.allWords,w))))continue;let score=0;let matched=[];
        if(terms.length){
          if(doc.title===phrase)score+=200;else if(phrase.length>3&&doc.title.includes(phrase))score+=70;
          for(const {w,weight} of terms){let part=(contains(doc.titleWords,w)?22:0)+(contains(doc.categoryWords,w)?4:0)+(contains(doc.labelWords,w)?7:0)+(contains(doc.bodyWords,w)?3:0);score+=part*weight;if(part&&direct.includes(w))matched.push(w);}
          if(!score)continue;
          if(direct[0]&&contains(doc.titleWords,direct[0]))score+=18;
          score+=matched.length*4;const coverage=concepts.filter(g=>g.some(w=>contains(doc.allWords,w))).length;score+=Math.max(0,coverage-1)*65;
        }
        const original=([query,...requiredTerms].join(' ').match(/[\p{L}’'-]+/gu)||[]);out.push({entry:e,score,matched:matched.map(w=>original.find(x=>normalize(x)===w)||w)});
      }
      return out.sort((a,b)=>b.score-a.score||a.entry.title.localeCompare(b.entry.title,'es'));
    }
    function formulaScore(f,query,goal){const {terms}=queryTerms(query);let n=f.kind==='principal'?1:0;const label=normalize(f.label);const names=normalize(f.names.join(' '));for(const {w,weight}of terms)if(contains(names,w))n+=12*weight;for(const {w,weight}of terms)if(contains(label,w))n+=5*weight;const boost={understand:['revelar','claridad','comprension','vision'],sustain:['sosten','calma','sostener','proteccion'],act:['actuar','accion','voluntad','limpiar'],integrate:['integrar','cierre','integracion','regulador']};for(const w of boost[goal]||[])if(contains(label,w)||f.kind===w)n+=2;return n;}
    function suggest(options){if(!tokens(options.query).length)return [];const hits=search(options),seen=new Set(),out=[];for(const h of hits){const ordered=h.entry.formulas.map(id=>formulas.get(id)).filter(f=>!f.review&&(!f.sequenceIndex||f.sequenceIndex===1)).sort((a,b)=>formulaScore(b,options.query,options.goal)-formulaScore(a,options.query,options.goal));const f=ordered.find(f=>!seen.has(f.codes.join(',')));if(!f)continue;seen.add(f.codes.join(','));out.push({...h,formula:f});if(out.length===3)break;}return out;}
    function facets(options={}){const selected=options.requiredTerms||[],base=search(options),ids=new Set(base.map(h=>h.entry.id));return keywordLabels.filter(t=>!selected.some(s=>normalize(s)===normalize(t))&&!tokens(options.query).some(s=>stem(s)===stem(normalize(t)))).map(label=>{const alternatives=queryTerms(label).terms;const count=documents.filter(doc=>ids.has(doc.e.id)&&alternatives.some(({w})=>contains(doc.allWords,w))).length;return {label,count};}).filter(x=>x.count>0);}
    return {codes,entries,formulas,search,suggest,facets,tokens,normalize};
  }
  root.TriadEngine={create,normalize,tokens};
  if(typeof module!=='undefined')module.exports=root.TriadEngine;
})(typeof window!=='undefined'?window:globalThis);
