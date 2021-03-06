import os
import subprocess
import config
import datetime

USE_GPU = config.USE_GPU

GAUS_KERNEL = 3
GAUS_STD = 1

OPTIMIZER = "Adam"

# Path
LOG_PATH = "./log/pretrain/"
DATA_PATH = "/cluster/project/infk/hilliges/lectures/mp19/project2/"

NUM_EPOCHS = 1
BATCH_SIZE = 32
WORKERS = 0
LEARNING_RATE = 0.001
WEIGHT_DECAY = 0
NOISE_STD = 1e-5  # Set to 0 to disable noising
LOG_ITER_FREQ = 10
SAVE_ITER_FREQ = 2000
PRINT_BATCH_FREQ = 500
BASE_WEIGHTS = None

BRANCH = subprocess.check_output(["git", "rev-parse", "--abbrev-ref",
                                  "HEAD"]).strip().decode("utf-8")
NAME = "%s-%s-%s-%s" % ("PRETRAIN", BRANCH, OPTIMIZER, NUM_EPOCHS)

if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

LOG_NAME = os.path.join(LOG_PATH,
                        datetime.datetime.now().strftime('%d-%m--%H-%M'))
