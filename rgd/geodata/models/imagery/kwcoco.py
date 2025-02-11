from django.contrib.gis.db import models

from ... import tasks
from ..common import ChecksumFile, ModifiableEntry
from ..mixins import TaskEventMixin
from .base import ImageSet


class KWCOCOArchive(ModifiableEntry, TaskEventMixin):
    """A container for holding imported KWCOCO datasets.

    User must upload a JSON file of the KWCOCO meta info and an optional
    archive of images - optional because images can come from URLs instead of
    files.

    """

    task_funcs = (tasks.task_load_kwcoco_dataset,)
    name = models.CharField(max_length=1000, blank=True)
    spec_file = models.OneToOneField(
        ChecksumFile,
        on_delete=models.CASCADE,
        related_name='kwcoco_spec_file',
        help_text='The JSON spec file.',
    )
    image_archive = models.OneToOneField(
        ChecksumFile,
        null=True,
        on_delete=models.CASCADE,
        related_name='kwcoco_image_archive',
        help_text='An archive (.tar or .zip) of the images referenced by the spec file (optional).',
    )
    # Allowed null because model must be saved before task can populate this
    image_set = models.OneToOneField(ImageSet, on_delete=models.SET_NULL, null=True)

    def _post_delete(self, *args, **kwargs):
        # Frist delete all the images in the image set
        #  this will cascade to the annotations
        images = self.image_set.images.all()
        for image in images:
            # This should cascade to the ImageFile and the ImageEntry
            image.image_file.file.delete()
        # Now delete the empty image set
        self.image_set.delete()
