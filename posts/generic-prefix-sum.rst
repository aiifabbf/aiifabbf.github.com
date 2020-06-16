===========
前缀和的推广
===========

.. default-role:: math

.. note:: 前情提要

    最近终于刷到了700题，终于有那么点赶上通货膨胀的希望了。做到现在有两个感受最明显

    -   题目真的是有套路的
    -   我太缺乏想象力了

上一篇前缀和技巧的总结写了没过多久，我又陆续发现了一些其他的题目也能套这个思路，但是它们又不是前缀“和”，而是累积最大值、前缀异或。

前缀异或
========

还记得前缀和里面我们是怎么做的吗？我们先定义了

.. math::

    A_j = a_0 + a_1 + \cdots + a_{j - 1}

然后每次需要计算substring累加和的时候，比如需要计算 `a_i + a_{i + 1} + \cdots + a_{j - 1}` 的时候，只需要 `A_j - A_i` 就可以了。

其实这个结论可以推广一下。有没有发现 `+` 和 `-` 是一对逆运算？不如大胆假设，对于任何互为逆运算 [#properties]_ 的 `\bullet` 和 `\circ` ，都可以这么做

.. math::

    A_j \circ A_i = a_i \bullet a_{i + 1} \bullet \cdots \bullet a_{j - 1}

比如 `\times` 和 `\div` 是互逆的，那可以出道题

    给一个不含0的array，计算任意substring（要连续）的累乘。

是不是直接定义

.. math::

    A_j = a_0 \times a_1 \times \cdots \times a_{j - 1}

然后

.. math::

    A_j \div A_i

就好了？

顺便 `1310 <https://leetcode.com/problems/xor-queries-of-a-subarray/>`_ 也能做了。题目是

    给一个array，计算任意substring（要连续）的累积异或。

也就是要算 `a_i \oplus a_{i + 1} \oplus \cdots \oplus a_{j - 1}` 。

那异或的逆运算是啥呢？似乎就是它本身……因为

.. math::

    a \oplus b \oplus b = a \oplus (b \oplus b) = a \oplus 0 = a

所以大胆定义

.. math::

    A_j = a_0 \oplus a_1 \oplus \cdots \oplus a_{j - 1}

然后

.. math::

    A_j \oplus A_i = a_i \oplus a_{i + 1} \oplus \cdots \oplus a_{j - 1}

就完事儿了。

.. note:: Rust里面要算这种累积和、累积乘之类的非常方便，直接用 ``Iterator`` 的 ``scan()`` 方法就可以了。上面的累积xor可以写成

    .. code-block:: rust

        let integrals: Vec<i32> = vec![0]
            .into_iter()
            .chain(array.into_iter().scan(0, |state, v| {
                *state = *state ^ v; // 要存的东西
                return Some(*state); // 要吐的东西
            }))
            .collect();

    出来之后 ``integrals[j] ^ integrals[i]`` 就是 ``array[i..j]`` 的累积xor了。

    Python的话，虽然有 ``itertools.accumulate()`` ，但是没有 ``itertools.accumulative_xor()`` （废话）。至今没有找到很好的写法，可能只能for了。

累积最大值
==========

说的就是 `42接雨水 <https://leetcode.com/problems/trapping-rain-water/>`_ 这道题。题目大概是

    给一个全是自然数的array， ``array[i]`` 表示第 `i` 格上有多少块石头。现在下雨了，这堆石头能接多少格水。

比如给

::

    0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1

表示这堆石头大概长这样

::

           o
       o   oo o
     o oo oooooo
    ------------

盛满雨水的话，就变成了

::

           o
       o~~~oo~o
     o~oo~oooooo
    ------------

能接6格雨水。官网的示意图更清楚。

第 `i` 格能接多少水取决于啥呢？假如你是水（误），如果你滴到一块凹的地方，就不会从两边流下去。怎么体现凹这件事情呢？其实就是从第 `i` 格比左右两边最高的石头要矮。严谨点说就是第 `i` 格的高度小于 `\min\{x, y\}` ，其中 `x` 是往左边看过去最高的石头的高度， `y` 是往右边看过去最高的石头的高度。

比如

::

           o
       o~~~oo~o
     o~oo~oooooo
    ------------
     <-- | -->

看第4格，从第4格往左边看，最高的是2，往右边看，最高的是3。第4格本身高度是0，所以能接的水就是 `\min\{2, 3\} - 0 = 2` 。

再比如

::

           o
       o~~~oo~o
     o~oo~oooooo
    ------------
          <-- | -->

看这一格，往左边看，最高的就是左边紧邻的3，往右边看过去，最高的是1。可是这一格本身的高度就是2，所以接不到水。

写严谨一点，第 `i` 格能接的水是

.. math::

        \max\left\{
            \min\left\{\begin{aligned}
                & \max\{a_j | j < i\} \\
                & \max\{a_j | j > i + 1\} \\
            \end{aligned}\right\} - a_i,
            0
        \right\}

那每到第 `i` 格，都要往前扫描一遍、往后扫描一遍，得到往两边看过去的最大值，就不太合算。不如把这个信息事先缓存起来。比如整一个 ``maximumBefore[i]`` 表示 ``max(array[: i])`` 、 ``maximumAfter[i]`` 表示 ``max(array[i: ])`` 。这样就能做到 `O(n)` 复杂度了。

`155 stack的最小值 <https://leetcode.com/problems/min-stack/>`_ 也是类似的做法。

2020/4/15

.. [#properties] 似乎还需要其他的性质，比如交换律。但是也不一定，可以巧妙规定 `\circ` 的规则，比如如果 `A_j` 是前 `j` 个矩阵的乘积，即 `A_j = \mathbf{A}_0 \mathbf{A}_1 \cdots \mathbf{A}_{j - 1}` ，定义 `A_i \circ A_j = A_i^{-1} A_j` ，那么 `A_j \circ A_i` 就能得到 `\mathbf{A}_i \mathbf{A}_{i + 1} \cdots \mathbf{A}_{j - 1}` 了。