from django.db import models


class Contact(models.Model):
    address = models.TextField(blank=True, null=True, default="-")
    phone_number = models.TextField(blank=True, null=True, default="-")
    timing = models.TextField(blank=True, null=True, default="-")
    facebook_page = models.TextField(blank=True, null=True, default="-")
    youtube_page = models.TextField(blank=True, null=True, default="-")
    twitter_page = models.TextField(blank=True, null=True, default="-")
    instagram_page = models.TextField(blank=True, null=True, default="-")
    google_map_code = models.TextField(blank=True, null=True, default="-")

    class Meta:
        ordering = ['-id']

    # to save the data
    def create_contact(self):
        self.save()
