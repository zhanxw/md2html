# Note of Markdown Syntax

This is a short list of Markdown syntax, taken from Mou.

## Standard Markdown

**Links and Email**

Inline:

    An [example](http://url.com/ "Title")

Reference-style labels (titles are optional):

    An [example][id]. Then, anywhere
    else in the doc, define the link:
    [id]: http://example.com/  "Title"


Email:

    An email <example@example.com> link.

**Images**

Inline (titles are optional):

    ![alt text](/path/img.jpg "Title")

Reference-style:

    ![alt text][id]
    [id]: /url/to/img.jpg "Title"


**Hard Line Breaks**

End a line with two or more spaces:

    Roses are red,   
    Violets are blue.
    
## Extra Syntax

Fenced Code Blocks

Start with a line containing 3 or more backtick \`characters, and ends with the first line with the same number of backtick \`:

```
Fenced code blocks are like Stardard
Markdown’s regular code blocks, except that
they’re not indented and instead rely on a
start and end fence lines to delimit the code
block.
```

**Tables**

A simple table looks like this:

	First Header | Second Header | Third Header
	------------ | ------------- | ------------
	Content Cell | Content Cell  | Content Cell
	Content Cell | Content Cell  | Content Cell
If you wish, you can add a leading and tailing pipe to each line of the table:

	| First Header | Second Header | Third Header |
	| ------------ | ------------- | ------------ |
	| Content Cell | Content Cell  | Content Cell |
	| Content Cell | Content Cell  | Content Cell |

Specify alignement for each column by adding colons to separator lines:

	First Header | Second Header | Third Header
	:----------- | :-----------: | -----------:
	Left         | Center        | Right
	Left         | Center        | Right

**Anchor**

You can also add an anchor for an element such as Headers, then you can link to this anchor anywhere, when you click that link in the Preview view, it'll auto scroll to the place of the destination anchor.

For example below is a normal h2 Header:

    ## This is an example


Now we add an anchor for it, here we use the name "anchor1" for the anchor, of course you can use any name you want.

    ## [This is an example](id:anchor1)

If you want to link to this anchor, simply write like this:

    Click this [link](#anchor1) in the Preview view will auto scroll to the place of the destination anchor.

## Math Syntax

Inline math use `\(`  and `\)`, for example, \(A = \pi r^2\)

Math block use `$$` and `$$` :

$$ V = \frac{4}{3} \pi r^3 $$
