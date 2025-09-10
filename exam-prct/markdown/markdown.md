
# What is Markdown?
Markdown is a lightweight plain-text markup language designed to be easy to read and write while converting cleanly to HTML. It’s used for README files, docs, blog posts, notes, and more. There’s no single universal “Markdown” — there’s a formal spec called CommonMark

# Basic inline formatting
*italic* or _italic_
**bold** or __bold__

`inline code`
1. # Text as link
 [Link text](https://example.com "optional title")
## Example
[Google][1]
[1]: (https://google.com "Search")

2. # Image as link 
[![Alt text](image.png "Tooltip text")](https://example.com) <br>
Steps: 
1. [![Google Logo]
2. (https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)]
3. (https://www.google.com "Go to Google") <br>
4. Remove numbers and join them

# Example
[![Google Logo](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)](https://www.google.com "Go to Google") <br>
👉 What happens: <br>
The Google logo appears. <br>
Hover = tooltip: “Go to Google”. <br>
Click = goes to https://www.google.com

# Social media links (common in READMEs)
[![X](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white "Follow me on Twitter")](https://x.com/MussaratShams) <br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white "Connect on LinkedIn")](https://www.linkedin.com/in/mussarat-shamsher-7618a6380/)
<br>
Steps: 
1. [![X]
2. (https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white "Follow me on Twitter")]
3. (https://x.com/MussaratShams)
# Local image:
[![My Profile](ms.png "Click to see my portfolio")](https://portfolio-mussarat-shamsher.vercel.app/) <br> <br>
Steps: 
1. [![My Profile] 
2. (ms.png "Click to see my portfolio")]
3. (https://portfolio-mussarat-shamsher.vercel.app/)

# Paragraph & line break
Separate paragraphs with a blank line.
Hard line break: end a line with two spaces, or use html 'br'tag<br>

 # Block-level delements
 Headings
 # h1
 ## h2
 ### h3

 # Block Quotes
 "writing text in block qoutes"

# Lists
 => unordered:
 - item 1
 + item 4
 => ordered
 1. first item
 2. second item

# Task lists(Github Style)
- [ ] todo item
- [ X ] done item

# Horizontal rule
----   minus
***     asteric
____     underscore
 
# Code Blocks
```python
def greet(name):
    return f"Hello, {name}" 
```
```typescript
function sum(a: number, b: number): number {
    return a + b;
    }   
```
# Tables
Simple pipe tables (common in GFM and many renderers):
| Name   | Role    | Score |
|:-------|:-------:|------:|
| Alice  | Dev     |   98  |
| Bob    | Designer|   88  |
# Footnotes, definition lists, math, and other extensions
Footnotes: Here is a sentence with a footnote.[^1]
[^1]: This is the footnote text.
 
Definition lists: 
Apple
: A sweet red or green fruit.
Banana
: A long yellow fruit.
: Often eaten as a snack.
# Math: 
Einstein’s famous equation: $E = mc^2$

# Strikethrough
use two tildes (~ ) before & after the text.
This is ~~deleted text~~.
