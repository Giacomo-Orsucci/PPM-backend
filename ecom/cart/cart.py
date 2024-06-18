from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session

        self.request = request

        #get the current session key if it exists
        cart = self.session.get('session_key')

        #if the user is new create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #assuring cart is available on all pages of the site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        else:
            pass
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            #to convert single marks in python dictionary to double marks
            temp_cart = str(self.cart).replace("\'", '\"')

            #saving it to the Profile model to make it persistence on logout
            current_user.update(old_cart=str(temp_cart))


    def __len__(self):
        return len(self.cart)

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #to convert single marks in python dictionary to double marks
            temp_cart = str(self.cart).replace("\'", '\"')

            #saving it to the Profile model to make it persistence on logout
            current_user.update(old_cart=str(temp_cart))


    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #get ids to lookup products in database
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True


        if self.request.user.is_authenticated:

            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #to convert single marks in python dictionary to double marks
            temp_cart = str(self.cart).replace("\'", '\"')

            #saving it to the Profile model to make it persistence on logout
            current_user.update(old_cart=str(temp_cart))

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

        if self.request.user.is_authenticated:

            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #to convert single marks in python dictionary to double marks
            temp_cart = str(self.cart).replace("\'", '\"')

            #saving it to the Profile model to make it persistence on logout
            current_user.update(old_cart=str(temp_cart))

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            value = int(value)
            for product in products:
                if product.id == key:
                    if product.is_on_sale:
                        total += value * product.sale_price
                    else:
                        total += value * product.price
        return total

