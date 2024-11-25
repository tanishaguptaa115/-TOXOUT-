import pytesseract
from PIL import Image
import cv2
import speech_recognition as sr

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

# List of harmful ingredients to check for
harmful_ingredients = [
    'Phthalates', 'Paraben', 'Sulfate', 'Fragrance', 'Triclosan', 'Synthetic colors', 'Toluene', 'Lead', 'Formaldehyde',
    'Polyethylene glycol', 'PEG', 'Talc', 'Alcohol', 'Hydroquinone', 'Mineral oil', 'Petrolatum', 'PABA', 'benzophenone',
    'oxybenzone', 'Diethanolamine', 'DEA', 'ethoxycinnmate', 'homosalate', 'sodium lauryl sulfate', 'sodium laureth sulfate',
    'benzene', 'phenylmethane', 'toluol', 'methylbenzene', 'Formalin', 'formaldehyde', 'glyoxal', 'bronopol', 'paraffin wax', 'FD&C', 'D&C',
    'Ethanol', 'methanol', 'denatured alcohol', 'ethyl alcohol', 'Methylisothiazolinone', 'Ethyl Acrylate', 'Ethyl Methacrylate',
    'Methyl Methacrylate', 'methylparaben', 'propylparaben', 'butylparaben', 'ethylparaben', 'Coconut Oil', 'SPF', 'dibutyl phthalate',
    'parfum', 'propylene glycol', 'PG', 'butylene glycol', 'BG', 'Siloxane', 'Octinoxate', 'Butylated Hydroxytoluene', 'BHT', 'Perfluorochemicals', 'PFCs',
    'Per- and poly-fluoroalkyl substances', 'PFAs', 'Polytetrafluoroethylene', 'PTFE', 'sodium lauryl ether sulfate', 'parabens', 'sulfates',
    'butylated hydroxytoluene', 'butylated hydroxyanisole', 'triethanolamine', 'ethanolamines', 'TEA', 'MEA', 'DEA', 'PEG-4'
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

    # Set up the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for speech...")

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source)
                print("Recognizing...")

                # Transcribe speech using Google's speech recognition
                text = recognizer.recognize_google(audio)
                print(f"Transcription: {text}")

                # Check for harmful ingredients in the transcribed text
                harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in text.lower()]

                if harmful_found:
                    print("Harmful ingredients found:", harmful_found)
                else:
                    print("No harmful ingredients found.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error: {str(e)}")

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip().lower()

# Main program
if __name__ == "__main__":
    choice = input("1. Manual Input\n2. Upload an Image\n3. Webcam Capture\n4. Call out the ingredients\nChoose input method: ")

    if choice == '1':
        # Manual input of ingredients
        ingredients_text = input("Enter the ingredient list: ").lower()
        harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
        if harmful_found:
            print("Harmful ingredients found:", harmful_found)
        else:
            print("No harmful ingredients found.")

    elif choice == '2':
        # Upload an image and extract ingredients
        image_path = input("Enter the path to the image file: ")
        try:
            ingredients_text = extract_text_from_image(image_path)
            print("Extracted Ingredients Text:\n", ingredients_text)
            harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
            if harmful_found:
                print("Harmful ingredients found:", harmful_found)
            else:
                print("No harmful ingredients found.")
        except Exception as e:
            print("Error processing image:", e)

    elif choice == '3':
        # Capture an image using webcam
        image_path = capture_image()
        if image_path:
            try:
                ingredients_text = extract_text_from_image(image_path)
                print("Extracted Ingredients Text:\n", ingredients_text)
                harmful_found = [ingredient for ingredient in harmful_ingredients if ingredient.lower() in ingredients_text]
                if harmful_found:
                    print("Harmful ingredients found:", harmful_found)
                else:
                    print("No harmful ingredients found.")
            except Exception as e:
                print("Error processing captured image:", e)
        else:
            print("No image captured.")

    elif choice == '4':
        # Call out the ingredients using speech recognition
        listen_and_transcribe()

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")