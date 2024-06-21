#Imports
import cv2 as cv
import face_recognition as fr
import os
from deepface import DeepFace

#Capturing Image:
def CaptureImage():
    cam = cv.VideoCapture(0)
    result, image = cam.read()

    if result:

        cv.imshow("Sup", image)
        print("Press any key to take the image!")
        cv.waitKey(0)
        cv.imwrite("Images/FirstImage.jpg", image)

    else:
        print("No image detected. Please! try again")
    cam.release()
#Face Recognition
def FaceRecognition():
    image = fr.load_image_file("Images/FirstImage.jpg")
    faceLocation = fr.face_locations(image)
    if not os.path.exists("DetectedFaces"):
        os.makedirs("DetectedFaces")

    top, right, bottom, left = faceLocation[0]
    face_image = image[top:bottom, left:right]
    cv.imwrite(f"DetectedFaces/face.jpg", face_image)

# Emotion Analyser
def EmotionRecognizer():
    faceAnalysis = DeepFace.analyze(img_path = "DetectedFaces/face.jpg")
    dominantEmotion = faceAnalysis[0]["dominant_emotion"]
    if dominantEmotion == "neutral":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://limitlessminds.com/neutral-thinking-is-limitless/?v=e2ae933451f4#:~:text=It%27s%20not%20positive.,behave%20as%20how%20you%20think.")
    elif dominantEmotion == "happy":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://positivepsychology.com/happiness/#:~:text=Happiness%20is%20linked%20to%20lower,of%20the%20stress%20hormone%20cortisol.")
    elif dominantEmotion == "angry":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://www.apa.org/topics/anger#:~:text=Anger%20is%20an%20emotion%20characterized,excessive%20anger%20can%20cause%20problems.")
    elif dominantEmotion == "disgust":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3189352/#:~:text=Disgust%20is%20not%20solely%20represented,or%20psychological%20deterioration%20%5B24%5D%2C")
    elif dominantEmotion == "fear":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://www.verywellmind.com/the-psychology-of-fear-2671696")
    elif dominantEmotion == "sad":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://www.psychologytoday.com/intl/blog/compassion-matters/201507/the-value-sadness")
    elif dominantEmotion == "surpise":
        print(f"Your analysed emotion is: {dominantEmotion}. Here is a link to a website to tell you more about this emotion: https://www.psychologs.com/the-psychology-behind-surprises/")

#Main Control
def Main():
    CaptureImage()
    FaceRecognition()
    EmotionRecognizer()

Main()
