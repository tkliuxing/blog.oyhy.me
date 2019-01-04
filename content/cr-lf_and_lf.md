Date: 2015-07-14
Title: Windows 换行符为什么设计成 CR+LF？
Published: true
Type: post
Category: Coding
Tags: django, python, celery
Slug: cl-rf-and-rf


CR 和 LF 最初是控制电传打印机（Teletype，所以 UNIX 里面有个 tty，就是这玩意的缩写）的，CR 把打印头移动到行首，LF 把纸上卷一行，因为 CR 要的时间更长所以一般要求换行的过程里面都是 CR 在前（有些早期设备甚至还会在 CR 和 LF 之间插 NUL，确保打印头完成复位）。DOS 从 DEC 和 CP/M 那里继承了这个设计，这样文本文件的字节序列可以直接控制打印机。而 Unix 的前身 Multics 里面有一个驱动程序，会自动将 LF 转换成 CR-LF（甚至 CR-NUL-LF），所以他们用了单一的 LF。

而 Windows 是从 DOS 而来的，所以继承了这个`传统`。