# Generated by Django 3.2.13 on 2022-04-20 21:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        ("wagtailpages", "0015_rename_video_url_to_embed_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="researchlandingpage",
            name="intro",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.CreateModel(
            name="ResearchLandingPageFeaturedResearchTopicRelation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
                (
                    "research_landing_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="featured_topics",
                        to="wagtailpages.researchlandingpage",
                    ),
                ),
                (
                    "research_topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailpages.researchtopic",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]
