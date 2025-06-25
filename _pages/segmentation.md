---
layout: page
permalink: /segmentation/
title: Redesigning Upsampling in Decoders with Aligned Feature Aggregation for Semantic Segmentation
authors: ["Qinjie Hu", "Fei Qi", "Kaiwen Fu", "Chengyuan Chang", "Xiaotian Wang", "Kun Liu", "Guangming Shi"]
description: ICME 2025, Nantes, France
---

# Abstract

Hierarchical decoders are widely employed in semantic segmentation architectures, where feature upsampling and fusion are critical at each layer. However, inaccuracies in feature position restoration during upsampling and misalignments in multi-scale feature fusion limit model performance. To address these issues, we propose the Aligned Feature Aggregation Upsampler (AFAU), a novel upsampling module. AFAU consists of two types of Aligned Feature Aggregation Modules (AFAM), which partition feature maps from both the encoder and decoder into multiple aligned patches. By applying attention mechanisms between corresponding patches, AFAM facilitates more effective contextual information fusion. Additionally, AFAM corrects feature position inaccuracies by calculating the similarity between linear embeddings of low-level (query) features and high-level features. This process allows semantic information aggregation guided by fine-grained high-resolution features. We conducted extensive experiments across multiple advanced semantic segmentation frameworks, demonstrating the universality and efficiency of AFAU. Notably, our results indicate that decoders incorporating AFAU significantly outperform SegFormer across all sizes of MiT encoders on the ADE20K and Cityscapes datasets.


# Model Architecture

![Model Architecture](/assets/images/AFAU-Decoder-framework.png){: width="100%"}


# Performance

![Performance vs Complexity](/assets/images/perf-Cityscapes-ADE20k.png){: width="80%"}
