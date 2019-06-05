# Martinez Parameters
TWOD = {
    'LINEAR_SIZE': 1024,
    'NUM_BLOCKS': 2,
    'p': 0.5,
    'IN_SIZE': 16 * 2,
    'OUT_SIZE': 17 * 3
}
THREED = {
    'LINEAR_SIZE': 1024,
    'NUM_BLOCKS': 2,
    'p': 0.5,
    'IN_SIZE': 17 * 3,
    'OUT_SIZE': 16 * 2
}

# HRNet Parameters
PRETRAINED = None
TARGET_TYPE = 'gaussian'
INIT_WEIGHTS = True
IMAGE_SIZE = [256, 256]
HEATMAP_SIZE = [64, 64]
NUM_JOINTS = 16
SIGMA = 2
EXTRA = {
    'PRETRAINED_LAYERS': [
        'conv1', 'bn1', 'conv2', 'bn2', 'layer1', 'transition1', 'stage2',
        'transition2', 'stage3', 'transition3', 'stage4'
    ],
    'FINAL_CONV_KERNEL':
    1,
    'STAGE2': {
        'NUM_MODULES': 1,
        'NUM_BRANCHES': 2,
        'NUM_BLOCKS': [4, 4],
        'NUM_CHANNELS': [32, 64],
        'BLOCK': 'BASIC',
        'FUSE_METHOD': 'SUM',
    },
    'STAGE3': {
        'NUM_MODULES': 4,
        'NUM_BRANCHES': 3,
        'NUM_BLOCKS': [4, 4, 4],
        'NUM_CHANNELS': [32, 64, 128],
        'BLOCK': 'BASIC',
        'FUSE_METHOD': 'SUM',
    },
    'STAGE4': {
        'NUM_MODULES': 3,
        'NUM_BRANCHES': 4,
        'NUM_BLOCKS': [4, 4, 4, 4],
        'NUM_CHANNELS': [32, 64, 128, 256],
        'BLOCK': 'BASIC',
        'FUSE_METHOD': 'SUM',
    }
}
