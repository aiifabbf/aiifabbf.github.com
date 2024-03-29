===================
Lambda calculus妙啊
===================

.. default-role:: literal

最近看了个 `讲lambda calculus的talk <https://www.youtube.com/watch?v=3VQ382QG-y4>`_ ，惊为天人，是我有生以来听过的最清晰、最舒服的talk，完全没有 `curse of knowledge <https://en.wikipedia.org/wiki/Curse_of_knowledge>`_ 。或许因为作者和我的认知路径是一样的，都是从日常编程逐渐发掘到这些；或许因为作者精心设计；也可能是因为lambda calculus本身就是一套极其优雅的系统，优雅到没有任何记忆负担：如果哪天不小心忘记了用函数怎么表示true、false、自然数，也可以根据仅仅三条简单的规则，完全从头开始推导。

只有单元函数的世界
================

Lambda calculus里只有3种东西

-   变量，比如 `a, b, c`
-   定义，比如 `λa. a`
-   作用，比如 `f a`

是的，就这么简单。这三样东西可以对应到Python、JavaScript等主流语言里我们都见过的东西

-   变量是个符号，用来标记函数接受的输入是什么、在函数的定义式里面是怎么使用的。当我们想要在函数的定义式里指代函数的输入的时候，可以用那个变量来表示。特别当函数有好几个输入的时候，变量可以用来区别你指代的是哪一个输入

    比如 `λa. λb. a` 里面的 `a, b` 都是变量。一种解释是 `a` 代表函数的第一个参数、 `b` 代表函数的第二个参数。显然 `λa. λb. a` 和 `λa. λb. b` 代表的是不同的含义。

-   定义可以对应单变量参数的匿名函数的定义

    比如 `λa. a` 用Python写是

    .. code-block:: python

        lambda a: a

    不能说完全相似，只能说简直是一模一样。

    复杂一点的，比如 `λn. λf. λa. f (n f a)` 也不难写，加几个括号就可以了，因为Python用 `f(x)` 这样的形式表示调用

    .. code-block:: python

        lambda n: lambda f: lambda a: f(n(f)(a))

    注意lambda calculus里函数定义是右结合的，比如

    ::

        λa. λb. λc. a

    括号拉满其实是

    ::

        λa. (λb. (λc. a))

    巧了Python的 `lambda` 也是右结合的

    .. code-block:: python

        lambda a: lambda b: lambda c: a

-   作用就是函数调用，传入参数，算出返回值

    比如 `f a` 就是Python里的

    .. code-block:: python

        f(a)

    `(λa. a) (λb. b)` 是

    .. code-block:: python

        (lambda a: a)(lambda b: b)

    Lambda calculus里作用是左结合的，比如

    ::

        f g a b c

    括号写全是

    ::

        (((f g) a) b) c

    在Python里是

    .. code-block:: python

        f(g)(a)(b)(c)

文章里不加括号可能有歧义的地方我都会把括号写全的。

现在有了这3样最基本的元素，那么calculus、所谓的运算在哪里？推导规则是怎样的？很简单的，和Python是一样的，举个例子

::

    (λa. a) x

推导出来是啥？想想Python里上面的式子怎么写

.. code-block:: python

    (lambda a: a)(x)

答案是 `x` 。

推导的过程中我们做了啥呢？我们把 `(λa. a) x` 右边那个输入，也就是 `x` ，带入到了左边的函数定义式 `λa. a` 里面，取出函数的定义式，把定义式里面所有的 `a` 都替换成了输入 `x` 。于是我们得到了 `x` 。

函数的输入为什么不能是另一个函数呢？完全可以，看看这个例子

::

    (λa. a) (λb. b)

推导出的结果是

::

    (λb. b)

发现 `λa. a` 这个函数很有意思吧？输入任何东西都会得到原模原样的东西回来。这叫 `identity` 函数。之后我们会用 `identity` 来代表 `λa. a` 。

啰嗦两句，这么做只是偷懒，为了节省一下敲键盘打出 `λa. a` 的时间（敲出 `λ` 真不容易啊），在所有 `identity` 出现的地方，你都可以替换成 `λa. a` 。有点类似C的宏？

