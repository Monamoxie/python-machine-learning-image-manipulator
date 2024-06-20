# IMAGE RUNNER

Work in progress (WIP) <br/>
An image manipulator built on
 - Python
 - Fast AI
 - OpenCV
 - Matplotlib
 - Django (for UI & Data Management)

## TRAINING THE MODEL LOCALLY
- The training of each model will be handled through the CLI. You can find this in the `management/commands` directory of each app.
-  For instance: running `python manage.py cat_dog_trainer` will run pre-train the model and save it to the mlmodels directory. 
- This is to be called once, usually during the first setup. 
- Subsequent requests from the web ui will be routed to the trained model via a service layer. 

## USING CLOUD BASED GPUS
- Due to how resource intensive these operations can be, and depending on your hardware, it is always advisable to use cloud platforms like Google Colab, Sage Maker etc. 
- Each CLI class has a private method in it called `__execute()`
- You should copy the content of that method, as well as all necessary imports at the top of the class, and run them in your cloud platform. 
- You should endeavour to change the path of the exported path. For instance, instead of setting your path as this:  `model_path = os.path.join("image", "mldmodels", "cat_dog_model.pkl")`, you can choose to set it as this: `model_path = '/content/model.pkl'` 
- If using Google colab, you could choose to connect to your drive and mount the file to it, then export the trained model when completed. 
- All trained models should be placed in the `mlmodels` directory of the respective apps.  


 # To use the GUI capabilities of OpenCV with this Docker container:
1. Install XQuartz (<a href="https://www.xquartz.org/" target="_blank">Download Link</a>)
2. Click on `Preferences` from the Menu bar and toggle on `Allow connections from network clients`
3. Vist the root of the cloned project and run `xauth list`
4. Copy the output from the above step
5. Run `echo "<OUTPUT_OF_STEP_3>" | sed -e 's/^..../ffff/' > .docker.xauth`
6. This should create a file  `.docker.xauth`. This file is already mapped and set within the python service
7. Run `xhost +`