

import cv2
from keras.models import load_model
import numpy as np
import random 
import time

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def get_user_choice():   
    return get_prediction

def get_computer_choice():
    choice_list = ['rock', 'paper', 'scissors']                             #While this code was working well when the choice_list was outside the function as a globla variable, based on feedback I placed it insie the function here and again in get_user_choice which is not taking any parameters
    comp_choice = random.choice(choice_list)
    print(f'Computer choice is {comp_choice}')
    return comp_choice

def get_winner(comp_choice, user_choice):                                  #Function with rules of rock paper scissors
    if comp_choice == 'rock' and user_choice =='rock':
        print("It's a tie!")
    elif comp_choice == 'paper' and user_choice =='paper':
        print("It's a tie!")
    elif comp_choice == 'scissors' and user_choice =='scissors':
        print("It's a tie!")
    elif comp_choice == 'rock' and user_choice == 'scissors':
        print("You lost!")
    elif comp_choice == 'rock' and user_choice == 'paper':
        print("You win!")
    elif comp_choice == 'paper' and user_choice == 'scissors':
        print("You win!")   
    elif comp_choice == 'paper' and user_choice == 'rock':
        print("You lost!")
    elif comp_choice == 'scissors' and user_choice == 'rock':
        print("You win!")
    elif comp_choice == 'scissors' and user_choice == 'paper':
        print("You lost!")


def play():                                                                 #Final fucntion wrapping previous fucntions togther- functions are assigned the variables as per get_winner arguments
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    winner = get_winner(comp_choice, user_choice)

play()


    
# print(get_prediction())