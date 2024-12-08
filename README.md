# Image Filter Library
Image Filter Library는 다양한 이미지 필터를 적용하고 FER(Facial Expression Recognition)을 기반으로 감정에 따라 필터를 적용하는 Python 라이브러리입니다.

# Features
Custom Filters:
사용자가 선택 가능한 필터: blur, sharpen, brighten, darken.
필터 강도 조정 가능 (e.g., intensity 값 설정).

Emotion-Based Filtering:
FER(표정 인식) 기반 감정 분석 후 자동 필터 적용:
예: 행복 → 노란색 필터, 슬픔 → 파란색 필터.

Easy Image Saving:
필터링된 이미지를 사용자 지정 디렉토리에 저장.

Unicode Path Support:
한글 또는 특수 문자가 포함된 경로에서도 정상 작동.

# Installation
아래 명령어를 통해 라이브러리를 설치하세요:
pip install image-filter-library

# Usage

### Example: 사용자 정의 필터 적용
```python
from image_filter_library import ImageFilterLibrary

# Load the image
image_path = "path/to/your/image.jpg"
library = ImageFilterLibrary(image_path)

# Apply Blur filter
filtered_image = library.apply_filter("blur", intensity=2)
filtered_image.show()
```


# Requirements
이 라이브러리는 다음 Python 패키지에 의존합니다:

numpy
opencv-python-headless
Pillow
fer
moviepy


# Contributing
라이브러리 개선 또는 제안 사항이 있으시면 언제든지 Issues를 통해 알려주세요. Pull Requests도 환영합니다!

# License
MIT 라이선스에 따라 배포됩니다. 자세한 내용은 LICENSE 파일을 확인하세요.
