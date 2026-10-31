/* Render the existing typographic poster as a downloadable image. No external assets. */
function makePosterImage(poster){
 const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');
 const width=1200,pad=90,maxWidth=width-2*pad;
 const accent=getComputedStyle(poster).getPropertyValue('--poster-accent').trim()||'#13a7bd';
 const blocks=[{text:poster.querySelector('.poster-kicker').textContent,size:28,bold:true,color:accent},{text:poster.querySelector('h3').textContent.toUpperCase(),size:64,bold:true,color:'#ffffff'},...[...poster.querySelectorAll(':scope > p')].map(p=>({text:p.innerText||p.textContent,size:36,bold:!!p.querySelector('strong'),color:'#d7e8ec'})),{text:'Alex Ehsan, MD, PhD\nEducational only',size:28,bold:false,color:'#aec7ce'}];
 function lines(text,size,bold){ctx.font=(bold?'700 ':'400 ')+size+'px Arial';const result=[];for(const paragraph of text.split('\n')){let line='';for(const word of paragraph.split(/\s+/)){const next=line?line+' '+word:word;if(line&&ctx.measureText(next).width>maxWidth){result.push(line);line=word}else line=next}result.push(line)}return result}
 const layout=blocks.map(b=>({...b,lines:lines(b.text,b.size,b.bold)}));
 canvas.width=width;canvas.height=Math.max(1500,pad*2+layout.reduce((sum,b)=>sum+b.lines.length*b.size*1.4+48,0));
 ctx.fillStyle='#071e2b';ctx.fillRect(0,0,width,canvas.height);ctx.strokeStyle=accent;ctx.lineWidth=24;ctx.strokeRect(12,12,width-24,canvas.height-24);ctx.textBaseline='top';let y=pad;
 for(const b of layout){ctx.font=(b.bold?'700 ':'400 ')+b.size+'px Arial';ctx.fillStyle=b.color;for(const line of b.lines){ctx.fillText(line,pad,y);y+=b.size*1.4}y+=48}
 return canvas.toDataURL('image/png');
}
function openPosterPreview(poster){
 let dialog=document.getElementById('poster-preview');
 if(!dialog){dialog=document.createElement('dialog');dialog.id='poster-preview';dialog.setAttribute('aria-labelledby','poster-preview-title');dialog.innerHTML='<div class="preview-tools"><button type="button" data-close>Close</button><a data-download>Download poster</a><button type="button" data-print>Print</button></div><h2 id="poster-preview-title"></h2><p>Save the poster using Download poster, or press and hold the image. Printing depends on your browser.</p><img alt="">';document.body.append(dialog);dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());dialog.querySelector('[data-print]').addEventListener('click',()=>window.print());dialog.addEventListener('close',()=>document.body.classList.remove('poster-preview-open'))}
 const title=poster.querySelector('h3').textContent;dialog.querySelector('h2').textContent=title;
 const data=poster.dataset.posterImage||makePosterImage(poster),img=dialog.querySelector('img');img.src=data;img.alt=poster.innerText.replace(/Open (?:illustrated poster|text reminder|poster)/g,'');
 const download=dialog.querySelector('[data-download]');download.href=data;
 const extension=poster.dataset.posterImage?.match(/\.(png|webp|jpe?g)(?:[?#]|$)/i)?.[1]?.toLowerCase()||'png';
 download.download=(title.toLowerCase().replace(/[^a-z0-9]+/g,'-')||'athlete')+'-poster.'+extension;
 document.body.classList.add('poster-preview-open');dialog.showModal();dialog.scrollTop=0;dialog.querySelector('[data-close]').focus();
}
