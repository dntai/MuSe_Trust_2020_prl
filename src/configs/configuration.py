########################################################################################################################
# EDIT THESE
########################################################################################################################

BASE_FOLDER = "/mnt/hvthong/XProject/MuSe/dataset/"
PARTITION_PROPOSAL_PATH = BASE_FOLDER + "metadata" + "/partition.csv"

########################################################################################################################
# The below are as they are
########################################################################################################################

TASK_FOLDER = dict()
TF_RECORDS_FOLDER = dict()
OUTPUT_FOLDER = dict()
map_tasks = {'task1': 'c1_muse_wild', 'task2': 'c2_muse_topic', 'task3': 'c3_muse_trust'}

for task in ["c1_muse_wild",
             "c2_muse_topic",
             "c3_muse_trust"]:
    TASK_FOLDER[task] = BASE_FOLDER + task
    TF_RECORDS_FOLDER[task] = BASE_FOLDER + task + "/tfrecords"
    OUTPUT_FOLDER[task] = BASE_FOLDER + task + "/output"

SEQ_LENGTH = 50

FEATURE_NUM = dict()

FEATURE_NUM["compare"] = 6373
FEATURE_NUM["lld"] = 130

FEATURE_NUM["au"] = 35
FEATURE_NUM["deepspectrum"] = 4096
FEATURE_NUM["egemaps"] = 88
FEATURE_NUM["fasttext"] = 300
FEATURE_NUM["gaze"] = 288
FEATURE_NUM["gocar"] = 350
FEATURE_NUM["landmarks_2d"] = 136
FEATURE_NUM["landmarks_3d"] = 204
FEATURE_NUM["openpose"] = 54
FEATURE_NUM["pdm"] = 40
FEATURE_NUM["pose"] = 6
FEATURE_NUM["vggface"] = 512
FEATURE_NUM["xception"] = 2048

FEATURE_NAMES = ["au",
                 "deepspectrum",
                 "egemaps",
                 "fasttext",
                 "gaze",
                 "gocar",
                 "landmarks_2d",
                 "landmarks_3d",
                 # "lld",
                 "openpose",
                 "pdm",
                 "pose",
                 "vggface",
                 "xception"]
