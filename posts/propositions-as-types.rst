===============
机器定理证明101
===============

.. default-role:: literal

.. contents::

你肯定听说过四色定理，但你可能不知道四色定理是第一个用电脑证明的定理，用的是一门叫做 `Coq <https://rocq-prover.org/>`_ 的语言（现在已经改名叫Rocq了）。我以前就在想，随机生成的地图有无限多种，难不成用电脑证明的意思是……

    好了，这一百万个用电脑随机生成的地图都可以用最多四种颜色标记，看起来很难找到反例，那这个定理应该是对的！

实际上当然不是这样，电脑确实检查了无限多种情况，但不是通过暴力穷举所有的情况、一个一个检查过去的方式，不然就要因为存在无限种情况而花费无限的时间。内存有限、运算时间有限的电脑能够检查无限多种情况，正如记忆有限、脑力有限的人可以解释和想象无限一样，也正如空白有限的白纸可以容纳关于无限的命题一样。其中最关键的诀窍就是通过Curry-Howard Correspondence——或者用直白一点的话叫Propositions as Types，“命题即类型”——这个原理，把 **检查某个证明是否是命题的证明** 这件事，转化、归约到 **检查某个实例是否是类型的实例** 这个等效的问题。具体一点说

*   命题存在证明，对应类型存在实例
*   为命题写证明，对应构造类型的实例
*   用已知的、已经证明的定理、引理作为building block来证明更复杂的命题，对应用已经构造的简单实例来构造其他更复杂的实例。
*   把简单的命题用与或非、任意、存在等等逻辑关系组合起来形成复杂的命题，对应把简单的类型用类似 `struct, enum` 等等方式组合起来产生新的自定义类型。

如果你不熟悉归约这个操作，不妨回想一下高中数学课的几何题经常用的数形结合：建一个坐标系，把几何问题转化成纯粹的代数问题，用二维坐标 :math:`(a, b)` 表示平面上的点，用类似 :math:`Ax + By + C = 0` 的方程表示平面上的直线。每当我们想判定某个点是否在某条直线上的时候，不用再鼓捣那些个晦涩的几何定理了，只要把点的二维坐标带入直线方程、检查是否满足方程就完事了。

机器定理证明这件事有什么意义呢？我觉得和历史上每一次不同的学科领域融合一样，机器定理证明把数学和计算机融合在一起，肯定能互相给各自的领域带来很多新奇的想法。对搞数学的人来说（我没搞过数学，瞎猜一下），有这些变化

*   以前用informal的自然语言来写证明，依赖同行评审检查证明，费时费力还容易出错；现在用一门谁都看得懂、形式化的、严谨无歧义的语言来写证明，用软件自动检查证明。如果早几百年就有电脑和Coq，估计就不会发生这么多一开始宣称证明费马大定理但后来发现乌龙的事情了。各类数学民科也都因为过不了机器检查，闻风而逃。
*   以前引用别人的定理很困难，因为别人也是用自然语言写的，数学的记号巨多——小写不够用大写，英文字母不够用希腊字母，希腊字母不够用 `希伯来、西里尔、平假名 <https://en.wikipedia.org/wiki/Mathematical_notation>`_ ，宋体黑体花体不够用 `哥特体 <https://en.wikipedia.org/wiki/Blackletter>`_ ，下标上标不够用左上标左下标——而且极其混乱不成体系，每个人每个流派用的notation都不一样，你引用过来之后首先要复述一遍，你不放心的话还要检查一遍别人的证明有没有问题；现在引用别人的定理就像做软件的时候引入第三方依赖库一样容易，定理想不起来的时候直接 `用关键字模糊搜索 <https://proofassistants.stackexchange.com/questions/354/how-to-search-for-an-existing-theorem-in-lean>`_ ，而且别人的证明也都是用机器检查过、保证没有bug的。
*   以前数学研究大规模合作很困难，通常都是小团体几个人一起合作。一个大定理的证明过程是先拆成几个小定理，分别一一证明，然后拼起来。证明小定理的任务会分给不同的人去做，互相之间必须高度信任、知根知底，不然万一有个人写的证明出问题，整个证明都错；现在大规模合作很容易，合作者之间可以零信任，随便怎么写，反正最后都要过机器检查。贡献证明可以像给GitHub上的开源项目贡献代码一样方便，比如Lean的 `mathlib <https://github.com/leanprover-community/mathlib4>`_ 。

现在这几年又出现了LLM大语言模型这类AI，有人说这能不能用来写证明？可以，但是你能相信AI说的吗？AI胡说八道、出现幻觉的时候你能一眼看出来吗？恐怕不能，也没那么多时间。目前看起来最可行的做法，就是让AI输出Coq或者Lean代码然后过一遍自动化的机器检查。

对搞软件的人来说（我确实是搞软件的），意义也很重大。软件完全正确，这是个多强的保证！多少人晚上睡眠质量都会因为这个变好。以前软件的正确性全靠测试，后来又引入了覆盖率、静态检查等等做法，但它们本质上还是无法保证软件完全正确。一般情况下这不是什么大问题，因为大多数软件都没必要特别靠谱，点外卖的软件需要很靠谱吗？不需要，出问题了刷新一下就好。即使真的出问题，软件很容易修改，改好了重新上线就好了。但有些软件需要非常靠谱，比如飞机汽车上的软件、医疗器械里的软件，还有一些非常底层非常基础的软件比如编译器、操作系统，单靠测试还有这些掩耳盗铃的指标（我认为）搞不定了；现在可以用定理证明器来严格证明软件的正确性，比如 `CompCert <https://compcert.org/>`_ 就是个完全形式化验证过的C编译器。

机器定理证明也解答了我上学学数学的时候产生的很多好奇和疑惑，要是早点知道这些高考说不定还能多考几分。一直以来我都感到自己从未真正理解证明到底是个什么东西，什么样的证明是有效的证明？写证明题到底写到哪一步，证明才能算是充分的？那些几百页的证明都是怎么写出来的、怎么想到的？为什么我这样写，数学老师觉得我跳步？数学归纳法为什么能work？

这篇文章我就给你讲讲机器定理证明到底是怎么一回事， **检查某个证明是否是命题的证明** 是怎么和 **检查某个实例是否是类型的实例** 联系到一起的。我看的很多教程都会上来直接给你讲Coq、Lean的语法甚至tactics，看的我云里雾里，到很后面才解释这两件事情的联系。我能理解这个思路的合理之处，毕竟多数人一开始只想知道如何使用这些工具，但这篇文章不会这样做，一方面，我觉得这个联系实在太重要了，值得放在最前面讲，而且相比know-how我对know-why更感兴趣；另一方面，对我自己来说，从已经学会的知识、经验，类比、迁移到另一个领域是比较自然且舒适的学习方式。我也不想把文章写成字典，你看完之后只能机械的记住一堆什么对应什么的枯燥结论，过两天全忘光，而是想引导你重新发明/发现机器定理证明的原理，这样过几天即使你真的忘记了也可以很快自己推导出来，我觉得这样才是真正的理解，正如Feynman所说

    What I cannot create, I do not understand.

回顾
=====

日常用的编程语言C、C++、Java里，类型可以说无处不在，每个变量、表达式都有类型，每个函数定义的时候都写清楚接受哪几个什么类型的参数、返回什么样类型的东西。如果乱用，编译的时候会报错。至于有时候不报错，多半是implicit cast隐式类型转换导致的。

.. code-block:: cpp

    std::string s = "Hello world!"; // 变量s的类型是std::string

    bool is_gt_zero(int32_t a) { // 函数is_gt_zero接受一个int32_t类型的实例，返回一个bool类型的实例
        // 也可以说函数is_gt_zero的类型是int32_t -> bool
        return a > 0; // >也是个函数哦！类型是(int32_t, int32_t) -> bool
    }

    is_gt_zero(s); // 不可以！

即使Python看上去好像没那么多条条框框，其实人家暗地里也是有类型的

.. code-block:: python3

    a = 1
    b = 2
    c = a + b # 两个int相加定义为整数相加，得到另一个int

    a = "Hello "
    b = "world!"
    c = a + b # 两个str相加定义为字符串连接，得到另一个str

如果你这样

.. code-block:: python3

    a = 1
    b = "Hello"
    c = a + b # 该怎么定义int + str？

会报错

::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

抽象一点说，类型把计算机能表示的所有的值分成了不同的类别，比如 `int` 这个类别里有 `1, 2, 3, ...` ， `str` 这个类别里有 `"", "1", "a", ...` 。我们把类型里的那些值叫做这个类型type的实例instance。每个类型内定义各种操作，操作被限定只能发生在特定类型的实例上，不能发生在其他类型的实例上。比如 `+` 操作只能同时发生在两个 `int` 实例、或者两个 `str` 实例上，不能一边是 `int` 另一边是 `str` 。

这么做的好处显而易见，极大减轻了记忆负担，减少了bug产生的机会。想象一下写汇编的一大痛苦，就是记住每个寄存器里面的bits现在放了什么东西、是什么含义，因为大部分指令都可以读写所有的寄存器，但不是所有的指令在当下都有意义，比如假设寄存器里放了个表示商品价格的数字，那么各种加减乘除指令也许是合理的操作，但跳转指令 `jmp` 就不太可能是合理的操作；假设寄存器里放了个函数的入口地址，那么函数调用指令 `call` 很大概率合理，但加减乘除就不太可能合理；假设放了个数字，如果想右移，也需要知道这个数字是unsigned还是signed才能正确选择用logical shift还是arithmetic shift。

