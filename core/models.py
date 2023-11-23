from django.db import models

class shoppingtrends(models.Model):
    Customer_ID = models.IntegerField()
    Age = models.IntegerField()
    Gender = models.TextField()
    Item_Purchased = models.TextField()
    Category = models.TextField()
    Purchase_Amount_USD = models.IntegerField()
    Location = models.TextField()
    Size = models.TextField()
    Color = models.TextField()
    Season = models.TextField()
    Review_Rating = models.IntegerField()
    Subscription_Status = models.TextField()
    Shipping_Type = models.TextField()
    Discount_Applied = models.TextField()
    Promo_Code_Used = models.TextField()
    Previous_Purchases = models.IntegerField()
    Payment_Method = models.TextField()
    Frequency_of_Purchases = models.TextField()

    

    