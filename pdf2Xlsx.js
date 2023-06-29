const pdf2excel = require('pdf-to-excel');
try {
    const options = {
      // when current pdf page number changes call this function(optional)
      onProcess: (e) => console.warn(`${e.numPage} / ${e.numPages}`),
      // pdf start page number you want to convert (optional, default 1)
      start: 1,
      // pdf end page number you want to convert (optional, default )
    //   end: 2,
    }
  
    
    pdf2excel.genXlsx('MATH152.pdf', 'MATH152.xlsx', options);
  } catch (err) {
    console.error(err);
  }