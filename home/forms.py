from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email_field']

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('email_field', css_class='form form__newsletter_email_input', placeholder='Enter your Email Address')
        )


class HeroJobSearchForm(forms.Form):
    search_field = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(HeroJobSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('search_field', css_class='form form__hero_search_input', placeholder='e.g. data scientist')
        )
