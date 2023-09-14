import cv2
from keras.models import load_model
import numpy as np
import random

def countdown_timer(seconds):
    print("Show your hand in...")
    while seconds > 0:
        cv2.waitKey(1000)  # Wait for 1 second (1000ms)
        print(seconds)
        seconds -= 1       #To create countdown

def get_prediction(model, cap):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    print(prediction)               #Helps visualise numpy array
    return prediction

def get_winner(comp_choice, user_choice):
    choices = ['rock', 'paper', 'scissors']
    print(f"Computer chose {choices[comp_choice]}.")        #Returns the index of the np.argmax(prediction) 
    print(f"You chose {choices[user_choice]}.")             #Returns the index of the random.randint(0, 2) 

    if comp_choice == user_choice:
        return "It's a tie!"
    elif (comp_choice == 0 and user_choice == 2) or (comp_choice == 1 and user_choice == 0) or (comp_choice == 2 and user_choice == 1):
        return "Computer wins!"
    else:
        return "You win!"

def play_game():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)

    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        countdown_timer(3)  # Start a 3-second countdown
        prediction = get_prediction(model, cap)

        user_choice = np.argmax(prediction)  # Determine user choice based on prediction
        #print("User choice:", user_choice)

        comp_choice = random.randint(0, 2)  # Randomly generate computer choice (0 for rock, 1 for paper, 2 for scissors)
        #print("Computer choice:", comp_choice)

        result = get_winner(comp_choice, user_choice)
        print(result)

        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        rounds_played += 1

        print(f"Player: {player_score} - Computer: {computer_score}\n")

        if player_score >= 3 or computer_score >= 3:
            if player_score > computer_score:
                print("Player wins the game!")
            else:
                print("Computer wins the game!")

            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

play_game()
