import os
from django.contrib.auth.models import User
from django.db import models
import uuid
from simple_history.models import HistoricalRecords
# from .middleware import get_current_request
from django.utils.timezone import now

# Create your models here.

class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_column="fld_created_at", db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_column="fld_updated_at", db_index=True)
    created_by = models.ForeignKey(User, db_column="fld_created_by", related_name='created_%(class)s_set', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    updated_by = models.ForeignKey(User, db_column="fld_updated_by", related_name='updated_%(class)s_set', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     self._request = get_current_request()
    #     super().save(*args, **kwargs)


class Module(AuditModel):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_column="fld_uid", db_index=True)
    name = models.CharField(max_length=100, db_column="fld_name", db_index=True, null=True, blank=True,)
    # header = models.CharField(max_length=100, db_column="fld_header", db_index=True,blank=True, null=True)
    # sequence = models.IntegerField(default=0, db_column="fld_sequence", db_index=True,blank=True, null=True)
    # type = models.CharField(max_length=20, db_column="fld_type", choices=(("Air", "Air"), ("Master", "Master"),("Sea", "Sea"),("Billing", "Billing")), db_index=True, null=True, blank=True,)
    # creation_time = models.DateTimeField(auto_now_add=True, db_column="fld_creation", db_index=True, null=True, blank=True,)
    # module_url = models.CharField(max_length=140, db_column="fld_module_url", blank=True, null=True, db_index=True)
    # title = models.CharField(max_length=140, db_column="fld_title", blank=True, null=True, db_index=True)
    # icon = models.CharField(max_length=140, db_column="fld_icon", blank=True, null=True, db_index=True)
    # is_active = models.BooleanField(default=True, db_column="fld_is_active", db_index=True)
    # is_hidden = models.BooleanField(default=False, db_column="fld_is_hidden", db_index=True)

    history = HistoricalRecords()

    class Meta:
        db_table = "tbl_module"
        verbose_name = "Module"

    def __str__(self) -> str:
        return str(self.uid)