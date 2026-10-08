#!/usr/bin/env python3
"""Genera procesos/visor.html a partir de los ficheros .md de esta carpeta.

Un HTML abierto desde el disco no puede leer otros ficheros, así que los procesos
se incrustan dentro. Ejecútalo cada vez que añadas o cambies un proceso:

    python3 procesos/generar_visor.py

Solo usa la librería estándar de Python.
"""
import json
import re
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
EXCLUIR = {"indice.md", "que-es-un-proceso.md", "readme.md"}


def leer(ruta):
    return ruta.read_text(encoding="utf-8-sig")


def titulo(md, por_defecto):
    for linea in md.splitlines():
        if linea.startswith("# "):
            return re.sub(r"^proceso\s*:\s*", "", linea[2:].strip(), flags=re.I)
    return por_defecto


def doc(ruta, grupo, id_):
    md = leer(ruta)
    return {"id": id_, "titulo": titulo(md, ruta.stem), "grupo": grupo, "md": md}


def main():
    docs = []
    intro = AQUI / "que-es-un-proceso.md"
    if intro.exists():
        docs.append(doc(intro, "Empieza aquí", "que-es"))
    plantilla = RAIZ / "plantillas" / "proceso.md"
    if plantilla.exists():
        d = doc(plantilla, "Empieza aquí", "plantilla")
        d["titulo"] = "Plantilla de proceso"
        docs.append(d)
    procesos = sorted(
        (p for p in AQUI.glob("*.md") if p.name.lower() not in EXCLUIR),
        key=lambda p: p.name.lower(),
    )
    for p in procesos:
        docs.append(doc(p, "Tus procesos", "p-" + re.sub(r"[^a-z0-9]+", "-", p.stem.lower())))

    datos = json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")
    html = PLANTILLA.replace("__DATOS__", datos)
    html = html.replace("__FECHA__", datetime.now().strftime("%d/%m/%Y %H:%M"))
    (AQUI / "visor.html").write_text(html, encoding="utf-8")
    print(f"visor.html generado con {len(procesos)} proceso(s).")


