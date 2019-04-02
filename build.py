import os
import sys

tasks = []

# build jupyter notebooks
if "--rst-only" not in sys.argv: # building jupyter is slow as hell...
    tasks.append(os.popen("jupyter nbconvert --template basic posts/*.ipynb"))

# build restructuredtext docs
for v in os.listdir("posts/"):
    if v.endswith(".rst"):
        name = v[: -4]
        tasks.append(os.popen(f"rst2html5.py 'posts/{v}' --template=rst-template.html --quiet --language=zh-cn --math-output=MathJax > 'posts/{name}.html'"))

for v in tasks:
    v.close() # wait for all tasks to finish

os.system("mv posts/*.html dist/")
