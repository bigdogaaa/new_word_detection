import re

pic_p = re.compile(r"\s*\[\[图片[\w\-/='?.:]*]]\s*")
s_p = re.compile(r'\s+')


def clean_text(content):
    content = pic_p.sub('', content)
    content = s_p.sub('', content)
    return content

