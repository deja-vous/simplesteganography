import numpy as np
from PIL import Image

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def embed_message(image_path, message, output_path):
    # Append a delimiter to mark the end of the message
    delimiter = "#####"
    full_message = message + delimiter
    message_bits = text_to_bits(full_message)
    n_bits = len(message_bits)
    
    # Open the image and get its data as a numpy array
    image = Image.open(image_path)
    image_data = np.array(image)
    
    # Calculate total capacity (each color channel can store one bit)
    rows, cols, channels = image_data.shape
    total_capacity = rows * cols * channels
    if n_bits > total_capacity:
        raise ValueError("Message is too large to embed in this image.")
    
    # Flatten the image data to simplify bit replacement
    flat_data = image_data.flatten()
    
    # Embed the message bits into the LSB of each byte in the image data
    for i in range(n_bits):
        flat_data[i] = (flat_data[i] & 254) | int(message_bits[i])
    
    # Reshape the modified data back to the original image dimensions
    modified_image_data = flat_data.reshape(image_data.shape)
    new_image = Image.fromarray(modified_image_data.astype('uint8'), image.mode)
    new_image.save(output_path)
    
# Wrote a small extraction program as well. Uncomment if you need to verify if your image has been encrypted or not. 
#def extract_message(image_path):
    # Open the image and convert to numpy array
 #   image = Image.open(image_path)
 #   image_data = np.array(image)
 #   flat_data = image_data.flatten()
    
    # Retrieve the bits from the LSBs
 #   bits = "".join([str(pixel & 1) for pixel in flat_data])
 #   chars = []
    
    # Convert bits back to characters (8 bits per character)
 #   for i in range(0, len(bits), 8):
 #       byte = bits[i:i+8]
 #       if len(byte) < 8:
 #           continue
 #       char = chr(int(byte, 2))
 #       chars.append(char)
        # Stop at delimiter if found
 #       if ''.join(chars[-5:]) == "#####":
 #           break
    # Return the message without the delimiter
 #   return ''.join(chars[:-5]) 

# Example usage:
if __name__ == "__main__":
    input_image = "input.png"      # Path to the original image
    output_image = "output.png"    # Path for the stego image
    secret_message = "agrace74"

print(f"Message embedded successfully in {output_image}.")
    
    #embed_message(input_image, secret_message, output_image)
    #extracted = extract_message(output_image)
    #print("Extracted message:", extracted)
