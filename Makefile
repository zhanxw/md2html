SOURCE = $(wildcard *.md)
TARGET = $(SOURCE:.md=.html)

.PHONY: check clean

all: $(TARGET)
%.html: %.md
	cat $< |tr '\r' '\n' > tmp.0.html
	pandoc -c "css/hatchddigital.css" -f markdown_github -t html tmp.0.html -s -o tmp.1.html
	python script/appendGA.py tmp.1.html > tmp.2.html
	python script/appendToc.py tmp.2.html > tmp.3.html
	python script/appendMathjax.py tmp.3.html > $@
	-rm tmp.0.html tmp.1.html tmp.2.html tmp.3.html

check: $(TARGET)
	linkchecker $^

clean: $(TARGET)
	rm -f $^
