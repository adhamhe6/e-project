from .models import Company

def get_company_info(request):
    company_info = Company.objects.last()
    return {'info':company_info}