from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://youtubepy:Ritesh8219@cluster0.lpqbnkm.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]



def list_videos():
    if (video_collection.count_documents({}) == 0):
        print(f"[Error] no videos found!")
        return

    for video in video_collection.find():
        print(f"ID: {video['_id']} Name: {video['name']} and Time: {video['time']}")

def add_new_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print(f"Added successfully!")

def update_video(new_name, new_time, video_id):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )
    print("Updated successfully!")

def delete_video(video_id, name, time):
    video_collection.delete_one({"_id": ObjectId(video_id)})
    print(f"Deleted successfully!")

def main():
    while True:
        print("\nYoutube manager App")
        print("1. List all the videos.")
        print("2. Add new video.")
        print("3. Update the video.")
        print("4. Delete the video.")
        print("5. Exit the App.") 

        choice = input("Enter your chioce: ")

        if (choice == '1'):
            list_videos()
        
        elif (choice == '2'):
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_new_video(name, time)

        elif (choice == '3'):
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the update video time: ")
            update_video(name, time, video_id)

        elif (choice == '4'):
           
            video_id = input("Enter the video ID to delete: ")
            name = input("Enter the video name (optional): ")
            time = input("Enter the video time (optional): ")
            delete_video(video_id, name, time)

        elif(choice == '5'):
            print("Exited successfully!")
            break

        else:
            print("[Error] Invalid choice!")

if __name__ == "__main__":
    main()