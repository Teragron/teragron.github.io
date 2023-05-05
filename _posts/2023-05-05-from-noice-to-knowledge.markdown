---
layout: post
title:  "From noise to knowledge"
date:   2023-05-05 03:36:51 +0200
categories: jekyll update
---
<img src="/blog_assets/brain.jfif">


To make AI Systems such as LLM's functional, we pre-train them. Then fine-tune them.
Then apply RLHF to them. All these steps help the model immensly. All these steps serve
as a building block to find the optimal model weights. But one thing, i've
realised we don't do it as often is trying to find the optimal dataset. Even though we
can enable Language models to gain a context via fine-tuning datasets, there is no cookbook
on how we can systematical create and optimize a dataset.

We've probably all seen people, which are so muscular that even their muscles have muscles.
I think we can also apply such a thing to Language models, meaning we can try to optimize 
almost every aspect of a language model by building smaller models to contribute to the models.
For example we can train an unsupervised model, which learns to manipulate the initial dataset 
to minimize the loss of the end-model. Maybe we can even call it Dataset Hyper-Optimization.