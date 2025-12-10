# config.py: Centralized Hyperparameters

# Data Parameters
# IMPORTANT: Update this path to your actual dataset file (e.g., MovieLens 1M)
DATASET_PATH = "data/ml-1m/ratings.dat"
TEST_RATIO = 0.2
K_NEGATIVES = 4  # NCF standard: 4 negative samples per positive interaction

# Model Parameters
GMF_EMBED_DIM = 8
MLP_EMBED_DIM = 8
# Note: Layer sizes should decrease for MLP: 2*E -> L4 -> L3 -> L2 -> L1
MLP_LAYER_SIZES = [64, 32, 16, 8]
TIME_FEATURE_DIM = 1  # For the single normalized delta_t feature

# Training Parameters
BATCH_SIZE = 256
LEARNING_RATE = 0.001
EPOCHS = 10
EARLY_STOP_PATIENCE = 5

# Evaluation Parameters
TOP_K = [5, 10, 20]

# Ablation Experiments
ABLATION_VARIANTS = [
    "GMF_Baseline",
    "MLP_Baseline",
    "NeuMF_Core",
    "NeuMF_Temporal",
    "NeuMF_No_Negatives",
]
