from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from fer import FER
import cv2


class ImageFilterLibrary:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.cv_image = cv2.imread(image_path)
        self.filters = {
            "blur": self.apply_blur, #블러 효과
            "sharpen": self.apply_sharpen, #샤픈 효과
            "brighten": self.apply_brighten, #밝게
            "darken": self.apply_darken, #어둡게
        }

    def apply_blur(self, intensity=1):
        """블러 필터 강도 적용"""
        return self.image.filter(ImageFilter.GaussianBlur(radius=intensity))

    def apply_sharpen(self, intensity=1):
        """샤프 필터 강도 적용"""
        enhancer = ImageEnhance.Sharpness(self.image)
        return enhancer.enhance(intensity)

    def apply_brighten(self, intensity=1):
        """밝기 필터 강도 적용"""
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(intensity)

    def apply_darken(self, intensity=1):
        """어두운 필터 강도 적용"""
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(1 / intensity)  # 강도에 반비례하여 어두워짐
    
    def save_image(self, save_path, image_to_save=None):
        if image_to_save is None:
            image_to_save = self.image  # 기본적으로 원본 이미지 저장

        image_to_save.save(save_path)
        print(f"Image saved to {save_path}")
        
    def apply_blue_tint(self):
        """파란 계열 필터 적용"""
        return ImageOps.colorize(ImageOps.grayscale(self.image), black="black", white="blue")

    def apply_red_tint(self):
        """붉은 계열 필터 적용"""
        return ImageOps.colorize(ImageOps.grayscale(self.image), black="black", white="red")

    def apply_yellow_tint(self):
        """노란 계열 필터 적용"""
        return ImageOps.colorize(ImageOps.grayscale(self.image), black="black", white="yellow")

    def apply_pink_tint(self):
        """분홍 계열 필터 적용"""
        return ImageOps.colorize(ImageOps.grayscale(self.image), black="black", white="pink")

    def apply_purple_tint(self):
        """보라 계열 필터 적용"""
        return ImageOps.colorize(ImageOps.grayscale(self.image), black="black", white="purple")

    def analyze_and_apply_filter(self):
    """Analyze emotions using FER and apply the corresponding filter."""
    detector = FER(mtcnn=True)

    # 감정 분석 시도
    results = detector.detect_emotions(self.cv_image)
    if not results:
        print("Error: No emotions detected. No faces found in the image.")
        return False

    try:
        # 감정 데이터 추출 및 주요 감정 결정
        dominant_emotions = results[0]["emotions"]
        emotion = max(dominant_emotions, key=dominant_emotions.get)

        # 감정에 따른 필터 매핑
        emotion_to_filter = {
            "happy": "yellow_tint",
            "sad": "blue_tint",
            "angry": "red_tint",
            "neutral": "purple_tint",
            "surprise": "pink_tint",
            "fear": "darken",
        }

        # 주요 감정에 해당하는 필터 이름 가져오기
        filter_name = emotion_to_filter.get(emotion)

        if not filter_name:
            print(f"Error: Unable to find a matching filter for emotion '{emotion}'.")
            return False

        # 필터 적용 및 결과 반환
        print(f"Detected dominant emotion: {emotion}")
        print(f"Applying filter: {filter_name}")
        apply_filter_method = getattr(self, f"apply_{filter_name}", None)

        if not apply_filter_method:
            print(f"Error: Filter method 'apply_{filter_name}' not found.")
            return False

        filtered_image = apply_filter_method()
        print(f"Filter '{filter_name}' applied successfully.")
        return filtered_image

    except KeyError as ke:
        print(f"Error: Missing key in emotion data - {ke}")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
