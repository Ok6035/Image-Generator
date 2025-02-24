import torch
from torchvision.utils import save_image
from PIL import Image

# Assuming you have a pre-trained GAN model saved as 'gan.pth'
MODEL_PATH = 'model/gan.pth'

class GANModel:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        model = torch.load(MODEL_PATH)
        model.eval()
        return model

    def generate_image(self):
        noise = torch.randn((1, 100))  # Example noise vector
        with torch.no_grad():
            generated_image = self.model(noise)
        return generated_image.squeeze().permute(1, 2, 0).cpu().numpy()

gan_model = GANModel()

def generate_image():
    image_array = gan_model.generate_image()
    img = Image.fromarray((image_array * 255).astype('uint8'))
    return img
