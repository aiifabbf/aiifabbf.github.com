====================
``Canon & Baroque``
====================

又换博客样式了（哪有？）。5年前，我用Vue把博客变成了个半自动前端渲染的单页面应用。所有逻辑都写在404.html里面，因为Github Pages会在找不到页面的时候加载404.html，于是里面的代码就去得到当前的URL，然后去_build里面找对应的HTML，拿出来放到DOM里。

这么做是因为Github速度有点慢，文章加载的时候页面会变成纯白色（或者暗黑模式下的黑色），而我想做出类似Youtube那样加载的时候页面无缝切换的效果。另一个就是觉得好玩啦。

当时这让我成就感满满，我想着也许这样我就不会再折腾样式，就能静下心来好好写内容。结果呵呵，大家也都看到了，博客的样式确实5年没变过，但内容我也没写多少😅。

但这么做也带来几个问题：Sphinx生成出来的HTML和文章源码混合在一起，而git仓库不应该包含任何生成出来的文件，就像不应该把GCC生成的可执行文件放在git仓库里一样；有的浏览器上，按回退无法回到上一个页面刚才看到的那一行，永远会回到页面的最上面；评论功能也不好做，我一开始想 `用Github的issues来做 <https://github.com/gitalk/gitalk>`_ ，看到过其他人的博客有这么实现的，但我不知道该怎么给我这个动态页面做。

所以，算了！回到博客的本真。我对前端技术的兴趣也没有以前那么强烈了。也许我还会为了可读性而调整样式。现在我的文章源码放在master分支上，Sphinx生成的HTML放在github-pages分支上，让Github Pages发布github-pages分支。这样好像还是违背了“生成出来的文件不应该被git管理”的原则，不过这样至少所有生成出来的文件在另一个分支上，我可以随时清理这个分支，不会使仓库大小无限增长。

.. toctree::
    :hidden:
    :glob:

    posts/*

最近
=====

-   :doc:`posts/backup-iphone-photos`
-   :doc:`posts/lambda-calculus`
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

    posts/lambda-calculus.rst
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
-   `MP <https://mpraiser.github.io>`_ 萌萌的MP子，微电子，但是软件
-   `Eden Chen <https://vendredii.github.io>`_ 可恶的资本家，生态学，最近在荷兰读博
-   `Bob <https://yyccli.github.io>`_ 可爱的学弟，超级喜欢他的文笔
-   `Dudu <https://star-du.github.io>`_ 爱思考的纯文学爱好者，阅读量浩如烟海，自学转码，最近被我安利了Rust

你是谁啊/这是什么破网站啊
==============================

在下Benjamin Shi，现在是某紫色EDA公司的码农。本科在 `华科 <http://www.hust.edu.cn>`_ 读的集成电路，硕士在米国读的计算机。

这个博客的定位是比较正经的 [#]_ 朋友圈。主要记录一点人生的经验 [#]_ （牢骚）。

如果你也恰好有缘学同样的东西，希望我的笔记能给你带来一点启发。笔记初衷都是为了写给我自己看的，我是理解能力很差、又很健忘的人，这些笔记承担着n年后唤起我回忆的重任。所以我相信我能懂的你也一定能懂。如果不懂你别打我QAQ，发邮件给我吧。

拒绝 `知识的诅咒 <https://en.wikipedia.org/wiki/Curse_of_knowledge>`_ 。我觉得我从小到大深受其害，希望自己以后不要落入这个陷阱、变成之乎者也自嗨的老学究。知识的精神是开放和传播，不是吗？所有人都能享受新知的快乐，岂不美哉？

留个邮箱吧 aiifabbf at outlook.com 。在 `知乎 <https://www.zhihu.com/people/benjamin-shi>`_ 上也可以找到我。有什么问题欢迎交流。一緒に遊びましょう〜〜

.. [#] 就是带公式的。你总不能在朋友圈里发DFT的理解吧……关爱智障的眼神.jpg
.. [#] 以后会多记录一点心路历程，最近转CS的路上遇到了太多烦心的事情。
