# pic2code
Screenshot of code to actual code

Ubuntu 20 with latest Python, pip, cv2, tesseract

### Training

Checkout https://github.com/tesseract-ocr/tesstrain

`make training MODEL_NAME=code START_MODEL=eng PSM=7 TESSDATA=/path/to/tessdata`

tessdata must contain START_MODEL trained model, e.g for START_MODEL=eng /path/to/tessdata must contain eng.traineddata

Trained model for english language could be downloaded using following command:

`wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata`

To start training we need to have at least 10 ground-truth samples located in `tesstrainRepo/data/code-ground-truth`

after training we need to use newly trained model, to do so we can copy it to tessract data folder, or overwrite TESSDATA_PREFIX=/custom/tessdata

on ubuntu this worked for me:

`sudo cp code.traineddata /usr/share/tesseract-ocr/4.00/tessdata/code.traineddata`:

### Checking results

`python3 ocr.py`

or 

`TESSDATA_PREFIX=/custom/tessdata python3 ocr.py`
