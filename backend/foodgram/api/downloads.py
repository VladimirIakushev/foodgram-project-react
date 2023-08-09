import io

from django.db.models import Sum
from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from recipes.models import RecipeIngredient


def download_shopping_cart_code(self, request):
    user = request.user
    if not user.shopping_cart.exists():
        return Response(status=HTTP_400_BAD_REQUEST)

    ingredients = RecipeIngredient.objects.filter(
        recipe__shopping_cart__user=request.user
    ).values(
        'ingredient__name',
        'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))

    pdfmetrics.registerFont(
        TTFont('ComicSans', 'data/ComicSans.ttf', 'UTF-8')
    )
    buffer = io.BytesIO()
    pdf_file = canvas.Canvas(buffer)
    pdf_file.setFont('ComicSans', 24)
    pdf_file.drawString(
        20,
        800,
        f'Список покупок для: {user.get_full_name()}'
        )
    pdf_file.setFont('ComicSans', 14)
    from_bottom = 750
    for ingredient in ingredients:
        pdf_file.drawString(
            50,
            from_bottom,
            f'- {ingredient["ingredient__name"]} '
            f'({ingredient["ingredient__measurement_unit"]})'
            f' - {ingredient["amount"]}',
        )
        from_bottom -= 20
        if from_bottom <= 50:
            from_bottom = 800
            pdf_file.showPage()
            pdf_file.setFont('ComicSans', 14)
    pdf_file.showPage()
    pdf_file.save()
    buffer.getvalue()
    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename='shopping_list.pdf'
        )
