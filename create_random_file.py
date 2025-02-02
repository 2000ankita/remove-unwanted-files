import os
import random
import string
import time

def generate_random_filename():
    """Generate a random filename."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.txt'

def create_random_file():
    """Create a random file with random content."""
    filename = generate_random_filename()
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))  # Random content
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Random file created: {filename}")

def create_and_delete_file():
    while True:
        create_random_file()  # Create a random file
        time.sleep(3600)  # Wait for 1 hour

# Uncomment this to run the file creation process
# create_and_delete_file()
