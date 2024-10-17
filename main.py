# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from postgre_support import PostgreSupport
import random

postgre = PostgreSupport()
postgre.connect_db()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    with open('posts.txt', 'r') as file:
        lines = file.readlines()
        print(f"lines = {len(lines)}")
        indx = 0
        for iu in range(1, 999931):
            count_posts = random.randint(1, 10)
            for i in range(0, count_posts):
                if indx+i >= len(lines):
                    indx = 0
                user_post = lines[indx+i]
                print(f"user_post = {user_post}")
                postgre.add_user_post(id_user=iu, post=user_post)
            indx +=count_posts