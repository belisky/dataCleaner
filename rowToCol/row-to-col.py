import pandas
import math

df = pandas.read_excel('midsem.xlsx', sheet_name='TT (PRINT)',usecols="A:F",header=None)
new_arr=[]

def isNaN(string):
    return string != string
# print whole sheet data
paperDate=df.iloc[0][0]
paperSession=df.iloc[1][0]
print(paperDate,paperSession)
i=2
# for index,row in df.iterrows():
#     print(row)
while i < len(df):
    edited_rows={}
    if isNaN(df.iloc[i][0]) and isNaN(df.iloc[i][2]):
        i+=1
    elif (not(isNaN(df.iloc[i][0])) and isNaN(df.iloc[i][1])):
        paperDate=df.iloc[i][0]
        paperSession=df.iloc[i+1][0]
        i+=3
    else:
        edited_rows['code']=df.iloc[i][0]
        edited_rows['course_name']=df.iloc[i][1]
        edited_rows['examiner']=df.iloc[i][2]
        edited_rows['class']=df.iloc[i][3]
        edited_rows['stds']=df.iloc[i][4]
        edited_rows['room_number']=df.iloc[i][5]   
        edited_rows['date']=paperDate
        edited_rows['session']=paperSession
        new_arr.append(edited_rows)
        i+=1
    # print(isNaN(df.iloc[i][0]),'-',type(df.iloc[i][1]),df.iloc[i][1],'-',df.iloc[i][2],'-',df.iloc[i][3],'-',df.iloc[i][4],'-',df.iloc[i][5],end='\n\n**')
        
    
         
    # if (str(df.iloc[i][3]).startswith('Total')):
    #     print(df.iloc[i][3],df.iloc[i][4])
    #     i+=1
    
    # if  str(df.iloc[i][0]) and  not(str(df.iloc[i][1])):        
    #     paperDate=df.iloc[i][0]
    #     paperSession=df.iloc[i+1][0]
    #     i+=2
    # else:
    #     i+=1
        # continue
    # if math.isnan(df.iloc[i][0]):
    #     # print(df.iloc[i][:])
    #     i+=1
     
    # print(df.iloc[i],'index=',i)
    # i+=1

    
    

new_df = pandas.DataFrame(data=new_arr)

#convert into excel
new_df.to_excel("cleaned_midsem.xlsx", index=False)
print("Dictionary converted into excel...")
 
 

     
 
     