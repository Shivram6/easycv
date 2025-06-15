import cv2

def draw_box_with_label(
    image,
    box,
    label=None,
    confidence=None,
    color=(0, 255, 0),
    thickness=2,
    font_scale=0.5,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    text_color=(255, 255, 255),
    text_bg_color=None,
    format="xywh"
):
    if format == "xyxy":
        x1, y1, x2, y2 = box
        x, y, w, h = x1, y1, x2 - x1, y2 - y1
    else:
        x, y, w, h = box

    cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

    if label:
        if confidence is not None:
            if confidence <= 1.0:
                confidence *= 100
            label = f"{label}: {confidence:.1f}%"

        (text_w, text_h), _ = cv2.getTextSize(label, font, font_scale, 1)
        text_x, text_y = x, y - 10 if y - 10 > 10 else y + text_h + 5

        if text_bg_color:
            cv2.rectangle(image, (text_x, text_y - text_h), 
                          (text_x + text_w, text_y), text_bg_color, -1)

        cv2.putText(image, label, (text_x, text_y), font, font_scale, text_color, 1)

    return image
