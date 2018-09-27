print("Welcome to Face Recognition System")
print("Choose your option")
print("(1) Register your Face.")
print("(2) Recognize your Face.")
choice = input()
if(choice is "1"):
    # do registration
    username = input("Username:")
    from save_faces import save_detected_faces
    save_detected_faces(username)
    print("Detected your face.")
    print("Training your face...")
    from faces_train import train_faces
    train_faces()
    print("Training successful")
    
elif(choice is "2"):
    # do recognition
    pass
else:
    print("Your choice is invalid.")