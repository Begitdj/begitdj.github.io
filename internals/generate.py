import os

EXCLUDE = ['index.html', 'generate.py', '.git', '.github', 'internals', 'README.md']

html_template = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Begitdj Archive</title>
<style type="text/css">
    body {{ font-family: sans-serif; background-color: #f0f0f0; margin: 0; padding: 20px; color: #333; }}
    .container {{ background-color: #ffffff; border: 1px solid #ccc; max-width: 800px; margin: 0 auto; padding: 20px; }}
    h1 {{ border-bottom: 2px solid #0055aa; color: #0055aa; padding-bottom: 10px; margin-top: 0; }}
    ul {{ list-style-type: none; padding: 0; }}
    li {{ padding: 8px; border-bottom: 1px solid #eee; }}
    li a {{ color: #0066cc; text-decoration: none; font-weight: bold; }}
    li a:hover {{ text-decoration: underline; color: #ff6600; }}
</style>
</head>
<body>
<div class="container">
    <h1>Begitdj Archive</h1>
    <p>If site doesn't open on old browser try proxy: <a href="https://nnp.nnchan.ru/glype/browse.php?u=https%3A%2F%2Fbegitdj.github.io%2F&b=14">Glype Proxy</a></p>
    <ul>
{links}
    </ul>
</div>
</body>
</html>"""

links = []
proxy_base = "https://nnp.nnchan.ru/glype/browse.php?u=https%3A%2F%2Fbegitdj.github.io%2F"

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDE]
    for file in files:
        if file in EXCLUDE:
            continue
        rel_path = os.path.relpath(os.path.join(root, file), '.')
        web_path = rel_path.replace('\\', '/')
        
        # Генерируем ссылку через прокси для каждого файла
        proxy_link = proxy_base + web_path.replace('/', '%2F') + "&b=14"
        
        links.append('        <li><a href="' + proxy_link + '">' + web_path + '</a></li>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template.format(links='\n'.join(sorted(links))))
