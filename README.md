# Colorful Print

**彩色文本格式化, 彩色文本输出, 控制打印字符颜色样式!**

![main][1]

## 安装

    pip install -U cprint-jianjun

## 简介

让你的终端输出各式各样的彩色文本, 以一种非常简便的方式嵌入到程序中!

```
# default
print("{0}  {1}".format("Hello", "World!"))

# use cprint
import cprint
print("@56056{0}@45031{1}".cformat("Hello ", " World!"))
```

![use][2]

只需要在 `{}` 前加上`@样式id`, 然后把 `format` 改为 `cformat` 就可以按照样式id输出彩色文本

## 查看颜色样式ID

颜色样式ID为 `@` 后面的数字, 安装完在命令行输入 `cpshow` 查看所有的样式id, 现在一共有 **70943** 个不同的样式可以选择, 不同的终端效果不一样, 有些终端可能不支持, 请自行测试.

![style][3]

## 其他命令行

* `cpshoww` : 显示详细颜色信息
* `cpdemo` : Hello World! 样例

  [1]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/1.png
  [2]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/2.png
  [3]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/3.png
