# 我怎么搭建这个博客的
*7/7*

自以为这个博客建的不错，略有成就感。在此分享下我的心路历程。

## 构想

我的原则是做任何事之前先搞明白自己的需求，然后再根据情况或保留或折中。

- 最好是不需要服务器后台维护的静态网站。不用找主机商了。
- 最好用Markdown写文章，以纯文本形式存储内容。方便编辑，也减少格式对写作思路的不利影响。
- 最好能远程托管。方便同步，内容也不会丢失。

## 架构

博客这个东西我还是第一次搞。之前看了[Ivy-end学长](http://ivy-end.com)的博客，异常精彩；又看了他的友情链接，发现其中没有一个不是一级域名的博客，土豪极了，然而我一是没这么土豪，二是没太多时间维护一个远在天边的服务端进程，于是准备搞静态站点，毕竟博客不需要多少动态内容；接着发现Github有个很赞的功能叫做Github Pages，可以给项目自动生成项目主页，更赞的是它的说明里鼓励用户用这个功能建博客。

**之前知乎上有过关于用Github Pages来建博客是否道德的[争论](http://www.zhihu.com/question/20717014)。*

于是在以上构想中，决定采用Markdown + Mkdocs + Git + Github Pages模式搭建博客。

整个博客是托管在github上的一个代码仓库，使用github提供的pages功能，是静态的。

github貌似推荐的是Jekyll作为静态网站生成器，但是Jekyll是用Ruby写的，国内下载速度很低，我想想，不如找找有没有现成的Python写成的静态站点生成器，找到了神器[Mkdocs](http://mkdocs.org)。

> MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

Mkdocs顾名思义本来是用来生成简易的项目文档的，但是我看了下它的最终界面，也很适合用来作为博客生成器，而且用起来很方便，无非就是下面的几个用法。

`mkdocs new projectName` 新建一个Mkdocs项目目录；

`mkdocs serve --dev-addr=:port` 在本机的`port`号端口上预览，Mkdocs还会自动检测文件变化；

`mkdocs build --clean` 生成站点，默认在目录`site`里；

其他的用法详见[Mkdocs官网](http://mkdocs.org)。

后来[Ivy-end学长](http://ivy-end.com)问我为啥没有评论系统，于是我找到了[Disqus](http://disqus.com)，这个Disqus从官网上看，是个类似百度贴吧的东东，大家在上面就各种话题讨论，不亦乐乎。然而，Disqus提供了站外评论的功能，貌似还是免费的，于是果断用起。当然是很简单的，因为Markdown转换成HTML的时候会自动保留里面的HTML元素，所以说只要写完文章，在后面加上Disqus的代码就好。而且Disqus也提供了放在你网站上的Universal Codes，直接复制粘贴在需要的位置就好。

## 特技

再后来，发现这样每篇文章都贴代码实在太别扭了，于是想着能否修改站点生成流程代码，正好Mkdocs提供了自定义主题的功能，于是我把我想用的主题从Mkdocs源码里找出来，复制到自己项目的目录里，开始修改模板代码。

模板代码目录里有一个`base.html`，里面是Jinja语法的模板代码，每个页面都是用这个替换关键字生成的，可以仔细观察每个节点的作用，看名字就很容易得出他们的作用。

`{{ nav }}`代表上部的大导航栏；

`{{ toc }}`代表左侧的文章内容导航栏；

`{{ content }}`代表渲染过后的文章内容；

这样我就在`{{ content }}`后面加上了Disqus评论系统的Universal Codes，然后重新build发布，评论系统就顺利批量加上了。

再再后来，我发现我应该有个首页，放我最近更新文章的链接，而且不需要左侧内容导航栏，也不需要评论，怎么办？

其实也很简单，方法我上面也提到了，就是在需要特殊处理的页面上随意加HTML元素，想加什么加什么，比如加`<script></script>`，于是这个页面加载的时候就会执行这段Javascript代码，而且我发现base.html有用到jQuery，那么问题更简单了，我可以直接调用jQuery把页面上不需要的部分删掉就好。于是我加了下面的代码用来把评论区和左侧导航栏删除。

```
<script>
jQuery("div#disqus_thread").ready(function(){
    jQuery("div.col-md-3").remove();
    jQuery("div#disqus_thread").remove();
});
</script>
```

## 总结

这样我就搭成了现在这样的博客，怎么说，虽然博客精彩与否取决于内容，但是谁愿意看纯文本？我不求过度的如洛可可一般的强烈装饰感，只求我的文章能看着顺眼，当然我顺眼的标准还是挺高的哈哈。