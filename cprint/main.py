import re
import cprint
from cprint.tools import getshow_config
from cprint.config import CONTANT_DICT
from forbiddenfruit import curse

STYLE_CONFIG = getshow_config(1)
# @加数字 中括号或者大括号 任意字符0或无限次 中括号或者大括号
# 3组 @123 123 {
PATTERN = re.compile(r'(@(\d+))([\{\[]).*?[\}\]]')

def cp(text: str, style_id: int) -> str:
    """
    Colorful Processing
    文档:
        使用style_id处理一个字符串
    参数:
        text: str
            需要处理的字符串
        style_id: int
            颜色id
    返回:
        返回处理好的字符串
    """
    return STYLE_CONFIG[style_id] + text + "\033[0;0m"

def cf(text: str) -> str:
    """
    Colorful Format
    文档:
        使用style_id格式化字符串
    参数:
        text: str
            需要格式化的字符串
    返回:
        返回格式化好的字符串
    """
    def pr_march(match):

        replace_text, style_id, format_symbol = match.groups()
        if format_symbol == "{":
            return match.group().replace(replace_text, STYLE_CONFIG[int(style_id)]) + "\033[0;0m"
        else:
            return match.group().replace(replace_text + '[', STYLE_CONFIG[int(style_id)])[:-1] + "\033[0;0m"

    for mark, mark_fun in CONTANT_DICT.items():
        text = text.replace(mark, mark_fun())

    return re.sub(PATTERN, pr_march, text)

def cformat(self, *args, **kwargs):
    return cf(self).format(*args, **kwargs)

curse(str, "cformat", cformat)

def idf(text: str) -> str:
    """
    Colorful Format
    文档:
        使用style_id格式化字符串
    参数:
        text: str
            需要格式化的字符串
    返回:
        返回格式化好的字符串
    """
    def pr_march(match):

        replace_text, style_id, format_symbol = match.groups()
        if format_symbol == "{":
            return match.group().replace(replace_text, STYLE_CONFIG[cprint.custom_style.get(int(style_id), int(style_id))]) + "\033[0;0m"
        else:
            return match.group().replace(replace_text + '[', STYLE_CONFIG[cprint.custom_style.get(int(style_id), int(style_id))])[:-1] + "\033[0;0m"

    for mark, mark_fun in CONTANT_DICT.items():
        text = text.replace(mark, mark_fun())

    return re.sub(PATTERN, pr_march, text)

def iformat(self, *args, **kwargs):
    return idf(self).format(*args, **kwargs)

curse(str, "iformat", iformat)