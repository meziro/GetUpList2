remote_path = git@
branch = master

MESSAGE = ${1:-"Default Message"}

git add .
git commit -m "${MESSAGE}"
git push origin master
