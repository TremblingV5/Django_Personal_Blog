import markdown

def parse_md(text):
    return markdown.markdown(text.replace("\r\n", ' \n'), extensions=[
        'utils.mdeditor_extensions.mermaid',
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'mdx_math',
    ])
