==========
换行缩进迷思
==========

很喜欢的VS Code的一个特性是，开启word wrap之后，如果某一行太长，会自动拐到下一行

::

    1  |a very long line a very long line
       |a very long line a very long line
       |a very long line
    2  |a very long line

当然这只是视觉上显示为多行，文本数据上第1行仍然是只有最后一个换行符。

这还不是最赞的，最赞的是，如果这一行开头有空格缩进，wrap过来的其他行前面也会有相同长度的缩进

::

    1  |    a very long line a very long
       |    line a very long line a very
       |    long line a very long line
    2  |a very long line

如果在vim上，wrap的其他行前面不会有相同长度的缩进，只有第一行有

::

    1  |    a very long line a very long
       |line a very long line a very long
       |line a very long line
    2  |a very long line

这在写代码和写文字的时候非常方便。比如写list item下面的补充文字，一眼就能看出整个块都属于当前item

::

    1  |*   butter
    2  |
    3  |    a very long line a very long
       |    line a very long line a very
       |    long line a very long line
    4  |
    5  |*   bread

找了半天也没找到这个特性的严谨称呼叫什么，更不知道用CSS如何实现，我想要在博客的代码块里也实现相同的效果。现在博客里的代码，如果某一行特别长，会像vim一样拐到下一行的最前面，显得非常杂乱。

终于找到了， `vim也有这个特性 <https://stackoverflow.com/questions/1204149/smart-wrap-in-vim>`_ ，叫做 `breakindent` ，可以用

::

    set breakindent

开启。

不过还是不知道CSS怎么实现。用F12看了VS Code的DOM，发现是用代码在前面动态插入相同数量的空格，并没有用纯CSS实现。

2025/3/19
