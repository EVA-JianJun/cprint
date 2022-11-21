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

## 固定常量

在字符串中使用 `@NOW`, `@DATE`, `@TIME` 可以获取到对应的时间字符串
```
print(" NOW: @NOW ".cformat())
print("DATE: @DATE ".cformat())
print("TIME: @TIME ".cformat())
```

## 实现方式

[How to Print Colored Text in Python](https://stackabuse.com/how-to-print-colored-text-in-python/)

![how][4]
![how][5]

除了输出颜色字符外, 这种方式还可以控制光标、清屏的操作, 在其他语言如 `c` 下还有控制终端整体更改背景颜色类似的更高级的方法

## 更新记录
* 20221116: 1.更新新的常量 `@NOW`, `@DATE`, `@TIME` 的功能 2.更新文档

  [1]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/1.png
  [2]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/2.png
  [3]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/3.png
  [4]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/4.jpg
  [5]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/5.jpg
