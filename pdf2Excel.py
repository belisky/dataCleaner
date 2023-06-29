# Import Module 
import tabula
import pandas as pd

# Read PDF File
# this contain a list 
df = tabula.read_pdf("MATH152.pdf", pages = 'all')
# Concatenate a list of dataframes using pandas
aggregate=pd.concat(df[:])
# Convert dataFrames to excel
aggregate.to_excel("aggregate.xlsx",index=False)
# for i in range(len(df)):
#     sheet=tabula.read_pdf("MATH152.pdf",pages='all')[i]
#     # pd.ExcelWriter('output.xlsx', mode='a')
#     sheet.to_excel("maths.xlsx")
    
# print(len(df),type(df))
# writer = df.ExcelWriter('converted-to-excel.xlsx')
# df.to_excel(writer)
 
# # save the excel
# writer.save()
print("DataFrame is exported successfully to 'converted-to-excel.xlsx' Excel File.")
# tabula.read_pdf("MATH152.pdf", stream=True)
  
# Convert into Excel File
# tabula.convert_into("MATH152.pdf","math152.json",output_format="json",pages='all')