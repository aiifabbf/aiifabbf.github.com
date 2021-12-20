====================
``Canon & Baroque``
====================

懒惰，真的是一件非常可怕的事情……我竟然已经一年多没有更新了。事实上这一年发生的事情非常非常多。

首先是2020/12我从米国（黯然）回来了，想着过完元旦再去工作。过完元旦之后，想着过年也不远了，算了算了不折腾了……终于到了2021/3，我去了上海某家紫色EDA厂，做一个我之前听说过、但是从来没用过的数字电路前端验证工具（内行人大概已经知道是什么了）。我本科的时候都在做模拟电路（虽然也没做出个啥），除了上过Verilog课、写过FPGA上的自动售货机之外没怎么接触过数字的东西。不过我大概知道是怎么回事。

我做其中一个听起来有点和验证不太相关的特性。我虽然写过Verilog，但是以前从来没听说过这个特性；听说了之后，也无法自发想出这个特性在验证数字电路的时候有什么用处。我有很多微电子在读研究生朋友，其中有研究方向是数字电路的，也很少听说过这个特性。

不过我最近发现它竟然和定理证明器有关系。机器证明定理是我最近非常感兴趣的领域，从外行人看热闹的角度，我觉得它大概有这些非常突出的优点

-   如果能像写代码一样，严谨的写出数学证明，再用软件自动检查，就会少很多假新闻了
-   一些已有的定理可以做成通用库，然后引用定理的时候像引用库一样import进来直接用
-   用数学来严谨推断程序的行为，可以让软件更可靠

所以最近在看数理逻辑方面的书。为啥是数理逻辑呢？其实一开始也是想强行看 `Software Foundations <https://softwarefoundations.cis.upenn.edu/>`_ 和 `Coq <https://coq.inria.fr/>`_ 的，实在是看不懂。

3月的时候写了个小玩具， `用Rust山寨了个Haskell里面的parsec <https://github.com/aiifabbf/parsec>`_ 。最开始写这个是想实现SQL数据库的、为了解析SQL文法的。可是写着写着发现自己又对Haskell感兴趣了。看了一点 `Learn You a Haskell <http://learnyouahaskell.com/>`_ ，启发挺大的，渐渐开始理解Rust里面一些东西设计的动机，开始觉得日常写的C/C++非常难看，看到全局变量、传入指针修改数据就烦，甚至周赛都不想用Python写了。

选择EDA之前也有过纠结，因为还拿到了别的互联网、游戏公司的offer，还有做图形驱动的，其实都是我很想做的领域。最后还是选了情怀加成最大的EDA。

所以不管了，All in EDA! Make EDA great again!

.. toctree::
    :hidden:
    :glob:

    posts/*

最近
=====

-   :doc:`posts/binary-search-ptsd`
-   刷Leetcode。现在刷了 **1100道** 了！人生巅峰上了一次2100分！虽然没几天就降下去了……

    -   `超级详细的代码注释 <https://github.com/aiifabbf/leetcode-memo>`_ 保准你一看就会
    -   `Leetcode个人主页 <https://leetcode.com/aiifabbf>`_ 哪天看我没做题请打我嘤嘤嘤

-   照着神书 `Ray Tracing in One Weekend <https://raytracing.github.io>`_ ，用Rust写了个 `光线追踪渲染器 <https://github.com/aiifabbf/ray-tracer>`_
-   未解之谜 :doc:`posts/multivariate-recurrence-equation`
-   :doc:`posts/generic-prefix-sum`
-   :doc:`posts/paypal-interview/index` 一面挂了
-   :doc:`posts/prefix-sum/index`
-   :doc:`posts/mathworks-interview/index` 三面挂了
-   :doc:`posts/amazon-interview/index` 根本不给我OA
-   :doc:`归约和NP问题 <posts/reduction-np>`
-   去米国了
-   :doc:`毕业了 <posts/after-graduation>`

略懂
====

.. toctree::
    :maxdepth: 1

    posts/binary-search-ptsd.rst
    posts/generic-prefix-sum.rst
    posts/prefix-sum/index.rst
    posts/reduction-np.rst

流水账
=========

-   :doc:`毕业了 <posts/after-graduation>`
-   `回到CS <jupyter/return-to-cs.html>`_
-   `GRE考场服务 <jupyter/gre-experience.html>`_
-   `港科面试 <jupyter/hkust-interview.html>`_

上岸
=====

.. toctree::
    :maxdepth: 1

    posts/paypal-interview/index
    posts/mathworks-interview/index
    posts/amazon-interview/index

笔记
=====

-   `离散数学 <jupyter/notes-discrete-mathematics.html>`_
-   `算法 <jupyter/notes-introduction-to-algorithms.html>`_
-   :doc:`Leetcode <posts/README>`
-   `数字信号处理 <jupyter/dsp.html>`_
-   `通信原理 <jupyter/principles-of-communication.html>`_
-   `CMOS模拟集成电路 <jupyter/cmos-ii.html>`_
-   `托福作文 <https://github.com/aiifabbf/toefl-writings>`_

学习愿望清单
===============

还没学的东西怎么可能有链接嘛(～￣▽￣)～

-   N1
-   CS全家桶（快了在学了）
-   控制原理
-   复分析
-   实分析
-   拓扑学
-   高等量子力学
-   微观经济学
-   乐理

未解之谜
========

-   :doc:`posts/multivariate-recurrence-equation`

友情链接
==========

下面是大佬时间。

-   `Ivy End <https://ivy-end.github.io>`_ 竞赛选手，文言大家，最近好像在做芯片方面的事情
-   `MP <https://mpraiser.github.io>`_ 萌萌的MP子，微电子
-   `Eden Chen <https://vendredii.github.io>`_ 可恶的资本家，生态学
-   `Bob <https://yyccli.github.io>`_ 可爱的学弟，超级喜欢他的文笔

你是谁啊/这是什么破网站啊
==============================

在下Benjamin Shi，现在是某紫色EDA公司的码农。本科在 `华科 <http://www.hust.edu.cn>`_ 读的集成电路，硕士在米国读的计算机。

这个博客的定位是比较正经的 [#]_ 朋友圈。主要记录一点人生的经验 [#]_ （牢骚）。

如果你也恰好有缘学同样的东西，希望我的笔记能给你带来一点启发。笔记初衷都是为了写给我自己看的，我是理解能力很差、又很健忘的人，这些笔记承担着n年后唤起我回忆的重任。所以我相信我能懂的你也一定能懂。如果不懂你别打我QAQ，发邮件给我吧。

拒绝 `知识的诅咒 <https://en.wikipedia.org/wiki/Curse_of_knowledge>`_ 。我觉得我从小到大深受其害，希望自己以后不要落入这个陷阱、变成之乎者也自嗨的老学究。知识的精神是开放和传播，不是吗？所有人都能享受新知的快乐，岂不美哉？

留个邮箱吧 aiifabbf at outlook.com 。在 `知乎 <https://www.zhihu.com/people/benjamin-shi>`_ 上也可以找到我。有什么问题欢迎交流。一緒に遊びましょう〜〜

.. [#] 就是带公式的。你总不能在朋友圈里发DFT的理解吧……关爱智障的眼神.jpg
.. [#] 以后会多记录一点心路历程，最近转CS的路上遇到了太多烦心的事情。
