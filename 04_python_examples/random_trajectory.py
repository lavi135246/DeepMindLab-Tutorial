import argparse
import os
from os.path import join

import numpy as np
import imageio as io

from envs import dmlab_env


parser = argparse.ArgumentParser(description='Random Trajectory Generator')
parser.add_argument('--seed', type=int, default=1,
                    help='random seed (default: 1)')
parser.add_argument('--max-episode-length', type=int, default=600,
                    help='maximum episode length (default: 600)')
parser.add_argument('--env-name', default='seekavoid_arena_01',
                    help='environment to train on (default: seekavoid_arena_01)')
parser.add_argument('--save-path', default='trajectory.gif',
                    help='path to save the trajectory')

if __name__ == '__main__':
    
    args = parser.parse_args()
    env = dmlab_env(env_id=args.env_name, obs_type=['RGB_INTERLEAVED'])

    s_record = []

    # random agent
    state = env.reset(seed=args.seed)
    action_space = env.get_action_space()
    s_record.append(state)

    reward_sum = 0
    done = True

    episode_length = 0
    
    # probability distribution of actions
    prob = [0.12, 0.08, 0.1, 0.1, 0.12, 0.08,
            0.15, 0.05, 0.075, 0.075, 0.05]

    while True:
        episode_length +=1
        action = np.random.choice(action_space, 1, p=prob)[0]

        state, reward, done = env.step(action)
        done = done or episode_length >= args.max_episode_length
        reward_sum += reward
        s_record.append(state)
        
        if done:
            #reset
            print('length %03d \t reward %02d ' %(len(s_record), reward_sum))
            s_rec = np.array(s_record) * 255. # s is in [0.0, 1.0]
            s_rec = s_rec.astype(np.uint8)
            io.mimsave(args.save_path, s_rec)
            break