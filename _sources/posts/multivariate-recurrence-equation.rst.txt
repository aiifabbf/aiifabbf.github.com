==================
多元递推方程怎么解？
==================

.. default-role:: math

.. note:: 前情提要

    头条三面的时候被问了一道 `Leetcode原题 <https://leetcode.com/problems/spiral-matrix/>`_ ，就是那道顺时针螺旋遍历矩阵的题。我先是解释了一下大致的思路，还使了个剥洋葱的比喻。用递归两分钟就美滋滋地写完了，一脸得意地看着面试官。

    然后面试官问，那你能不能求一下最后一个被遍历的元素的坐标的通项公式呢？假设矩阵是 `m` 行 `n` 列的。我有点懵了，搞了半天都没搞出来，只能先分情况讨论、先拿点步骤分了。我先是分出 `m = n` 和 `m \neq n` 的情况。 `m = n` 的情况又要细分成 `m, n` 是偶数和奇数两种情况。

    `m \neq n` 的情况搞了十五分钟都没有搞出来。最后我只能说，那我把递推式先写出来吧。

    递推式很快就写出来了，很简单

    .. math::

        \mathbf{f}(m, n) = (1, 1) + \mathbf{f}(m - 2, n - 2)

    还有4个初始条件

    .. math::

        \begin{aligned}
            \forall m \geq 1, &\qquad \mathbf{f}(m, 1) = (m - 1, 0) \\
            \forall n \geq 1, &\qquad \mathbf{f}(1, n) = (0, n - 1) \\
            \forall m \geq 2, &\qquad \mathbf{f}(m, 2) = (1, 0) \\
            \forall n \geq 2, &\qquad \mathbf{f}(2, n) = (1, 0) \\
        \end{aligned}

    然后我就盯着递推式盯了十分钟，还是没有任何思路。

面完之后回头一想，这个问题真的是不简单……我只知道形如单元标量函数的递推方程用特征方程能求出闭式解，比如斐波那契数列

.. math::

    f(n) = f(n - 1) + f(n - 2)

初始条件 [#initial-condition]_

.. math::

    \begin{aligned}
        f(0) &= 0 \\
        f(1) &= 1 \\
    \end{aligned}

可以写成矩阵乘法的形式

.. math::

    \left(\begin{matrix}
        f(n) \\
        f(n - 1) \\
    \end{matrix}\right) = \left(\begin{matrix}
        1 & 1 \\
        1 & 0
    \end{matrix}\right) \left(\begin{matrix}
        f(n - 1) \\
        f(n - 2) \\
    \end{matrix}\right)

进一步得到

.. math::

    \left(\begin{matrix}
        f(n) \\
        f(n - 1) \\
    \end{matrix}\right) = \left(\begin{matrix}
        1 & 1 \\
        1 & 0 \\
    \end{matrix}\right)^n \left(\begin{matrix}
        f(1) \\
        f(0) \\
    \end{matrix}\right)

到这里啥都会了，不就是要求矩阵 `\left(\begin{matrix} 1 & 1 \\ 1 & 0 \end{matrix}\right)` 的特征值和特征向量吗？算出来是两个特征值，每个分别对应一个特征向量。接着把

.. math::

    \left(\begin{matrix}
        f(1) \\
        f(0) \\
    \end{matrix}\right)

用两个特征向量分解，或者说用两个特征向量作为基底来表示，带进去就能算出来了。

那回到原问题……这里有两个难点

-   这个函数的输入是二维的
-   这个函数的输出也是二维的

对于第二个难点，好像可以用拆分解决，把 `\mathbf{f}(m, n)` 拆成 `(f_1(m, n), f_2(m, n))` 。

但是第一个难点就怎么也没法绕过去了，看上去 `m, n` 不是独立的，是耦合的，所以没法分离变量。

搜了一下，发现也没什么通用的方法

-   `stackexchange <https://math.stackexchange.com/questions/162010/linear-multivariate-recurrences-with-constant-coefficients>`_ 讲到了一个什么kernel method
-   `维基百科上 <https://en.wikipedia.org/wiki/Generating_function>`_ 提到了多元生成函数

.. [#initial-condition] 用了 `维基百科 <https://en.wikipedia.org/wiki/Fibonacci_number>`_ 的定义。