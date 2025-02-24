import cv2

def encrypt_image():
    
    img = cv2.imread("camera.jpg") 
    if img is None:
        print("Error: Image not found or unable to load.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    index = 0
    for i in range(len(msg)):
        row = index // img.shape[1]
        col = index % img.shape[1]
        channel = index % 3 

        if row >= img.shape[0]:
            print("Error: Message is too long for the image.")
            return

        img[row, col, channel] = ord(msg[i])
        index += 1

    cv2.imwrite("encryptedImage.png", img)  # Use PNG to avoid compression artifacts
    print("Image encrypted and saved as 'encryptedImage.png'.")

if __name__ == "__main__":
    encrypt_image()