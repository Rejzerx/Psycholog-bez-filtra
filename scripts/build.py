from pathlib import Path
import shutil,re,html,json,yaml,mistune
root=Path(__file__).resolve().parent.parent;out=root/'dist'
if out.exists():shutil.rmtree(out)
ignore=shutil.ignore_patterns('dist','node_modules','_posts','scripts','.git','.pages.yml','package.json','package-lock.json','netlify.toml','README*','.gitignore')
shutil.copytree(root,out,ignore=ignore)
shutil.rmtree(out/'blog',ignore_errors=True);(out/'blog').mkdir()
blogtpl=(root/'blog/index.html').read_text();arttpl=(root/'blog/adhd-a-cptsd-roznice/index.html').read_text()
def esc(s):return html.escape(str(s or ''),quote=True)
def nav(s):return re.sub(r'href="(?:\.\./)+([^"#]+)"',lambda m:'href="/'+re.sub(r'index\.html$','',m[1])+'"',s)
posts=[]
for f in (root/'_posts').glob('*.md'):
 text=f.read_text();match=re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$',text,re.S)
 if not match:raise ValueError(f'Brak nagłówka YAML: {f}')
 data=yaml.safe_load(match[1]);data['slug']=f.stem;data['body']=match[2]
 if not data.get('title') or not data.get('description'):raise ValueError(f'Brak tytułu lub opisu: {f}')
 if data.get('draft') is True:continue
 posts.append(data)
posts.sort(key=lambda x:str(x.get('date','')),reverse=True)
tiles=''.join(f'<a class="tile" href="/blog/{p["slug"]}/"><div class="visual"><span>{esc(p.get("category","Psychologia"))}</span></div><div class="tile-body"><h2>{esc(p["title"])}</h2><p>{esc(p["description"])}</p><span class="more">Czytaj artykuł ↗</span></div></a>' for p in posts)
blog=re.sub(r'<div class="grid">.*?</div></section>',lambda m:f'<div class="grid">{tiles}</div></section>',blogtpl,count=1,flags=re.S)
(out/'blog/index.html').write_text(nav(blog))
for p in posts:
 slug=p['slug'];url=f'https://psychologbezfiltra.pl/blog/{slug}/'
 main=f'<main class="article"><a class="back" href="/blog/">← Wróć do bloga</a><div class="eyebrow" style="margin-top:45px">{esc(p.get("category","Psychologia"))} · Daniel Kampa</div><h1>{esc(p["title"])}</h1><p class="lead">{esc(p["description"])}</p><div class="line" style="margin:35px 0"></div><div class="article-body">{mistune.html(p["body"])}</div><div class="note"><strong>Materiał edukacyjny.</strong> Artykuł nie zastępuje indywidualnej diagnozy ani konsultacji.</div><p><a class="cta" href="/konsultacje-psychologiczne-wroclaw/">Zobacz konsultacje ↗</a></p></main>'
 s=re.sub(r'<main class="article">.*?</main>',lambda m:main,arttpl,count=1,flags=re.S)
 for pattern,repl in [(r'<title>.*?</title>',f'<title>{esc(p["title"])} | Psycholog bez filtra</title>'),(r'<meta content="[^"]*" name="description"/>',f'<meta content="{esc(p["description"])}" name="description"/>'),(r'<link href="[^"]*" rel="canonical"/>',f'<link href="{url}" rel="canonical"/>'),(r'<meta content="[^"]*" property="og:title"/>',f'<meta content="{esc(p["title"])}" property="og:title"/>'),(r'<meta content="[^"]*" property="og:description"/>',f'<meta content="{esc(p["description"])}" property="og:description"/>'),(r'<meta content="[^"]*" property="og:url"/>',f'<meta content="{url}" property="og:url"/>')]:s=re.sub(pattern,lambda m:repl,s,count=1,flags=re.S)
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':p['title'],'description':p['description'],'datePublished':str(p.get('date','')),'author':{'@type':'Person','name':'Daniel Kampa'},'mainEntityOfPage':url}
 s=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script>',s,count=1,flags=re.S)
 css='.article-body h2{font-size:clamp(24px,4vw,30px);margin-top:38px}.article-body h3{font-size:22px;margin-top:28px}.article-body p,.article-body li{font-size:17px;line-height:1.85;color:#4f4b47}.article-body img{max-width:100%;height:auto;border-radius:12px}.article-body a{text-decoration:underline;text-underline-offset:3px}.article-body blockquote{border-left:3px solid #b93e46;margin:28px 0;padding:8px 20px;background:#f4e7df}@media(max-width:800px){.article-body p,.article-body li{font-size:16px}}'
 s=s.replace('</style>',css+'</style>',1);s=nav(s)
 dest=out/'blog'/slug;dest.mkdir();(dest/'index.html').write_text(s)
urls=[]
for f in out.rglob('index.html'):
 rel=f.relative_to(out).parent.as_posix();urls.append('https://psychologbezfiltra.pl/'+('' if rel=='.' else rel+'/'))
(out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join('  <url><loc>'+u+'</loc></url>' for u in sorted(urls))+'\n</urlset>\n')
print(f'Zbudowano {len(urls)} stron, w tym {len(posts)} artykułów.')
