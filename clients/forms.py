from django import forms
from .models import Client
from django.db import transaction
from django.contrib.auth import get_user_model

User = get_user_model()


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = [
            'user', 
            'is_active', 
            'is_deleted', 
            'creator', 
            'created_at', 
            'updated_at'
        ]

    def save(self, commit=True):
        client = super().save(commit=False)

        if not client.pk and not client.user:
            try:
                with transaction.atomic():
                    username = client.email if client.email else client.phone
                    
                    if User.objects.filter(username=username).exists():
                        import uuid
                        username = f"{username}_{str(uuid.uuid4())[:4]}"

                    user = User.objects.create_user(
                        username=username,
                        email=client.email,
                        password=client.phone, 
                        usertype='client',
                        first_name=client.fullname.split(' ')[0] 
                    )
                    
                    client.user = user
                    
                    if commit:
                        client.save()
                        self.save_m2m()
            
            except Exception as e:
                print(f"Error creating user for client: {e}")
                raise e
        else:
            if commit:
                client.save()
                self.save_m2m()

        return client