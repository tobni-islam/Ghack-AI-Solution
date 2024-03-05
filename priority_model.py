import prioritize as pr


mail ='''Subject: Unlock Exclusive Savings with Our Limited Time Offers!

Dear [Customer's Name],

We're thrilled to announce an array of spectacular deals and promotions designed exclusively for our valued customers. As a part of our latest marketing campaign, we aim to bring you not only quality but also incredible value that's simply too good to pass up.

Dive into our Flash Sale frenzy with a range of bestsellers and new arrivals that define trendy and stylish. The clock is ticking on these deals, so act fast to secure your savings!

Crave a more personalized touch? Explore our bespoke and made-to-order collections—where innovative meets classic—for that unique and authentic addition to your [relevant personal or home category].

We didn't forget our loyal members—your dedication hasn't gone unnoticed. Enjoy early access and sneak peeks into our Exclusive Collection, plus earn rewards points with every purchase.

And because we love giving back, join our contest and sweepstakes for a chance to win glamorous prizes. Or simply shop and receive a gift as a token of our appreciation. Don't miss out on our special BOGO offers, and grab your VIP coupon code from this email for an additional discount.

Remember, these offers are for a limited time only. Be sure to visit our online store and use the coupon code [INSERT CODE HERE] before [end date]. From luxury to casual chic, get the most out of your shopping experience with us - where affordability meets elegance.

Eager for more? Stay tuned for our upcoming newsletter for insights into the latest trends and tailor-made deals just for you.

Thank you for your continued support, and happy shopping!

Warm regards,
[Your Company's Name] Marketing Team'''
cat = 'Marketing and Promotions'
print(pr.GetPriority(mail, cat))