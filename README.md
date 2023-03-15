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

# cformat
import cprint
print("@56056{0}@45031{1}".cformat("Hello ", " World!"))

# iformat
import cprint
cprint.custom_style = {1: 612, 2: 1224}
print("@1{0}@2{1}".iformat("Hello ", " World!"))

# [] format
print("@56056{0}@45031[ World!]".cformat("Hello "))
```

![use][2]

只需要在 `{}` 前加上`@样式id`, 然后把 `format` 改为 `cformat` 就可以按照样式id输出彩色文本

## 查看颜色样式ID

**命令行输入 `cpshow` 查看所有的样式id**

颜色样式ID为 `@` 后面的数字, 现在一共有 **70943** 个不同的样式可以选择, 不同的终端效果不一样, 有些终端可能不支持, 请自行测试.

![style][3]

## 其他命令行

* `cpdemo` : Hello World! 样例
* `cpdemoid` : Hello World! 样例并显示样式ID

可以多次调用 `cpdemoid` 查看样式配色, 选择喜欢的ID.

## iformat
可以通过赋值 `cprint.custom_style` 来自定义配置自己的id映射表, 这样可以提前配置几套不同的 `id theme` id主题, 然后可以根据喜好或者根据不同的终端配色切换主题配色

```
# iformat
import cprint

# theme 1
cprint.custom_style = {1: 612, 2: 1224}
print("@1{0}@2{1}".iformat("Hello ", " World!"))

# theme 2
cprint.custom_style = {1: 5547, 2: 66795}
print("@1{0}@2{1}".iformat("Hello ", " World!"))
```

也可以提前把配色序列写入 `.py` 文件中, 然后在程序启动的时候导入赋值就行.

## 固定常量

在字符串中使用 `@NOW`, `@DATE`, `@TIME` 可以获取到对应的时间字符串
```
print(" NOW: @NOW ".cformat())
print("DATE: @DATE ".cformat())
print("TIME: @TIME ".cformat())
```
```
 NOW: 2023-02-23 10:23:35
DATE: 2023-02-23
TIME: 10:23:35
```

## 实现方式

[How to Print Colored Text in Python](https://stackabuse.com/how-to-print-colored-text-in-python/)

![how][4]
![how][5]

除了输出颜色字符外, 这种方式还可以控制光标移动、清屏、控制终端更改背景颜色等操作.

## 更新记录
最新版本: **cprint-jianjun v1.3.0**
* 20221116: 1.更新新的常量 `@NOW`, `@DATE`, `@TIME` 的功能 2.更新文档
* 20230223: 1.更新文档 2.增加 `cpdemoid` 命令行.
* 20230303: 1.更新 `iformat` 函数.
* 20230315: 1.更新 `[]` 功能.

  [1]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/1.png
  [2]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/2.png
  [3]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/3.png
  [4]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/4.jpg
  [5]: https://raw.githubusercontent.com/EVA-JianJun/cprint/master/img/5.jpg
