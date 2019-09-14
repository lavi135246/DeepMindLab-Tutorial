import deepmind_lab
import numpy as np

def _action(*entries):
    return np.array(entries, dtype=np.intc)

def set_action_id():
    action_id = {
    0: _action(-20, 0, 0, 0, 0, 0, 0), # look_left
    1: _action(20, 0, 0, 0, 0, 0, 0),  # look_right
    2: _action(0, 10, 0, 0, 0, 0, 0),  # look_up
    3: _action(0, -10, 0, 0, 0, 0, 0), # look_down
    4: _action(0, 0, -1, 0, 0, 0, 0),  # strafe_left
    5: _action(0, 0, 1, 0, 0, 0, 0),   # strafe_right
    6: _action(0, 0, 0, 1, 0, 0, 0),   # forward
    7: _action(0, 0, 0, -1, 0, 0, 0),  # backward
    8: _action(0, 0, 0, 0, 1, 0, 0),   # fire
    9: _action(0, 0, 0, 0, 0, 1, 0),   # jump
    10: _action(0, 0, 0, 0, 0, 0, 1)   # crouch
    }
    return action_id


class dmlab_env(object):
    def __init__(self, env_id='seekavoid_arena_01', obs_type=['RGB'],
                 config={'fps': '30', 'width': '80', 'height': '60'},
                 renderer='software'):
        self.env = deepmind_lab.Lab(env_id, obs_type, renderer=renderer, config=config)

        self.obs_type = obs_type[0]
        self.action_id = set_action_id()
        self.action_space = np.arange(len(self.action_id))
        self.observation_space = self.get_observation_space()

        
    def reset(self, seed=None):
        if seed!=None:
            self.env.reset(seed=seed)
        else:
            self.env.reset()        
        observation = self.observations()

        return observation

    
    def observations(self):
        if self.env.is_running():
            return self.env.observations()[self.obs_type]/255.
        else:
            return np.zeros(self.observation_space.shape)


    def step(self, action, num_steps=1):
        if action not in self.action_space:
            raise ValueError('Invalid action: ', action)

        a = self.action_id[action] # convert to real action representation
        reward = self.env.step(a, num_steps=1)
        observation = self.observations()
        done = not self.env.is_running()
        
        return observation, reward, done

    
    def get_action_space(self):
        return self.action_space

    
    def get_observation_space(self):
        if not self.env.is_running():
            #print(self.reset().shape)
            return self.reset()
        else:
            return self.observations()

        
    def get_random_action(self):
        return np.random.choice(self.action_space, 1)[0]
    