import hashlib
import random


def get_file_hash(filepath):
    """Returns a hash value of a file

    # Arguments
    filepath: Absolute filepath

    # Returns
    md5 hexdigest of file content
    """
    algorithm = hashlib.md5()
    with open(filepath, 'rb') as f:
        file_content = f.read()
        algorithm.update(file_content)

    return algorithm.hexdigest()


def apply_seed(seed=None):
    """Applies a global random seed to the application state.

    In particular, the method seeds Python's random module and numpy, tensorflow and pytorch packages if available.

    Arguments:
    seed: Int|None, the random seed. Use None to unset seeding
    """
    if not isinstance(seed, int):
        return False

    random.seed(seed)

    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import tensorflow as tf
        try:
            tf.random.set_seed(seed)
        except AttributeError:
            tf.compat.v1.set_random_seed(seed)

    except ImportError:
        pass

    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass

    return True


def generate_seed(random_state=None):
    """Generates a seed from a random state

    # Arguments
    random_state: Random state or None

    Returns:
    int32 seed value
    """
    if random_state is None or isinstance(random_state, int):
        random_state = random.Random(random_state)

    return random_state.randint(0, 2**31 - 1)
