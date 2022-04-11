# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    user_id = models.IntegerField(primary_key=True)
    admin_id = models.IntegerField(unique=True)
    num_events = models.IntegerField(blank=True, null=True)
    num_student = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Eventtbl(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_email = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(unique=True)
    event_category = models.CharField(max_length=30, blank=True, null=True)
    event_description = models.CharField(max_length=255, blank=True, null=True)
    event_phone = models.IntegerField(blank=True, null=True)
    location_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventtbl'
        unique_together = (('event_id', 'date'),)


class PrivateEvent(models.Model):
    event_id = models.IntegerField(primary_key=True)
    uni_id = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'private_event'
        unique_together = (('event_id', 'date'),)


class PublicEvent(models.Model):
    event_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    superadmin_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'public_event'
        unique_together = (('event_id', 'date'),)


class Review(models.Model):
    user_id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('user_id', 'event_id'),)


class Rso(models.Model):
    rso_id = models.IntegerField(primary_key=True)
    uni_id = models.IntegerField()
    num_students = models.IntegerField(blank=True, null=True)
    num_events = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rso'


class RsoEvent(models.Model):
    rso_id = models.IntegerField()
    event_id = models.IntegerField(primary_key=True)
    admin_id = models.IntegerField(unique=True)
    date = models.DateTimeField(unique=True)

    class Meta:
        managed = False
        db_table = 'rso_event'
        unique_together = (('event_id', 'date'),)


class SuperAdmin(models.Model):
    superadmin_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'super_admin'


class University(models.Model):
    uni_id = models.IntegerField(primary_key=True)
    uni_name = models.CharField(max_length=30, blank=True, null=True)
    num_students = models.IntegerField(blank=True, null=True)
    uni_description = models.CharField(max_length=200, blank=True, null=True)
    uni_location = models.CharField(max_length=50, blank=True, null=True)
    gallery = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'


class Usertbl(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_password = models.CharField(max_length=30)
    uni_id = models.IntegerField(blank=True, null=True)
    rso_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usertbl'