import os
import sys
import warnings

# To ignore the deprecation warning from scikit-image
warnings.filterwarnings("ignore",category=UserWarning)

#############################################################
# PARAMS
#############################################################

PROCESS_LRW_DIR = os.path.dirname(os.path.realpath(__file__))

if PROCESS_LRW_DIR not in sys.path:
    sys.path.append(PROCESS_LRW_DIR)

LRW_DIR = os.path.normpath(os.path.join(PROCESS_LRW_DIR, ".."))

if LRW_DIR not in sys.path:
    sys.path.append(LRW_DIR)

LRW_DATA_DIR = '/n/fs/scratch/jiaqis/LRS3-TED/'
LRW_SAVE_DIR = '/n/fs/scratch/jiaqis/LRS3-TED-Extracted/'

#############################################################
# CONSTANTS
#############################################################

SHAPE_PREDICTOR_PATH = os.path.realpath(os.path.join(PROCESS_LRW_DIR, '../dlib/shape_predictor_68_face_landmarks.dat'))

FACIAL_LANDMARKS_IDXS = dict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 35)),
    ("jaw", (0, 17))
])

VIDEO_FPS = 25
VIDEO_FRAMES_PER_WORD = 30

MOUTH_SHAPE_FROM = FACIAL_LANDMARKS_IDXS["mouth"][0]
MOUTH_SHAPE_TO = FACIAL_LANDMARKS_IDXS["mouth"][1]

MOUTH_TO_FACE_RATIO = 0.65

#############################################################
# LOAD VOCAB LIST
#############################################################


# def load_lrw_vocab_list(GRID_VOCAB_LIST_FILE):
#     lrw_vocab = []
#     with open(LRW_VOCAB_LIST_FILE) as f:
#         for line in f:
#             word = line.rstrip().split()[-1]
#             lrw_vocab.append(word)
#     return lrw_vocab

# LRW_VOCAB_LIST_FILE = os.path.join(LRW_DIR, 'lrw_vocabulary.txt')

# LRW_VOCAB = load_lrw_vocab_list(LRW_VOCAB_LIST_FILE)

#############################################################
# EXAMPLES
#############################################################

# Examples
# videoFile = 'media/voletiv/01D2BF774AC76280/Datasets/LRW/lipread_mp4/ABOUT/test/ABOUT_00001.mp4'
# wordFileName = '/home/voletiv/Datasets/LRW/lipread_mp4/ABOUT/test/ABOUT_00001.txt'
# wordFileName = '/media/voletiv/01D2BF774AC76280/Datasets/LRW/lipread_mp4/ABOUT/test/ABOUT_00001.txt'
# wordFileName = '/shared/magnetar/datasets/LipReading/LRW/lipread_mp4/ABOUT/test/ABOUT_00001.txt'
