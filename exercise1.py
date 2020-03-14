import gym
env = gym.make('CartPole-v0')
#########################################################

init_obs = env.reset()

def get_action(obs):
    """Return observation"""
    return env.action_space.sample()

def run_episode(render=False):
    done = False
    obs = env.reset
    while not done:
        if(render):
            env.render()
        action = get_actions(obs)
        obs, reward, done, _ = env.step(ation)

run_episode(render=True)

env.close()

########################################################

# for _ in range(200):
#     env.render()
#     observation, reward, done, info = env.step(env.action_space.sample())
# env.close()

#########################################################

# print('action space = ', env.action_space)
# print('observation space = ', env.observation_space)
# print('observation space high = ', env.observation_space.high)
# print('observation space low = ', env.observation_space.low)

# env = gym.make('Pendulum-v0')
# print('action space = ', env.action_space)
# print('observation space = ', env.observation_space)
# print('observation space high = ', env.observation_space.high)
# print('observation space low = ', env.observation_space.low)

# env = gym.make('MountainCar-v0')
# print('action space = ', env.action_space)
# print('observation space = ', env.observation_space)
# print('observation space high = ', env.observation_space.high)
# print('observation space low = ', env.observation_space.low)

################################################################