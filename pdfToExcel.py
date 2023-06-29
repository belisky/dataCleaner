import pdftables_api
  
# API KEY VERIFICATION
conversion = pdftables_api.Client('hljnzlaylwbk')
  
# PDf to Excel 
# (Hello.pdf, Hello)
conversion.xlsx("MATH152.pdf", "math.xlsx")