from email.policy import default
from re import L
from django import forms

# استmodelsاين فايل از لحاظ ساختاري بسيار شبيه فايل
# اما اون براي تنظيمات دسترسي ادمين بود و اين يكي براي ساختن همون دسترسي ها براي يوزر است

# مراحل كار:
# ابتدا تو همين فايل،فرم را درست كن
# سپس در فايل ويوي،ويو را درست كن
# زيباسازي كنtemplate در فايل html,cssسپس با


class PostForm(forms.Form):
    title = forms.CharField(help_text='اينجا عنوانت رو بذار سيد')
    text = forms.CharField(widget=forms.Textarea, required=False,
                           label='your texttt', label_suffix='===>>>')
    is_enable = forms.BooleanField(required=False)
    publish_date = forms.DateField()