.. 注意类似 `λa. c` 这样的东西是没有意义的，因为我们在哪里都没有说明 `c` 是什么。 `c` 是一个free variable，没有在前面的参数列表里出现过，没有和任何一个 `λ` 黏在一起。

再看看这个例子

::

    (λa. λb. a) x y

我们又遇到了 `λa. λb. a` 这个函数。这个 `λa. λb. a` 函数接受2个输入，输出第一个输入。

用这种视角，推导过程是取出函数定义式 `a` ，然后同时把 `a` 替换成 `x` 、把 `b` 替换成 `y` ，得到了

::

    x

写成Python可能会帮助你理解

.. code-block:: python

    (lambda a, b: a)(x, y)

你也可以用另一个角度来看这个函数，认为 `λa. λb. a` 接受1个输入，输入任何东西 `a` 之后，得到另一个函数 `λb. a` ，这个新的函数接受1个输入，但是不管输入什么，都输出那个 `a` 。

用这种视角，推导过程是把输入一个一个放进去的：先输入一个 `x` ，此时 `(λa. λb. a) x` 推导出

::

    λb. x

然后再输入另一个 `y` ，`(λb. x) y` 推导出

::

    x

写成Python大概是这样的

.. code-block:: python

    (lambda a: (lambda b: a))(x)(y)

有点晕了……我应该用哪一种视角呢？是把 `λa. λb. a` 当作接受2个输入的函数呢，还是当作接受1个输入、返回另一个函数的函数呢？这就是著名的 `Currying <https://en.wikipedia.org/wiki/Currying>`_ 。我觉得两种视角没有什么区别，但我更倾向于第二种，这样有一种简单的美感，所有的函数都只有1个输入，没有例外。

顺便把 `λa. λb. a` 叫做 `left` 吧。

.. note:: 你可能会纠结 `λa. λb. λa. a` 这种情况，最右边的 `a` 指的是第一个输入还是第三个输入。是第三个输入，所以 `(λa. λb. λa. a) x y z` 推导出的结果是 `z` 。

    和Python是一样的

    .. code-block:: python

        (lambda a: lambda b: lambda a: a)(1)(2)(3) = 3

    这种叫做 `shadowing <https://en.wikipedia.org/wiki/Variable_shadowing>`_ ，不过我们不用特别纠结这种情况……

当然也有 `λa. λb. b` 这样的接受2个输入、永远输出第二个输入的函数，不妨叫做 `right` 。

`left` 和 `right` 之间有啥关系吗？试着推导一下 `left identity`

::

    left identity
    (λa. λb. a) (λa. a)
    λb. (λa. a)

天哪，我们得到了什么！这不是就是 `right` 吗？等一下， `right` 不是 `λa. λb. b` 吗？和这个 `λb. λa. a` 是一样的吗？是一样的，试试看，你给这两个函数输入 **任何** 相同的东西，得到的结果都是一样的。这两个函数完全等价。还记得我们刚才介绍变量的时候是怎么说的吗？变量只是用来标记使用哪一个输入而已，除此以外没有别的用途。

.. note:: 所以 `λx. x` 和 `λy. y` 完全相同。

    如果你喜欢emoji，也可以用 `λ😂. 😂` 。

此处建议停下来深呼吸一下。然后我们来看更复杂的例子

::

    (λf. f f) x
    x x

这个 `λf. f f` 有一点烧脑了。输入某个东西 `f` ，输出的是这个东西作用在自身上的结果 `f f`。

我们没有说过一个函数不能输入自身吧？

::

    (λf. f f) (λf. f f)

推导一下呢？

::

    (λf. f f) (λf. f f)

……奇怪，推导出来怎么还是这个。别试了，再来一次还是这个。有没有让你想到数学里的不动点呢？所谓不动点就是使得 `f(x) = x` 的那个 `x` 。如果把我们到现在为止做的推导游戏写成一个函数 `eval` 的话（比如我们用Python写了个lambda calculus解释器）， `(λf. f f) (λf. f f)` 似乎就是 `eval` 这个函数的不动点了。

