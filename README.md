# Note - 주의

Don't expect any help from the author, CWK. You're on your own if you choose to accept this Quest.

Tested on MacOS Ventura with Anaconda. Should work on Windows or Linux, if you know how to tweak your environment.

프로젝트 퀘스트를 제안한 대두족장은 어떤 식으로도 도움을 드리지 않습니다. 퀘스트를 수락하는 순간 모든 걸 스스로 해결해야 하는 여러분의 여정입니다.

MacOS Ventura에서 Anaconda (conda) 환경으로 테스트했습니다. 윈도우와 리눅스에서도 환경을 구축할 줄 아는 분이면 실행에 문제가 없어야 합니다.

소울류 해보신 분만 알아들으시겠지만... 나그네 또는 영체 찬스는 여러분만의 피파(ChatGPT4)를 소환하세요. 뭐든 다 해줄 수 있는 친구니까...

# Testing pulic-cwk-pippa 

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
