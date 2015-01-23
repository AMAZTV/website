from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

import urllib2
import json

from amaztv_app.models import Posts
from amaztv_app.scripts.utilities import better_time_format
from amaztv.config import solr_core, solr_host, host, tags_page


def index(request):
    music_posts = []
    movie_posts = []
    tv_posts = []
    fashion_posts = []
    lifestyle_posts = []

    query = 'select/?indent=on&q=category:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format('music')
    response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
    out = response.read()
    result = json.loads(out)['response']['docs']
    for each in result:
        main_post = {}
        main_post['id'] = each['id']
        main_post['title'] = each['title']
        main_post['thumbnail'] = each['thumbnail']
        main_post['description'] = each['description']
        main_post['embed_links'] = each['embed_link']
        main_post['img_link'] = each['img_link']
        music_posts.append(main_post)

    query = 'select/?indent=on&q=category:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format('movie')
    response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
    out = response.read()
    result = json.loads(out)['response']['docs']
    for each in result:
        main_post = {}
        main_post['id'] = each['id']
        main_post['title'] = each['title']
        main_post['thumbnail'] = each['thumbnail']
        main_post['description'] = each['description']
        main_post['embed_links'] = each['embed_link']
        main_post['img_link'] = each['img_link']
        movie_posts.append(main_post)

    query = 'select/?indent=on&q=category:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format('tv')
    response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
    out = response.read()
    result = json.loads(out)['response']['docs']
    for each in result:
        main_post = {}
        main_post['id'] = each['id']
        main_post['title'] = each['title']
        main_post['thumbnail'] = each['thumbnail']
        main_post['description'] = each['description']
        main_post['embed_links'] = each['embed_link']
        main_post['img_link'] = each['img_link']
        tv_posts.append(main_post)

    query = 'select/?indent=on&q=category:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format('lifestyle')
    response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
    out = response.read()
    result = json.loads(out)['response']['docs']
    for each in result:
        main_post = {}
        main_post['id'] = each['id']
        main_post['title'] = each['title']
        main_post['thumbnail'] = each['thumbnail']
        main_post['description'] = each['description']
        main_post['embed_links'] = each['embed_link']
        main_post['img_link'] = each['img_link']
        lifestyle_posts.append(main_post)

    context = {'host': host,
               "music_posts": music_posts,
               'movie_posts': movie_posts,
               'tv_posts': tv_posts,
               'lifestyle_posts': lifestyle_posts
               }
    return render(request, 'index.html', context)

def category(request, cat):
    if cat.lower() in ['music', 'movie', 'tv', 'fashion', 'lifestyle']:
        query = 'select/?indent=on&q=category:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format(cat)
        response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
        out = response.read()
        result = json.loads(out)['response']['docs']
        posts = []
        for each in result:
            post = {}
            post['id'] = each['id']
            post['title'] = each['title']
            post['pub_date'] = better_time_format(each['pub_date'])
            post['sourceUrl'] = each['sourceUrl']
            post['description'] = each['description']
            post['embed_links'] = each['embed_link']
            post['img_link'] = each['img_link']
            post['tags'] = each['tags']

            posts.append(post)

        context = {'host':host, 'category':cat.title(), 'posts':posts, 'tags_page':tags_page}
    else:
        context = {'host':host, 'error':"The page does not exists"}
    return render(request, 'category.html', context)

def tag(request, tag):
    query = 'select/?indent=on&q=tags:{0}&wt=json&omitHeader=true&sort=pub_date%20desc'.format(tag)
    response = urllib2.urlopen("{0}{1}{2}".format(solr_host, solr_core, query))
    out = response.read()
    result = json.loads(out)['response']['docs']
    tag_posts = []
    for each in result:
        post = {}
        post['title'] = each['title']
        post['pub_date'] = better_time_format(each['pub_date'])
        post['sourceUrl'] = each['sourceUrl']
        post['description'] = each['description']
        post['embed_links'] = each['embed_link']
        post['img_link'] = each['img_link']
        post['tags'] = each['tags']

        tag_posts.append(post)
    context = {'host':host, 'tag':tag, 'tag_posts':tag_posts, 'tags_page':tags_page}
    return render(request, 'tag.html', context)


def aboutus(request):
    context = {'host':host}
    return render(request, 'aboutus.html', context)
