import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL

    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall(): 
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)",(name, time))
    conn.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ?, id = ?",(new_name, new_time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ",(video_id,))
    conn.commit()

def exit():
    pass


def main():
    video = []
    while True:
        print("YouTube manager app with DB\n")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("\nEnter your choice(1-5): ")

        if (choice == '1'):
            list_videos()

        elif(choice == '2'):
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
            print("\nAdded successfully!\n")

        elif(choice == '3'):
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id,name,time)
            print("\nUpdated successfully!\n")

        elif(choice == '4'):
            video_id = input("Enter the video ID to delete: ")
            delete_videos()
            print("\nDeleted successfully!\n")

        elif(choice == '5'):
            print("\nExit successfully!\n")
            break

        else:
            print("\n[Error] Enter the valid choice!\n")
        
    conn.close()

if __name__ == "__main__":
    main()