from django.db import models

# Create your models here.
class CustomPermission(models.Model):     
    class Meta:
        verbose_name_plural = "Custom Permission"
        permissions = (
            ("can_add_case", "Can Add Case"),
            ("can_update_case", "Can Update Case"),
            ("can_approve_case", "Can Approve Case"),
            ("can_see_reports", "Can See Reports"),
        )