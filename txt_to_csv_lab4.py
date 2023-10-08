import pandas as pd

def convert_txt_to_csv_4(string):
    #print(type(text))
    new_text = string.replace('\r', '\n').replace('*\n', '')

    if new_text[-1:] == '\r' or new_text[-1:] == '\n':
        new_text = new_text[0:-1]

    print(new_text[-1:])
    data_list1 = new_text.split('\t')
    data_list2 = []

    data_dict = {}
    i = 0
    temp_list = []
    #print(data_list1)
    for e in data_list1:
        print(e, i)
        if '\n' in e:
            data_dict[i] += [e.split('\n')[0]]
            data_dict[i+1] = [e.split('\n')[1]]
            i += 1
        else:
            if not i in data_dict:  
                data_dict[i] = [e]
            else:
                data_dict[i] += [e]
    #print(data_dict)  
    df = pd.DataFrame(data=data_dict).transpose()
    print(df)
    df.columns = df.iloc[0]
    df = df.drop(0)
    return df.to_csv()