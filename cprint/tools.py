import os
import math
import traceback
from cprint.config import COLOR32, COLOR256

def getshow_config(mode: int=1) -> dict or None:
    """
    文档:
        获取 or 显示 32 colors 配置信息
    参数:
        mode: int
            运行模式(1, 2, 3)
            1: 只获取配置不显示
            2: 只显示颜色列表
            3: 显示详细颜色信息
    返回:
        mode 1 返回颜色配置, 其他情况只打印
    """
    # print("DEBUG Caclute 1!")
    if mode == 1:
        use_print_1 = lambda *args, **kwargs : None
        use_print_2 = lambda *args, **kwargs : None
    elif mode == 2:
        use_print_1 = lambda *args, **kwargs : None
        use_print_2 = print
    else:
        use_print_1 = print
        use_print_2 = print

    id_plus = 0
    # 32样式字典
    STYLE_ID_DICT = {}

    """ 打印所有颜色详细信息 """
    # 打印默认样式
    for style in COLOR32.STYLE:
        use_print_1('ID {6:>4} style {0} text_color {1} background_color {2}: \033[{3};{4};{5}m CHERRY \033[0;0m'.format(
            COLOR32.STYLE[style], COLOR32.TEXT_COLOR["01"], COLOR32.BACKGROUND_COLOR["01"],
            style, "01", "01",
            id_plus,
        ))
        STYLE_ID_DICT[id_plus] = "\033[{0};{1};{2}m".format(style, "01", "01")
        id_plus = 0

    # 按颜色分类打印样式 32
    background_color_list = list(COLOR32.BACKGROUND_COLOR)
    text_color_list = list(COLOR32.TEXT_COLOR)
    for index in range(8):
        background_color = background_color_list[1:9][index]
        for text_color in COLOR32.TEXT_COLOR:
            for style in COLOR32.STYLE:
                use_print_1('ID {6:>4} style {0} text_color {1} background_color {2}: \033[{3};{4};{5}m CHERRY \033[0;0m'.format(
                    COLOR32.STYLE[style], COLOR32.TEXT_COLOR[text_color], COLOR32.BACKGROUND_COLOR[background_color],
                    style, text_color, background_color,
                    id_plus,
                ))
                STYLE_ID_DICT[id_plus] = "\033[{0};{1};{2}m".format(style, text_color, background_color)
                id_plus += 1

        background_color = background_color_list[9:][index]
        for text_color in COLOR32.TEXT_COLOR:
            for style in COLOR32.STYLE:
                use_print_1('ID {6:>4} style {0} text_color {1} background_color {2}: \033[{3};{4};{5}m CHERRY \033[0;0m'.format(
                    COLOR32.STYLE[style], COLOR32.TEXT_COLOR[text_color], COLOR32.BACKGROUND_COLOR[background_color],
                    style, text_color, background_color,
                    id_plus,
                ))
                STYLE_ID_DICT[id_plus] = "\033[{0};{1};{2}m".format(style, text_color, background_color)
                id_plus += 1

        text_color = text_color_list[1:9][index]
        for text_color in COLOR32.TEXT_COLOR:
            for style in COLOR32.STYLE:
                use_print_1('ID {6:>4} style {0} text_color {1} background_color {2}: \033[{3};{4};{5}m CHERRY \033[0;0m'.format(
                    COLOR32.STYLE[style], COLOR32.TEXT_COLOR[text_color], COLOR32.BACKGROUND_COLOR[background_color],
                    style, text_color, background_color,
                    id_plus,
                ))
                STYLE_ID_DICT[id_plus] = "\033[{0};{1};{2}m".format(style, text_color, background_color)
                id_plus += 1

        text_color = text_color_list[9:][index]
        for text_color in COLOR32.TEXT_COLOR:
            for style in COLOR32.STYLE:
                use_print_1('ID {6:>4} style {0} text_color {1} background_color {2}: \033[{3};{4};{5}m CHERRY \033[0;0m'.format(
                    COLOR32.STYLE[style], COLOR32.TEXT_COLOR[text_color], COLOR32.BACKGROUND_COLOR[background_color],
                    style, text_color, background_color,
                    id_plus,
                ))
                STYLE_ID_DICT[id_plus] = "\033[{0};{1};{2}m".format(style, text_color, background_color)
                id_plus += 1

    # 按颜色分类打印样式 256
    for fgbg in COLOR256.FGBG:
        for color_code in COLOR256.COLOR_CODE:
            use_print_1('ID {0:>4} FGBG {1} Color Code {2:>3}: \033[{1};5;{2}m CHERRY \033[0;0m'.format(
                id_plus, fgbg, color_code,
                ))
            STYLE_ID_DICT[id_plus] = "\033[{0};5;{1}m".format(fgbg, color_code)
            id_plus += 1

    for color_code_48 in COLOR256.COLOR_CODE:
        for color_code_38 in COLOR256.COLOR_CODE:
            # use_print_1("\033[48;5;{0}m\033[38;5;{1}m CHERRY \033[0;0m".format(color_code_48, color_code_38))
            STYLE_ID_DICT[id_plus] = "\033[48;5;{0}m\033[38;5;{1}m".format(color_code_48, color_code_38)
            id_plus += 1

    """ 打印所有颜色样式列表 """
    print_n = 0
    try:
        columns = os.get_terminal_size().columns
    except Exception as err:
        # File "/usr/local/lib/python3.9/site-packages/cprint/main.py", line 7, in <module>
        #     STYLE_CONFIG = getshow_config(1)
        # File "/usr/local/lib/python3.9/site-packages/cprint/tools.py", line 109, in getshow_config
        #     columns = os.get_terminal_size().columns
        # OSError: [Errno 25] Inappropriate ioctl for device
        columns = 100
        print("WARNING: os.get_terminal_size Err, Get default columns = 100.")
        traceback.print_exc()
        print(err)

    for style_id, style_code in STYLE_ID_DICT.items():
        use_print_2('{0} {1:^5} \033[0;0m'.format(style_code, style_id), end="")
        print_n += 1
        if print_n % math.floor(columns / 7) == 0:
            use_print_2()

    # print("DEBUG Caclute 2!")
    if mode == 1:
        return STYLE_ID_DICT

def demo():
    """ 随机测试 """
    import cprint
    import random

    # print("@56056{0}@45031{1}".cformat("Hello ", " World!"))
    for _ in range(10):
        style_id_1 = random.randrange(0, 70943)
        style_id_2 = random.randrange(0, 70943)
        print(("@" + str(style_id_1) + "{0}@" + str(style_id_2) + "{1}").cformat("Hello ", " World!"))

def demoid():
    """ 随机测试并显示id """
    import cprint
    import random

    # print("@56056{0}@45031{1}".cformat("Hello ", " World!"))
    for _ in range(10):
        style_id_1 = random.randrange(0, 70943)
        style_id_2 = random.randrange(0, 70943)
        print(("@" + str(style_id_1) + "{0}@" + str(style_id_2) + "{1} {2:>6} {3:>6}").cformat(
            "Hello ", " World!", style_id_1, style_id_2
            ))