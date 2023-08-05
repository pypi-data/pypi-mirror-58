# Generated by Django 2.2.4 on 2019-11-01 22:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
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
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "code",
                    models.TextField(
                        default="USD",
                        validators=[django.core.validators.MinLengthValidator(1)],
                    ),
                ),
                (
                    "issuer",
                    models.TextField(
                        default="GCXEIFQV5CAFTMDWW3YYUBMRXHQEE3DWQCGQLJMC4PUK6GGWERICUTOQ",
                        validators=[django.core.validators.MinLengthValidator(56)],
                    ),
                ),
                ("deposit_enabled", models.BooleanField(default=True)),
                ("deposit_fee_fixed", models.FloatField(blank=True, default=1.0)),
                ("deposit_fee_percent", models.FloatField(blank=True, default=0.01)),
                ("deposit_min_amount", models.FloatField(blank=True, default=10.0)),
                ("deposit_max_amount", models.FloatField(blank=True, default=10000.0)),
                ("withdrawal_enabled", models.BooleanField(default=True)),
                ("withdrawal_fee_fixed", models.FloatField(blank=True, default=1.0)),
                ("withdrawal_fee_percent", models.FloatField(blank=True, default=0.01)),
                ("withdrawal_min_amount", models.FloatField(blank=True, default=10.0)),
                (
                    "withdrawal_max_amount",
                    models.FloatField(blank=True, default=10000.0),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "stellar_account",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[("deposit", "deposit"), ("withdrawal", "withdrawal")],
                        default="deposit",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "completed"),
                            ("pending_external", "pending_external"),
                            ("pending_anchor", "pending_anchor"),
                            ("pending_stellar", "pending_stellar"),
                            ("pending_trust", "pending_trust"),
                            ("pending_user", "pending_user"),
                            (
                                "pending_user_transfer_start",
                                "pending_user_transfer_start",
                            ),
                            ("incomplete", "incomplete"),
                            ("no_market", "no_market"),
                            ("too_small", "too_small"),
                            ("too_large", "too_large"),
                            ("error", "error"),
                        ],
                        default="pending_external",
                        max_length=30,
                    ),
                ),
                (
                    "status_eta",
                    models.IntegerField(blank=True, default=3600, null=True),
                ),
                ("stellar_transaction_id", models.TextField(blank=True, null=True)),
                ("external_transaction_id", models.TextField(blank=True, null=True)),
                ("amount_in", models.FloatField(blank=True, null=True)),
                ("amount_out", models.FloatField(blank=True, null=True)),
                ("amount_fee", models.FloatField(blank=True, null=True)),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("completed_at", models.DateTimeField(null=True)),
                ("from_address", models.TextField(blank=True, null=True)),
                ("to_address", models.TextField(blank=True, null=True)),
                ("external_extra", models.TextField(blank=True, null=True)),
                ("external_extra_text", models.TextField(blank=True, null=True)),
                ("deposit_memo", models.TextField(blank=True, null=True)),
                (
                    "deposit_memo_type",
                    models.CharField(
                        choices=[("text", "text"), ("id", "id"), ("hash", "hash")],
                        default="text",
                        max_length=10,
                    ),
                ),
                ("withdraw_anchor_account", models.TextField(blank=True, null=True)),
                ("withdraw_memo", models.TextField(blank=True, null=True)),
                (
                    "withdraw_memo_type",
                    models.CharField(
                        choices=[("text", "text"), ("id", "id"), ("hash", "hash")],
                        default="text",
                        max_length=10,
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polaris.Asset"
                    ),
                ),
            ],
            options={"ordering": ("-started_at",),},
        ),
    ]
