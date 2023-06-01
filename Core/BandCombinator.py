import numpy as np
import rasterio


class BandCombinator:
    B01_index = 1  # Ultra Blue (Coastal and Aerosol)
    B02_index = 2  # Blue
    B03_index = 3  # Green
    B04_index = 4  # Red
    B05_index = 5  # Visible and Near Infrared (VNIR)
    B06_index = 6  # Visible and Near Infrared (VNIR)
    B07_index = 7  # Visible and Near Infrared (VNIR)
    B08_index = 8  # Visible and Near Infrared (VNIR)
    B8A_index = 9  # Visible and Near Infrared (VNIR)
    B09_index = 10  # Short Wave Infrared (SWIR)
    B11_index = 11  # Short Wave Infrared (SWIR)
    B12_index = 12  # Short Wave Infrared (SWIR)

    def combine(self, image_path, combination_name):
        with rasterio.open(image_path) as src:
            # Display the masked image

            B01 = src.read(self.B01_index)
            B02 = src.read(self.B02_index)
            B03 = src.read(self.B03_index)
            B04 = src.read(self.B04_index)
            B05 = src.read(self.B05_index)
            B06 = src.read(self.B06_index)
            B07 = src.read(self.B07_index)
            B08 = src.read(self.B08_index)
            B8A = src.read(self.B8A_index)
            B09 = src.read(self.B09_index)
            B11 = src.read(self.B11_index)
            B12 = src.read(self.B12_index)

            # Piksel değerlerini 2.5 ile çarpıp parlaklığı artır
            B01 = np.multiply(B01, 2.5)
            B02 = np.multiply(B02, 2.5)
            B03 = np.multiply(B03, 2.5)
            B04 = np.multiply(B04, 2.5)
            B05 = np.multiply(B05, 2.5)
            B06 = np.multiply(B06, 2.5)
            B07 = np.multiply(B07, 2.5)
            B08 = np.multiply(B08, 2.5)
            B8A = np.multiply(B8A, 2.5)
            B09 = np.multiply(B09, 2.5)
            B11 = np.multiply(B11, 2.5)
            B12 = np.multiply(B12, 2.5)

            # Piksel değerlerini 0-255 aralığına sınırla

            B01 = np.clip(B01, 0, 255)
            B02 = np.clip(B02, 0, 255)
            B03 = np.clip(B03, 0, 255)
            B04 = np.clip(B04, 0, 255)
            B05 = np.clip(B05, 0, 255)
            B06 = np.clip(B06, 0, 255)
            B07 = np.clip(B07, 0, 255)
            B08 = np.clip(B08, 0, 255)
            B8A = np.clip(B8A, 0, 255)
            B09 = np.clip(B09, 0, 255)
            B11 = np.clip(B11, 0, 255)
            B12 = np.clip(B12, 0, 255)

            if (combination_name == "Natural_Color"):
                result = self.NaturalColor(B04, B03, B02)

            elif (combination_name == "False_Color"):
                result = self.FalseColor(B08, B04, B03)

            elif (combination_name == "SWIR"):
                result = self.SWIR(B12, B8A, B04)

            elif (combination_name == "Agriculture"):
                result = self.Agriculture(B11, B04, B02)

            elif (combination_name == "Geology"):
                result = self.Geology(B12, B11, B02)

            elif (combination_name == "Bathimetric"):
                result = self.Bathimetric(B04, B03, B01)

            elif (combination_name == "RGB (8,6,4)"):
                result = self.RGB864(B08, B06, B04)

            elif (combination_name == "RGB (8,5,4)"):
                result = self.RGB854(B08, B05, B04)

            elif (combination_name == "RGB (8,11,4)"):
                result = self.RGB8114(B08, B11, B04)

            elif (combination_name == "RGB (8,11,12)"):
                result = self.RGB81112(B08, B11, B12)

            elif (combination_name == "RGB (11,8,3)"):
                result = self.RGB1183(B11, B08, B03)

            elif (combination_name == "Vegetation_Index"):
                result = self.VegetationIndex(B08, B04)

            elif (combination_name == "Moisture_Index"):
                result = self.MoistureIndex(B8A, B11)

            return result

    def NaturalColor(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def FalseColor(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def SWIR(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def Agriculture(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def Geology(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def Bathimetric(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def RGB864(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def RGB854(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def RGB8114(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def RGB81112(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def RGB1183(self, Band1, Band2, Band3):
        return np.dstack((Band1, Band2, Band3))

    def VegetationIndex(self, Band1, Band2):
        np.seterr(divide='ignore', invalid='ignore')
        result = np.true_divide(Band1 - Band2, Band1 + Band2)
        result[result == np.inf] = 0
        return np.nan_to_num(result)

    def MoistureIndex(self, Band1, Band2):
        np.seterr(divide='ignore', invalid='ignore')
        result = np.true_divide(Band1 - Band2, Band1 + Band2)
        result[result == np.inf] = 0
        return np.nan_to_num(result)
