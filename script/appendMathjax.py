from bs4 import BeautifulSoup
import sys
fname = sys.argv[1]
html_doc = open(fname).read()
soup = BeautifulSoup(html_doc)

# check if already have google analytics script
result = [i for i in soup.find_all("script") if str(i).find('mathjax') >= 0]
if len(result) > 0:
    print >> sys.stderr, "already have mathjax script, skipping..."
    print(str(soup))
    sys.exit(0)

## import jquery
new_tag = soup.new_tag("script")
new_tag["type"] = "text/javascript"
new_tag["src"] = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
tag = soup.head
tag.append(new_tag)

print(str(soup))
