from django.db import models


# specifying choices
LAYOUT_CHOICES = (
    ('1', '40%'),
    ('2', '60%'),
    ('3', '65%'),
    ('4', '75%'),
    ('5', 'TKL'),
    ('6', 'Full-size'),
    ('7', 'Other'),
),

BODY_MATERIAL_CHOICES = (
    ('1', 'Aluminum'),
    ('2', 'Polycarbonate'),
),

BODY_FINISH_ALU_CHOICES = (
    ('1', 'Anodized'),
    ('2', 'Cerakote'),
    ('3', 'E-Coat'),
),

BODY_FINISH_PC_CHOICES = (
    ('1', 'Clear'),
    ('2', 'Frosted'),
    ('3', 'Dyed'),
),

PLATE_MATERIAL_CHOICES = (
    ('1', 'Aluminum'),
    ('2', 'Brass'),
    ('3', 'Polycarbonate'),
    ('4', 'POM'),
    ('5', 'Carbon Fiber'),
),

PLATE_FINISH_ALU_CHOICES = (
    ('1', 'Anodized'),
    ('2', 'Bead Blasted'),
),

PLATE_FINISH_BRASS_CHOICES = (
    ('1', 'Polished'),
    ('2', 'Bead Blasted'),
),

PLATE_FINISH_PC_CHOICES = (
    ('1', 'Clear'),
    ('2', 'Frosted'),
),

WEIGHT_MATERIAL_CHOICES = (
    ('1', 'Brass'),
    ('2', 'Stainless Steel'),
    ('3', 'None'),
),

WEIGHT_FINISH_CHOICES = (
    ('1', 'Polished'),
    ('2', 'Bead Blasted'),
    ('3', 'PVD'),
),

MOUNTING_STYLE_CHOICES = (
    ('1', 'Gasket (Isolation)'),
    ('2', 'Gasket (O-Ring)'),
    ('3', 'Top Mount'),
    ('4', 'Other'),
),


# declaring models
class Keyboards(models.Model):
    layout = models.CharField(
        max_length=25,
        choices=LAYOUT_CHOICES,
        default='2',
    ),
    angle = models.CharField(max_length=25),

    body_material = models.CharField(
        max_length=25,
        choices=BODY_MATERIAL_CHOICES,
        default='1',
    ),

    body_finish_alu = models.CharField(
        max_length=25,
        choices=BODY_FINISH_ALU_CHOICES,
        default='1',
    ),

    body_finish_pc = models.CharField(
        max_length=25,
        choices=BODY_FINISH_PC_CHOICES,
        default='2'
    ),

    plate_material = models.CharField(
        max_length=25,
        choices=PLATE_MATERIAL_CHOICES,
        default=5,
    ),

    plate_finish_alu = models.CharField(
        max_length=25,
        choices=PLATE_FINISH_ALU_CHOICES,
        default='1',
    ),

    plate_finish_brass = models.CharField(
        max_length=25,
        choices=PLATE_FINISH_BRASS_CHOICES,
        default='1',
    ),

    plate_finish_pc = models.CharField(
        max_length=25,
        choices=PLATE_FINISH_PC_CHOICES,
        default=2,
    ),

    weight_material = models.CharField(
        max_length=25,
        choices=WEIGHT_MATERIAL_CHOICES,
        default=2,
    ),

    weight_finish = models.CharField(
        max_length=25,
        choices=WEIGHT_FINISH_CHOICES,
        default=3,
    ),

    mounting_style = models.CharField(
        max_length=25,
        choices=MOUNTING_STYLE_CHOICES,
        default='1',
    ),
    