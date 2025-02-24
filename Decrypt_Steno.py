import cv2

def decrypt_image():
    
    img = cv2.imread("encryptedImage.png")
    if img is None:
        print("Error: Encrypted image not found or unable to load.")
        return

    password = input("Enter passcode for Decryption: ")
    pas = input("Confirm passcode: ")

    if password != pas:
        print("YOU ARE NOT AUTHORIZED.")
        return

    msg_length = int(input("Enter the length of the secret message: "))

    message = ""
    index = 0
    for _ in range(msg_length):
        row = index // img.shape[1]
        col = index % img.shape[1]
        channel = index % 3  

        if row >= img.shape[0]:
            print("Error: Message length exceeds image capacity.")
            return

        message += chr(img[row, col, channel])
        index += 1

    print("Decrypted message:", message)

if __name__ == "__main__":
    decrypt_image()