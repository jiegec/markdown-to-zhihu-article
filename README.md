# markdown-to-zhihu-article

Usage:

1. Clone and enter this repo
2. Run `poetry install`
3. Goto zhihu website, create an new article
4. Open developer tools, locate `draft` http post request, right click, copy as curl
5. Run `poetry run python3 -m markdown_to_zhihu_article.upload --md /path/to/your-markdown`, press enter twice
6. Find updated article online

使用方法：

1. 克隆本仓库，然后进入仓库路径
2. 运行 `poetry install`
3. 在知乎上，新建文章
4. 打开开发者工具，找到 `draft` 的 HTTP POST 请求，右键选择 Copy as cURL
5. 运行 `poetry run python3 -m markdown_to_zhihu_article.upload --md /path/to/your-markdown`，按照提示回车两次
6. 在网页上看到更新后的文章
