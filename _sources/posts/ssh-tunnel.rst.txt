================
用SSH隧道开心上网
================

.. default-role:: literal

1.  获得一个国外的VPS

    简单来说就是买了一台在国外的电脑，这台电脑有一个公网IP地址。

    可以去 `vultr <https://www.vultr.com/>`_ 或者 `bandwagon <https://bandwagonhost.com/cn2gia-vps.php>`_ 买一个服务器，算下来大概每个月5 usd。

    或者蹭朋友的。

2.  用

    .. code-block:: bash

        ssh -D 1080 -g -C <用户名>@<VPS的IP地址>

    建立到VPS的隧道

    假设你买的VPS的地址是 `123.321.123.321` ，用户名是 `benja` ，那么

    .. code-block:: bash

        ssh -D 1080 -g -C benja@123.321.123.321

    就可以登录到这台VPS上，并且打开了电脑到VPS的隧道。

    解释下

    *   `-D 1080` 的作用是在你电脑的本地打开1080端口，用于监听代理请求，马上我们会在本地配置，让流量都发送到本地的1080端口，这样流量就能通过隧道到达VPS了
    *   `-g` 是监听本地所有的IP地址，这样局域网上其他电脑（比如你的手机）也可以通过连接到你电脑的1080端口来开心上网
    *   `-C` 是打开你到VPS之间通信的压缩，可以节约VPS的流量。

3.  设置浏览器代理

    有2种方法

    +   设置windows的全局代理

        以windows 10为例

        1.  打开设置
        2.  网络和internet
        3.  网络和共享中心
        4.  internet选项
        5.  连接
        6.  局域网设置
        7.  打开“为LAN使用代理服务器”
        8.  高级
        9.  套接字里面，代理服务器地址写 `127.0.0.1` 、端口写 `1080`
        10. 确定

        就好了，windows上所有的软件都会走代理。

    +   或者可以装一个叫做SwitchyOmega的插件，在chrome和firefox上都有

        装好之后，在auto switch情景模式下，填入

        ::

            https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt

        规则列表格式是 `AutoProxy` 。

        这样就能做到对于需要开心的网站，自动走隧道；对于不需要开心的网站，不走隧道。

2022/7/2
