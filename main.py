from gomool.ui.root import Root
from gomool import update
import os

def main():
    if not os.path.exists("./data"):
        os.mkdir("./data")
        update.song_list()

    root = Root()
    root.mainloop()
    
if __name__ == "__main__":
    main()