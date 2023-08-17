# cwk-pippa

pip install -r requirements.txt

## Installing ChromeDriver

Download ChromeDriver: First, you'll need to download the ChromeDriver that matches your version of Google Chrome. You can find the ChromeDriver downloads here: https://sites.google.com/chromium.org/driver/downloads

Check Chrome Version: To find the correct version of ChromeDriver, you'll need to know the version of Google Chrome you're using. You can find this by clicking the three dots in the upper right corner of Chrome, then selecting "Help" > "About Google Chrome."

Unzip ChromeDriver: Once downloaded, you'll need to unzip the file. You can do this by double-clicking the downloaded file in Finder.

Move ChromeDriver to a Suitable Location: You can move the unzipped chromedriver file to a directory that's in your system's PATH, such as /usr/local/bin. You can do this using the terminal:

mv /path/to/your/chromedriver /usr/local/bin/chromedriver

Replace /path/to/your/chromedriver with the actual path to the unzipped chromedriver file.

Make ChromeDriver Executable: You may also need to make the chromedriver file executable. You can do this with the following command:

chmod +x /usr/local/bin/chromedriver

After completing these steps, you should be able to use ChromeDriver with Selenium.

## ImportError: failed to find libmagic. Check your installation

On MacOS: brew install libmagic

## pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.

On MacOS: brew install tesseract

## PDF, Image OCR - 한글 인식 문제

On MacOS: brew install tesseract-lang

tesseract --list-langs

kor 가 목록에 보여야 합니다.
