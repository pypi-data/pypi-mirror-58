import base64
import random
import hashlib as hl
import numpy as np
from PIL import Image, ImageFile
from Crypto.Cipher import AES


ImageFile.LOAD_TRUNCATED_IMAGES = True
SUPPORTED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png']


class Cryptemis():
    def password_processor(self, password):
        seed = int(''.join(str(ord(char)) for char in hl.blake2b(password.encode()).hexdigest()))
        password = list(password)
        random.Random(seed).shuffle(password)
        password = ''.join(password)
        return password

    def aes_key_iv_generator(self, password):
        key = hl.sha3_512(hl.sha1(password.encode()).hexdigest().encode()).hexdigest()[:AES.block_size].encode()
        iv = hl.sha3_512(hl.blake2s(password.encode()).hexdigest().encode()).hexdigest()[:AES.block_size].encode()
        return key, iv

    def aes_cipher_generator(self, key, iv):
        aes_cipher = AES.new(key, AES.MODE_CFB, iv)
        return aes_cipher

    def img_file_to_byte_array(self, img_filename):
        img_array = np.asarray(Image.open(img_filename))
        img_shape = img_array.shape
        img_bytes = img_array.tobytes()
        return img_array, img_bytes, img_shape

    def byte_array_to_img_array(self, byte_array, img_shape):
        return np.uint8(np.reshape(list(byte_array), img_shape))

    def byte_array_to_img(self, byte_array, img_shape):
        img = Image.fromarray(self.byte_array_to_img_array(byte_array, img_shape))
        return img

    def byte_array_to_img_file(self, byte_array, img_shape, out_img_filename):
        self.byte_array_to_img(byte_array, img_shape).save(out_img_filename, 'png')

    def img_file_processor(self, keep_filename, password, img_filename, encrypt, decrypt):
        img_name = img_filename.split('.')[0]
        img_ext = img_filename.split('.')[-1]
        if img_ext not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError(img_ext + ' image format is not supported! Supported image formats: ' + ', '.join(
                SUPPORTED_IMAGE_FORMATS) + '.')
        password = self.password_processor(password)
        key, iv = self.aes_key_iv_generator(password)
        img_array, img_bytes, img_shape = self.img_file_to_byte_array(img_filename)
        if decrypt:
            aes_decipher = self.aes_cipher_generator(key, iv)
            dec_data = aes_decipher.decrypt(img_bytes)
            if not keep_filename:
                aes_decipher = self.aes_cipher_generator(key, iv)
                enc_img_name = base64.urlsafe_b64decode(img_name)
                dec_img_name = aes_decipher.decrypt(enc_img_name).decode()
                self.byte_array_to_img_file(dec_data, img_shape, dec_img_name + '.' + img_ext)
            else:
                self.byte_array_to_img_file(dec_data, img_shape, img_name + '.' + img_ext)
        elif encrypt:
            aes_cipher = self.aes_cipher_generator(key, iv)
            enc_data = aes_cipher.encrypt(img_bytes)
            if not keep_filename:
                aes_cipher = self.aes_cipher_generator(key, iv)
                enc_img_name = aes_cipher.encrypt(img_name.encode())
                base64_img_name = base64.urlsafe_b64encode(enc_img_name).decode()
                self.byte_array_to_img_file(enc_data, img_shape, base64_img_name + '.' + img_ext)
            else:
                self.byte_array_to_img_file(enc_data, img_shape, img_name + '.' + img_ext)
