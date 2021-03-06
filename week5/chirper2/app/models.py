from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ("-created",)

    @property  # CAN ONLY TAKE METHODS WITH 'SELF' AS THE ONLY PARAMETER
    def score(self):
        return sum([chirp_obj.score for chirp_obj in self.vote_set.all()])


class Vote(models.Model):
    user = models.ForeignKey('auth.User')
    chirp = models.ForeignKey('app.Chirp')
    value = models.BooleanField()

    class Meta:
        unique_together = ('user', 'chirp')

    @property
    def score(self):
        if self.value:
            return 1
        return -1

    def __str__(self):
        return "{} - {}".format(self.chirp.body, self.score)


# #######################################gi#########################
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
# class Profile(models.Model):
#     user = models.OneToOneField('auth.User')
#     fav_snack = models.CharField(max_length=25, null=True)
#
# @receiver(post_save, sender'auth.User')
# def create_user_profile(**kwargs):
#     created = kwargs.get('created')
#     instance = kwargs.get('instance')
#
#     if created:
#         Profile.objects.create(user=instance)
#
#
#
#
# ##########
# # below is if ran in shell, and imports needed assumed
# asdf = User.objects.get(username='asdf')
# Profile.objects.create(user=asdf, fav_snack='cookies')
#
# # asdf.profile
# #  # will give <Profile: Profile object>
# # asdf.profile.fav_snack
# #  # will give 'cookies'
