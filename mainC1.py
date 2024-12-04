from PIL import Image, ImageFilter, ImageEnhance, ImageOps


class ImageFilterLibrary:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
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
        """FER를 사용하여 감정을 분석하고 필터를 적용"""
        pass
