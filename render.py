import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)

markdown_text = open('docs/history.md', 'r').read()

#html = markdown('```python\nassert 1 == 1\n```')
html = markdown(markdown_text)
#print(html)
open('docs/history.html', 'w').write(html)
