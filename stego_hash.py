import numpy as np
from PIL import Image
import hashlib

def password_to_hash_bits(password: str) -> str:
    # Compute the SHA-256 hash (hexadecimal string)
    # Converting to SHA-256 and then to binary makes it almost impossible for a third party to extract your password. 
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # Convert the hexadecimal hash to binary string (each hex digit -> 4 bits)
    binary_hash = ''.join(format(int(c, 16), '04b') for c in password_hash)
    return binary_hash

def embed_bits_in_image(image_path: str, bits: str, output_path: str) -> None:
    image = Image.open(image_path)
    image_data = np.array(image)
    # Flatten the image array for simpler processing
    flat_data = image_data.flatten()
    
    # Ensure the image has enough capacity
    if len(bits) > len(flat_data):
        raise ValueError("The provided image is too small to encode the data.")

    # Modify the LSBs of the image data with the message bits
    for i in range(len(bits)):
        # Zero out the LSB and then OR with the bit
        flat_data[i] = (flat_data[i] & ~1) | int(bits[i])
    
    # Reshape back to the original image dimensions and save
    modified_data = flat_data.reshape(image_data.shape)
    stego_image = Image.fromarray(modified_data.astype('uint8'), image.mode)
    stego_image.save(output_path)
    print(f"Password hash embedded successfully in {output_path}")

# Example usage:
if __name__ == "__main__":
    input_image = "input.png"      # Path to the original image file
    output_image = "encoded.png"   # Path where the encoded image will be saved
    password = "your-password-here"   # The user-provided password
    
    bits_to_embed = password_to_hash_bits(password)
    embed_bits_in_image(input_image, bits_to_embed, output_image)
