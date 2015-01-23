import os
import urllib
import shutil
import json
import time
from datetime import datetime
from amaztv.config import django_path, amaztv_app_name, solr_host, solr_path, solr_core


json_folder = "{0}/static/json".format(amaztv_app_name)
json_history_folder = "{0}/static/json/history".format(amaztv_app_name)
json_removed_folder = "{0}/static/json/removed".format(amaztv_app_name)
post_solr = "{0}exampledocs".format(solr_path)
solr_core_path = "{0}{1}dist/solr-core-4.10.2.jar".format(django_path, solr_path)


def clear_solr():
    urllib.urlopen("{0}{1}update?stream.body=<delete><query>*:*</query></delete>&commit=true".format(solr_host, solr_core))


def index_json_solr(json_file):
    print django_path
    print "java -classpath {0} -Dauto org.apache.solr.util.SimplePostTool {1}".format(solr_core_path, json_file)
    os.system("java -classpath {0} -Dauto org.apache.solr.util.SimplePostTool {1}".format(solr_core_path, json_file))


def remove_json_from_solr(obj):
    print "fuck"
    class_name = obj.__class__.__name__
    if class_name == 'Posts':
        #post_id = obj.id
        post_id = obj.post_number
        json_file_name = "{0}.json".format(post_id)
        if os.path.isfile("{0}/{1}".format(json_folder, json_file_name)):
            shutil.copyfile("{0}/{1}".format(json_folder, json_file_name), "{0}/{1}__{2}.json".format(json_removed_folder, post_id, time.strftime("%d_%m_%Y__%H_%M_%S")))
            os.remove("{0}/{1}".format(json_folder, json_file_name))
            urllib.urlopen('{0}update?stream.body=<delete><query>id:{1}</query></delete>&commit=true'.format(solr_host, post_id))
        else:
            print 'WARNING: The {0}/{1} file does not exists.'.format(json_folder, json_file_name)
        #remove data as well
        os.remove("{0}{1}".format(django_path, obj.thumbnail.name))
        os.remove("{0}{1}".format(django_path, obj.img_link.name))


def create_json(post_id, post_title, post_pub_date, post_category, post_thumbnail, post_sourceUrl, post_description, post_embed_link, post_img_link, post_tags):
    json_file_name = "{0}.json".format(post_id)
    if os.path.isfile("{0}/{1}".format(json_folder, json_file_name)):
        shutil.copyfile("{0}/{1}".format(json_folder, json_file_name), "{0}/{1}__{2}.json".format(json_history_folder, post_id, time.strftime("%d_%m_%Y__%H_%M_%S")))
    with open("{0}/{1}".format(json_folder, json_file_name), 'w') as json_file:
        json_file.write(json.dumps([{
                                    "id" : str(post_id),
                                    "title" : post_title,
                                    "pub_date": str(post_pub_date.strftime('%Y-%m-%dT%H:%M:%SZ')),
                                    "category" : post_category,
                                    "thumbnail" : "static/data/{0}".format(post_thumbnail),
                                    "sourceUrl" : post_sourceUrl,
                                    "description" : post_description,
                                    "embed_link" : post_embed_link,
                                    "img_link" : str(post_img_link),
                                    "tags" : [tag.replace(' ','') for tag in post_tags.split(',')]
                                    }]))
    json_file.close()
    index_json_solr("{0}/{1}".format(json_folder, json_file_name))


def get_admin_form(obj):
    class_name = obj.__class__.__name__
    if class_name == 'Posts':
        #post_id = obj.id
        post_number = obj.post_number
        post_title = obj.title
        post_pub_date = obj.pub_date
        post_category = obj.category
        post_thumbnail = obj.thumbnail.name.split("/")[-1]
        print post_thumbnail
        post_sourceUrl = obj.sourceUrl
        post_description = obj.description
        post_embed_link = obj.embed_link
        post_img_link = obj.img_link
        post_tags = obj.tags
        create_json(post_number,
                   post_title,
                   post_pub_date,
                   post_category,
                   post_thumbnail,
                   post_sourceUrl,
                   post_description,
                   post_embed_link,
                   post_img_link,
                   post_tags
                   )