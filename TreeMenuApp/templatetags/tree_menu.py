from django import template
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from ..models import *

register = template.Library()


def findNode(tree, leaf):
    # print(tree)
    if tree.get(leaf['parent__title']) == None:
        for node in tree:
            if tree[node] != {}:
                findNode(tree[node], leaf)
    else:
        tree[leaf['parent__title']].update({leaf['title']: {}})


# def TreeMenu(title):
class TreeMenu(template.Node):
    def __init__(self, title):
        self.title = title.replace('"', '')

    def render(self, context):
        nodes = FooModel.objects.all().values('title', 'parent__title')
        tree = {}
        for node in nodes:
            if node['parent__title'] == None and node['title'].lower() == self.title.lower():
                tree.setdefault(node['title'], {})
        for node in nodes:
            if node['parent__title'] != None:
                findNode(tree, node)
        t = template.loader.get_template('tree.html')
        html = t.render({'tree': tree})
        return html


def draw_menu(parser, token):
    print(token)
    tag_name, title = token.split_contents()
    return TreeMenu(title)


register.tag('draw_menu', draw_menu)
