jupyter nbconvert --template basic jupyter/*.ipynb
mkdir -p _build/html/jupyter/
mv jupyter/*.html _build/html/jupyter/