可以，很精彩，可是这玩意可以做啥呢？

布尔运算
=======

先来试一下在这个世界里构造出最简单的true和false。我们需要思考一下true和false到底是什么东西。如果你学过其他的编程语言，可能会想到这几种答案

-   false是0、true是非0的数字

    这里面出现了3个这个世界里还不存在的东西：0、非、数字。现在我们的世界里还没有这些东西。但我们等下会定义的，别着急。

    您可能是C语言的受害者（bushi），因为C一直以来都没有 `bool` 这个类型，一般大家都用个宏或者 `enum` 来定义true和false。

-   false和true是满足一些运算规则的符号

    想到false和true之间可以通过一些运算符来互相转化，比如

    ::

        not false = true
        not true = false

    还有 `and, or` 。

    一样的问题，这个世界里还没有 `not, and, or` 这些函数。不过你能想到这里已经很好了！你脱离了纠结某个东西 **是什么** ，开始考虑用某个东西 **能够做什么** 来定义这个东西本身。

-   false和true是两种不同的状态，不是这个就是那个

    和刚才说的用C里面的 `enum` 来定义是类似的

    .. code-block:: c

        enum Bool {
            True,
            False,
        }

转了一圈发现，这个世界里空空荡荡，什么都没有。我们不能随便写个 `true` 然后指着它说“钦定了！你就是true”，因为别人不知道这是什么。不同于我们刚才写 `identity, left, right` ，刚才我们只是偷懒做了个字符串替换而已，你随时都可以在看到 `identity` 的时候就把它替换成真正的定义式 `λa. a` 。

似乎我们唯一能做的事情是定义一个函数，然后像刚才那样，把这个函数的定义当作是 `true` 。或者反过来说，用函数来表示 `true` 。

我知道这个一下子不太好理解，怎么可能用函数来代表某个东西呢？但我们不是一直在做类似的事情吗？用十进制数100来表示100个苹果放在一起的数量。其实这个数量还可以用另一个二进制数来表示。还有用ASCII编码表示字母。为什么这里用函数作为底层的、表示一切的基础就不行了呢？爱函数协会表示强烈谴责。

那我们还能用函数来玩出什么花样呢？回想一下刚才见过的函数， `identity` 这个函数似乎太简单了，没什么意思，只是机械的把输入原模原样的输出出去； `left` 呢？虽然也是机械的把输入原模原样的输出，但是它有选择，只把第一个输入当作输出，忽略第二个； `right` 也是类似，只把第二个输入当作输出，忽略第一个。这是不是我们在苦苦寻找的 `true` 和 `false` 呢？

先不着急，假设是呢？能定义一个 `not` 函数，使得

::

    not left = right
    not right = left

吗？

你可以在这里停下想一想。想不出也没关系，我知道一开始这很难。给个提示， `left, right` 都可以用来 **选择** 分支，比如 `left x y` 选择的是 `x` ， `right x y` 选择的是 `y` 。我们之前一直关注的是给定 `left` 或者 `right` ，选择后面的两个东西。也就是固定住前面的选择器要么是 `left` 要么是 `right` ，活动的部分是后面的两个选项。为什么我们不能反过来，选择前面的 `left` 或者 `right` 、固定住后面的两个选项呢？

::

    ? x y

现在我们希望，如果前面的 `?` 恰好是 `left` 的话，返回 `right` 。既然 `left` 选择左边的分支、也就是第一个输入，那么我们就确定了 `x` ！

::

    ? right y

我们还希望，如果前面的 `?` 恰好是 `right` 的话，返回 `left` 。同理，既然 `right` 选择右边的分支、也就是第二个输入，那么我们也就确定了 `y`

::

    ? right left

所以 `not` 的定义式是？

::

    λn. (n right left)

可以去掉括号

::

    λn. n right left

写完整是

::

    λn. n (λa. λb. b) (λa. λb. a)

还是不相信吗？我们再倒过来来一遍，验证一下我们的猜想对不对。首先我们先试着输入 `left`

