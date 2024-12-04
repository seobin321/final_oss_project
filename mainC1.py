from PIL import Image


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
    
