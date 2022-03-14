from django.db import models


class Contact(models.Model):
    address = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    timing = models.TextField(blank=True, null=True)
    facebook_page = models.TextField(blank=True, null=True)
    youtube_page = models.TextField(blank=True, null=True)
    twitter_page = models.TextField(blank=True, null=True)
    instagram_page = models.TextField(blank=True, null=True)
    google_map_code = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    # to save the data
    def create_contact(self):
        self.save()
