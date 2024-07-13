from allauth.socialaccount.models import SocialAccount



def optener_datos_gogle(user):
    
    foto_perfil = None
    try:
        social_account = SocialAccount.objects.get(user=user, provider='google')
        return social_account.extra_data.get('picture', None)
    except SocialAccount.DoesNotExist:
        return None