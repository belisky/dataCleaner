import os
import sys
import tabula
import pandas as pd


 
# Function to convert multiple pdf files in folder-tree
def main():
    try:
        if (sys.argv[1]): # Takes the foldername as argument when running the script.
            folder=sys.argv[1]
    except:    
        folder="Combined"
   
    count=0
    for department in os.listdir(folder):
        for year in os.listdir(f"{folder}/{department}/"):
            for filename in os.listdir(f"{folder}/{department}/{year}"):
             
                new_name=filename.replace(' ','').split('.')[0]
                renamed_file = f"{year}-{new_name}"
                src =f"{folder}/{department}/{year}/{filename}"   
                filepath=f"{folder}/{department}/{year}/{filename}"
                print(filename)
            
  
                # Read PDF File
                # this contains a list 
                df = tabula.read_pdf(filepath, pages = 'all')
                # Concatenate a list of dataframes using pandas
                aggregate=pd.concat(df[:])
                # Convert dataFrames to excel
                new_filename=filename.split('.')[0]
                new_filename=renamed_file+'.xlsx'
                dst =f"cleaned/{new_filename}"
                aggregate.to_excel(dst,index=False)
                print("converted",filename,"to",new_filename,"successfully!!!",len(aggregate),"students")
            # print(year)
        # print(sub)
    print("All done!!!")
 
# Driver Code
if __name__ == '__main__':
    main()
