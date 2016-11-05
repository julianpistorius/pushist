cat header.md > docs/history.md
tail -n 20 history.txt >> docs/history.md
cat footer.md >> docs/history.md
#mmd docs/history.md
python render.py
