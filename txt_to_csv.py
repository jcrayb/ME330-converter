import pandas as pd

def convert_txt_to_csv(text):
    new_text = text.replace('*\n', '')
    text = new_text.split(' ')
    text[0] = text[0].replace('*\r', '')
    data_list1 = [e.split('\t') for e in text]
    data_list2 = []

    for e in data_list1:
        for es in e:
            if es:
                data_list2 += [es]

    data_dict = {}
    i = 0
    temp_list = []
    for e in data_list2:
        
        if '\n' in e:
            temp_list += [e.replace('\n', '')]
            data_dict[i] = temp_list
            i += 1
            temp_list = []
        else:
            temp_list += [e]
            
    df = pd.DataFrame(data=data_dict).transpose()
    df.columns = df.iloc[0]
    df = df.drop(0)
    return df.to_csv()