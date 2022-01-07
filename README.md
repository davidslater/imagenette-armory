# Overview

One-off Armory scenario leveraging ImageNette as a stand-in for ImageNet

# Scenario

The scenario takes the ImageNette dataset (10 label subset) and maps the labels to that of ImageNet (1000 labels).
It assumes that the underlying models map from [0, 1] image inputs to a 1000-length output vector

# Json

The json are set to skip the attack and run the benign on the first 10 samples. Using this, I get 60% accuracy with resnet18 and 80% accuracy with resnet50.
```
armory run resnet18_imagenette.json
...
2022-01-07 00:32:09 9f0488d892d2 armory.utils.metrics[7] INFO Average categorical_accuracy on benign test examples relative to ground truth labels: 60.00%
```

```
armory run restnet50_imagenette.json
...
2022-01-07 00:31:14 2afa23b2b1db armory.utils.metrics[8] INFO Average categorical_accuracy on benign test examples relative to ground truth labels: 80.00%
```

NOTE: Use Armory version 0.14.2

# To Submit

Modify either `.json` file as needed and submit using the standard `armory-sender` process.
