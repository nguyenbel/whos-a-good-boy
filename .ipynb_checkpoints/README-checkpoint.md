<img src = 'https://www.newstatesman.com/sites/default/files/styles/cropped_article_image/public/blogs_2016/10/untitled_design_21_.png?itok=Pgb5QJg3'>

Image from: https://www.newstatesman.com/science-tech/internet/2016/10/why-are-smol-puppers-cuter-little-dogs

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


### Conclusion:


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