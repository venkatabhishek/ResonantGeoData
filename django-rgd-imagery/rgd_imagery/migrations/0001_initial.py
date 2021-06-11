# Generated by Django 3.2.4 on 2021-06-11 14:51

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rgd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
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
                ('caption', models.CharField(blank=True, max_length=100, null=True)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('annotator', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                (
                    'keypoints',
                    django.contrib.gis.db.models.fields.MultiPointField(null=True, srid=0),
                ),
                ('line', django.contrib.gis.db.models.fields.LineStringField(null=True, srid=0)),
            ],
            bases=('rgd.modifiableentry',),
        ),
        migrations.CreateModel(
            name='ImageEntry',
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
                ('name', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('driver', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('number_of_bands', models.PositiveIntegerField()),
            ],
            bases=('rgd.modifiableentry',),
        ),
        migrations.CreateModel(
            name='ImageSet',
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
                ('name', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.ManyToManyField(to='rgd_imagery.ImageEntry')),
            ],
            bases=('rgd.modifiableentry',),
        ),
        migrations.CreateModel(
            name='RasterEntry',
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
                ('description', models.TextField(blank=True, null=True)),
                ('ancillary_files', models.ManyToManyField(blank=True, to='rgd.ChecksumFile')),
                (
                    'image_set',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageset'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.CreateModel(
            name='Segmentation',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'outline',
                    django.contrib.gis.db.models.fields.PolygonField(
                        help_text='The bounding box', null=True, srid=0
                    ),
                ),
                (
                    'annotation',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.annotation'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='PolygonSegmentation',
            fields=[
                (
                    'segmentation_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='rgd_imagery.segmentation',
                    ),
                ),
                (
                    'feature',
                    django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=0),
                ),
            ],
            bases=('rgd_imagery.segmentation',),
        ),
        migrations.CreateModel(
            name='RLESegmentation',
            fields=[
                (
                    'segmentation_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='rgd_imagery.segmentation',
                    ),
                ),
                ('blob', models.BinaryField()),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
            ],
            bases=('rgd_imagery.segmentation',),
        ),
        migrations.CreateModel(
            name='SubsampledImage',
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
                (
                    'sample_type',
                    models.CharField(
                        choices=[
                            ('pixel box', 'Pixel bounding box'),
                            ('geographic box', 'Geographic bounding box'),
                            ('geojson', 'GeoJSON feature'),
                            ('annotation', 'Annotation entry'),
                        ],
                        default='pixel box',
                        max_length=20,
                    ),
                ),
                ('sample_parameters', models.JSONField()),
                (
                    'data',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='rgd.checksumfile',
                    ),
                ),
                (
                    'source_image',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageentry'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.CreateModel(
            name='RasterMetaEntry',
            fields=[
                (
                    'spatialentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to='rgd.spatialentry',
                    ),
                ),
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
                ('crs', models.TextField(help_text='PROJ string')),
                (
                    'origin',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=2
                    ),
                ),
                (
                    'extent',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=4
                    ),
                ),
                (
                    'resolution',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=2
                    ),
                ),
                (
                    'transform',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=6
                    ),
                ),
                (
                    'cloud_cover',
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    'parent_raster',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.rasterentry'
                    ),
                ),
            ],
            bases=('rgd.modifiableentry', 'rgd.spatialentry'),
        ),
        migrations.CreateModel(
            name='KWCOCOArchive',
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
                (
                    'image_archive',
                    models.OneToOneField(
                        help_text='An archive (.tar or .zip) of the images referenced by the spec file (optional).',
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='kwcoco_image_archive',
                        to='rgd.checksumfile',
                    ),
                ),
                (
                    'image_set',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='rgd_imagery.imageset',
                    ),
                ),
                (
                    'spec_file',
                    models.OneToOneField(
                        help_text='The JSON spec file.',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='kwcoco_spec_file',
                        to='rgd.checksumfile',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.CreateModel(
            name='ImageSetSpatial',
            fields=[
                (
                    'spatialentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to='rgd.spatialentry',
                    ),
                ),
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
                ('name', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                (
                    'image_set',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageset'
                    ),
                ),
            ],
            bases=('rgd.modifiableentry', 'rgd.spatialentry'),
        ),
        migrations.CreateModel(
            name='ImageFile',
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
                (
                    'file',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd.checksumfile'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.AddField(
            model_name='imageentry',
            name='image_file',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imagefile'
            ),
        ),
        migrations.CreateModel(
            name='ConvertedImageFile',
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
                (
                    'converted_file',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='rgd.checksumfile',
                    ),
                ),
                (
                    'source_image',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageentry'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('rgd.modifiableentry', models.Model),
        ),
        migrations.CreateModel(
            name='BandMetaEntry',
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
                ('band_number', models.IntegerField()),
                (
                    'description',
                    models.TextField(
                        blank=True,
                        help_text='Automatically retreived from raster but can be overwritten.',
                        null=True,
                    ),
                ),
                ('dtype', models.CharField(max_length=10)),
                ('max', models.FloatField(null=True)),
                ('min', models.FloatField(null=True)),
                ('mean', models.FloatField(null=True)),
                ('std', models.FloatField(null=True)),
                ('nodata_value', models.FloatField(null=True)),
                ('interpretation', models.TextField()),
                (
                    'parent_image',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageentry'
                    ),
                ),
            ],
            bases=('rgd.modifiableentry',),
        ),
        migrations.AddField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='rgd_imagery.imageentry'
            ),
        ),
    ]