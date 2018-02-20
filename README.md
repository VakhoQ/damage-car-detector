# damage-car-detector
Using machine learning (deep learning),  detects whether car is damaged or not. 


# how to run application
In order to check if a car is damaged or not run the application with the following command: 
`python3 manage.py runserver`

You should see the following message after running the comand:

`Starting development server at http://127.0.0.1:8000/ `


# how to test 
if application is  runing, open browser and copy the followig URL

`http://127.0.0.1:8000/DamageCarDetector/?img=${IMAGE_URL}`

Instead of ${IMAGE_URL} please pass HTTP url of image. For example:

`http://127.0.0.1:8000/DamageCarDetector/?img=https://example.com/image.jpg`

Results should be something like that:

![not damaged](https://serving.photos.photobox.com/31841523401cdeff503e2db22774fee2aba5a9184cb7d3705c8d5ade6a95e2ecc9c4c097.jpg)
![not damaged](https://serving.photos.photobox.com/49042668c16cdbb3d68b3eac5baddbdeea7ba48d97526fc517cd492081124dff5d1bde9b.jpg)



# Tensorboard information about training and validation
![thensorboard](https://serving.photos.photobox.com/47059690d7f0d1026e7a085567b839106c854a7818a045b83dd69529ce520768b41ffe2d.jpg)
