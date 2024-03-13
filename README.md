# Waste_detection

Waste has always been a big issue for society requiring constant innovation. The major problem with waste is its categorisation which takes a lot of time to do manually. With the recent technological advancements, digital segregation of waste has seen an upsurge. Computer vision algorithms can now be trained to label an object as a waste with a confidence score (probability). 

Here I have Implemented a state of the art Computer vision model meant for object detection: YOLOv5. I had to first collect waste image data manually and then label them using autodistill. I chose to go with 13 different waste objects, each having more than 50 images and their labelled counterparts. The images were properly augmented and fed into the model for trainig. The best model right now is trained on 200 epochs with a batch size of 16. The data about other parameters used can be found in "config_entity" file. 

The trained model was packaged into an application using Flask and is ready to be deployed on AWS with the help of Docker. 

You can install all the required dependencies with requirements.txt file and then run the app.py file to run the app. The application interface looks like:
(Here we have uploaded image of a banana to detect)

![Screenshot from 2024-03-11 20-01-11](https://github.com/shazam37/Waste_detection/assets/119686545/387b8bf1-c56c-4689-80c4-ed4ec304b932)

You can train the model on your local system by clicking on the button given. You can even run a live camera for waste detection. The interface looks like (You can see a plastic bottle being detected with a probability of 0.8): 

![Screenshot from 2024-03-11 20-03-06](https://github.com/shazam37/Waste_detection/assets/119686545/7c6fbb2f-a67e-4c90-a2bb-5049c270acc3)

Feel free to add more waste objects into your pipeline!
