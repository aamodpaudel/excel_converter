import pandas as pd

def transform_researchers(input_path, output_path):
   
    df = pd.read_excel(r'C:\Users\aamod\OneDrive\Desktop\input.xlsx', header=None, skiprows=1, names=['Data'])

    
    researchers = []
    total_rows = len(df)
    
    
    for i in range(0, total_rows, 6):
        researcher_data = df.iloc[i:i+6]['Data'].values
        if len(researcher_data) == 6:
            researchers.append({
                'Name': researcher_data[0],
                'Field': researcher_data[1],
                'Position': researcher_data[2],
                'Education': researcher_data[3],
                'Where to find?': researcher_data[4],
                'General Field': researcher_data[5]
            })
    
    
    output_df = pd.DataFrame(researchers)
    output_df.to_excel(output_path, index=False)
    print(f"Transformed data saved to {output_path}")

#Aamod's Example
transform_researchers("input.xlsx", "output.xlsx")