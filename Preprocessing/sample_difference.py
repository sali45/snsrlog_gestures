import pandas as pd


def sample_difference(filename):
    data = pd.read_csv(filename, header=None, names=['timestamp', 'time skipped', 'x', 'y', 'z', 'label']).set_index('timestamp')
    data.assign(dx=data.x.diff(), dy=data.y.diff(), dz=data.z.diff())
    return data


