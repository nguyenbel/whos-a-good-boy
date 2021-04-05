<img src = 'https://www.newstatesman.com/sites/default/files/styles/cropped_article_image/public/blogs_2016/10/untitled_design_21_.png?itok=Pgb5QJg3' width = '750'>

<center>
    Image from: <a href = 'https://www.newstatesman.com/science-tech/internet/2016/10/why-are-smol-puppers-cuter-little-dogs'>https://www.newstatesman.com/science-tech/internet/2016/10/why-are-smol-puppers-cuter-little-dogs</a>
</center>

## Using Image Processing and Transferring Learning to Classify Dog Breeds
The idea for this project is to classify different dog breeds through machine learning. A lot of dog breeds can look somewhat similar, especially to the human eye, so can a convolutional neural network do better at identifying various types of dogs?

Given an image, the Dog Classifier can:
- Identify the type of dog breed
- Tell the dog they are a good dog

### Data Sources:

http://vision.stanford.edu/aditya86/ImageNetDogs/main.html

### Background Information:

The data comes from Stanford (also known as Stanford Dogs Dataset). The data has 20,580 images of dogs and 120 different classifications of dog breeds (at least 150 images of each dog breed).

I used transfer learning to incorporate the models of Inception ResNet V2 and VGG16 to perform image classification of the dataset and compared which model performed better (based off accuracy of their predictions). For both models, the optimizer ADAM with a learning rate of 0.0001 were used. Both models were trained, validated, and tested on the same set of images and each model pre-processed the images in the training set (using their respective pre-processing technique from their module.)

### Results:
Although Inception ResNet V2 had a better accuracy score better during training and validation, the model was overfit and only guessed 4 breeds: Tibetan Mastiff, English Foxhound, Great Pyrenees, and Saluki. As we can see from the confusion matrix generated from the Inception ResNet V2, there are two very distinct lines where Tibetan Mastiff (dark red line) and English Foxhound (blue line) are, showing that these two predictions came up quite often.

<center>
<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/incep_Confusion_Matrix.jpg?raw=true" width = '600' height = '600'>
</center>

Tibetan Mastiff was predicted 3186 times, English Foxhound was predicted 928 times and Saluki and Great Pyrenees were only predicted 3 and 5 times, respectively. The Inception RresNet V2 model had a 0.006 test accuracy, which was worse than guessing the dog breed randomly and getting it correctly (approximately 0.008).
</br>
</br>
</br>
On the other hand, the VGG16 model was not too accurate during training and validation, but on the test set, the model had a test accuracy of 0.353. As we can see from the confusion matrix of the VGG16 model, the model was able to accurately predict each breed approximately 10-20 times (out of approximately 30 pictures in each category).

<center>
<img src = 'https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/vgg16_Confusion_Matrix.jpg?raw=true' width = '600' height = '600'>
</center>

Note: The diagonal line shows the true positives, or the images that the model predicted correctly and were actually correct.

After running both models on my own pictures, there is a noticeable difference between the two. Out of four pictures, Inception ResNet V2 guessed the dog(s) in the picture was a Tibetan Mastiff and the last one was predicted to be an English Foxhound (see below):


<div class="images">
<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/inception_predict_Thor.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/inception_predict_loaf.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/inception_predict_pugmas.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/inception_predict_Thor3.jpg?raw=true">

</div>

</br>
</br>

When these images were read into the VGG16 model, the model accurately predicted two out of four of the images (the image of the three pugs and the Pembroke Corgi).
<div class="images">
<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/predict_thor.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/predict_loaf.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/predict_pugmas.jpg?raw=true">

<img src="https://github.com/nguyenbel/whos-a-good-boy/blob/master/img/predict_Thor3.jpg?raw=true">

</div>


### Conclusion:
Transfer learning is a powerful tool and extremely useful tool and baseline when building an image processing convolutional neural network. Although the models were not as accurate as I wanted them to be, I believe they still performed well given the task at hand. The biggest take away I had from this project was lighting and angles of images make a difference. If possible, when building a model, make sure to distort images (e.g. change lighting using contrast and brightness, different angles for pictures, etc.) during training so the model can, potentially, have more accurate predictions during testing.

### Future Direction:
- Try different models using transfer learning
- Build a CNN from scracth; see how it compares to the models from transfer learning
- Incorporate more dog breeds as targets
- Differentiate between similar dog breeds (like Siberian Husky and Alaskan Malamute. Will the model be able to detect the difference or, rather, is there a noticeable difference?)
- Detect dog age
- Identify breeds of multiple dogs in one picture (object ddetection)
- Detect different types of animals (cats and humans) and predict which dog breed they most likely resemble

### References:
[1] https://github.com/moonbeam5115/JointAngleMeasurement

[2] https://medium.com/@ksusorokina/image-classification-with-convolutional-neural-networks-496815db12a8

[3] https://machinelearningmastery.com/how-to-use-transfer-learning-when-developing-convolutional-neural-network-models/ 