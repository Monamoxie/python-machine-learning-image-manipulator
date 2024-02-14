# IMAGE RUNNER

Work in progress <br/>
An image manipulator built on
 - Python
 - OpenCV
 - Matplotlib
 - Django (for UI)

 # To use the GUI capabilities of OpenCV with this Docker container:
  1. Install XQuartz (<a href="https://www.xquartz.org/" target="_blank">Download Link</a>)
2. Click on `Preferences` from the Menu bar
3. Vist the root of the cloned project and run `xauth list`
4. Copy the output from the above step
5. Run `echo "<OUTPUT_OF_STEP_3>" | sed -e 's/^..../ffff/' > .docker.xauth`
6. This should create a file  `.docker.xauth`. This file is already mapped and set within the python service
7. Run `xhost +`