import pyshorteners
import time

def shortener(expanded_link):
    if expanded_link.startswith("ht"):
        print("Link Input Successful")
    else:
        print(f"Input a valid link: {expanded_link}")
    pys = pyshorteners.Shortener()  # fix #1
    try:
        short_url = pys.tinyurl.short(expanded_link)
        print("Communicating with tinyurl servers.....")
        time.sleep(0.5)
        print(short_url)
    except Exception as e:
        print(f"I am facing some issues, please try again after a while. {e}")
    
def expander(shortened_link):
    if "tinyurl" in shortened_link:  # fix #2
        print("Link Input Successful")
    else:
        print(f"Input a valid link: {shortened_link}")
    try: 
        pys = pyshorteners.Shortener()  # fix #1
        expand_url = pys.tinyurl.expand(shortened_link)
        print("Communicating with tinyurl servers.....")
        time.sleep(0.5)
        print(expand_url)
    except Exception as f:
        print(f"I am facing some issues, please try again after a while. {f}")
    
    
catalog = """
|---------------------------------------------------------------------------------------------|
| Welcome to the link shortener console.                                                      |
| I use tinyurl to generate shortened links and expand shortened links generated from tinyurl.|
|                                                                                             |
|https://tinyurl.com/app/                                                                     |
|                                                                                             |
|                                                                                             |
| Here You Can:                                                                               |
|                                                                                             |
| 1, Shorten an expanded link using tinyurl link shortener.                                   |
| 2, Expand a shortened link using tinyurl's shortened link expander function.                |
|                                                                                             |
| Press CTRL+C to close the application.                                                      |
| OR                                                                                          |
| 0                                                                                           |
|---------------------------------------------------------------------------------------------|
""" 
    
def main():
    
        print(catalog)
        
        choice = int(input("\nEnter your choice: "))  # fix #3
        if choice == 1:
            expanded_link = str(input("Enter the expanded link that you want to shorten: \n"))
            shortener(expanded_link)
        elif choice == 2:  # fix #4
            shortened_link = str(input("Enter the shortened link that you want to expand: \n"))
            expander(shortened_link)
        else:  # fix #4
            print("Invalid choice.")
      
    
while True:       
    main()