::

    not left
    (λn. n right left) left
    left right left
    right

当当！ `not left` 确实推导出了 `right` 。试着输入一下 `right` 呢？

::

    not right
    (λn. n right left) right
    right right left
    left

完全正确！ `not right` 也推导出了 `left` ！哇哦，看起来 `left, right` 就是我们要找的 `True, False` 了。太激动了（好吧可能只有我一个人会那么激动）。我们真的在一个虚无的世界里，用定义函数来无中生有了。

剩下的其他逻辑函数 `and, or` 如法炮制。先来看 `and` 吧。首先 `and` 有两个输入，所以 `and` 定义式的形状大概是这样的

::

    λn. λm. ?

这个 `?` 怎么构造呢？不如分情况讨论一下，反正情况也不是很多

-   如果第一个输入是 `False` ，那么不用看第二个输入了，结果直接就是 `False`

    利用 `False` 选择右边分支这个特性，写出

    ::

        λn. λm. n ? False

-   如果第一个输入是 `True` ，那么继续看第二个输入，

    -   如果第二个输入是 `True` ，那么结果是 `True`

        利用 `True` 选择左边分支这个特性，继续补全 `?`

        ::

            λn. λm. n (m True ?) False

    -   如果第二个输入是 `False` ，那么结果是 `False`

        利用 `False` 选择右边分支这个特性，补全最后一个 `?`

        ::

            λn. λm. n (m True False) False

搞定了！是不是很简单呢？ `or` 也是一样的道理，当作课后习题吧。

自然数
======

还是照例思考一下自然数是什么

-   自然数是 `0, 1, 2, ...`

    这只是自然数的十进制表示而已。可是自然数本身是什么呢？

-   自然数是 `0, 1, 10, 11, ...,`

    一样，这只是自然数的二进制表示。

-   自然数是满足一些运算——比如加法、减法、乘法——的符号

    你能想到哪些关于自然数加法的定理呢？

    -   对任意自然数 `n` ， `n + 0 = n`
    -   对任意自然数 `n, m` ， `n + m = m + n`
    -   对任意自然数 `n` ，总是存在一个 `m` ，使得 `n + 1 = m`

你知道吗？除了我们常用的二进制、十进制、十六进制以外，其实还有个最简单的 `一进制 <https://en.wikipedia.org/wiki/Unary_numeral_system>`_ 。在一进制里面，数字是这样表示的

::

    (空的)
    1
    11
    111
    1111
    ...

是的，就是原始人（或者在监狱里）用的木棍/结绳记事。多划一道，就表示在原来那个数字上加1，或者说，表示原来那个数字的后一个数字。

这给了我们什么灵感呢？我们能不能也用类似的方法在lambda calculus空荡荡的世界里（当然现在已经有 `True, False` 了，不是空荡荡了），用函数来表示自然数呢？

假设我们就是原始人吧，现在面前有好多根 **木棍** ，我们能做的动作是在地上 **放** 一根木棍。放了多少根木棍，地上就有多少根木棍。所以或许我们能这样定义

0.  不对木棍做任何事，表示0

    ::

        λ放. λ木棍. 木棍

1.  在不对木棍做任何事之后（废话），放了一根木棍，表示1

    ::

        λ放. λ木棍. 放 木棍

2.  在已经做了刚才的事情之后（刚才做了 `放 木棍` 这件事），放了一根木棍，表示2

    ::

        λ放. λ木棍. 放 (放 木棍)

3.  在已经做了刚才的事情之后（刚才做了 `放 (放 木棍))` 这件事），放了一根木棍，表示3

    ::

        λ放. λ木棍. 放 (放 (放 木棍))

4.  ...

放木棍这件事情做了 `n` 次，表示 `n` 这个数字

::

    λf. λa. f (f (f ... (f a)))
           |--------------| n个f

这就是著名的 `Church encoding <https://en.wikipedia.org/wiki/Church_encoding>`_ 啦。

你可以把 `f` 想象成任何操作， `a` 是那个操作的对象， `n` 是个自然数，那么

::

    n f a

推导出

