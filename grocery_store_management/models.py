from django.db import models

# Create your models here.
# managing customers / orders
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=40)
    customer_email = models.EmailField(null = True)
    customer_address = models.CharField(max_length=100,null = True)
    customer_phone = models.CharField(max_length=10)
    customer_add =models.DateField(auto_now=True)
    objects=models.Manager()

class Orders (models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discon_bill = models.DecimalField(max_digits=10,decimal_places=2)
    dic_on_bill_rs = models.DecimalField(max_digits=10,decimal_places=2)
    bill_date = models.DateTimeField(auto_now=True)
    bill = models.FileField()
    objects=models.Manager()

# to manage product / seller details
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)
    seller_phone = models.CharField(max_length=10 )
    seller_email = models.EmailField(null =True)
    seller_address = models.CharField(max_length=100,null=True)
    Seller_Timestamp = models.DateField(auto_now=True) 
    seller_payment_paid = models.DecimalField(max_digits=10,decimal_places=2)
    seller_payment_due = models.DecimalField(max_digits=10,decimal_places=2)
    objects=models.Manager()
 

class product_catagories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50) 

class Product (models.Model):
    id = models.AutoField(primary_key=True) 
    category = models.ForeignKey(product_catagories, on_delete= models.CASCADE)
    bar_code = models.CharField(max_length=13 )
    product_name = models.CharField(max_length=100)
    product_seller = models.ForeignKey(Seller,on_delete= models.CASCADE)
    product_date = models.DateField(auto_now=True)
    product_image = models.FileField(null=True)
    objects=models.Manager()


class Product_details(models.Model):
    id = models.AutoField(primary_key=True) 
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_Purchase_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_selling_price =  models.DecimalField(max_digits=10,decimal_places=2)
    product_units = models.IntegerField()
    product_purchase_date = models.DateField(auto_now=True)
    objects=models.Manager()



class Purchased_product(models.Model):
    id = models.AutoField(primary_key=True)
    seller_name = models.ForeignKey(Seller,on_delete = models.CASCADE)
    pproduct_name = models.ForeignKey(Product,on_delete = models.CASCADE)
    pproduct_Quantity = models.IntegerField()
    pproduct_price = models.DecimalField(max_digits=10, decimal_places=2)
    pproduct_total_price =models.DecimalField(max_digits=10, decimal_places=2)
    pproduct_purchased = models.DateField(auto_now=True)
    pproduct_payment_paid=models.DecimalField(max_digits=10,decimal_places=2)
    pproduct_payment_due = models.DecimalField(max_digits=10,decimal_places=2)
    objects=models.Manager()


# managing sales amount 
class Daily_sales(models.Model):
    sales_amount= models.DecimalField(max_digits=30,decimal_places=2)
    timestamp = models.DateField(auto_now=True)


class Monthly_sales(models.Model):
    daily_sales = models.ForeignKey(Daily_sales, on_delete=models.CASCADE)
    monthly_sales = models.DecimalField(max_digits=30,decimal_places=2)

class Expences(models.Model):
    exp_name = models.CharField(max_length=40)
    exp_disc = models.CharField(max_length=100)
    exp_amaount= models.DecimalField(max_digits=20,decimal_places=2)
    timestamp = models.DateField(auto_now=True)



   

