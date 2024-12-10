import os
import sys

def install(text):
    os.system(f'say "{text}"')
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <text>")
    else:
        text = sys.argv[1]
        install(text)
