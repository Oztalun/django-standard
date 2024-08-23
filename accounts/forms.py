from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = "__all__"
        exclude = ["password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined", "following", "Groups", "User permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text
            
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = UserCreationForm.Meta.fields# + (필요시 추가필드)