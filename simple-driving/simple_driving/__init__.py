from gymnasium.envs.registration import register
ENV_IDS = []
env_id = 'SimpleDriving-v0'
register(
    id= env_id,
    entry_point='simple_driving.envs:SimpleDrivingEnv',
)
ENV_IDS.append(env_id)