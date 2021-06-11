# Generated by Django 3.2.4 on 2021-06-11 13:45

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import rgd.utility
import s3_file_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=127)),
            ],
            options={
                'default_related_name': 'collections',
            },
        ),
        migrations.CreateModel(
            name='ModifiableEntry',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'modified',
                    models.DateTimeField(
                        editable=False, help_text='The last time this entry was saved.'
                    ),
                ),
                (
                    'created',
                    models.DateTimeField(
                        editable=False, help_text='When this was added to the database.'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='SpatialEntry',
            fields=[
                ('spatial_id', models.AutoField(primary_key=True, serialize=False)),
                ('acquisition_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('footprint', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('outline', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                (
                    'instrumentation',
                    models.CharField(
                        blank=True,
                        help_text='The instrumentation used to acquire these data.',
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='WhitelistedEmail',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ChecksumFile',
            fields=[
                (
                    'modifiableentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='rgd.modifiableentry',
                    ),
                ),
                ('failure_reason', models.TextField(null=True)),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('created', 'Created but not queued'),
                            ('queued', 'Queued for processing'),
                            ('running', 'Processing'),
                            ('failed', 'Failed'),
                            ('success', 'Succeeded'),
                        ],
                        default='created',
                        max_length=20,
                    ),
                ),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('checksum', models.CharField(max_length=128)),
                ('validate_checksum', models.BooleanField(default=False)),
                ('last_validation', models.BooleanField(default=True)),
                ('type', models.IntegerField(choices=[(1, 'FileField'), (2, 'URL')], default=1)),
                (
                    'file',
                    s3_file_field.fields.S3FileField(
                        blank=True, null=True, upload_to=rgd.utility.uuid_prefix_filename
                    ),
                ),
                ('url', models.TextField(blank=True, null=True)),
            ],
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.CreateModel(
            name='CollectionPermission',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'role',
                    models.SmallIntegerField(
                        choices=[(1, 'Reader'), (2, 'Owner')],
                        db_index=True,
                        default=1,
                        help_text='A "reader" can view assets in this collection. An "owner" can additionally add/remove other users, set their permissions, delete the collection, and add/remove other files.',
                    ),
                ),
                (
                    'collection',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='collection_permissions',
                        to='rgd.collection',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='collection_permissions',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'default_related_name': 'collection_permissions',
            },
        ),
        migrations.CreateModel(
            name='SpatialAsset',
            fields=[
                (
                    'spatialentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='rgd.spatialentry',
                    ),
                ),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('files', models.ManyToManyField(to='rgd.ChecksumFile')),
            ],
            bases=('rgd.spatialentry',),
        ),
        migrations.AddConstraint(
            model_name='collectionpermission',
            constraint=models.UniqueConstraint(fields=('collection', 'user'), name='unique_user'),
        ),
        migrations.AddField(
            model_name='checksumfile',
            name='collection',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='checksumfiles',
                related_query_name='checksumfiles',
                to='rgd.collection',
            ),
        ),
        migrations.AddConstraint(
            model_name='checksumfile',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ('file__regex', '.+'),
                        ('type', 1),
                        models.Q(('url__in', ['', None]), ('url__isnull', True), _connector='OR'),
                    ),
                    models.Q(
                        ('type', 2),
                        models.Q(('url__isnull', False), ('url__regex', '.+')),
                        models.Q(('file__in', ['', None]), ('file__isnull', True), _connector='OR'),
                    ),
                    _connector='OR',
                ),
                name='rgd_checksumfile_file_source_value_matches_type',
            ),
        ),
    ]
