# pic2code
Screenshot of code to actual code


### Checking results

`python3 ocr.py`

### Training

`make training MODEL_NAME=code START_MODEL=eng PSM=7 TESSDATA=/path/to/tessdata`

tessdata must contain START_MODEL trained model, e.g for START_MODEL=eng /path/to/tessdata must contain eng.traineddata

Trained model for english language could be downloaded using following command:

`wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata`
