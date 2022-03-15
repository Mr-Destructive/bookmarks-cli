from bookmarks import get_bookmarks
import argparse 

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args() 
    get_bookmarks() 

if __name__ == "__main__":
    main()


    
    