类型其实还有个更重要但是常常被人忽视的好处，它可以用来严格定义接口，限定数据可能的状态，让不该出现的状态根本无法被表示出来，每个实例都和每个状态一一对应，实现 `make impossible states impossible <https://www.youtube.com/watch?v=IcgmSRJHu_8>`_ 。给类型起个有意义的名称还能让代码talk itself，相比于自然语言书写的冗长文档，能更清晰简要的解释代码的含义。

日常写代码定义类型的时候，实际上是在给现实问题建模，用实例来表示现实中的某种状态。理想情况下，当然希望实例和状态严格一一对应、不多不少，但是受限于编程语言的表达能力，实例总是比状态多。这些多余的实例怎么处理？

*   要不就定义成非法状态，这样需要各处设防，在内部、接口处到处写 `assert` 阻止非法状态传播。
*   要不就无视它们，认为它们只是另一些实例的另一种写法，通过定义某种归一化的方式、或者自定义相等的条件（在C++里的话就是自定义 `operator==` ），让不同但含义上对应同一状态的实例“看起来相等”。

这两种做法都太不优雅了。来看看我最喜欢的例子，Rust标准库表示IP地址的类型，简直严丝合缝

.. code-block:: rust

    pub enum IpAddr { // IP地址只有下面二选一的情况
        V4(Ipv4Addr), // 要么是IPv4
        V6(Ipv6Addr), // 要么是IPv6
    } // 不可能是其他情况，也不可能既是IPv4又是IPv6

    pub struct Ipv4Addr {
        octets: [u8; 4], // 4个byte组成的定长数组
    }

    pub struct Ipv6Addr {
        octets: [u8; 16], // 16个byte组成的定长数组
    }

Rust的 `enum` 和C++的非常相似，语义也一样是列举出所有可能的情况，称作variant，这里 `V4, V6` 就是两种variant，不同的是Rust的 `enum` 里面每个variant可以携带额外的数据，例如这里variant `V4` 携带了类型是 `Ipv4Addr` 的额外数据，我们可以用各种方法读到里面的额外数据

.. code-block:: rust

    if let IpAddr::V4(addr) = ip {
        .. // addr: Ipv4Addr
    }

    match ip {
        IpAddr::V4(addr) => .. // addr: Ipv4Addr
        IpAddr::V6(addr) => .. // addr: Ipv6Addr
    }

因为C++的 `enum` 没有这种携带额外数据的能力，在不借助C++17标准库新特性 `std::variant` 的情况下，新手大概率会写出这样的代码

.. code-block:: cpp

    enum class IpAddrKind {
        V4,
        V6,
    };

    struct IpAddr {
        std::string addr;
        IpAddrKind kind;
    };

`IpAddrKind kind` 只有 `V4, V6` 两个状态，可以约束IP地址的版本要么是v4、要么是v6，但 `std::string addr` 的情况可就多了，如果不定义其他的constructor（吐槽下C++ constructor的种类多到令人发指，各种规则堪比法律条文），我完全可以构造出这样的实例

.. code-block:: cpp

    auto addr = IpAddr { .addr = "hello", .kind = IpAddrKind::V4 };

显然 `hello` 完全不是个合法的IPv4地址。这种定义让不该出现的非法状态出现了。相比之下，Rust的 `IpAddr` 完全没有非法状态的空间，构造链条环环相扣，因为如果要构造 `IpAddr` ，你必须要么已经构造了一个 `Ipv4Addr` 、要么已经构造了一个 `Ipv6Addr` ；如果要构造 `Ipv4Addr` ，你必须已经有了一个 `[u8; 4]` ，而 `"hello"` 这种字符串根本不是 `[u8; 4]` 类型的实例。

Rust的 `enum` 可以被看作是另一种自定义类型的方式，或者说，组合已有的类型来产生新类型的方式。它和 `struct` 不太一样在于，要构造 `struct` 定义的类型的实例，需要首先构造出每个属性所属的类型的实例，才能组合成一个大的实例，比如上面C++版的 `IpAddr` ，要构造 `IpAddr` 实例，首先需要一个 `std::string` 实例和一个 `IpAddrKind` 实例，然后传给constructor `IpAddr { .. }` 才能产生 `IpAddr` 实例。而 `enum` 不用先构造每个variant所属的类型实例，比如上面Rust版的 `IpAddr` ，只需要 `Ipv4Addr` 实例或 `Ipv6Addr` 实例中的某一个就够了。

`struct` 隐含了某种 **和** 的含义，一个二维平面上的点由横坐标 **和** 纵坐标组成，它不是横坐标或者纵坐标二选一。用 `struct` 定义的新类型的实例数量（如果有限的话），正好是每个属性所属的类型的实例数量乘起来

.. code-block:: rust

    struct Point2D {
        x: i32,
        y: i32,
    }

`Point2D` 有多少个实例？

::

      |i32| * |i32|
    = 2^32 * 2^32

`enum` 隐含了某种 **或** 的含义，一个IP地址由一个IPv4地址 **或** 一个IPv6地址组成，这和既是IPv4又是IPv6不一样。用 `enum` 定义的新类型的实例数量，正好是每个variant里类型的实例的数量相加

`IpAddr` 有多少个实例？

::

      |Ipv4Addr| + |Ipv6Addr|
    = |[u8; 4]| + |[u8; 16]|
    = (2^8)^4 + (2^8)^16

和类型打交道的日常里还有个花活叫范型，见的最多的地方是各种容器，Rust里有 `Vec<T>, HashMap<K, V>` ，C++里有 `std::vector<T>, std::unordered_map<K, V>` 。有2种不同的视角看待范型

*   定义了一族类型 `Vec<u32>, Vec<u64>, Vec<i32>, ..`

    这种视角是在说，当我们写下 `Vec<T>` 的定义时，我们不只是为某些特殊的 `T` 定义了 `Vec<T>` ，而是一下子写了无限多个定义。只是编辑器空白太小，写不下无限多个定义，而且这茫茫多个定义里大部分内容都是相同的，没必要重复劳动，所以我们才提取公因式，用 `T` 表示那个可能变化的部分，其他一模一样的部分就不用烦劳重复写了。有点类似宏的感觉。

*   定义了个类型生成器 `Vec: Type -> Type`

    这种视角是在说，函数定义用圆括号，范型定义用尖括号，圆括号和尖括号都是括号，所以范型也是某种特别的函数，普通函数的参数和返回值都是实例，而范型的参数和返回值都是类型，往 `Vec` 丢进参数 `i32` ，得到名为 `Vec<i32>` 的新类型。

    这种视角下，范型可以看作是除 `struct, enum` 以外第三种自定义新类型的方式。

为什么叫做花活呢？因为范型的参数其实可以不只是类型，还可以是数字、字符串之类的实例，导致它的表达能力巨强，甚至是 `图灵完备的 <https://stackoverflow.com/questions/189172/c-templates-turing-complete>`_ 。你永远想象不出用它能做什么匪夷所思的事情，就拿斐波那契数列来说，最常见的写法是递归

.. code-block:: cpp

    size_t fib(size_t n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }

太low了，请欣赏用范型实现的斐波那契数列

.. code-block:: cpp

    template<size_t N>
    struct Fib {
        static constexpr size_t res = Fib<N - 1>::res + Fib<N - 2>::res;
    };

    template<>
    struct Fib<0> {
        static constexpr size_t res = 0;
    };

    template<>
    struct Fib<1> {
        static constexpr size_t res = 1;
    };

    int main() {
        std::cout << Fib<20>::res << std::endl;
    }

用第一种视角来看，通过 `template` 为每个 `size_t` 的实例 `n` 都定义了一个名叫 `Fib<n>` 的类型，虽然代码只写了3个定义，但实际上一共定义了一族 `2^64 - 1` 个类型，它们分别是

.. code-block:: cpp

    struct Fib<0> {
        static constexpr size_t res = 0;
    };
    struct Fib<1> {
        static constexpr size_t res = 1;
    };
    struct Fib<2> {
        static constexpr size_t res = Fib<1>::res + Fib<0>::res;
    };
    struct Fib<3> {
        static constexpr size_t res = Fib<2>::res + Fib<1>::res;
    };
    struct Fib<4> {
        static constexpr size_t res = Fib<3>::res + Fib<2>::res;
    };
    ...

STL标准库也有个很常见的例子定长数组 `std::array<T, N>` 。后面介绍机器证明的时候经常会遇到这个，别惊讶，类型和实例的界限并没有你想象的那么泾渭分明。

类型可以递归定义从而包含自己，或者说，可以定义一个类型，它的某个属性还是这个类型的实例。和数字范型一样，虽然日常编程很少会用这个，但机器证明里非常常见，所以还是提一下。回想一下当初学数据结构的时候，单链表是怎么定义的？用自然语言来描述什么是单链表

*   空链表是单链表
*   如果已经有了一个元素和一个单链表，把这个元素接在单链表前面，仍然得到的是单链表

