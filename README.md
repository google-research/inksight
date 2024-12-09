<p align="left">
  <img src="figures/cor.svg" alt="Organization Icon" style="max-width: 30%; min-width: 240px; vertical-align: middle; margin: 0 auto;">
</p>

# InkSight: Offline-to-Online Handwriting Conversion by Learning to Read and Write

<p align="center" style="font-size: 16px;">
    <a href="https://scholar.google.com/citations?user=L6rrZxAAAAAJ&hl=en"><strong>Blagoj Mitrevski&dagger;</strong></a> &bull; 
    <a href="https://github.com/arinaruck"><strong>Arina Rak&dagger;</strong></a> &bull; 
    <a href="https://scholar.google.com/citations?user=P02RNa8AAAAJ&hl=en"><strong>Julian Schnitzler&dagger;</strong></a> &bull; 
    <a href="https://scholar.google.com/citations?user=yTNl4IYAAAAJ&hl=en"><strong>Chengkun Li&dagger;</strong></a> &bull; 
    <a href="https://scholar.google.com/citations?user=QZd-fvAAAAAJ&hl=en"><strong>Andrii Maksai&ddagger;</strong></a> &bull; 
    <a href="https://scholar.google.com/citations?hl=en&user=CSHNLDcAAAAJ&view_op=list_works&sortby=pubdate"><strong>Jesse Berent</strong></a> &bull; 
    <a href="https://scholar.google.com/citations?user=n4bdAtIAAAAJ&hl=en"><strong>Claudiu Musat</strong></a>
</p>

<p align="center" style="font-size: 14px; color: #555;">
    <sup>&dagger;</sup> First authors (<a href="https://www.aeaweb.org/journals/policies/random-author-order/search?RandomAuthorsSearch%5Bsearch%5D=NEK4dy3K6mjr">random order</a>) &nbsp;&nbsp;|&nbsp;&nbsp; <sup>&ddagger;</sup> Corresponding author: <a href="mailto:amaksai@google.com">amaksai@google.com</a>
</p>

<p align="center">
  <a href="https://research.google/blog/a-return-to-hand-written-notes-by-learning-to-read-write/">
    <img src="https://img.shields.io/badge/Google_Research_Blog-333333?&logo=google&logoColor=white" alt="Google Research Blog">
  </a>
  <a href="https://arxiv.org/abs/2402.05804">
    <img src="https://img.shields.io/badge/Read_the_Paper-4CAF50?&logo=arxiv&logoColor=white" alt="Read the Paper">
  </a> 
  <a href="https://huggingface.co/spaces/Derendering/Model-Output-Playground">
    <img src="https://img.shields.io/badge/Output_Playground-007acc?&logo=huggingface&logoColor=white" alt="Try Demo on Hugging Face">
  </a> 
    <a href="https://charlieleee.github.io/publication/inksight/">
    <img src="https://img.shields.io/badge/🔗_Project_Page-FFA500?&logo=link&logoColor=white" alt="Project Page">
  </a>
  <a href="https://huggingface.co/datasets/Derendering/InkSight-Derenderings">
    <img src="https://img.shields.io/badge/Dataset-InkSight-40AF40?&logo=huggingface&logoColor=white" alt="Hugging Face Dataset">
  </a>
  <a href="https://githubtocolab.com/google-research/inksight/blob/main/colab.ipynb">
    <img src="https://img.shields.io/badge/Example_Colab-F9AB00?&logo=googlecolab&logoColor=white" alt="Example colab">
  </a>
</p>

---

<p align="center">
  <img src="figures/inksight.gif" alt="Inksight" width="100%">
<br>
  <em>Animated teaser</em>
</p>


## Overview

InkSight is an offline-to-online handwriting conversion system that transforms photos of handwritten text into digital ink through a Vision Transformer (ViT) and mT5 encoder-decoder architecture. By combining reading and writing priors in a multi-task training framework, our models process handwritten content without requiring specialized equipment, handling diverse writing styles and backgrounds. The system supports both word-level and full-page conversion, enabling practical digitization of physical notes into searchable, editable digital formats. In this repository we provide the model weights of Small-p, dataset, and example inference code (listed in the [releases section](#releases)).

<div>
<p align="center">
  <img src="figures/derender_diagram.svg" alt="Derender Diagram" width="100%">
<br>
  <em>InkSight system diagram (<a href="figures/full_diagram.gif">gif version</a>)</em>
</p>

</div>

## Releases
> **:warning: Notice:** Please use TensorFlow and tensorflow-text between version 2.15.0 and 2.17.0. Versions later than 2.17.0 may lead to unexpected behavior. We are currently investigating these issues.


We provide open resources for InkSight public version model. Choose the options that best fit your needs:

- Model weights:
  - Public version [Small-p model for CPU/GPU inference](https://huggingface.co/Derendering/InkSight-Small-p)
  - Public version [Small-p model for TPU inference](https://storage.googleapis.com/derendering_model/small-p-tpu.zip)
- A [dataset](docs/dataset.md) containing subsets of:
  - Model-generated samples in universal `inkML` format
  - Human expert digital ink traces in `npy` format
- [Example inference code](colab.ipynb): Demonstrates both word-level and full-page text inference using free, open-source alternatives to the [Google Cloud Vision Handwriting Text Detection API](https://cloud.google.com/vision/docs/handwriting). The implementation supports [docTR](https://github.com/mindee/doctr) and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). <a href="https://githubtocolab.com/google-research/inksight/blob/main/colab.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
- [Samples](figures/) of model outputs.


## News

- **October 2024**: We release [**Small-p model weights**](https://huggingface.co/Derendering/InkSight-Small-p) and our [**dataset**](https://huggingface.co/datasets/Derendering/InkSight-Derenderings) on Hugging Face.
- **October 2024**: Our work is now featured on the **[Google Research Blog](https://research.google/blog/a-return-to-hand-written-notes-by-learning-to-read-write/)**! 

- **February 2024**: The **[InkSight Demo on Hugging Face](https://huggingface.co/spaces/Derendering/Model-Output-Playground)** is live!


## GPU Inference Environment Setup with Conda
To set up the environment and run the model inference locally on GPU, you can use the following steps:
```bash
# Clone the repository
git clone https://github.com/google-research/inksight.git
cd inksight

# Create and activate conda environment
conda env create -f environment.yml
conda activate inksight
```
If you encounter any issues during setup or running the model, please open an issue with details about your environment and the error message.


## Run Gradio 🤗 Playground Locally

To set up and run the Gradio <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a> Playground locally, you can use the following steps:

```bash
# Clone the huggingface space
git clone https://huggingface.co/spaces/Derendering/Model-Output-Playground

# Install the dependencies
cd Model-Output-Playground
pip install -r requirements.txt
```

Then you can run the following command to interact with the playground:
```bash
# Run the Gradio Playground
python app.py
```


## Licenses
![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg) 
The code in this repository is released under the [Apache 2 license](https://github.com/google-research/google-research/blob/master/LICENSE).



## Disclaimer

*Please note: This is not an officially supported Google product.*



## Citation

If you find our code or dataset useful for your research and applications, please cite using BibTeX:

```bibtex
@article{mitrevski2024inksight,
  title={InkSight: Offline-to-Online Handwriting Conversion by Learning to Read and Write},
  author={Mitrevski, Blagoj and Rak, Arina and Schnitzler, Julian and Li, Chengkun and Maksai, Andrii and Berent, Jesse and Musat, Claudiu},
  journal={arXiv preprint arXiv:2402.05804},
  year={2024}
}
```
