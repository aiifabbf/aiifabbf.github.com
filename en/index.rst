===================
Yuchen SHI 施宇晨
===================

.. default-role:: literal

Greetings! I am currently working as an R&D engineer at `Synopsys VCS <https://www.synopsys.com/verification/simulation/vcs.html>`_ constraint team, focusing on enhancing VCS's constrained random test case generation.

I was a master student in Computer Engineering in `Northwestern University <https://northwestern.edu>`_ from 2019/9 to 2020/12.

I received my bachelor degree in Integrated Circuit Design in `Huazhong University of Science and Technology <https://english.hust.edu.cn>`_ in 2019/6. I wrote a `small tool <https://github.com/aiifabbf/sizer>`_ to compute optimal circuit parameters for analog amplifiers as `my undergraduate project <https://github.com/aiifabbf/undergraduate-thesis>`_.

I enjoy coding and building. I also enjoy explaining what I know to people. I keep a `blog <https://aiifabbf.github.io>`_ written in Chinese. It mostly contains my personal thoughts about computers, physics and math. Someday I will write in English. I promise.

My resume/CV is `here <https://aiifabbf.github.io/resume/cv.html>`_. You can open the link and print the web page in Firefox or Chrome to get a PDF version. [#paper-cv]_

Feel free to contact me at aiifabbf@outlook.com .

Experiences
===========

I am currently working full-time at Synopsys VCS constraint team in Shanghai, building and enhancing solvers that help customers generate huge number of test cases to quickly meet their verification sign-off goals. I write mostly C and C++ in production, sometimes Python and Rust to prototype.

I was a full stack intern, writing CSS and doing UI tuning in a local data visualization company in 2019 summer.

I wrote a `single-page web application <https://github.com/SicunStudio/aunet-flask>`_ that works as the administration dashboard for a campus organization during undergraduate. My main role was front-end, but I also worked with back-end teammates on RESTful API design.

While I was seeking an intern position for 2020 summer, I solved `over 1000 problems on Leetcode <https://leetcode.com/aiifabbf>`_. My `code and comments <https://github.com/aiifabbf/leetcode-memo>`_ helped many friends learn algorithms and prepare for interviews.

Projects
========

``sizer``
---------

My undergraduate project. A small tool to compute optimal parameters for circuit components like analog amplifiers, logic gates.

Learn more `here <https://github.com/aiifabbf/sizer>`_.

``steve``
---------

A computer graphics course project. I made a naive 3D engine around WebGL's drawing primitives to make my and my teammate's life easier. This engine supports changing object's material on the fly by on-demand, lazy loading of shader program. I also implemented a simple frame-rate-independent animation system to enable you to program key frames like CSS.

Learn more `here <https://github.com/aiifabbf/steve>`_.

``simple-tcp``
--------------

A computer networking project. I implemented a simple TCP-like protocol on top of UDP to enable reliable transport.

Learn more `here <https://github.com/aiifabbf/simple-tcp>`_.

``ray-tracer``
--------------

A toy ray-tracing renderer in Rust, inspired by `Ray Tracing in One Weekend <https://raytracing.github.io/>`_ series. The book uses C++, but I thought it would be nice to do it in Rust. Features I implemented include:

-   `bounding volume hierarchy <https://en.wikipedia.org/wiki/Bounding_volume_hierarchy>`_ (which you can think of as a 3D binary search tree) to accelerate ray-object intersection
-   multi-thread rendering
-   arbitrary transform to objects
-   diffusive, reflective, refractive materials
-   isotropic volume (like smoke and fog)

I also ported it to WebAssembly and made a `live demo <https://aiifabbf.github.io/ray-tracer-wasm/www/dist/index.html>`_, so you can run it in your browser!

Learn more `here <https://github.com/aiifabbf/ray-tracer>`_.

`parsec`
--------

A parser combinator framework in Rust, mimicing the famous Haskell library `parsec`. Parser combinator is a way to build complicated parsers by composing small parsers.

This is where I grew interest in functional programming languages and all the amazing stuff behind!

Learn more `here <https://github.com/aiifabbf/parsec>`_.

This blog
---------

My `blog <https://aiifabbf.github.io>`_. This blog is a hybrid structure. I write posts in `reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ and Jupyter Notebook, then they are converted to HTML using `Sphinx <http://www.sphinx-doc.org/en/master/>`_. Those HTML used to be loaded dynamically using AJAX and injected into DOM using Vue.js, but later I found static HTML works well enough for the purpose of a blog.

See source `here <https://github.com/aiifabbf/aiifabbf.github.com>`_.

Publications
============

I wrote heat simulation in Python for paper [zhou2020]_.

.. [zhou2020] Zhou, Ling, Yufei Zhou, **Yuchen Shi,** Tianwei Chen, Tenghao Zou, Dongxiang Zhou, and Qiuyun Fu. "Enhancing thermal stability of P (VDF-HFP) based nanocomposites with core-shell fillers for energy storage applications." Composites Science and Technology 186 (2020): 107934. `doi: 10.1016/j.compscitech.2019.107934 <https://doi.org/10.1016/j.compscitech.2019.107934>`_

Courses
=======

During master study, I have taken

-   algorithms
-   operating systems
-   computer networking
-   databases
-   computer graphics
-   machine learning
-   deep learning
-   compilers
-   distributed systems
-   scalable systems
-   concurrent programming

During undergraduate study, I have taken

-   computer architecture
-   analog circuits
-   digital circuits
-   signals and systems
-   quantum mechanics

.. [#paper-cv] Paper resume/CV looks better if you have `Latin Modern <http://www.gust.org.pl/projects/e-foundry/latin-modern/index_html>`_ fonts installed.
