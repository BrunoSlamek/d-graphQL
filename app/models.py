from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: str = 'tb_type'
        managed: bool = True
