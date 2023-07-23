import click
from markdown_to_zhihu_article import convert
import re
import pyperclip
import urllib
import os
import json
import shlex


@click.command()
@click.option("-m", "--md", type=click.STRING, help="markdown path", required=True)
def main(md):
    content = open(md, 'r').read()
    html = convert.convert(content)

    print("Copy addupdate request as curl in chrome and press enter:")
    input()

    curl = pyperclip.paste()
    new_command = ''
    for line in curl.split('\n'):
        if '--data-raw' in line:
            content = ' '.join(line.strip().split(' ')[1:-1])
            obj = json.loads(content[1:-1])

            obj['content'] = html
            new_json = json.dumps(obj)

            new_command += f'  --data-raw {shlex.quote(new_json)}'
        else:
            new_command += line + '\n'

    print("I'm going to execute:")
    print(new_command)

    print('Press enter to execute the command:')
    input()
    os.system(new_command)


main()
