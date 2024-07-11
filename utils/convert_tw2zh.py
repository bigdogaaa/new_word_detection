#! coding=utf-8
from langdetect import detect, DetectorFactory, detect_langs
from langdetect.lang_detect_exception import LangDetectException
import pandas as pd
import zhconv
import opencc
import re

chinese_pattern = r'[\u4e00-\u9fa5]'


converter = opencc.OpenCC('t2s')
target_lang = ['zh-cn', 'zh-tw']


def is_chinese_word(w):
    match = re.fullmatch(chinese_pattern * len(w), w)
    return match is not None


def convert_tw2zh(text, detect_lang=True):
    if detect_lang:
        try:
            det_lang = detect(text)
            if det_lang not in target_lang:
                print(det_lang)
                raise Exception('非中文。')
            if det_lang == 'zh-tw':
                content_simple_cn = zhconv.convert(text, 'zh-cn')
                return content_simple_cn
            else:
                return text
        except LangDetectException as e:
            print('文本无内容，跳过。')
            raise Exception('文本无内容。')


def convert_tw2zh_opencc(text):
    return converter.convert(text)


# print(is_chinese_word('文本无内容.'))

