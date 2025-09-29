#!/usr/bin/env python3
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 md_to_html_inline.py <markdown_file>")
    sys.exit(1)

md_file = sys.argv[1]
html_file = os.path.splitext(md_file)[0] + '.html'

with open(md_file, 'r') as f:
    md_content = f.read()

html_template = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1, h2, h3 {{ color: #333; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
    <div id="content">
{md_content}
    </div>
    <script>
        document.getElementById('content').innerHTML = marked.parse(document.getElementById('content').textContent);
    </script>
</body>
</html>'''

with open(html_file, 'w') as f:
    f.write(html_template)

print(f"Created {html_file} with inline markdown")
