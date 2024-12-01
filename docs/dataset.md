# InkSight Dataset Documentation
<a href="https://huggingface.co/datasets/Derendering/InkSight-Derenderings">
    <img src="https://img.shields.io/badge/Dataset-InkSight-40AF40?&logo=huggingface&logoColor=white" alt="Hugging Face Dataset">
</a>

## Dataset Overview

The dataset includes model outputs from three variants (Small-p, Small-i, Large-i) on three public datasets:

- [IMGUR5K](https://github.com/facebookresearch/IMGUR5K-Handwriting-Dataset)
- [IAM](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)
- [HierText](https://github.com/google-research-datasets/hiertext?tab=readme-ov-file)

Each sample includes:

1. Original input image
2. Generated digital ink in `.inkml` format
3. Results from three different inference modes


## Download the Dataset

Download the dataset with the following command:

```bash
git clone https://huggingface.co/datasets/Derendering/InkSight-Derenderings
```


## Dataset Structure and Format

The structure of the dataset is as follows:
```
├── <Dataset>                      # IMGUR5K, IAM, or HierText
│   └── images_sample/            # Original input images
│       ├── <exampleId>.png
│       └── ...
├── <model>_<dataset>_inkml/      # Model outputs (e.g. large-i_IMGUR5K_inkml)
│   ├── d+t/                      # Derender with Text mode
│   ├── vanilla/                  # Vanilla Derendering mode
│   └── r+d/                      # Recognize and Derender mode
```
where `<exampleId>` is the unique identifier of the image and `<model>` is one of `small-p`, `small-i`, or `large-i`, and `<dataset>` is one of `IMGUR5K`, `IAM`, or `HierText`.

The digital ink traces are stored in `.inkml` format, which is a standard format for representing digital ink data. The format includes the following annotation fields:

- **application**: 
  - Value: "InkSight"
  - Indicates the model/system that generated the ink

- **sourceDataset**: 
  - Values: "HierText", "IMGUR5K", or "IAM"
  - Original dataset where the input image comes from

- **inferenceMode**:
  - Values: "Derender with Text", "Vanilla", or "Recognize and Derender"
  - Indicates which model inference mode was used:
    - "Derender with Text": Uses OCR text for guidance
    - "Vanilla": Direct derendering without text input
    - "Recognize and Derender": Combines recognition and derendering

- **exampleId**:
  - Example: "0d44ea16f816055c_76"
  - Unique identifier matching the original dataset

- **textField**:
   - Contains the text content
   - For "Derender with Text" mode: OCR text used for guidance
   - For "Recognize and Derender": Recognized text from the model

## Inference Modes

- **d+t (Derender with Text):** Uses OCR ([Google Cloud Vision API](https://cloud.google.com/vision/docs/samples/vision-document-text-tutorial?utm_source=chatgpt.com)) to recognize text in the image before derendering and feed it as guidance to the model.
- **vanilla:** Direct derendering without text guidance.
- **r+d (Recognize and Derender):** Asks the model to recognize text in the image and then derender the text.

## Usage

Examples are provided in the [colab notebook](colab.ipynb). The utils functions are organized in the `utils` folder. We also provide an example script to visualize samples from the dataset with different inference modes, use the demo script `visualize_dataset.py`:

```bash
# Show 3 samples from HierText dataset using Small-i model
python visualize_dataset.py --dataset HierText --num_samples 3 --model Small-i
```

## Citation

If you use this dataset, please cite:

```bibtex
@article{mitrevski2024inksight,
  title={InkSight: Offline-to-Online Handwriting Conversion by Learning to Read and Write},
  author={Mitrevski, Blagoj and Rak, Arina and Schnitzler, Julian and Li, Chengkun and Maksai, Andrii and Berent, Jesse and Musat, Claudiu},
  journal={arXiv preprint arXiv:2402.05804},
  year={2024}
}
```