两种情况是或者的关系，很自然应该用 `enum` 而不是 `struct` 来定义。此外，观察到单链表的定义里没有出现对元素类型的限定，换句话说，不管单链表里装 `i32, u32, u64` 还是什么别的类型的元素，除了元素类型，其他定义都应该是一样的，看起来是这里应该放个范型

.. code-block:: rust

    enum List<T> { // 什么是单链表？
        Empty, // 空链表是单链表
        Cons(T, Box<List<T>>), // T后接另一个单链表，还是单链表
    }

你可能会问，那如果现在有两个元素和一个单链表，把这两个元素接在单链表前面，得到的不也是个单链表吗？那链表应该这样定义

.. code-block:: rust

    enum List<T> { // 什么是单链表？
        Empty, // 空链表是单链表
        Cons(T, Box<List<T>>), // T后接一个单链表，还是单链表
        Cons2(T, T, Box<List<T>>), // 2个T后接一个单链表，还是单链表
    }

当然是，但为什么不用考虑这种情况呢？因为没必要，只用 `Empty, Cons` 两个variant已经足以构造出涵盖单链表的所有状态、并且还和每个状态一一对应的实例了。如果用这种定义， `[1, 2, 3]` 这个链表可以有3个不同的实例来表示

.. code-block:: rust

    Cons(1, Cons(2, Cons(3, Empty))))
    Cons(1, Cons2(2, 3, Empty)))
    Cons2(1, 2, Cons(3, Empty)))
    // 忽略Box，不然噪音太多了

但在单链表的使用场景下，区分这3个实例毫无意义，我们只关心链表以什么顺序存储了哪些元素，我们直观上认为的两个链表相等也并不是表示方式上相等而是实例所表达的状态相等。如果真的这么定义，要让相等符合直觉，要不就定义一种归一化的方法，把后两个实例归一化canonicalize全部变成第一个实例然后再判定相等，要不就自定义什么叫做相等。何必呢。

.. 不过，处处极端贯彻make impossible states impossible原则有时候并不划算，有时候甚至完全做不到，我们等下就会看到例子。

求单链表的长度怎么写？既然已经用递归定义了单链表，用while就没意思了，也并不好写，不如也用递归写

.. code-block:: rust

    impl<T> List<T> {
        fn len(&self) -> usize {
            match self {
                List::Empty => 0,
                List::Cons(head, tail) => 1 + tail.len(),
            }
        }
    }

非常优雅，完美对应了单链表的递归定义

*   如果是空链表，那么长度是0
*   如果是一个元素后接一个单链表，那么长度是1加上后面单链表的长度

对日常编程中的类型检查问题就回顾到这里。接下来我将用时下非常流行的语言Lean来介绍机器定理证明，虽然语法不同，但和刚才回顾的内容并没有本质差别。我不会纠结具体语法的细节，比如应该用 `def` 还是 `theorem` 、constructor前面加不加type前缀。我也不会过多使用语法糖或者标准库里的东西，这样虽然会让代码看起来稍显杂乱、括号特别多、语句特别长，但我的学习经历让我感觉过早引入这些反而无助于理解。

如果你觉得安装Lean麻烦（需要开心上网），这里有个 `Lean online playground <https://live.lean-lang.org/>`_ 可以在线运行。

自然数
=======

自然数就像数学的hello world，所以我们这里开始。从小家里学校里就教你数数，一开始是从一到十，然后百千万亿……不管是写成十进制阿拉伯数字 `0, 1, 2, ...` 还是写成二进制、写成英文中文、用苹果还是橙子，它都只是个记号，描述了那个代表数量或者顺序的抽象概念

.. code-block:: lean

    inductive Nat where
    | zero : Nat
    | one : Nat
    | two : Nat
    ...

任意一个记号代表的自然数紧随其后又有另一个自然数，因而自然数有无限多个，无法像列举星期几一样全部列举一遍。有个叫做Peano的人，不知道是不是从发明数字之前原始人在石头上刻画记日子的事情里得到了灵感，说可以这样定义自然数，只有两种情况

*   0是个自然数
*   如果 `n` 是个自然数，那么 `succ n` 是下一个自然数

看起来又是一个该用 `enum` 定义的类型。刚才已经用Rust的 `enum` 构造过单链表了，自然数比这个还要简单一点。Lean中类似 `enum` 的关键字叫 `inductive`

.. code-block:: lean

    inductive Nat where
    | zero : Nat
    | succ (n : Nat) : Nat

这样就可以定义出所有你熟悉的自然数了，0就是 `Nat.zero` ；1是0的下一个自然数；2是1的下一个自然数。Lean中用 `def` 来给出定义， `def` 之后先是变量名（好吧其实不能变），然后是冒号 `:` 紧接类型的名字，再是 `:=` 紧接着定义的内容。函数调用不需要括号，参数之间用空格隔开，比如 `f(a, b)` 写成 `f a b` ，比如 `f(a, g(b, c))` 写成 `f a (g b c)` 。

.. code-block:: lean

    def zero : Nat := Nat.zero
    def one : Nat := Nat.succ zero
    def two : Nat := Nat.succ one

如果你记得刚才的例子，你会发现不管是 `IpAddr` 还是 `Point2D, i32` ，它们都只有有限个实例，唯一有无限个实例的类型只有单链表 `List<i32>, List<u32>, ...` ——先不论计算机物理实现上的问题，从逻辑上看至少它们有无限多个实例，你写不完所有的实例——而单链表是用递归的方式定义的。

相等
=====

有了自然数就可以写下我们的第一个命题了！试试 `0 = 0`

.. code-block:: lean

    def zero_eq_zero : Nat.zero = Nat.zero := ?

还记得开头说的吗？命题是类型，证明是实例，所以命题写在冒号 `:` 后面，证明写在 `:=` 后面。

等一下，还没定义什么是相等 `=` 。你说这玩意也要定义？当然，再显然也要定义。那怎么定义呢？看起来毫无头绪，别着急，先列举一下所有用相等可以写出的命题，所有形如 `n = m` 的命题

::

    0 = 0   1 = 0   2 = 0   3 = 0   ...
    0 = 1   1 = 1   2 = 1   3 = 1   ...
    0 = 2   1 = 2   2 = 2   3 = 2   ...
    0 = 3   1 = 3   2 = 3   3 = 3   ...
    ...

既然最开头说了，命题就是类型，上面表格里每一项都是个命题，所以每一项都应该对应一个类型

::

    Eq_0_0   Eq_1_0   Eq_2_0   Eq_3_0   ...
    Eq_0_1   Eq_1_1   Eq_2_1   Eq_3_1   ...
    Eq_0_2   Eq_1_2   Eq_2_2   Eq_3_2   ...
    Eq_0_3   Eq_1_3   Eq_2_3   Eq_3_3   ...
    ...

不是每个命题都是正确的，显然 `1 = 0` 就是个假命题。最开头说到，证明就是实例，因此我们希望 **所有和真命题对应的类型都有实例，所有和假命题对应的类型都没有实例。** 就像这样

::

    inductive Eq_0_0 where   inductive Eq_1_0 where   inductive Eq_2_0 where   ...
    | true : Eq_0_0          --                       --

    inductive Eq_0_1 where   inductive Eq_1_1 where   inductive Eq_2_1 where   ...
    --                       | true : Eq_1_1          --

    inductive Eq_0_2 where   inductive Eq_1_2 where   inductive Eq_2_2 where   ...
    --                       --                       | true : Eq_2_2

    ...

类型 `Eq_0_0` 代表命题 `0 = 0` ，它是个真命题，所以类型 `Eq_0_0` 有实例，可以用 `Eq_0_0.true` 构造得到。 `true` 只是个随便起的名字，没有特殊的意义。标准库里的 `Eq` 选用了 `refl` 这个名字，代表reflexivity自反性，也就是自己和自己永远相等（或者用我最喜欢的说法，相等就是把一个东西在等号左右两边写两遍）。

类型 `Eq_1_0` 代表命题 `1 = 0` ，它是个假命题，所以类型 `Eq_1_0` 没有实例，没有任何方法可以构造得到，因为没定义任何variant。

回到我们的第一个命题 `0 = 0` ，现在它的证明应该这么写

.. code-block:: lean

    def zero_eq_zero : Eq_0_0 := Eq_0_0.true

这就完事了？这就完事了！恭喜你学会了机器证明的99%，剩下的都是一些细节了。第一件细节是，这么多 `Eq_n_m` 根本写不完啊，难道为了证明 `10000 = 10000` 我要先定义个 `Eq_10000_10000` 吗？而且这些 `Eq_n_m` 看起来重复部分挺多，在对角线上，也就是那些满足 `n = m` 的 `Eq_n_m` 都有实例，不在对角线上的都没实例，看起来很像是范型的用武之地。你说的没错，这就改成范型

.. code-block:: lean

    inductive Eq : Nat -> Nat -> Type where

这样再也不用敲下划线 `_` 了， `Eq 0 0` 表示 `0 = 0` ，太爽了。

呃，怎么表达“只有 `n = m` 的那些类型才有variant `true` 这件事”呢？还记得刚才的自然数 `Nat` 的第二个variant `succ` 是携带额外数据 `n : Nat` 的吗？

.. code-block:: lean

    inductive Nat where
    ...
    | succ (n : Nat) : Nat

我们也可以让这个 `true` 额外携带数据

