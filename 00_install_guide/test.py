import deepmind_lab
from PIL import Image

from os.path import join
import sys


'''
argv1: env_name
argv2: save_path
'''

image_path = './images/'

observations = ['RGBD']
env = deepmind_lab.Lab(sys.argv[1], observations,
                       config={'width': '800',
                               'height': '600'},
                       renderer='software')

env.reset()
obs = env.observations()
#print(obs['RGBD'].shape) 
im = Image.fromarray(obs['RGBD'].transpose(1,2,0))
im.save(sys.argv[2])
