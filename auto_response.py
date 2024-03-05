

def GetResponse(sender,category , num_rep=0):
    
    
    response = {
    'Complaints': [f'''
            Greeting {sender}
            Thank you for reaching out us. We apologize for any inconvenience you've experienced. Our team is currently reviewing your complaint and will get back to you as soon as possible.
                '''],
    'Customer Feedback': [
        f'''
            Greeting {sender}
            Thank you for your positive feedback! We're glad to hear that you had a great experience with us.
        ''',
        f'''   
            Greeting {sender}
            We are sorry to hear about your experience. Our team will review your feddback and work to improve our services.
        ''',
        f'''
            Greeting {sender}
            Thank you for your feedback. We appreciate your input and will use it to enhance our offerings.
        '''
    ]
    }

    return response[category][num_rep]

