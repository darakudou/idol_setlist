from django.db import models


class Sound(models.Model):
    title = models.CharField(max_length=255)
    remarks = models.TextField(null=True) # 備考

    def __str__(self):
        return self.title


class Single(models.Model):
    title = models.CharField(max_length=255)
    idol = models.ForeignKey("core.Idol", on_delete=models.CASCADE)
    sound = models.ManyToManyField("Sound")

    def __str__(self):
        return f"{self.idol.name}-{self.title}"


class SingleOrder(models.Model):
    single = models.ForeignKey("Single", on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.single.title}-{self.order}"


class Album(models.Model):
    title = models.CharField(max_length=255)
    idol = models.ForeignKey("core.Idol", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AlbumOrder(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.album.title}-{self.order}"
