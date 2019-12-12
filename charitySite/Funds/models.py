from django.db import models

# Models for the API wikipedia pages, this will make the app run smoother


class wikiPagesModel(models.Model):
    fundOneURL = models.CharField(max_length=100)
    fundTwoURL = models.CharField(max_length=100)
    fundThreeURL = models.CharField(max_length=100)
    fundFourURL = models.CharField(max_length=100)

    #  wikiPagesModel.objects.bulk_create(([wikiPagesModel(**{'batch_cola' : m[0],
        #                                'batch_colb' : m[1],
        #                                'batch_colc' : m[2],
        #                                'batch_cold' : m[3],
        #                                'batch_cole' : m[4]}
        #                    for m in mylist]);
