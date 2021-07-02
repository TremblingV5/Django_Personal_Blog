import markdown

def parse_md(text):
    return markdown.markdown(text.replace("\r\n", ' \n'), extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'mdx_math',
    ])
