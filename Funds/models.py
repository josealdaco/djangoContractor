from django.db import models

# Models for the API wikipedia pages, this will make the app run smoother


class wikiPagesModel(models.Model):
    fundOneURL = models.TextField()
    fundOneTitle = models.TextField()
    fundTwoURL = models.TextField()
    fundTwoTitle = models.TextField()
    fundThreeURL = models.TextField()
    fundThreeTitle = models.TextField()
    fundFourURL = models.TextField()
    fundFourTitle = models.TextField()

    #  wikiPagesModel.objects.bulk_create(([wikiPagesModel(**{'batch_cola' : m[0],
        #                                'batch_colb' : m[1],
        #                                'batch_colc' : m[2],
        #                                'batch_cold' : m[3],
        #                                'batch_cole' : m[4]}
        #                    for m in mylist]);
