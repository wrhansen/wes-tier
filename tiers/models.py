from django.db import models

DEFAULT_TIERLIST_ROW_NAMES = ["S", "A", "B", "C", "D", "E", "F", "G", "H", "I"]


class TierListManager(models.Manager):
    def create_list_and_rows(self):
        tierlist, _ = self.get_or_create(
            id=1,
            defaults={
                "name": "First Tierist",
                "description": ":Testing out the first tierlist.",
            },
        )

        if not tierlist.rows.all():
            for order, row_name in enumerate(DEFAULT_TIERLIST_ROW_NAMES):
                TierRow.objects.bulk_create(
                    [
                        TierRow(name=row_name, order=order, tierlist=tierlist),
                    ]
                )
        return tierlist


class TierList(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    objects = TierListManager()

    def __str__(self):
        return f"id={self.id} name={self.name} description={self.description}"


class TierRow(models.Model):
    name = models.CharField(max_length=64)
    order = models.PositiveSmallIntegerField()
    tierlist = models.ForeignKey(
        TierList, on_delete=models.CASCADE, related_name="rows"
    )


class TierItem(models.Model):
    name = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="items")
    tierlist = models.ForeignKey(TierList, on_delete=models.CASCADE)
    tierrow = models.ForeignKey(
        TierRow, on_delete=models.CASCADE, null=True, related_name="items"
    )

    def __str__(self):
        return f"id={self.id} name={self.name} image={self.image.url} tierlist={self.tierlist_id} tierrow={self.tierrow_id}"

    def save(self, *args, **kwargs):
        if self.tierrow:
            if self.tierrow.tierlist_id != self.tierlist_id:
                raise ValueError(
                    f"Invalid TierList: {self.tierrow.tierlist_id} != {self.tierlist_id}"
                )
        super().save(*args, **kwargs)
