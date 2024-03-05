from lastmileai import LastMile


def GenerateMail(category, keywords, min_words=50, max_words=200):

    category=category
    keywords=','.join(keywords)

    lastmile = LastMile(api_key="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..lAaWOcJueOKg15Ba.UZSRptV66z-JPBMf6wGgYDhcpUgicZhLzYqoO3_JHX1xX2JbLG3rvpCz-NVYX1BxM4qTCawWkE3o_kNY_amNFDRij_6vkYFkWgXB8-H4B-zZUH4tRAC-CQ-3g2GPX--FMg5XaeJh_T9WfiVM-QmfPadpdJ-gLFhnEkoY5s9bxZtm7AyXEgyH32zp5osfY095UFCA7YK2gwDMu0v6_00J_Tj4KzrzNzu9vpYH4RtbG5LshS9lxkw0oqbD4HB4FCcmqKPGUOLMlyFJzGaIdm4LQK2vvk0pEPu2yZEMV7mT7zP6-1zbkgnvazJP4Y8psrKapMH9HK6g3AUKB5fEbkGzHMB4P63Iz-QDpjz9DkIpSOmyA5bE6k2GDImtpY_e1wq8CFSjx0Ad.Rv9asjCY1o925juyvK6kHQ")
    completion = lastmile.create_openai_chat_completion(
                completion_params = {
                "model": "gpt-4-1106-preview",
                "messages": [
                    {"role":"system", "content":f'You are an email generative you will be given an email category and a list of keywords related to this category and you must generate an email message from {min_words} to {max_words} words based on these features:'},
                    { "role": "user", "content": f'this category:{category},and this are Keywords :{keywords}' }
                    ,]
                ,}
            )
    x = completion['completionResponse']['choices'][0]['message']['content']
    x = x.replace("json","")

    return x