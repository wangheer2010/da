from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.forms import ModelForm
class Meta:
    managed = True
class Format(models.Model):
    Distance=models.FloatField(
            help_text=_('Yards need to get the next first down'),
            )
    One='One'
    Two='Two'
    Three='Three'
    Four='Four'
    
    DOWN_CHOICES=(
            (One,'One'),
            (Two,'Two'),
            (Three,'Three'),
            (Four,'Four'),
            )
    Down=models.CharField(
            max_length=100,
            choices = DOWN_CHOICES,
            blank = True,)
    NE='NE'
    KC='KC'
    BUF='BUF'
    NYJ='NYJ'
    ATL='ATL'
    CHI='CHI'
    CIN='CIN'
    BAL='BAL'
    CLE='CLE'
    PIT='PIT'
    ARI='ARI'
    DET='DET'
    JAX='JAX'
    HOU='HOU'
    OAK='OAK'
    TEN='TEN'
    WAS='WAS'
    PHI='PHI'
    LA='LA'
    IND='IND'
    SEA='SEA'
    GB='GB'
    CAR='CAR'
    SF='SF'
    DAL='DAL'
    NYG='NYG'
    NO='NO'
    MIN='MIN'
    DEN='DEN'
    LAC='LAC'
    TB='TB'
    MIA='MIA'
    CHOICES=(
    (NE,'NE'),
    (KC,'KC'),
    (BUF,'BUF'),
    (NYJ,'NYJ'),
    (ATL,'ATL'),
    (CHI,'CHI'),
    (CIN,'CIN'),
    (BAL,'BAL'),
    (CLE,'CLE'),
    (PIT,'PIT'),
    (ARI,'ARI'),
    (DET,'DET'),
    (JAX,'JAX'),
    (HOU,'HOU'),
    (OAK,'OAK'),
    (TEN,'TEN'),
    (WAS,'WAS'),
    (PHI,'PHI'),
    (LA,'LA'),
    (IND,'IND'),
    (SEA,'SEA'),
    (GB,'GB'),
    (CAR,'CAR'),
    (SF,'SF'),
    (DAL,'DAL'),
    (NYG,'NYG'),
    (NO,'NO'),
    (MIN,'MIN'),
    (DEN,'DEN'),
    (LAC,'LAC'),
    (TB,'TB'),
    (MIA,'MIA'),
     )
    Your_Team = models.CharField(
            max_lenth=100,
            choices= CHOICES,
            blank = True,
            )
    Opponent = models.CharField(
            max_lenth=100,
            choices= CHOICES,
            blank = True,
            )