.. code-block:: lean

    inductive Eq : Nat -> Nat -> Type where
    | true ? : Eq ? ?

问题是，带什么数据？带了数据之后变成哪个类型的实例？

既然是只有 `n = m` 的时候类型 `Eq n m` 才有实例，那不直接扔掉 `m` ，用 `n` 代替，只有 `Eq n n` 才有实例。所以当然是变成 `Eq n n` 的实例

.. code-block:: lean

    inductive Eq : Nat -> Nat -> Type where
    | true ? : Eq n n

`n` 从哪里来？让 `true` 带着

.. code-block:: lean

    inductive Eq : Nat -> Nat -> Type where
    | true (n : Nat) : Eq n n

这样就搞定了！再反过来检查这个定义，它满足我们对相等命题的所有约束

*   任何一个 `n = m` 命题都能写出来，用类型 `Eq n m` 代表命题 `n = m` 。并不是只有对角线上的那些命题才能被写出来，因为命题只是命题，命题不一定需要证明，真命题才需要证明，假命题不需要、也不能有证明（否则就会变成真命题）。但无论真假命题，都需要能被写出来。第一行 `Eq : Nat -> Nat -> Type` 保证了 `Eq n m` 里面的两个数字 `n` 和 `m` 互相独立无关，所以任何 `Eq 1 0, Eq 999 2` 都能写出来。
*   只有所有的真命题 `n = n` 的证明能被写出来，用 `true n` 能构造 `Eq n n` 的实例。但无论 `n` 是什么， `true n` 都构造不出对角线以外的 `Eq n m` 类型的实例。第二行 `true (n : Nat) : Eq n n` 保证了这件事，因为你只给了 `true` 一个数字 `n` ，没给 `m` ，所以当然只能构造 `Eq n n` 的实例。

还不理解？重新把表格写出来

::

    inductive Eq 0 0 where   inductive Eq 1 0 where   inductive Eq 2 0 where   ...
    | true 0 : Eq 0 0        --                       --

    inductive Eq 0 1 where   inductive Eq 1 1 where   inductive Eq 2 1 where   ...
    --                       | true 1 : Eq 1 1        --

    inductive Eq 0 2 where   inductive Eq 1 2 where   inductive Eq 2 2 where   ...
    --                       --                       | true 2 : Eq 2 2

    ...

类型 `Eq 0 0` 代表命题 `0 = 0` ，它是个真命题，所以类型 `Eq 0 0` 有实例，可以用 `true 0` 构造得到。

类型 `Eq 1 0` 代表命题 `1 = 0` ，它是个假命题，所以类型 `Eq 1 0` 没有实例，没有任何方法可以构造得到，因为虽然定义了 `true n` ，但是如果把 `true` 能构造出来的实例写出来

::

    true 0 : Eq 0 0
    true 1 : Eq 1 1
    true 2 : Eq 2 2
    ...

会发现这里面根本没有哪一行冒号的右边是 `Eq 1 0` ，根本没有哪个实例的类型是 `Eq 1 0`。

再改写一下我们的第一个命题 `0 = 0` ，现在它变成了这样

.. code-block:: lean

    def zero_eq_zero : Eq Nat.zero Nat.zero := Eq.true Nat.zero

从这里开始，我们可以拿着 `zero_eq_zero` 当作一条已知的定理来用，就像写代码的时候定义的helper function一样。如果另一条定理的证明需要用到 `zero_eq_zero` ，就可以直接塞进去。

同理， `1 = 1` 也是这样证明， `2 = 2` 也是， `3 = 3` ……好无聊啊，我们知道任何自然数都等于自己，能不能证明一下

    对任意自然数 `n` ，都有 `n = n`

全称量词，数学里一般写作 `∀` 。这个任意第一次看到还挺吓人，但正如我们所见它不过就是一种偷懒的写法，意思是不管 `n` 取哪个自然数，后面构造的关于 `n` 的命题都成立

*   对自然数0，有 `0 = 0`
*   对自然数1，有 `1 = 1`
*   对自然数2，有 `2 = 2`
*   ...

或者说，不管 `n` 取哪个 `Nat` 实例，类型 `Eq n n` 都有实例

*   `n` 取0， `Eq 0 0` 有实例 `Eq.true 0`
*   `n` 取1， `Eq 1 1` 有实例 `Eq.true 1`
*   `n` 取2， `Eq 2 2` 有实例 `Eq.true 2`
*   ...

关键是怎么用代码表示这种“不管给我什么，我都能给你个实例”的含义呢？

*   给我0，给你实例 `Eq.true 0`
*   给我1，给你实例 `Eq.true 1`
*   给我2，给你实例 `Eq.true 2`
*   ...

这不就是函数吗？定义这样一个函数，输入 `Nat` 实例 `n` ，输出 `Eq n n` 实例

.. code-block:: lean

    def n_eq_n (n : Nat) : Eq n n := Eq.true n

反过来看看是不是这样

::

    n_eq_n 0 : Eq 0 0 := Eq.true 0
    n_eq_n 1 : Eq 1 1 := Eq.true 1
    n_eq_n_2 : Eq 2 2 := Eq.true 2
    ...

`n = n` 的证明要多少有多少，告诉我你的 `n` 就行。

`n_eq_n` 的类型是什么？我们知道对于任意 `n : Nat` ，有 `n_eq_n n : Eq n n` ，但是 `n_eq_n` 本身是个啥？你可能会写下

::

    n_eq_n : Nat -> Eq n n

问题是这里的 `n` 哪里来？如果问Lean `n_eq_n` 是什么类型，它会说

::

    #check @n_eq_n -- @表示输出真实类型，不要忽略隐含参数
    -- n_eq_n : (n : Nat) → Eq n n

这样的类型 `(n : Nat) -> Eq n n` 在Rust、C++等日常使用的编程语言里根本写不出来，我们无法定义一个函数，让它的输出类型取决于某个输入参数的值

.. code-block:: rust

    fn n_eq_n(n: Nat) -> Eq<n, n> // 不可以

除非让 `n` 变成范型参数。Rust目前只支持 `usize, i32` 之类的数值类型作范型参数，下面这种写法只是示意一下，实际上过不了编译

.. code-block:: rust

    fn n_eq_n<const n: Nat>() -> Eq<n, n>

这里的麻烦在于，每个 `Eq<n, n>` 都是个不同的类型，理论上编译器要为每个 `Eq<0, 0>, Eq<1, 1>` 生成不同的代码，所以它在编译期间需要知道你用到的所有类型，你用到哪个就给你生成哪个；到了运行期，此时编译器已经完成了工作，一切类型都被固定下来（或者说都被擦除了，毕竟exe里的机器码没有类型的概念），编译器不可能再动态的给你变一个新的类型出来。在Lean里就没这个限制，实例和类型可以出现在任何地方，也没有什么编译期和运行期的区别。不要让过去的经验束缚你的想象力！这个特性称作 `dependent type <https://stackoverflow.com/questions/9338709/what-is-dependent-typing>`_ 。

下面来证明一个更复杂的命题

    对任意自然数 `n, m` ，如果 `n = m` ，那么 `succ n = succ m` 。

刚才已经看到这种“任意”的命题其实是函数，这里任意的对象是两个自然数 `n, m` ，所以自然是个接受两个参数的函数

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) : ? := ?

那这个“如果……那么……”怎么表示？还是写几个特例找找规律。最典型的是这两个，前面的“如果”是真或者假

*   如果命题 `0 = 0` 是真命题，那么命题 `1 = 1` 是真命题
*   如果命题 `0 = 1` 是真命题，那么命题 `1 = 2` 是真命题

第一个命题毫无疑问是真命题，如果和那么部分全都是真命题；第二个命题是不是真命题？很多人会犹豫一下，但其实第二个也是真命题，因为命题 `0 = 1` 是假命题，所以后面的结论无论说什么都可以。

从类型-实例的视角看

*   如果类型 `Eq 0 0` 有实例，那么类型 `Eq 1 1` 有实例
*   如果类型 `Eq 0 1` 有实例，那么类型 `Eq 1 2` 有实例

如果有实例……这意味着有办法拿到这个实例，并且用它来构造另一个实例，所以“如果……那么……”形式的命题对应的仍然是函数！

*   如果给我 `Eq 0 0` 类型的实例，那么我可以用它来构造出 `Eq 1 1` 类型的实例
*   如果给我 `Eq 0 1` 类型的实例，那么我可以用它来构造出 `Eq 1 2` 类型的实例

其实有时候“对任意……”形式的命题也会表述成“如果……那么……”，听上去并不违和，这也侧面说明任意和如果是一回事。我们现在在证明的“对任意自然数……”的命题也可以表述成这样

    如果 `n, m` 是自然数，如果 `n = m` ，那么 `succ n = succ m` 。

用Lean表述出来是

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) : Eq n m -> Eq (succ n) (succ m) := ?

因为要用 `Eq n m` 实例来做事情，同样可以把冒号 `:` 后面的 `Eq n m` 提到前面来，并给一个名字。起个什么名字呢？既然是如果前面的假设，那就叫hypothesis好了

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) (h : Eq n m) : Eq (succ n) (succ m) := ?

现在考虑，有了 `n, m, h` 的情况下，如何构造出 `Eq (succ n) (succ m)` 实例。把现在已知的东西和目标都写出来

