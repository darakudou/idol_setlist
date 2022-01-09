from django.db import models


class Live(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey("core.Place", on_delete=models.CASCADE, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)
    is_online_only = models.BooleanField(default=False)  # 配信ライブなど、配信もあるライブではFalse

    def __str__(self):
        return f"{self.name}-{self.start.isoformat()}"


class LiveAppearance(models.Model):
    live = models.ForeignKey("Live", on_delete=models.CASCADE)
    idol = models.ForeignKey("core.Idol", on_delete=models.CASCADE)
    stage = models.CharField(max_length=255, null=True)  # tifの○○ステージみたいな用途を想定
    start = models.DateTimeField(null=True)  # 出演開始時間、書いてあれば
    end = models.DateTimeField(null=True)  # 出演終了時間、書いてあれば

    def __str__(self):
        return f"{self.live.name}-{self.idol.name}"


class Setlist(models.Model):
    live_apparance = models.ForeignKey("LiveAppearance", on_delete=models.CASCADE)
    sound = models.ForeignKey("Sound", on_delete=models.CASCADE, null=True)
    is_mc = models.BooleanField(default=False)
    order = models.IntegerField()