const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const html=fs.readFileSync('dist/index.html','utf8');
const ids=new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]));const nodes={};
function node(key){return nodes[key]??=( {value:'',innerHTML:'',textContent:'',hidden:false,style:{},dataset:{},children:[],events:{},setAttribute(){},addEventListener(e,f){this.events[e]=f},focus(){},blur(){},scrollIntoView(){}});}
const ctx={console,URLSearchParams,location:{search:'?category=Blood'},window:{},setTimeout:f=>f(),document:{getElementById:id=>{assert(ids.has(id),'Missing DOM id '+id);return node(id)},querySelectorAll:()=>[],querySelector:s=>{assert(html.includes(s.replace(/[\[\]]/g,'')),'Missing selector '+s);return node(s)}}};
vm.createContext(ctx);vm.runInContext(fs.readFileSync('dist/genetics-index.js','utf8'),ctx);vm.runInContext(fs.readFileSync('dist/genetics-search.js','utf8'),ctx);vm.runInContext(fs.readFileSync('dist/medical-library.js','utf8'),ctx);
assert(node('condition-grid').innerHTML.includes('Anemia'));
vm.runInContext("chooseCategory('all','AML')",ctx);assert(node('condition-grid').innerHTML.includes('aml-guide.html'));
vm.runInContext("chooseCategory('all','CDH1')",ctx);assert(node('genetics-matches').innerHTML.includes('CDH1'));
vm.runInContext("chooseCategory('MentalSpanish','')",ctx);assert(node('condition-grid').innerHTML.includes('Español'));
vm.runInContext("chooseCategory('all','zzzzzznomatch938')",ctx);assert.equal(node('condition-grid').innerHTML,'');
node('home-search-input').value='diabetes';node('home-search-form').events.submit({preventDefault(){}});assert(node('condition-grid').innerHTML.toLowerCase().includes('diabetes'));
console.log('Homepage runtime passed: initial category link, AML, CDH1, Spanish, no results, top search form.');
