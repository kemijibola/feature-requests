from app import ma

class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id','fullname','phone_number','email','address1','created_at','updated_at')

class FeatureSchema(ma.Schema):
    class Meta:
        fields = ('id','client_id','title','description','priority','target_date','product_id','created_at','updated_at')

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','created_at','updated_at')