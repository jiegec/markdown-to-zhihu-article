import markdown
from bs4 import BeautifulSoup
import urllib
import sys


def convert(md):
    html = markdown.markdown(
        md, extensions=['pymdownx.arithmatex', 'pymdownx.superfences'])
    soup = BeautifulSoup(html, features="html.parser")

    # process inline math
    elements = soup.find_all("span", attrs={"class": "arithmatex"})
    for element in elements:
        latex = element.contents[1].contents[0]

        new_img = soup.new_tag("img")
        new_img["eeimg"] = "1"
        encoded = urllib.parse.quote(latex)
        new_img["src"] = "//www.zhihu.com/equation?tex=" + encoded
        new_img["alt"] = encoded
        element.replace_with(new_img)

    # process block math
    elements = soup.find_all("div", attrs={"class": "arithmatex"})
    for element in elements:
        latex = element.contents[1].contents[0]

        new_img = soup.new_tag("img")
        new_img["eeimg"] = "1"
        encoded = urllib.parse.quote(latex)
        new_img["src"] = "//www.zhihu.com/equation?tex=" + encoded
        new_img["alt"] = encoded
        element.replace_with(new_img)

    # process code block
    elements = soup.find_all("pre", attrs={"class": "highlight"})
    for element in elements:
        language = element.contents[0]['class'][0].split('-')[1]
        code = element.contents[0].contents[0]

        new_pre = soup.new_tag("pre")
        new_pre["lang"] = language
        new_pre.string = code

        element.replace_with(new_pre)

    return soup.prettify()


if __name__ == '__main__':
    for file in sys.argv[1:]:
        md = open(file, 'r').read()
        print(convert(md))
