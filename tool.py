import pytesseract
from PIL import Image
import cv2
import speech_recognition as sr

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# List of harmful ingredients to check for
harmful_ingredients = [
    'Phthalates', 'Paraben', 'Sulfate', 'Fragrance', 'Triclosan', 'Synthetic colors', 'Toluene', 'Lead', 'Formaldehyde',
    # (trimmed for brevity)
]

# Function to capture an image using the webcam
def capture_image():
    cap = cv2.VideoCapture(0)
    print("Press 'Space' to take a photo or 'Esc' to cancel...")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Capture Image", frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC pressed
            print("Capture cancelled.")
            cap.release()
            cv2.destroyAllWindows()
            return None
        elif key % 256 == 32:  # Space pressed
            img_path = "captured_image.png"
            cv2.imwrite(img_path, frame)
            print(f"Image captured and saved as {img_path}")
            cap.release()
            cv2.destroyAllWindows()
            return img_path

# Function to listen to speech and transcribe it
def listen_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")

        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"Transcription: {text}")

            harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in text.lower()]
            if harmful_found:
                print("Harmful ingredients found:", harmful_found)
            else:
                print("No harmful ingredients found.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")
        except Exception as e:
            print(f"Error: {str(e)}")

# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip().lower()
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

# Main program
if __name__ == "__main__":
    choice = input("1. Manual Input\n2. Upload an Image\n3. Webcam Capture\n4. Call out the ingredients\nChoose input method: ")

    if choice == '1':
        ingredients_text = input("Enter the ingredient list: ").lower()
        harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
        print("Harmful ingredients found:", harmful_found if harmful_found else "None")

    elif choice == '2':
        image_path = input("Enter the path to the image file: ")
        ingredients_text = extract_text_from_image(image_path)
        harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
        print("Harmful ingredients found:", harmful_found if harmful_found else "None")

    elif choice == '3':
        image_path = capture_image()
        if image_path:
            ingredients_text = extract_text_from_image(image_path)
            harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
            print("Harmful ingredients found:", harmful_found if harmful_found else "None")

    elif choice == '4':
        listen_and_transcribe()

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
