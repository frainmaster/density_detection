#!/usr/bin/python3.7

#----------------------------------------------
#--- Author         : Irfan Ahmad
#--- Mail           : irfanibnuahmad@gmail.com
#--- Date           : 21st July 2020
#----------------------------------------------

# Object detection imports
from utils import backbone
from api import density_detection_api as dd_api

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_0.75_depth_300x300_coco14_sync_2018_07_03', 'mscoco_label_map.pbtxt') # 26 ms
# detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt') # 30 ms
# detection_graph, category_index = backbone.set_model('faster_rcnn_inception_v2_coco_2018_01_28', 'mscoco_label_map.pbtxt') # 58 ms

input_video_path = './input/'

##########################################################
##########################################################

# input_video = 'ktm_serdang.mp4'
# start_point = (100, 100)
# end_point = (600, 350)

# input_video = 'kl_sentral_4.mp4'
# start_point = (127, 149)
# end_point = (572, 355)

input_video = 'lrt_bandaraya.mp4'
start_point = (149, 198)
end_point = (308, 394)
# start_point = (0, 0)
# end_point = (0, 0)

##########################################################
##########################################################

dd_api.density_detection(input_video_path + input_video, detection_graph, category_index, start_point, end_point)
