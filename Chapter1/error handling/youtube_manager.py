import json

def load_data():
    try:
        with open("YouTube.txt",'r') as file:
            test = json.load(file)
            print(test)
            print(type (test))
            return test
    except FileNotFoundError:
        return []
    finally:
        pass

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name' : name,'time' : time})
    save_data_helper(videos)
    print("Video added successfully!")

def update_video(videos):
    list_all_videos(videos)
    if not videos: return 

    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ") 
            time = input("Enter the new video time: ")
            videos[index-1] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("\n[Success] Video updated successfully!")
        else:
            print("\n[Error] Invalid index selected!")
    except ValueError:
        print("\n[Error] Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if(index >= 1 <= len(videos)):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid video index(number)!")
def exit():
    pass


def save_data_helper(videos):
    with open("YouTube.txt",'w') as file:
        json.dump(videos,file)
        print("Video saved successfully!")


def main():
    videos = load_data()
    while True:
        print("\n----------------- YouTube Manager | choose an option -----------------")
        print("1. List of all Youtube videos.")
        print("2. Add a YouTube video.")
        print("3. Update YouTube video details.")
        print("4. Delete a YouTube video.")
        print("5. Exit the app.")

        choice = input("Enter your choice btw (1-5): ")
        print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("[error] Invalid choice!")

if __name__ ==  "__main__":
    main()