PLANTILLA = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mis procesos</title>
<style>
:root{--bg:#fafafa;--panel:#fff;--tx:#1a1a1a;--mut:#6b6b6b;--line:#e5e5e5;--ac:#1a1a1a;--acbg:#f1f1f1}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--panel:#1a1a1a;--tx:#ededed;--mut:#9a9a9a;--line:#2c2c2c;--ac:#ededed;--acbg:#262626}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.app{display:grid;grid-template-columns:320px 1fr;min-height:100vh}
aside{background:var(--panel);border-right:1px solid var(--line);padding:20px;position:sticky;top:0;height:100vh;overflow:auto}
h1.t{font-size:18px;margin:0 0 12px}
input{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--tx);font:inherit}
.g{margin:18px 0 6px;font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--mut)}
.i{display:block;padding:8px 10px;border-radius:8px;color:var(--tx);text-decoration:none;cursor:pointer;font-size:15px}
.i:hover{background:var(--acbg)}
.i.on{background:var(--acbg);color:var(--ac);font-weight:600}
.vacio{color:var(--mut);font-size:14px;padding:6px 10px}
main{padding:40px 48px;max-width:860px}
main h1{font-size:30px;margin-top:0}main h2{margin-top:32px;font-size:21px}main h3{font-size:17px}
code{background:var(--acbg);padding:2px 6px;border-radius:5px;font-size:.92em}
pre{background:var(--panel);border:1px solid var(--line);padding:14px;border-radius:8px;overflow:auto}pre code{background:none;padding:0}
blockquote{margin:16px 0;padding:10px 16px;border-left:3px solid var(--ac);background:var(--acbg);border-radius:0 8px 8px 0}
table{border-collapse:collapse;width:100%;margin:16px 0}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left}th{background:var(--acbg)}
a{color:var(--tx);text-decoration:underline}hr{border:0;border-top:1px solid var(--line);margin:28px 0}
.pie{margin-top:48px;color:var(--mut);font-size:13px}
@media (max-width:760px){.app{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:24px 20px}}
</style>
</head>
<body>
<div class="app">
<aside>
<h1 class="t">Mis procesos</h1>
<input id="q" type="search" placeholder="Buscar en los procesos…" autocomplete="off">
<div id="lista"></div>
</aside>
<main id="doc"></main>
</div>
<script>
const DOCS = __DATOS__;
const FECHA = "__FECHA__";
const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
function inline(s){
  s = esc(s);
  s = s.replace(/`([^`]+)`/g,"<code>$1</code>");
  s = s.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");
  s = s.replace(/(^|[^*])\*([^*\s][^*]*)\*/g,"$1<em>$2</em>");
  s = s.replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>');
  return s;
}
function render(md){
  const L = md.replace(/\r/g,"").split("\n"); let h = "", i = 0;
  const esTabla = n => /^\s*\|.*\|\s*$/.test(L[n]||"");
  while(i < L.length){
    const l = L[i]; let m;
    if(/^```/.test(l)){ const c=[]; i++; while(i<L.length && !/^```/.test(L[i])){c.push(L[i]); i++} i++; h += "<pre><code>"+esc(c.join("\n"))+"</code></pre>"; continue; }
    if((m = l.match(/^(#{1,6})\s+(.*)$/))){ h += "<h"+m[1].length+">"+inline(m[2])+"</h"+m[1].length+">"; i++; continue; }
    if(/^\s*---+\s*$/.test(l)){ h += "<hr>"; i++; continue; }
    if(/^>/.test(l)){ const q=[]; while(i<L.length && /^>/.test(L[i])){q.push(L[i].replace(/^>\s?/,"")); i++} h += "<blockquote>"+inline(q.join(" "))+"</blockquote>"; continue; }
    if(/^\s*[-*]\s+/.test(l)){ h+="<ul>"; while(i<L.length && /^\s*[-*]\s+/.test(L[i])){ h+="<li>"+inline(L[i].replace(/^\s*[-*]\s+/,""))+"</li>"; i++ } h+="</ul>"; continue; }
    if(/^\s*\d+\.\s+/.test(l)){ h+="<ol>"; while(i<L.length && /^\s*\d+\.\s+/.test(L[i])){ h+="<li>"+inline(L[i].replace(/^\s*\d+\.\s+/,""))+"</li>"; i++ } h+="</ol>"; continue; }
    if(esTabla(i) && /^\s*\|?\s*:?-{2,}/.test(L[i+1]||"")){
      const cel = r => r.trim().replace(/^\||\|$/g,"").split("|").map(x=>inline(x.trim()));
      h += "<table><thead><tr>"+cel(L[i]).map(x=>"<th>"+x+"</th>").join("")+"</tr></thead><tbody>"; i += 2;
      while(i<L.length && esTabla(i)){ h += "<tr>"+cel(L[i]).map(x=>"<td>"+x+"</td>").join("")+"</tr>"; i++ }
      h += "</tbody></table>"; continue;
    }
    if(l.trim()===""){ i++; continue; }
    const p=[l]; i++;
    while(i<L.length && L[i].trim()!=="" && !/^(#{1,6}\s|```|>|\s*[-*]\s|\s*\d+\.\s|\s*\|)/.test(L[i])){ p.push(L[i]); i++ }
    h += "<p>"+inline(p.join(" "))+"</p>";
  }
  return h;
}
const $lista = document.getElementById("lista"), $doc = document.getElementById("doc"), $q = document.getElementById("q");
let actual = (location.hash||"").slice(1) || (DOCS[0] && DOCS[0].id);
function pintaLista(){
  const t = $q.value.trim().toLowerCase();
  const ok = DOCS.filter(d => !t || (d.titulo+" "+d.md).toLowerCase().includes(t));
  let h = "";
  for(const g of ["Empieza aquí","Tus procesos"]){
    const del = ok.filter(d => d.grupo===g);
    h += '<div class="g">'+g+"</div>";
    if(!del.length){ h += '<div class="vacio">'+(g==="Tus procesos" && !t ? "Todavía no hay ninguno. Pídele a Claude que documente el primero." : "Sin resultados.")+"</div>"; continue; }
    h += del.map(d => '<a class="i'+(d.id===actual?" on":"")+'" href="#'+d.id+'">'+esc(d.titulo)+"</a>").join("");
  }
  $lista.innerHTML = h;
}
function pintaDoc(){
  const d = DOCS.find(x => x.id===actual) || DOCS[0];
  $doc.innerHTML = d ? render(d.md)+'<div class="pie">Visor generado el '+FECHA+". Ejecuta procesos/generar_visor.py para actualizarlo.</div>" : "<p>No hay nada que mostrar todavía.</p>";
}
function todo(){ pintaLista(); pintaDoc(); }
window.addEventListener("hashchange", () => { actual = location.hash.slice(1); todo(); window.scrollTo(0,0); });
$q.addEventListener("input", pintaLista);
todo();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
