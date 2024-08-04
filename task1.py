"""task1.py"""
import pandas as pd

def read_and_sort_excel_files(file_names):
    dfs = [pd.read_excel(file, engine='openpyxl') for file in file_names]
    combined_df = pd.concat(dfs, ignore_index=True)
    sorted_df = combined_df.sort_values(by=combined_df.columns[0], ascending=False)
    return sorted_df

def save_to_excel(df, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
        worksheet = writer.sheets['Sheet1']
        for row in worksheet.iter_rows(min_row=1, max_col=worksheet.max_column, max_row=worksheet.max_row):
            for cell in row:
                cell.font = cell.font.copy(name='Arial', size=12)
                cell.border = cell.border.copy(
                    left=cell.border.left,
                    right=cell.border.right,
                    top=cell.border.top,
                    bottom=cell.border.bottom
                )

if __name__ == "__main__":
    file_names = ['1111.xlsx', '2222.xlsx', '3333.xlsx']
    sorted_df = read_and_sort_excel_files(file_names)
    save_to_excel(sorted_df, 'sorted_output.xlsx')
