import categories as cat
import categorize as func
import random
import pandas as pd
import prioritize as pr



l = list(cat.categories_key_words_dict.keys())



try:
    df = pd.read_csv('dataset.csv')
except:
    results = {
        'mail': [],
        'category': [],
        'priority': []
    }

    df = pd.DataFrame(results)
    df.to_csv('dataset.csv', index=False)





for i in range(5000):
    index_cat = random.randint(0,9)
    category = l[index_cat]
    n_words = random.randint(1,4)
    key_words = random.sample(cat.categories_key_words_dict[category], n_words)
    mail = str(func.GenerateMail(category, cat.categories_key_words_dict[category]))
    priority = pr.GetPriority(mail, category)

    df = pd.read_csv('dataset.csv')
    mail_list = list(df['mail']) + [mail]
    category_list = list(df['category']) + [category]
    priority_list = list(df['priority']) + [priority]
    results = {'mail': mail_list, 'category': category_list, 'priority': priority_list}
    df = pd.DataFrame(results)
    df.to_csv('dataset.csv', index=False)
    print(i)

    
