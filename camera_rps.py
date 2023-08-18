

import cv2
from keras.models import load_model
import numpy as np
import random 
import time

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    num_predictions = 0
    # start_time = time.time()                            #Records start time
    # elapsed_time = 0


    while num_predictions < 3:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)

        # current_time = time.time()                      #Records current time
        # elapsed_time = current_time - start_time      #Calculates elapsed time from start of function to this point

        # if elapsed_time < 10:                            #Counts down from 3 to 1
        #     print(f"Countdown: {int(10 - elapsed_time)} seconds")

        number = 3
        print("Countdown begins")
        while True:
            print(number)
            number -= 1
            if number == 0:   
                user_choice = np.argmax(prediction)
                print(user_choice)
                break
            
        num_predictions += 1

        # number = 3
        # print("Countdown!") 
        # while True: 
        #     print(number) 
        #     number = number - 1 
        #     if number <= 0: 
        #       break 
        #     print(user_choice)
        
        # print(get_user_choice(prediction))
            # break
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    # return user_choice


def get_user_choice():
    user_choice = get_prediction()
    if user_choice == 0:
        print("You chose rock!")
    if user_choice == 1:
        print("You chose paper!")
    if user_choice == 2:
        print("You chose scissors!")
    if user_choice == 3:
        print("There is no user choice detected")
    # return user_choice


    return get_prediction()

def get_computer_choice():
    choice_list = ['rock', 'paper', 'scissors']                             #While this code was working well when the choice_list was outside the function as a globla variable, based on feedback I placed it insie the function here and again in get_user_choice which is not taking any parameters
    comp_choice = random.choice(choice_list)
    print(f'Computer choice is {comp_choice}')
    return comp_choice

def get_winner(comp_choice, user_choice):                                  #Function with rules of rock paper scissors
    if comp_choice == user_choice =='rock':
        print("It's a tie!")
    elif (comp_choice == 'rock' and user_choice == 2) or (comp_choice == 'paper' and user_choice == 0) or (comp_choice == 'scissors' and user_choice == 1):
        print("You lost!")
    else:
        print("You win!")

def play():                                                                 #Final fucntion wrapping previous fucntions togther- functions are assigned the variables as per get_winner arguments
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    get_winner(comp_choice, user_choice)


# start = time.time()
# get_prediction()
# end = time.time()
# print(f"time taken to run get_predection function is {end - start}")

play()

    
# print(get_prediction())


