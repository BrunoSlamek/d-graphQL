from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=User)

    class Meta:
        db_table: str = 'tb_type'
        managed: bool = True

    @staticmethod
    def return_all_active():
        return Type.objects.filter(is_active=True)
    
    @staticmethod
    def get_by_id(type_id: int):
        if not Type.objects.filter(id=type_id, is_active=True).exists():
            return Exception('Do not exists!')
        return Type.objects.get(id=type_id)
