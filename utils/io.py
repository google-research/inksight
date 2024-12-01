import xml.etree.ElementTree as ET
from .ink import Stroke, Ink
from PIL import Image


def inkml_to_ink(inkml_file):
    """Convert InkML file to Ink object.

    Args:
        inkml_file (str): Path to InkML file

    Returns:
        Ink: Ink object containing strokes
    """
    tree = ET.parse(inkml_file)
    root = tree.getroot()
    inkml_namespace = {"inkml": "http://www.w3.org/2003/InkML"}
    strokes = []

    for trace in root.findall("inkml:trace", inkml_namespace):
        points = trace.text.strip().split()
        stroke_points = []
        for point in points:
            x, y = point.split(",")
            stroke_points.append((float(x), float(y)))
        strokes.append(Stroke(stroke_points))
    return Ink(strokes)


def parse_inkml_annotations(inkml_file):
    """Extract annotations from InkML file.

    Args:
        inkml_file (str): Path to InkML file

    Returns:
        dict: Dictionary of annotation types and values
    """
    tree = ET.parse(inkml_file)
    root = tree.getroot()
    annotations = root.findall(".//{http://www.w3.org/2003/InkML}annotation")

    return {annotation.get("type"): annotation.text for annotation in annotations}


def load_and_pad_img_dir(file_dir, im_size=224):
    """Load and pad image to 224x224 maintaining aspect ratio.

    Args:
        file_dir (str): Path to image file
        im_size (int): Size of padded

    Returns:
        PIL.Image: Padded image
    """
    image = Image.open(file_dir)
    width, height = image.size
    ratio = min(im_size / width, im_size / height)
    image = image.resize((int(width * ratio), int(height * ratio)))
    width, height = image.size

    if height < im_size:
        # Pad top and bottom
        top_padding = (im_size - height) // 2
        padded_image = Image.new("RGB", (width, im_size), (255, 255, 255))
        padded_image.paste(image, (0, top_padding))
    else:
        # Pad left and right
        left_padding = (im_size - width) // 2
        padded_image = Image.new("RGB", (im_size, height), (255, 255, 255))
        padded_image.paste(image, (left_padding, 0))
    return padded_image