::

    f (f (f (f ... (f a))))
    |----------------| n个f

也就是在 `a` 上做 `n` 次 `f` 之后得到的结果。

-   假如在水果店， `f` 是从货架上拿， `a` 是苹果（算了我讨厌苹果），那么

    ::

        3 拿 苹果
        (λf. λa. f (f (f a))) 拿 苹果
        拿 (拿 (拿 苹果))

    你就拿了3个苹果。

-   假如你在家， `f` 是吃， `a` 是薯片，那么

    ::

        3 吃 薯片
        (λf. λa. f (f (f a))) 吃 薯片
        吃 (吃 (吃 薯片))

    你就吃了3个薯片。

-   假如你在玩帝国时代2， `f` 是伐， `a` 是木工，那么

    ::

        3 伐 木工
        (λf. λa. f (f (f a))) 伐 木工
        伐 (伐 (伐 木工))

    你就能听到“伐伐伐木工”了 [1]_ ……

以上只是把 `f, a` 替换成具体的操作和对象的实例而已，目的是为了让你更容易接受自然数的这种定义 [2]_ 。另一方面我们应该承认自然数和刚才的 `True, False` 一样，都是一种很抽象的存在，是从现实世界里提取出来的某种概念。这种概念不依赖于 `f, a` 具体是什么。所以我们才用 `λf. λa. f (f a)` 来表示2，而不是用 `放 (放 木棍)` 来表示2。同样 `True, False` 在选择分支的时候也从不考虑 `a, b` 具体是什么。正如3个苹果和3个橘子在初学数学的小朋友眼里可能是完全不同的东西，但为什么我们都用“3”来表达这两堆水果的某种性质呢？3的概念并不取决于这堆水果是一堆苹果还是一堆橘子。出版社的编辑在小学一年级课本上画3个苹果让小朋友数数只是为了让小朋友的注意力更容易被吸引到这上面来。总有一天小朋友会意识到，哦，不管这里画的是苹果还是橘子，哪怕是从未见过的图形，这里也是3。我想这种 **抽象** 解释了为什么维基百科上把lambda calculus中的函数定义称作 **abstraction** 而不是初看起来更容易理解的function definition吧。

.. note:: 不知道为什么写到这里想到了泛型。

补充一下，每次做 `f` 这个动作的时候，都在前一次动作做完的基础上再来一次 `f` 动作，而不是始终在一开始的状态上

::

    f (f (f (f ... (f a))))
      |--------------------| 前n-1次的结果

在你将要吃第13片薯片的时候，你是用已经吃了12片薯片的那个身体吃下第13片薯片的；同样，在你将要取第13个苹果的时候，你的购物袋里已经有12个苹果了，而不是每次都用一个新的袋子来装那个苹果。

这样定义自然数的话，我们怎样做那些我们习以为常的操作呢？先试试最简单的，给某个数字加1？和之前一样，先构建一个框架出来，一时不知道怎么办的部分就用 `?` 先空着，慢慢来。就叫加1的这个函数 `succ` 吧（代表successor，后继者）。显然这个函数至少有一个输入，输入的是那个数字 `n`

::

    λn. ?

先随便写几个，找一找规律

::

    (λn. ?) 0 = 1
    (λn. ?) 1 = 2
    (λn. ?) 2 = 3

写完整

::

    (λn. ?) (λf. λa. a)         = (λf. λa. f a)
    (λn. ?) (λf. λa. f a)       = (λf. λa. f (f a))
    (λn. ?) (λf. λa. f (f a))   = (λf. λa. f (f (f a)))

Oh no怎么办，好像除了右边比左边多个 `f` 以外，毫无规律啊。想一想 `succ n` 的结果是什么？是另一个自然数。既然是一个自然数，那么任何自然数本身就是个接受2输入的函数。比如 `succ 2` 推导出 `3` ，正因为这样， `succ 2 f a` 推导出来才是

::

    succ 2 f a
    3 f a
    f (f (f a))

所以不妨把 `succ` 的3个输入都写全了，也许会有点帮助

::

    λn. λf. λa. ?

再回过头看

