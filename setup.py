import os

# Create 100 folders named 001 to 100
for i in range(1, 101):
    # Format folder name with leading zeros
    folder_name = f"{i:03}"
    
    # Create the directory
    os.makedirs(folder_name, exist_ok=True)
    
    # Define the path for the new file
    file_path = os.path.join(folder_name, "main.py")
    
    # Create a new file named main.py in the folder
    open(file_path, 'w')

print("Folders and files created successfully.")