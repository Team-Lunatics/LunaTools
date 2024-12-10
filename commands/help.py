import os
import sys

def install(text):
    print(f"{text}")
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <text>")
    else:
        text = sys.argv[2]
        install(text)