::

    n m : Nat
    h : Eq n m := Eq.true n
    goal : Eq n.succ m.succ := ?

我们知道 `Eq n m` 如果有实例的话，只能有唯一一个实例，就是 `Eq.true n` （或者 `Eq.true m` ）。同样， `Eq (succ n) (succ m)` 要有实例的话，也只能有唯一一个实例，就是 `Eq.true (succ n)` （或者 `Eq.true (succ m)` ）。那么，直接从 `h` 里提取出 `n` ，变成 `succ n` ，再用它构造 `Eq.true (succ n)` 是不是就可以了？用 `match` 语句从 `h` 里提取出那个 `n`

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) (h : Eq n m) : Eq (succ n) (succ m) :=
      match h with
      | Eq.true n => Eq.true (succ n)

这样就完成了证明。

你可能会好奇，这样构造出的实例 `Eq.true (succ n)` ，类型写出来其实是 `Eq (succ n) (succ n)` ，并不是函数返回值类型 `Eq (succ n) (succ m)` ，编译器是怎么知道这两个类型是一样的呢？换个问法，既然编译器知道 `Eq (succ n) (succ n)` 和 `Eq (succ n) (succ m)` 是同一个类型，为什么不能跳过 `match h` 这一步，直接 `Eq.true (succ n)` 一步到位

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) (h : Eq n m) : Eq (succ n) (succ m) :=
      Eq.true (succ n)

Lean会报错

::

    Type mismatch
      Eq.true n.succ
    has type
      Eq n.succ n.succ
    but is expected to have type
      Eq n.succ m.succ

我倾向于从unused variable的角度理解这个问题。如果函数的定义里没有用到 `h` ，那么 `h` 就成了个未被使用的参数。要是你日常写C发生类似的情况，编译器会给个warning，这说明我们定义的函数有没有参数 `h` 都一样，不如去掉这个多余的参数

.. code-block:: lean

    def eq_imply_succ_eq (n m : Nat) : Eq (succ n) (succ m) :=
      Eq.true (succ n)

但如果去掉 `h` 的话，命题就变成这样了

    对任意自然数 `n, m` ，有 `succ n = succ m` 。

这个命题一眼假，因为我们知道 `succ n = succ m` 只有在 `n = m` 的前提下才会发生， `Eq (succ n) (succ m)` 实例必须通过 `Eq n m` 实例来构造，所以 `h` 不能去掉，在定义里也必须一定要用到它。

和任意相对应的是存在 `∃` 。试试证明这个命题

    存在自然数 `n` ，有 `succ n = 1` 。

太简单了，一眼看出 `n` 取0就能满足 `succ n = 1` 。所以证明存在性命题只要给2个东西

*   一个实例
*   证明这个实例满足了后面的命题

就像这里，只要给出

*   一个自然数的实例0
*   `succ 0 = 1` 的证明

就完成了证明。

和相等一样，我们也需要想个自定义类型，让所有形如“存在自然数怎么怎么样”的命题都写得出来，同时做到只有真命题对应的类型存在实例

.. code-block:: lean

    inductive Exists ? where

`?` 这里应该放个什么？放个命题吗？

.. code-block:: lean

    inductive Exists (p : Type) where

但这样只能放 `0 = 0, 0 = 1, 1 = 1` 那样的命题，从而只能写出这些类型和这些命题

*   `Exists (Eq 0 0)` 存在某个自然数，有 `0 = 0`
*   `Exists (Eq 0 1)` 存在某个自然数，有 `0 = 1`
*   `Exists (Eq 1 1)` 存在某个自然数，有 `1 = 1`

这类命题和前面的存在没半点关系，后半段本身已经是个独立的命题了。我们刚才看的命题

    存在自然数 `n` ，有 `succ n = 1` 。

后半句里面有个 `n` ，用来指代前半句里的那个即将被列举出的自然数。这个 `n` 是个placeholder占位符，就像函数的参数一样，可以替换成任意字母或者代号，只要和其他参数没冲突随便改，不会改变命题的含义

    存在自然数 `m` ，有 `succ m = 1` 。

    存在自然数 `k` ，有 `succ k = 1` 。

    存在自然数 `😂` ，有 `succ 😂 = 1` 。

所以 `Exists` 后面应该放这样一个东西，给这个东西输入一个自然数，这个东西会输出一个命题。这样的东西是啥？是个函数

.. code-block:: lean

    inductive Exists (p : Nat -> Type) where

这样就可以愉快的表达刚才的命题了，而且也满足可以替换成任意代号的要求

.. code-block:: lean

    Exists (fun n => Eq (succ n) 1)
    Exists (fun m => Eq (succ m) 1)
    Exists (fun k => Eq (succ k) 1)
    Exists (fun 😂 => Eq (succ 😂) 1) -- 好吧Lean还不支持emoji

这件事如果不好理解，也可以反过来想：如果这里不是个函数的话怎么写？直接写 `Eq (succ n) 1` 吗？

.. code-block:: lean

    Exists (Eq (succ n) 1)

可是写 `Eq (succ n) 1` 的时候还没有定义 `n` 。

然后想想constructor该怎么定义。刚才说了，证明由2部分组成，一个自然数，以及证明了这个自然数满足命题的proof（证明既作动词又作名词好奇怪啊）

.. code-block:: lean

    inductive Exists (p : Nat -> Type) where
    | true (n : Nat) ? : Exists p

这个proof怎么写？举个例子，假如 `p := fun n => Eq (succ n) 1` ，那么 `p 0 := Eq (succ 0) 1` 代表 `succ 0 = 1` 这个命题。 `p 0` 本身是个类型，所以它的实例 `h : p 0` 当然就是命题 `succ 0 = 1` 的证明。

这里需要我们提供 `p n` 的证明，所以

.. code-block:: lean

    inductive Exists (p : Nat -> Type) where
    | true (n : Nat) (h : p n) : Exists p

验证一下这样的定义对不对，找几个例子

*   存在自然数 `n` ，有 `succ n = 1` 。

    对应的类型是 `Exists (fun n => Eq (succ n) 1)` 。满足条件的自然数只有0，所以这个类型的实例只有一个

    .. code-block:: lean

        def exist_n_succ_n_eq_one : Exists (fun n => Eq (Nat.succ n) one) :=
          Exists.true zero (Eq.true one)

*   存在自然数 `n` ，有 `n = n` 。

    对应的类型是 `Exists (fun n => Eq n n)` 。任意自然数都满足 `n = n` ，所以这个类型的实例也有无限多个

    .. code-block:: lean

        Exists.true 0 (Eq.true 0)
        Exists.true 1 (Eq.true 1)
        Exists.true 2 (Eq.true 2)
        ...

*   存在自然数 `n` ，有 `succ n = 0` 。

    对应的类型是 `Exists (fun n => Eq (succ n) 0)` 。不存在这样的自然数，所以这个类型的实例也不存在。

    实例不存在，不是因为构造不出 `n : Nat` ，而是构造不出后面的那个证明 `h : p n` ，不信你试试

    .. code-block:: lean

        Exists.true 0 (? : Eq (succ 0) 0)
        Exists.true 1 (? : Eq (succ 1) 0)
        Exists.true 2 (? : Eq (succ 2) 0)
        ...

    无论 `n` 是多少，类型 `Eq (succ n) 0` 始终都不存在实例，换言之，对任意自然数 `n` ，类型 `p n` 都不存在实例。而 `p n` 的实例又是构造 `Exists (fun n => Eq (succ n) 0)` 所必须的，所以对任意自然数 `n` ，类型 `Exists (fun n => Eq (succ n) 0)` 都不存在实例。

数学归纳法
==========

我们先引入自然数上最简单的操作、我们最熟悉的加法，然后证明几个关于加法的定理。

先看加法的定义。加法应该是个函数，输入两个自然数，输出另一个自然数

.. code-block:: lean

    def add : Nat -> Nat -> Nat := ?

不过我们马上就要用到这两个输入参数，所以不如直接给它们起个名字

.. code-block:: lean

    def add (n : Nat) (m : Nat) : Nat := ?

`n, m` 有相同类型，Lean可以写成更简略的形式

.. code-block:: lean

    def add (n m : Nat) : Nat := ?

这句话有另一个读法：如果 `n, m` 是两个自然数，那么 `add n m` 也是个自然数。

该怎么定义加法呢……日常写C++、Python的时候从来没注意过加法怎么定义，如此基础的操作怎么还要我们手动定义呢。别忘了，现在用的自然数定义不是你熟悉的十进制阿拉伯数字，而是用 `zero, succ` 两个variant拼出来的

::

    0 := zero
    1 := succ zero
    2 := succ (succ zero)
    3 := succ (succ (succ zero))
    ...

除了 `0` 以外，其他所有自然数的最外层都是 `succ` ，换句话说，其他自然数 `n` 都是它前一个自然数 `n'` 的下一个自然数，所以都可以拆成 `succ n'` 。要不要试试分情况讨论？C++有 `switch, case` ，Rust有 `match` 语句，Lean也有 `match`

.. code-block:: lean

    def add (n m : Nat) : Nat :=
      match n with
      | zero => ? -- add zero m等于什么？
      | succ n' => ? -- add (succ n') m等于什么？