::

    (λn. λf. λa. ?) (λf. λa. a) = (λf. λa. f a)

有点思路了吗？我们想要把 `λf. λa. a` 里面的 `a` 外面包一层 `f` ，让 `a` 变成 `f a` 。现在既然 `n, f, a` 全都有了，那这还不好办？

::

    λn. λf. λa. f (n f a)

还是不相信吗？我们来举个例子验证一下，就验证一下 `succ 2 = 3` 吧

::

    succ 2                      // 展开succ
    (λn. λf. λa. f (n f a)) 2   // 代入2
    λf. λa. f (2 f a)

还记得 `2 f a` 是啥吗？是 `f (f a)` ，所以

::

    λf. λa. f (f (f a))
    3

太神奇了……建议再次停一下，体会一下这里的精妙之处。

现在有了 `succ` 这个大杀器之后，剩下的操作就非常简单了！（才怪）至少加任意两个数是没问题了？什么？你说还是有问题？哪里有问题？ `add n m` 不就是在 `n` 的上面做 `m` 次加1的操作吗（或者在 `m` 上做 `n` 次加1的操作）？给你闭着眼睛写出来

::

    add
    λn. λm. m succ n

试一试 `add 1 2`

::

    add 1 2
    (λn. λm. m succ n) 1 2      // 同时代入1和2
    2 succ 1
    (λf. λa. f (f a)) succ 1    // 代入succ
    (λa. succ (succ a)) 1       // 代入1
    succ (succ 1)
    succ 2
    3

有了加法，乘法也容易了， `n` 乘 `m` 就是在 `0` 上做加 `m` 这个操作 `n` 次呀（或者在 `0` 上做加 `n` 这个操作 `m` 次）

::

    mult
    λn. λm. n (add m) 0

用 `mult 2 3` 验证一下

::

    mult 2 3
    (λn. λm. n (add m) 0) 2 3
    2 (add 3) 0
    (λf. λa. f (f a)) (add 3) 0 // 代入add 3
    (λa. (add 3) ((add 3) a)) 0 // 代入0
    (add 3) ((add 3) 0)         // 去掉括号，因为(add 3) 0和add 3 0没区别
    (add 3) (add 3 0)
    (add 3) 3                   // 还是去掉括号
    add 3 3
    6

有了乘法，乘方也容易了……不写了。

很好，减法呢？额，这个有点难。已经吃下了13个苹果的我，要怎么恢复成只吃了12个苹果的我呢？我们可以先看看还能构造哪些别的有意思的东西，或许就能无意中发现减法的定义方法了。

对子
=====

到现在为止我们能定义的都是一些很原子的东西，不管是 `True, False` 还是自然数，在几乎所有编程语言里都是非常基本的存在，称作primitive types。怎样用lambda calculus表示更复杂的复合数据类型呢？最简单的复合数据类型，比如表示平面上的格点，这需要两个自然数放在一起，类似 `(9, 10)` 。

怎样构造一个函数 `pair` ，当输入两个东西的时候，输出一个包含这两个东西的对子呢？首先 `pair` 这个函数肯定是个2输入的函数

::

    pair
    λa. λb. ?

因为返回的是个对子，而我们又不知道对子怎么构造……根据刚才定义 `True, False` 和自然数的经验，只要有我们不会定义的东西，那大概这个东西就是用函数来定义的。所以 `?` 部分是另一个函数。先写一个输入吧

::

    λa. λb. (λf. ?)

似乎又卡住了。到底要怎么样才能暂存住传入的 `a, b` 呢……方法很简单，放着别管就好了

::

    λa. λb. λf. f a b

验证一下

::

    pair 1 2
    (λa. λb. λf. f a b) 1 2
    λf. f 1 2

这就可以了。这个函数已经保存了 `1, 2` 的信息在里面。

对子的另一个功能是，我们可以定义另外两个函数 `first, second` 来取出一个对子的第一个元素和第二个元素，比如

::

    first (pair 1 2) = 1
    second (pair 1 2) = 2

有没有想到可以用来选择分支的 `True, False` 呢？似乎

