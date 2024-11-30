# InkSight Dataset Documentation
<a href="https://huggingface.co/datasets/Derendering/InkSight-Derenderings">
    <img src="https://img.shields.io/badge/Dataset-InkSight-40AF40?&logo=huggingface&logoColor=white" alt="Hugging Face Dataset">
</a>

This repository contains supplementary materials for the InkSight project, including model-generated digital inks and corresponding input images from various public datasets.

## Download the Dataset

Download the dataset with the following command:

```bash
git clone https://huggingface.co/datasets/Derendering/InkSight-Derenderings
```

## Dataset Overview

The dataset includes model outputs from three variants (Small-p, Small-i, Large-i) on three public datasets:

- [IMGUR5K](https://github.com/facebookresearch/IMGUR5K-Handwriting-Dataset)
- [IAM](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)
- [HierText](https://github.com/google-research-datasets/hiertext?tab=readme-ov-file)

Each sample includes:

1. Original input image
2. Generated digital ink in .inkml format
3. Results from three different inference modes


## Directory Structure

```
├── <Dataset>                      # IMGUR5K, IAM, or HierText
│   └── images_sample/            # Original input images
│       ├── <hash>.png
│       └── ...
├── <model>_<dataset>_inkml/      # Model outputs (e.g. large-i_IMGUR5K_inkml)
│   ├── d+t/                      # Derender with Text mode
│   ├── vanilla/                  # Vanilla Derendering mode
│   └── r+d/                      # Recognize and Derender mode
```

## Inference Modes

- **d+t (Derender with Text):** Uses OCR ([Google Cloud Vision API](https://cloud.google.com/vision/docs/samples/vision-document-text-tutorial?utm_source=chatgpt.com)) to recognize text in the image before derendering and feed it as guidance to the model.
- **vanilla:** Direct derendering without text guidance.
- **r+d (Recognize and Derender):** Asks the model to recognize text in the image and then derender the text.