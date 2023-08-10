import sys
import time

# Define valid credentials (replace these with your actual valid credentials)
VALID_USERNAME = "user123"
VALID_PASSWORD = "password123"

# Compare username and password
def authenticate(username, password):
    if not username or not password:
        print("EMPTY")
    elif username == VALID_USERNAME and password == VALID_PASSWORD:
        print("SUCCESS")
    else:
        print("FAILURE")

# Main function
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("EMPTY")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    #delay for 3 seconds
    
    authenticate(username, password)
    time.sleep(10)
    print("FINISH")
