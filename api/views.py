# api/views.py
import json, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@csrf_exempt
def ask(request):
    if request.method != "POST":
        return JsonResponse({"detail": 'Use POST with JSON {"prompt":"..."}'}, status=405)

    data = json.loads(request.body or b"{}")
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return JsonResponse({"error": "Field 'prompt' is required"}, status=400)

    # Первый запрос
    text = "Найди хорошо рецензированную и качественную статью и отправь ТОЛЬКО НАЗВАНИЕ И ССЫЛКУ НА НЕЕ, больше ничего не надо!!! тема статьи - "
    resp1 = client.responses.create(model="gpt-4o", input=f"{text} {prompt}")

    # Берём текст ответа первого запроса
    first_answer = resp1.output_text.strip()

    # Второй запрос (можешь подставить свой промпт)
    second_prompt = f"Дай краткий обзор стаьи на 200 слов: {first_answer}"
    resp2 = client.responses.create(model="gpt-4o", input=second_prompt)

    return JsonResponse(
        {
            "first_answer": first_answer,
            "second_answer": resp2.output_text
        },
        json_dumps_params={"ensure_ascii": False}
    )
