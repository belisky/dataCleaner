# importing os module
import os
import sys
 
# Function to rename multiple files
def main():
    try:
        if (sys.argv[1]):
            folder=sys.argv[1]
    except:    
        folder="mock"
   
     
    for department in os.listdir(folder):
        for year in os.listdir(f"{folder}/{department}/"):
            for filename in os.listdir(f"{folder}/{department}/{year}"):
                 
                new_name=filename.replace(' ','')
                dst = f"{year}-{new_name}"
                src =f"{folder}/{department}/{year}/{filename}"  # foldername/filename, if .py file is outside folder
                dst =f"{folder}/{department}/{year}/{dst}"
                # print(filename)
            
        # rename() function will
        # rename all the files
                os.rename(src, dst)
            # print(year)
        # print(sub)

        # print(department)
 
# Driver Code
if __name__ == '__main__':
    main()
