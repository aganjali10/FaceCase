## AIM
The main purpose behind our project is to unite lost people with their
families, especially during the time of calamities when the percentage of
people separated from their families is comparatively high.
## MOTIVATION
During the time of disasters/ calamities unfortunately a lot of people are
separated from their families and it takes a lot of time and legal procedures
before they meet again with their families.
Also during such conditions, there is an extensive coverage of such events
with numerous cameras by various agencies, thereby giving us a huge
amount of data to exploit into. This data could be used to detect the
missing people and could be further processed to match them with the
missing photo present in the database.
## ALGORITHM
1. The reporter uploads short videos of the calamity recorded by him on
the website with all the relevant details pertaining to the location of
the video.
2. The videos get added to the folder containing all the previously
uploaded videos. At the same time, each video is fragmented into
frames and all the frames belonging to each video is saved to its
corresponding folder.
3. For each video, all the frames are checked for a face. All the frames
which do not contain a face are discarded.
4. Families of missing people file a report with the police, who in turn
uploads the photograph of the missing person on the website with all
the relevant details.
5. For each missing report, the photo is matched with each frame of
each video using facial recognition algorithms.
6. A match with a frame confirms the presence of the missing person in
the area in which the video was taken. Such a match triggers a
notification to the police with the all the details of the uploaded video
including the details of the reporter and the location of the video.

##### FRAMEWORKS USED: 
DJANGO, Bootstrap
##### LANGUAGES USED: 
Python, Javascript, CSS, HTML
##### ALGORITHMS: 
Facial recognition algorithms

#### How to run?
Install the following libraries
<ol>
<li>Django
<li>face-recognition
<li>imutils
<li>matplotlib
<li>numpy
<li>opencv-python
<li>glob
</ol>
Open your command prompt and run the following commands:
<ol>
<li>python manage.py migrate
<li>python manage.py makemigrations
<li>python manage.py migrate
<li>python manage.py runserver
</ol>
This will start the server at 127.0.0.1:8000. Open it in your browser.
<p>
<ul>
<li>On the home page, click on the "CLICK HERE TO UPLOAD THE VIDEO" link.
<li>This will redirect you to a page where you can upload the video from the "foruploadingpurposes" folder. Type your location too and click Upload.
<li>After that, sign yourself up and log in.
<li>This will redirect you to the homepage, where you need to click on the "POLICE! UPLOAD DETAILS OF A LOST KID" link.
<li>This will redirect you to a page where you can upload the image from the "foruploadingpurposes" folder. Type other details too and click "Find the missing person".
<li>This will redirect you to the result page with the message that the person was found in the location that you typed because the person in the image is there in the video.
</ul>