把 `add n m` 分成了2个子问题，只要凑出这两个问题的回答，定义也就完成了

*   `add zero m` 等于什么？

    简单，当然是 `m` 。

*   `add (succ n') m` 等于什么？

    所有已经对十进制加法形成肌肉记忆的人都不太能轻易想到。

    刚才说过，用 `zero, succ` 来定义自然数的方式，就像原始人用树枝木棍记日子。 `zero` 就是一块空地，一根木棍都没有； `succ` 就是一根木棍； `succ n'` 就是 `n` 根木棍前面放了1根木棍； `add (succ n') m` 就是，你面前有两堆木棍，左边一堆是1根木棍后面跟着另外 `n` 根木棍，右边一堆是 `m` 根木棍，现在你要数清楚左右两堆放一起有多少根木棍

    ::

        ||||..n根木棍..|||    |||..m根木棍..|||

    那么你现在化身为原始人，该怎么办？当然是把这根木棍放到外面，然后接着数剩下的 `add n' m` 啊！

    ::

        | <- 拿出左边一堆木棍的第一根，放一边
        |||..n'根木棍..|||    |||..m根木棍..||| <- 接着数剩下的

    等到数完了剩下的 `add n' m` ，再把一开始放在一边的那一根放进来

    ::

        | |||..add n' m根木棍..|||

    所以结果是 `succ (add n' m)` 。

