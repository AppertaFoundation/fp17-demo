import pprint

from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard import views as wizard_views

from . import forms


class FP17FormWizard(wizard_views.SessionWizardView):
    form_list = (
        ('1', forms.PartOne),
        ('2', forms.PartTwo),
        ('3', forms.PartThree),
        ('4', forms.PartFour),
        ('5', forms.PartFive),
        ('5a', forms.PartFiveA),
        ('6', forms.PartSix),
        ('7', forms.PartSeven),
        ('8', forms.PartEight),
        ('9', forms.PartNine),
    )

    def get(self, *args, **kwargs):
        # Always reset when we hit the main page, no need to pass '?reset'
        if 'step' not in kwargs:
            self.storage.reset()

        return super().get(*args, **kwargs)

    def get_template_names(self):
        return 'fp17_form/part_{}.html'.format(self.steps.current)

    def done(self, form_list, form_dict, **kwargs):
        return HttpResponse("<pre>{}</pre>".format(pprint.pformat({
            x: y.cleaned_data for x, y in form_dict.items()
        })))
