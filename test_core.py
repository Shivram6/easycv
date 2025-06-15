import cv2
import numpy as np
from easycv.core import draw_box_with_label

def test_draw_box():
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    box = (10, 10, 100, 150)
    result = draw_box_with_label(img, box, label="Test", confidence=0.95)
    assert result is not None