.. code-block:: lean

    def add (n m : Nat) : Nat :=
        match n with
        | zero => -- add zero m等于什么？
          m
        | succ n' => -- add (succ n') m等于什么？
          succ (add n' m)

试着证明一下

    对任意自然数 `n` ，有 `0 + n = n` 。

.. code-block:: lean

    def zero_add_n_eq_n (n : Nat) : Eq (add zero n) n :=
      Eq.true n

好简单啊。Lean编译器顺着 `add` 的定义、匹配了 `match` 的第一个variant，得知 `add zero n := n` 。

加法有交换律，所以 `n + 0 = n` ，试着证明一下

    对任意自然数 `n` ，有 `n + 0 = n` 。

.. code-block:: lean

    def n_add_zero_eq_n (n : Nat) : Eq (add n zero) n := ?

人类理解加法有交换律（不，你并不理解，你只是记忆了这件事），所以 `n + 0 = 0 + n` 非常显然，但Lean不知道，它甚至不知道你在刻画自然数。这里它也试图顺着定义展开 `add n zero` ，但因为这次 `n` 在左边， `add` 的定义匹配的正好是左边的自然数的2种情况（哪2种？），所以它不知道该走哪个variant了，需要我们引导一下

.. code-block:: lean

    def n_add_zero_eq_n (n : Nat) : Eq (add n zero) n :=
      match n with
      | zero => -- 构造Eq (add zero zero) zero实例
        Eq.true zero -- 显然
      | succ n' => -- 构造Eq (add (succ n') zero) (succ n')实例
        -- Lean知道展开add，得到add (succ n') zero := succ (add n' zero)
        -- 构造Eq (succ (add n' zero)) (succ n')实例
        ?

`n` 等于0，显然直接 `Eq.true zero` ，不谈了。

`n` 等于 `succ n'` 的情况有点复杂，我一步一步给你讲

1.  把 `n := succ n'` 代入 `Eq (add n zero) n` ，得到 `Eq (add (succ n') zero) (succ n')` ，意味着需要构造 `Eq (add (succ n') zero) (succ n')` 的实例
2.  Lean很贴心，看到左边有 `add (succ ?) ?` ，于是尝试用 `add` 的定义展开左边 `add (succ n') zero := succ (add n' zero)` ，所以只需要构造 `Eq (succ (add n' zero)) (succ n')` 的实例

那怎么构造 `Eq (succ (add n' zero)) (succ n')` 实例？观察到这个类型长得像 `Eq (succ n) (succ m)` ，我们刚刚才证明过 `eq_imply_succ_eq`

    对任意自然数 `n, m` ，如果 `n = m` ，那么 `succ n = succ m` 。

只要能拿到 `Eq (add n' zero) n'` 实例再丢进 `eq_imply_succ_eq` 就搞定了。

怎么拿到 `Eq (add n' zero) n'` 实例？谜底就在谜面上

.. code-block:: lean

    def n_add_zero_eq_n (n : Nat) : Eq (add n zero) n :=

递归调用，`n_add_zero_eq_n n'` 就是我们想要的 `Eq (add n' zero) n'` 实例。

等一下！可是我们还没写完 `n_add_zero_eq_n` 的定义啊，怎么能在写完函数完整定义之前调用自己呢？这不是相当于楼还没建成，从10楼爬到11楼吗？你发现了盲点，但是请你回忆一下，递归不就是这样用的吗？刚才写单链表长度的时候也是这样写的， `.len` 还没写完，就调用了剩余部分 `tail.len()` 。只要保证递归能结束、不会无限进行下去、最终必定落入某个base case就够了。

其实这就是数学归纳法，区别在于课本上的数学归纳法通常是假定 `p n` 成立然后证明 `p (n + 1)` 成立；递归正好反过来，证明命题 `p n` 的时候，假定 `p (n - 1), p (n - 2), ...` 全都已经证明过了，直接用它们的结论。 `它们是等价的 <https://en.wikipedia.org/wiki/Mathematical_induction#Complete_(strong)_induction>`_ 。

再来一遍，写的紧凑点

::

    goal : Eq (add n zero) n -- 代入n := succ n'
    goal : Eq (add (succ n') zero) (succ n') -- 展开add
    goal : Eq (succ (add n' zero)) (succ n') -- 递归
    ih : Eq (add n' zero) n' -- 调用eq_imply_succ_eq给左右两边套上succ
    eq_imply_succ_eq (add n' zero) n' ih : Eq (succ (add n' zero)) (succ n') -- 大功告成

完整代码

.. code-block:: lean

    def n_add_zero_eq_n (n : Nat) : Eq (add n zero) n :=
      match n with
      | zero => -- 构造Eq (add zero zero) zero实例
        Eq.true zero -- 显然
      | succ n' => -- 构造Eq (add (succ n') zero) (succ n')实例
        -- Lean知道展开add，得到add (succ n') zero := succ (add n' zero)
        -- 构造Eq (succ (add n' zero)) (succ n')实例
        -- 先递归，构造Eq (add n' zero) n'实例
        let ih : Eq (add n' zero) n' := n_add_zero_eq_n n'
        -- 给ih的两边套上succ
        eq_imply_succ_eq (add n' zero) n' ih

自上而下
========

证明 `n_add_zero_eq_n` 的过程中用到了 `eq_imply_succ_eq` ，所以 `eq_imply_succ_eq` 可以看作是 `n_add_zero_eq_n` 的引理。这是一种自下而上的工作模式：手头先有一些引理，然后用它们组合成大的定理。但通常定理证明起来都很复杂，一般情况下我们无法预见证明过程会用到哪些引理。这和写代码一样，不可能一上来就知道项目要依赖什么库，只能一边做一边想，需要的时候引入进来。此时自上而下的工作模式更合适：先确定要证明的定理依赖什么引理，然后再去证明引理。

证明关于加法最复杂的定理，加法的交换律

    对任意自然数 `n, m` ，有 `n + m = m + n` 。

.. code-block:: lean

    def add_comm (n m : Nat) : Eq (add n m) (add m n) :=
      match n with
      | zero =>
        -- Eq (add zero m) (add m zero)
        -- Eq m (add m zero)
      | succ n' =>
        -- Eq (add (succ n') m) (add m (succ n'))
        -- Eq (succ (add n' m)) (add m (succ n'))

2个variant都不太容易。第一个variant稍微容易一些，要证明 `m = m + 0` 。刚才已经证明过 `n + 0 = n` ，只要证明一下相等具有对称性就可以拼上这块拼图

    对任意自然数 `n, m` ，如果 `n = m` ，那么 `m = n` 。

.. code-block:: lean

    def eq_symm (n m : Nat) (h : Eq n m) : Eq m n :=
      match h with
      | Eq.true n => Eq.true n

拼上这块拼图 `m = m + 0`

.. code-block:: lean

    match n with
    | zero =>
      -- Eq (add zero m) (add m zero)
      -- Eq m (add m zero)
      -- 先用n_add_zero_eq_n得到m + 0 = m
      let h : Eq (add m zero) m = n_add_zero_eq_n m
      -- 再用eq_symm把m + 0 = m变成m = m + 0
      eq_symm (add m zero) m h

第2个variant稍显复杂，看起来没什么头绪。递归可以给我们多一个已知条件

::

    goal : Eq (succ (add n' m)) (add m (succ n'))
    ih : Eq (add n' m) (add m n') := add_comm n' m

试试用 `eq_imply_succ_eq` 给 `ih` 两边套上 `succ` ？

::

    goal : Eq (succ (add n' m)) (add m (succ n'))
    eq_imply_succ_eq ? ? ih : Eq (succ (add n' m)) (succ (add m n'))

这下两个式子的左边都一样了。能不能让右边也一样？右边相等的条件是， `succ` 不仅可以从 `add` 的左边参数 `n` 里跑出来，也可以从右边的 `m` 里跑出来

    对任意自然数 `n, m` ，有 `n + (succ m) = succ (n + m)` 。

.. code-block:: lean

    def n_add_succ_m (n m : Nat) : Eq (add n (Nat.succ m)) (Nat.succ (add n m)) :=
      match n with
      | Nat.zero =>
        -- Eq (add 0 (succ m)) (succ (add 0 m))
        -- Eq (succ m) (succ m)
        Eq.true (Nat.succ m)
      | Nat.succ n' =>
        -- Eq (add (succ n') (succ m)) (succ (add (succ n') m))
        -- Eq (succ (add n' (succ m))) (succ (succ (add n' m)))
        -- 先递归得到n' + (succ m) = succ (n' + m)
        let ih : Eq (add n' (Nat.succ m)) (Nat.succ (add n' m)) := n_add_succ_m n' m
        -- 再用eq_imply_succ_eq两边套上succ
        eq_imply_succ_eq (add n' (Nat.succ m)) (Nat.succ (add n' m)) ih

有了这个引理，两个式子右边就相等了

::

    goal : Eq (succ (add n' m)) (add m (succ n'))
    eq_imply_succ_eq ? ? ih : Eq (succ (add n' m)) (succ (add m n'))
    n_add_succ_m m n' : Eq (add m (succ n')) (succ (add m n'))

现在，还需要一个引理，把这3个数字联系在一起，是什么呢？相等的传递性

    对任意自然数 `n, m, k` ，如果 `n = m` 并且 `m = k` ，那么 `n = k` 。

证明方式和 `eq_symm` 差不多，只是这里要连续 `match` 两次

.. code-block:: lean

    def eq_trans (n m k : Nat) (h1 : Eq n m) (h2 : Eq m k) : Eq n k :=
      match h1 with
      | Eq.true n =>
        match h2 with
        | Eq.true n => Eq.true n

这样所有的依赖都搞定了！回过来看最初的目标。先把刚刚证明的几个依赖项写出来，然后再看看怎么用 `eq_trans, eq_symm` 组合起来

.. code-block:: lean

    | succ n' =>
      -- Eq (add (succ n') m) (add m (succ n'))
      -- Eq (succ (add n' m)) (add m (succ n'))
      -- 递归得到的条件
      let ih : Eq (add n' m) (add m n') := add_comm n' m
      -- 等式两边套succ
      let succ_ih : Eq (succ (add n' m)) (succ (add m n')) := eq_imply_succ_eq (add n' m) (add m n') ih
      -- 右边succ从add里面跑到add外面
      let succ_right : Eq (add m (succ n')) (succ (add m n')) := n_add_succ_m m n'
      -- 等式左右两边互换
      let succ_right_rev : Eq (succ (add m n')) (add m (succ n')) :=
        eq_symm (add m (succ n')) (succ (add m n')) succ_right
      -- succ_ih右边和succ_right_rev左边相等，所以succ_ih左边和succ_right_rev右边相等
      let res : Eq (succ (add n' m)) (add m (succ n')) :=
        eq_trans (succ (add n' m)) (succ (add m n')) (add m (succ n')) succ_ih succ_right_rev
      -- res就是goal
      res

可读性有点过于低下了……原因有3

*   语法噪音太大了，很多参数可以从别的参数推断出来，没必要全都写出来。

    比方说 `eq_trans` 的 `n, m, k` 完全可以从后面的 `h1, h2` 直接推断出来，没必要写出来，但定义不能没有这个参数（否则就是另一个命题了）。这时候怎么办呢？Rust和C++都有范型类型自动推断，Lean也有，把参数用花括号 `{}` 包起来，调用的时候就不需要显式写出这个参数了

    .. code-block:: lean

        def eq_trans {n m k : Nat} (h1 : Eq n m) (h2 : Eq m k) : Eq n k :=

        def eq_symm {n m : Nat} (h : Eq n m) : Eq m n :=

        def eq_imply_succ_eq {n m : Nat} (h : Eq n m) : Eq (Nat.succ n) (Nat.succ m) :=

    调用的时候

    .. code-block:: lean

        | succ n' =>
          -- Eq (add (succ n') m) (add m (succ n'))
          -- Eq (succ (add n' m)) (add m (succ n'))
          -- 递归得到的条件
          let ih : Eq (add n' m) (add m n') := add_comm n' m
          -- 等式两边套succ
          let succ_ih : Eq (succ (add n' m)) (succ (add m n')) := eq_imply_succ_eq ih
          -- 右边succ从add里面跑到add外面
          let succ_right : Eq (add m (succ n')) (succ (add m n')) := n_add_succ_m m n'
          -- 等式左右两边互换
          let succ_right_rev : Eq (succ (add m n')) (add m (succ n')) :=
            eq_symm succ_right
          -- succ_ih右边和succ_right_rev左边相等，所以succ_ih左边和succ_right_rev右边相等
          let res : Eq (succ (add n' m)) (add m (succ n')) :=
            eq_trans succ_ih succ_right_rev
          -- res就是goal
          res

    清爽多了吧？

*   全都是前缀表达式，看起来不习惯。加法、相等这些表达式我们习惯了放在中间。

    有道理，接下来会用标准库的类型（虽然只剩最后一点内容了）。刚才一直用丑陋的前缀表达式的原因是，我想明确区分命题、类型、定理，命题我都用我们熟悉的 `a = b` 写，对应的类型都用 `Eq a b` ，这样看起来更像类型，定理都用下划线全小写。这样更便于你理解，否则命题和类型都用 `a = b` 写，你会搞不清楚这里的 `a = b` 指的是命题还是对应的类型。到这里你基本上已经接受了命题和对应类型的设定，这种区分命题和类型的写法反而成了障碍，那么接下来确实没必要继续这样写了。

    Lean里面有办法自定义操作符、指派到具体函数，就像把 `+` 指派到 `add` ，标准库帮忙做了这件事。这个规则很难写，因为存在操作符优先级的问题，比如 `a + b = c` 应该解释成 `(a + b) = c` 还是 `a + (b = c)` 的问题；还有左结合右结合的问题，比如 `a + b + c` 解释成 `(a + b) + c` 还是 `a + (b + c)` ，对加法来说当然无所谓因为加法有结合律，左右结合都不影响结果，但别的操作不一定有结合律。

*   构造最终证明的过程仍然是自下而上的，和思维过程相反，非常别扭。

    这点应该是最重要的原因。我们思考证明的过程是把原始证明目标goal尽可能转化成简单且等价的另一个goal，然后去拆解goal、思考满足goal需要的条件，这是个自上而下的过程。就像做汉堡，考虑需要面包、烤熟的牛肉饼、番茄生菜、奶酪、烧烤酱（好饿）。烤熟的牛肉饼又需要生牛肉饼和烤箱……

    但观察刚才写的证明，整个书写过程是先准备了一大堆引理，然后神奇的变出了最终的goal的证明。就像手头正好有面包、牛肉饼、番茄生菜，顺手做了一道汉堡。

    为什么书写过程不能和思维过程匹配呢？这就是tactics解决的问题了。上面所有的证明的写法都用的是所谓的term mode，和写程序一样，先准备好需要的所有东西、拼出中间结果、用中间结果拼出最终结果。还有一种tactics mode，看上去非常简略，全是各种缩写 `apply, rw, simp, exact` 。画风长这样

    .. code-block:: lean

        theorem add_comm : ∀ (n m : Nat), n + m = m + n
          | n, 0   => Eq.symm (Nat.zero_add n) -- 这是term mode
          | n, m+1 => by -- 进入tactics mode
            have : succ (n + m) = succ (m + n) := by apply congrArg; apply Nat.add_comm
            rw [succ_add m n]
            apply this

    要是数学家们和医生一样，发展出了类似处方鬼画符一样的证明写法，估计差不多就长这样。

    Tactics mode还有个好处，如果你装了VSCode的Lean插件，当你在左边写证明，编辑器右边会即时显示当前证明的进度——当前有哪些可用的引理、目标goal化简到了什么样子——移动光标位置，还会显示每一步tactics作用的效果、化简了goal或者引理的哪一部分。Lean、Coq、Agda都有类似的功能，它们宣传自己是interactive proof assistant，其中的interactive指的就是这个。

    Tactics本质上是什么？我的理解是tactics类似macro，展开这些tactics得到的还是term，所以编译器最终检查的仍然是term而不是tactics。所以tactics mode和term mode并不是非此即彼水火不容的，它们可以混着写，当前哪个方便就用哪个。这个内容就留给202了。

小于等于
========

和相等一样的套路，先写下所有形如 `n <= m` 的命题

::

    0 <= 0  0 <= 1  0 <= 2 ...
    1 <= 0  1 <= 1  1 <= 2 ...
    2 <= 0  2 <= 1  2 <= 2 ...
    ...

每个命题都对应一个类型

::

    LE_0_0  LE_0_1  LE_0_2 ...
    LE_1_0  LE_1_1  LE_1_2 ...
    LE_2_0  LE_2_1  LE_2_2 ...
    ...

你马上反应过来 `LE` 应该是个范型类型，太聪明了！

.. code-block:: lean

    inductive LE : Nat -> Nat -> Type where

现在考虑定义哪些constructor，能够让 `LE 0 0, LE 0 1` 这些真命题对应的类型有实例，同时让 `LE 1 0, LE 2 0` 这样的假命题对应的类型没有实例。

观察一下表格的形状，真命题组成了个上三角形，对角线上的命题都是形如 `n <= n` 的真命题，从对角线往左都是假命题，往右都是真命题

::

    LE 0 0 -> LE 0 1 -> LE 0 2 -> LE 0 3 -> ...
    LE 1 0    LE 1 1 -> LE 1 2 -> LE 1 3 -> ...
    LE 2 0    LE 2 1    LE 2 2 -> LE 2 3 -> ...
    LE 3 0    LE 3 1    LE 3 2    LE 3 3 -> ...
    ...

所以我们继承发扬Peano的精神，小于等于无非是下列这两种情况

*   对任意自然数 `n` ，有 `n <= n`

    这是描述对角线上都是真命题。

*   对任意自然数 `n, m` ，如果 `n <= m` ，那么 `n <= m + 1`

    这是描述任何一个真命题往右走一格也是真命题。或者说，这是在描述如果 `n <= m` ，那么左边 `n` 不变，右边 `m` 增加1，不等式仍然成立。作用是把 `n <= m` 的证明变成 `n <= m + 1` 的证明。

.. code-block:: lean

    inductive LE : Nat -> Nat -> Type where
    | base (n : Nat) : LE n n
    | step {n m : Nat} (h : LE n m) : LE n (Nat.succ m) -- n, m可以从h推导出来

还有另一种写法，观察到表格第一行都是真命题，并且从任意一个真命题出发往右下方走一格也是真命题

::

    LE 0 0 ↘  LE 0 1 ↘  LE 0 2 ↘  LE 0 3 ↘  ...
    LE 1 0    LE 1 1 ↘  LE 1 2 ↘  LE 1 3 ↘  ...
    LE 2 0    LE 2 1    LE 2 2 ↘  LE 2 3 ↘  ...
    LE 3 0    LE 3 1    LE 3 2    LE 3 3 ↘  ...
    ...

*   对任意自然数 `m` ，有 `0 <= m`

    这是在描述第一行都是真命题。

*   对任意自然数 `n, m` ，如果 `n <= m` ，那么 `n + 1 <= m + 1`

    这是在描述任意一个真命题往右下方走一格也是真命题。作用是把 `n <= m` 的证明转化成 `n + 1 <= m + 1` 的证明。

.. code-block:: lean

    inductive LE' : Nat -> Nat -> Type where
    | base (m : Nat) : LE' 0 m
    | step {n m : Nat} (h : LE' n m) : LE' (Nat.succ n) (Nat.succ m) -- n, m可以从h推导出来

证明 `1 <= 2` 。首先用 `LE.base 1` 产生 `1 <= 1` 的证明，然后用 `LE.step` 把 `1 <= 1` 的证明转化成 `1 <= 2` 的证明

.. code-block:: lean

    def one_le_two : LE 1 2 := LE.step (LE.base 1)

或者如果用另一种定义，就是用 `LE'.base 1` 产生 `0 <= 1` 的证明，然后用 `LE'.step` 把 `0 <= 1` 的证明转化成 `1 <= 2` 的证明

.. code-block:: lean

    def one_le_two' : LE' 1 2 := LE'.step (LE'.base 1)

这两种方式等价吗？ `LE n m` 能推导出 `LE' n m` 吗？反过来也可以吗？

.. code-block:: lean

    def le_to_le' {n m : Nat} (h : LE n m) : LE' n m := ?
    def le'_to_le {n m : Nat} (h : LE' n m) : LE n m := ?

一眼看上去有点难。要不先试试分别证明两种表示都有对方的性质？对于第一种表示方法， `n <= n` 和 `n <= m -> n <= m + 1` 是显然的，但 `0 <= m` 和 `n <= m -> n + 1 <= m + 1` 不显然。第二种正好相反。

先证明第一种表示方法有第二种表示方法的2个显然性质

*   用第一种表示方法 `LE` ，证明

        对任意自然数 `m` ，有 `0 <= m` 。

    .. code-block:: lean

        def le_base (n : Nat) : LE 0 n :=
          match n with
          | 0 => LE.base 0 -- 显然0 <= 0
          | Nat.succ n' =>
            let ih : LE 0 n' := le_base n' -- 归纳法0 <= n'
            LE.step ih -- 0 <= n'变0 <= succ n'

*   用第一种表示方法 `LE` ，证明

        对任意自然数 `n, m` ，如果 `n <= m` ，那么 `n + 1 <= m + 1` 。

    试一下就会发现 `match n` 走不通，只能 `match h`

    .. code-block:: lean

        def le_succ {n m : Nat} (h : LE n m) : LE (Nat.succ n) (Nat.succ m) :=
          match h with
          | LE.base n => -- 说明n = m
            LE.base (Nat.succ n) -- 显然(succ n) <= (succ m)
          | @LE.step n m' h' =>
            -- h : LE n (succ m') := @LE.step n m' h'
            -- m := succ m'
            -- h' : LE n m'
            -- goal : LE (succ n) (succ m)
            -- goal : LE (succ n) (succ (succ m'))
            -- 遇事不决先归纳法
            let ih : LE (Nat.succ n) (Nat.succ m') := le_succ h'
            -- step的作用是右边succ
            LE.step ih

然后反过来证明第二种表示方法也具有第一种表示方法的2个显然性质

*   用第二种表示方法 `LE'` ，证明

        对任意自然数 `n` ，有 `n <= n` 。

    .. code-block:: lean

        def le'_refl (n : Nat) : LE' n n :=
          match n with
          | 0 => -- 显然0 <= 0
            LE'.base 0
          | Nat.succ n' =>
            let ih : LE' n' n' := le'_refl n' -- 归纳法n' <= n'
            LE'.step ih -- n' <= n'变(succ n') <= (succ n')

*   用第二种表示方法 `LE'` ，证明

        对任意自然数 `n, m` ，如果 `n <= m` ，那么 `n <= m + 1` 。

    同样，试一下就会发现 `match n` 走不通，只能 `match h`

    .. code-block:: lean

        def le'_step {n m : Nat} (h : LE' n m) : LE' n (Nat.succ m) :=
          match h with
          | LE'.base m => -- 说明0 <= m
            LE'.base (Nat.succ m) -- 显然0 <= (succ m)
          | @LE'.step n' m' h' =>
            -- h : LE' (succ n') (succ m') h' := step h'
            -- n := succ n'
            -- m := succ m'
            -- h' : LE' n' m'
            -- goal : LE' n (succ m)
            -- goal : LE' (succ n') (succ (succ m'))
            -- 归纳法
            let ih : LE' n' (Nat.succ m') := le'_step h'
            -- step两边套succ
            LE'.step ih

有了这4个引理，原来的2个命题就很好证了

.. code-block:: lean

    def le_to_le' {n m : Nat} (h : LE n m) : LE' n m :=
      match h with
      | LE.base n =>
        -- h : LE n n
        le'_refl n
      | @LE.step n m' h' =>
        -- h : LE n (succ m')
        -- h' : LE n m'
        -- m := succ m'
        -- goal : LE' n (succ m')
        let ih : LE' n m' := le_to_le' h'
        -- 右边套succ
        le'_step ih

    def le'_to_le {n m : Nat} (h : LE' n m) : LE n m :=
      match h with
      | LE'.base m =>
        -- h : LE' 0 m
        le_base m
      | @LE'.step n' m' h' =>
        -- h : LE' (succ n') (succ m')
        -- h' : LE' n' m'
        -- n := succ n'
        -- m := succ m'
        -- goal : LE (succ n') (succ m')
        let ih : LE n' m' := le'_to_le h'
        -- 两边套succ
        le_succ ih

通过 `le_to_le', le'_to_le` ，两种不同表示方法下的不等式终于可以互相转换了。

然后呢
=======

然后我可能会断更几年再写个201，还有茫茫多的话题没有讲，比如与或非对应什么，整数、有理数、实数如何定义，还有tactics，还有如何证明现实中有实际用途的程序是正确的，比如证明自己写的快速排序是正确的……可惜写到这里猛然发现已经写了4万多字了，再写下去要出书了。如果你等不及了，可以继续去看 `Theorem Proving in Lean 4 <https://lean-lang.org/theorem_proving_in_lean4/>`_ 。还有大名鼎鼎的 `Software Foundations <https://softwarefoundations.cis.upenn.edu/>`_ 你应该也不会看起来一头雾水了。

-----

呼……终于写完了。其实比起担心你是否有耐心读完这么长这么啰嗦的文字，我更担心你到底能不能理解。很惭愧，我没有十足的把握。虽然我想讲这个话题很久了，但一直不知道怎么讲。在自认为理解了propositions as types之后，我在线下给好多朋友试图讲明白这件事，只有一位朋友看起来真的理解了。多数朋友对这件事并无太大兴趣。我承认我对写出正确的代码这件事有一种极其理想、不切实际的执念，这种执念才是我接触机器定理证明的动机。现在我终于可以说，写出完全正确的代码并不是不可能的，只是目前很难也很麻烦。我不知道这是不是个纯粹的成本问题，因为大家对代码正确性的需求并不大，所以无人关注，没有像投入AI、互联网那样投入精力来研究如何让形式化验证变得更好用。不过知道这件事是可能的已经让我非常安心了。

2025/12/18
