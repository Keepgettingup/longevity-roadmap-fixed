@echo off
cd /d "C:\Users\Anwender\Desktop\Gleichschalt-Kommie\longevity\longevity"
node -e "const h=require('http'),f=require('fs'),p=require('path');h.createServer((q,r)=>{let fp=p.join('.',q.url.split('?')[0]);if(fp.endsWith('/')||fp==='.')fp+='index.html';try{const d=f.readFileSync(fp);r.writeHead(200,{'Content-Type':fp.endsWith('.html')?'text/html':fp.endsWith('.js')?'application/javascript':'text/plain','Access-Control-Allow-Origin':'*'});r.end(d)}catch(e){r.writeHead(404);r.end('not found')}}).listen(3000,()=>console.log('Server running on http://localhost:3000'))"
pause
