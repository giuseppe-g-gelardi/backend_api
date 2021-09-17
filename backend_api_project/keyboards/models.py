from django.db import models

class Keyboards(models.Model):
    layout = models.CharField(max_length=50),
    color = models.CharField(max_length=50),
    keycap_color = models.CharField(max_length=50),


# LAYOUT_CHOICES = (
#     ('1', '60%'),
#     ('2', 'alice'),
#     ('3', 'TKL'),
    
# ),

# COLOR_CHOICES = (
#     ('1', 'obsidian'),
#     ('2', 'ewhite'),
#     ('3', 'polycarb'),
# ),

# KEYCAP_COLOR_CHOICES = (
#     ('1', 'dracula'),
#     ('2', 'muted'),
#     ('3', 'futurefunk')
# )

# class Keyboards(models.Model):
#     layout = models.CharField(
#         max_length=50,
#         choices=LAYOUT_CHOICES,
#         default='1',
#     ),

#     color = models.CharField(
#         max_length=50,
#         choices=COLOR_CHOICES,
#         default='1', 
#     ),

#     keycap_color = models.CharField(
#         max_length=50,
#         choices=KEYCAP_COLOR_CHOICES,
#         default=1,
#     ),