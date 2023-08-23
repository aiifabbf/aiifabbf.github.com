jupyter nbconvert jupyter/*.ipynb --to html
mkdir -p _build/html/jupyter/
mv jupyter/*.html _build/html/jupyter/
