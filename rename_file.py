import os 
dir_path = 'images'
files = os.listdir(dir_path)
counter=0
for file_name in files:
    counter+=1
    file_extension= file_name.split('.')

    new_name = f'image_{counter}.{file_extension[-1]}'
    print(new_name)
    old_path = os.path.join(dir_path, file_name)
    new_path = os.path.join(dir_path, new_name)
    print(old_path, "   ", new_path)
    os.rename(old_path, new_path)
    
    