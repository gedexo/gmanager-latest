from django.db import models


class Setting(models.Model):
    logo = models.ImageField(upload_to="logo", null=True, blank=True)
    site_name = models.CharField(max_length=100, null=True, blank=True)
    site_title = models.CharField(max_length=100, null=True, blank=True)
    site_description = models.TextField(null=True, blank=True)

    background_image = models.ImageField(upload_to="background", null=True, blank=True)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"


class Access(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    subdepartment = models.ForeignKey("employees.SubDepartment", on_delete=models.CASCADE)
    access_type = models.CharField(max_length=100, choices=(("Viewer", "Viewer"), ("Editor", "Editor")))

    def __str__(self):
        return f"{self.user} - {self.subdepartment}"

    class Meta:
        verbose_name = "Access Right"
        verbose_name_plural = "Access Right"
        unique_together = ("user", "subdepartment")
