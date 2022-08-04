
"""
https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
generate Readme file for github
"""

workspace="C:\\Users\\18178\PycharmProjects\\bibliograph_smart_contract_machine_learning\\"
input_excel="C:\\Users\\18178\\2021__papers\\smart contracts__machine learning\\smart_contracts_machine_learning.xlsx"
output_file_name='readMe.md'

import pandas as pd

# read paper data from an excel
# df_paper_data=pd.read_excel(paper_dir,sheet_name=0,index_col=None, na_values=['NA'], usecols="A,C:AA")
df_paper_data=pd.read_excel(input_excel,sheet_name=0,index_col=None, na_values=['NA'], usecols="A,B,D,E,G")

num_columns=df_paper_data.shape[1]
num_rows=df_paper_data.shape[0]

# remove rows that have values for column year
df_paper_data= df_paper_data[df_paper_data['year'].notna()]


df_paper_data = df_paper_data.sort_values(["year", "paper"], ascending = (False, True))




# write to a file
output_file_path=workspace+output_file_name
with open(output_file_path, 'w',encoding='utf8') as f:
    f.write('A bibliography of papers on security and testing of Ethereum smart contracts\n')
    f.write('========\n')

    f.write("| No | Title | Year | citation | abstract | \n")
    f.write("| ---- | ----- | ---- | ----- | ------ | \n")
    i=1
    for index, row in df_paper_data.iterrows():
        citation="<details><summary>cite</summary>"+\
        str(row[3])+"</details>"
        abstract="<details><summary>abstract</summary>"+\
        str(row[4]).replace('\n','</br>')+"</details>"

        # line="|"+str(i)+"|["+str(row[0]) +"]("+str(row[2])+")|"+str(int(row[1]))+"|"+citation+"|\n"
        line="|"+str(i)+"|["+row[0] +"]("+row[2]+")|"+str(row[1])+"|"+citation+"|" +abstract +"|\n"
        f.write(line)
        i+=1


    # f.write("| No | Title | Year | citation | abstract |\n")
    # f.write("| -- | ----- | ---- | -------- | -------- |\n")
    # i=1
    # for index, row in df_paper_data.iterrows():
    #     citation="<details><summary>cite</summary>"+\
    #     str(row[3])+"</details>"
    #
    #     abs_con=str(row[4]).replace('\n','</br>')
    #     abstract="<details><summary>abstract</summary>"+\
    #     abs_con+"</details>"
    #
    #     line="|"+str(i)+"|["+str(row[0]) +"]("+str(row[2])+")|"+str(int(row[1]))+"|"+citation+"| "+abstract+"|\n"
    #     f.write(line)
    #     i+=1


