---
layout: page
title: Teaching
use-site-title: false
---

# 《图像处理与成像制导》作业(2018-01)

## 提交作业相关信息

- 提交作业截止时间： 2018/05/01 23:59:59 (CST)
- 作业提交方式：
  - 发送电子邮件至 fred DOT qi AT ieee DOT org
  - 邮件标题格式： \[IMGNAV\] HW1801-学号-姓名 
- 提交作业注意事项
  - 需要撰写书面报告，汇报所实现程序的实现方案，并进行功能展示。
  - 若源代码包括多个文件，请将源代码压缩。
  - 书面报告与源代码分两个附件文件提交，报告文档请勿压缩。
  - 请勿提交示例图像文件及编译语言编译产生的二进制文件。
  - 请勿使用链接方式提交附件。
  
## 1. 图像读写

阅读[BMP文件格式说明](https://zh.wikipedia.org/wiki/BMP)，选择自己熟悉(或喜欢)的
编程语言实现**灰度BMP图像**文件的读写功能。即实现以下两个函数：

- `imread`
- `imwrite`

对于使用Python语言的同学有以下提示：
- 推荐使用 Python 3
- 函数接口可以参
  考[`scikit-image`的函数](http://scikit-image.org/docs/dev/api/skimage.io.html)`imread`
  和`imsave`。
- 对文件头数据的解析请参考使用 [`struct`库](https://docs.python.org/3/library/struct.html)