::

    (pair 1 2) True
    (λf. f 1 2) True        // 用True替换掉f
    True 1 2
    1

搞定了。所以

::

    first
    λp. p True

验证一下

::

    first (pair 1 2)
    (λp. p True) (λf. f 1 2)    // 用λf. f 1 2替换掉p
    (λf. f 1 2) True            // 用True替换掉f
    True 1 2
    1

同理

::

    second
    λp. p False

我还在想怎么定义减法……这怎么没完没了呢。别急，我们先看一个奇怪的函数 `phi` ，这个函数的输入是一个自然数对子（就是两个元素都是自然数的对子），输出是另一个自然数对子，定义式是这样的

::

    phi
    λp. pair (second p) (succ (second p))

`phi` 输出的对子的第一个元素是输入的那个对子的第二个元素，输出的对子的第二个元素是输入的对子的第二个元素加1。比如

::

    phi (pair 9 13) = pair 13 14
    phi (pair 0 0) = pair 0 1
    phi (pair 0 1) = pair 1 2
    phi (pair 1 2) = pair 2 3
    phi (pair 2 3) = pair 3 4

真是别有用心的例子，如果你还没看出来这个和减法有啥关系……是否注意到无论输入什么， `phi` 输出的对子永远都满足第一个元素是第二个元素减1？这样就可以用来构造减法了。要得到 `n` 的前一个数字，只要从0开始不停的往上加1，同时加的过程中记住刚才的数字是什么。比如我们想知道3的前一个数字是多少，就从0开始数，加3次。一边数，一边记着加之前的数字是多少

::

    phi (pair 0 0) = pair 0 1 // 第1次加1，得到了1，加之前的数字是0
    phi (pair 0 1) = pair 1 2 // 第2次加1，得到了2，加之前的数字是1
    phi (pair 1 2) = pair 2 3 // 第3次加1，得到了3，加之前的数字是2

现在能写出 `pred` 的定义式了吗？pred代表predecessor，前一个的意思。 `pred n` 是 `n` 的前一个数字。当然0没有前一个数字，那就返回0自身吧。首先 `pred` 的输入是一个自然数

::

    pred
    λn. ?

根据刚才的分析，输出是某个pair的第一个元素

::

    λn. first ?

`?` 是从 `pair 0 0` 开始，做 `phi` n次。想到 `n f a` 了吗？这边的 `f` 现在是 `phi` ， `a` 现在是 `pair 0 0`

::

    λn. first (n phi (pair 0 0))

验证一下吧

::

    pred 3
    (λn. first (n phi (pair 0 0))) 3    // 用3替换n
    first (3 phi (pair 0 0))            // 展开3 phi (pair 0 0)
    first (phi (phi (phi (pair 0 0))))  // 推导phi (pair 0 0)
    first (phi (phi (pair 0 1)))        // 推导phi (pair 0 1)
    first (phi (pair 1 2))              // 推导phi (pair 1 2)
    first (pair 2 3)
    2

真够折腾的。减1不能直接减1，而是间接的通过保留不断加1过程的前一个状态来实现。

任意减法 `sub n m` 也搞定了，在 `n` 上做 `m` 次减1的操作

::

    sub n m
    m pred n

验证一下

::

    sub 3 2
    2 pred 3        // 推导2 pred 3
    pred (pred 3)   // 推导pred 3
    pred 2          // 推导pred 2
    1

因为还没有定义负数，所以 `sub 2 3` 应该是0

::

    sub 2 3
    3 pred 2
    pred (pred (pred 2))
    pred (pred 1)
    pred 0
    0

2022/7/2

.. [1] 在帝国时代2里，你选择一个中国文明里的村民，让他去砍树，鼠标右键多次点击要砍的那个树，会听到非常滑稽的“伐伐伐伐伐伐伐木工”。咳咳低级趣味了属于是。
.. [2] 我觉得以小见大、从具体到抽象是更自然的学习方式，很反感大学微积分课本上那种先来定理、再来习题的格式，可能这种格式更适合学会之后用来查漏补缺的类似字典的存在吧，实在是对初学者太不友好了。
