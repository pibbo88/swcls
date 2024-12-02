import os
import camelot
import pandas as pd

parse_info = {
    "2007.pdf": [
        { "page": "3", "table_area": ["45, 750, 550, 80"], "columns": ["130, 215, 300, 385, 470"] },
        { "page": "4", "table_area": ["45, 775, 550, 80"], "columns": ["130, 215, 300, 385, 470"] },
        { "page": "5", "table_area": ["45, 775, 550, 80"], "columns": ["130, 215, 300, 385, 470"] },
        { "page": "6", "table_area": ["45, 775, 550, 80"], "columns": ["130, 215, 300, 385, 470"] },
        { "page": "7", "table_area": ["45, 775, 550, 80"], "columns": ["130, 215, 300, 385, 470"] },
        { "page": "8", "table_area": ["45, 775, 550, 80"], "columns": ["130, 215, 300, 385, 470"] }
    ],
    "2011.pdf": [
        { "page": "5", "table_area": ["20, 770, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] },
        { "page": "6", "table_area": ["20, 785, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] },
        { "page": "7", "table_area": ["20, 785, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] },
        { "page": "8", "table_area": ["20, 785, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] },
        { "page": "9", "table_area": ["20, 785, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] },
        { "page": "10", "table_area": ["20, 785, 570, 65"], "columns": ["100, 176, 248, 350, 435, 510"] }
    ],
}


for pdf_file in parse_info:
    pdf_path = os.path.join("./documents", pdf_file)
    df_list = []
    for page_info in parse_info[pdf_file]:
        tables = camelot.read_pdf(
            pdf_path, 
            flavor="stream", 
            pages=page_info["page"],
            table_areas=page_info["table_area"],
            columns=page_info["columns"],
            split_text=True
        )
        df = tables[0].df
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(drop=True, inplace=True)
        
        df_list.append(df)
    
    df = pd.concat(df_list, ignore_index=True)
    df.to_csv(f"{pdf_file[:-4]}.csv", index=False)