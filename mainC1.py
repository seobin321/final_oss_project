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
        pass

    def apply_sharpen(self, intensity=1):
        """샤프 필터 강도 적용"""
        pass

    def apply_brighten(self, intensity=1):
        """밝기 필터 강도 적용"""
        pass

    def apply_darken(self, intensity=1):
        """어두운 필터 강도 적용"""
        pass
    
    def save_image(self, save_path, image_to_save=None):
        """저장"""
        pass
    