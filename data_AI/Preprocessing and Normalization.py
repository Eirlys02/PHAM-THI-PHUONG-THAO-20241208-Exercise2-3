import numpy as np
import torch
from PIL import Image

def preprocess_image(img, desired_size=(224, 224)):
    """
    Preprocess image for PyTorch models:
    1. Resize
    2. Convert to numpy
    3. Scale to [0,1]
    4. Convert to tensor (C,H,W)
    5. Add batch dimension
    """
    img_resized = img.resize(desired_size)
    arr = np.array(img_resized, dtype=np.float32)
    arr /= 255.0
    arr = np.transpose(arr, (2, 0, 1))
    # Convert to Tensor
    tensor = torch.tensor(arr, dtype=torch.float32)
    # Add batch dimension → (1, C, H, W)
    tensor = tensor.unsqueeze(0)
    return tensor
