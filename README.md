# DRIVEN BY DATA
## Fraud App Detection 

___

## Idea and Implementation
Fraudulent App Detection in the financial sector. Our solution aimed at providing a comprehensive self sufficient software that could detect fraudulent apps both reactively and proactively in areas such as betting, investment, loan fraud, and fantasy sports on the Google Play Store before or even after they could commence operations and harm unsuspecting citizens.

Using Microsoft Azure for compute power, we collected various information from the Google Play Store using a scraper and developed a host of 8 models to detect fraudulent apps, including sentiment analysis, RC analysis, version tracer, description model, developer record analysis, and metric analysis, most of which were based on machine learning and other heuristic algorithms and were trained on data from official sources.


## How To Use
1. Download all the Python Libraries

- google-play-scraper
- difflib
- re
- urllib
- numpy
- cv2
- skimage.metrics
- structural_similarity
- csv handler
- envelope
- path lib
- path
- csv
- language_tool_python
- pandas
- pickle
- timer
- time

2. Run all the files excluding FDriver.ipynb

3. In FDriver :
   Set FROM, PASS & TO using  https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317CAP - max number of items to be sent in the mail.
   Set FIRST = 1 the first time it’s being used, and change it to zero after that.

   Line 30 has been commented and replaced with line 31 as the code takes a really long time to execute
   for real scenarios, line 30 should be uncommented and 31 should be commented
   
   Ignore all warnings as they are expected and dont affect the final output
   incase NotFoundError is displayed during testing, check the app id's properly in the list

   Individual drivers and files can be tested, write the app id's or code under the last code block in that file 
   (first line will be 'if  _ _name _ _ == 'main': ')

4. Run FDriver.ipynb


