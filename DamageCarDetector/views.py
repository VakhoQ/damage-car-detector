import os
import io
import urllib.request as url
import tensorflow as tf

from django.conf import settings as path
from django.shortcuts import render
from PIL import Image


def hello(request):
    car_status = ""
    img_url =request.GET.get('img');
    fd = url.urlopen(img_url)
    image_data = fd.read()

    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(os.path.join(path.TENSORFLOW_ROOT, "retrained_labels.txt"))]

    # Unpersists graph from file
    with tf.gfile.FastGFile(os.path.join(path.TENSORFLOW_ROOT, "retrained_graph.pb"), 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    damaged = label_lines[top_k[0]]
    damaged_score = predictions[0][top_k[0]]

    good = label_lines[top_k[0]]
    good_score = predictions[0][top_k[0]]

    if damaged_score > good_score:
        return  render(request, "car.html", {"car_status": damaged, "score": damaged_score, 'img':img_url })
    else:
        return  render(request, "car.html", {"car_status": good, "score": good_score, 'img':img_url })

