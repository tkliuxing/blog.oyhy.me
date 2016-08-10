Date: 2016-08-10
Title: ECMAscript Startup (1)
Published: true
Type: post
Category: Coding
Tags: javascript, ECMAscript, ES2015
Slug: es-startup-01

### ECMAscript 简介

ECMAscript 简称 ES。之前 ECMAscript 发布了5个版本，从 ES1 到 ES5 。
该标准在2015年后将每年发布一次，所以最新的标准应为 ES2016 。
但是因为 ES2016 之比 ES2015 增加了两个 feature ：

* Array.prototype.includes (Domenic Denicola, Rick Waldron)
* Exponentiation Operator (Rick Waldron)

所以还是从 ES6/ES2015 这个阶段的标准开始认识 ECMAscript 吧。

** 更多关于 ES 的历史请看 [这里](http://es6.ruanyifeng.com/#docs/intro)

### 环境准备

#### nodejs

在这个时间点上，nodejs 已经发布了 v6 版本，具体的版本号为 v6.3.0。
其已经涵盖了绝大多数 ES6 的特性，故而安装此最新版本。

#### babel 转换器

Babel是一个广泛使用的ES6转码器，可以将ES6代码转为ES5代码，从而在现有环境执行。
可使用 npm 安装：

~~~.sh
npm install --save-dev babel-cli
npm install --save-dev babel-polyfill
npm install --save-dev babel-preset-react
~~~

