# models.py: Contains GMF, MLP, and the main NeuMF_Temporal class definitions.
import torch
import torch.nn as nn


# --- 1. GMF Component ---
class GMF(nn.Module):
    def __init__(self, num_users, num_items, embed_dim):
        super(GMF, self).__init__()
        # TODO: Define user and item embeddings and element-wise product logic
        pass

    def forward(self, user_input, item_input):
        # TODO: Implement GMF forward pass
        return None


# --- 2. MLP Component ---
class MLP(nn.Module):
    def __init__(self, num_users, num_items, embed_dim, mlp_layer_sizes):
        super(MLP, self).__init__()
        # TODO: Define user/item embeddings, concatenation, and MLP layers
        pass

    def forward(self, user_input, item_input):
        # TODO: Implement MLP forward pass
        return None


# --- 3. NeuMF Temporal (Main Model) ---
class NeuMF_Temporal(nn.Module):
    def __init__(
        self,
        num_users,
        num_items,
        gmf_embed_dim,
        mlp_embed_dim,
        mlp_layer_sizes,
        time_feature_dim=1,
    ):
        super(NeuMF_Temporal, self).__init__()
        # TODO: Initialize GMF and MLP components
        # TODO: Define the final prediction layer with fusion_input_size = GMF_dim + MLP_last_dim + time_feature_dim
        pass

    def forward(self, user_input, item_input, time_input=None):
        # TODO: Implement combined forward pass and temporal feature fusion
        return None
